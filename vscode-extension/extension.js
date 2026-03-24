const vscode = require('vscode');
const { spawnSync } = require('child_process');

function quoteArg(value) {
    if (process.platform === 'win32') {
        return `"${value.replace(/"/g, '\\"')}"`;
    }
    return `'${value.replace(/'/g, `'\\''`)}'`;
}

function getExecutablePath() {
    return vscode.workspace.getConfiguration('algolab').get('executablePath', 'algolab');
}

function getDiagnosticsTimeoutMs() {
    return vscode.workspace.getConfiguration('algolab').get('diagnosticsTimeoutMs', 3000);
}

function canExecuteAlgoLab(executablePath) {
    const check = spawnSync(executablePath, ['--help'], {
        encoding: 'utf8',
        timeout: 3000,
        windowsHide: true
    });
    return !(check.error || check.status !== 0);
}

function runCommand(executablePath, args, timeoutMs) {
    return spawnSync(executablePath, args, {
        encoding: 'utf8',
        timeout: timeoutMs,
        windowsHide: true
    });
}

function parseAlgoLabError(output) {
    const trimmed = (output || '').trim();
    if (!trimmed) {
        return null;
    }

    const firstLine = trimmed.split(/\r?\n/)[0];
    const match = firstLine.match(
        /^Erreur\s+(Syntaxique|Semantique|d execution)\s*(?:\(Ligne\s+(\d+),\s*Colonne\s+(\d+)\))?\s*:\s*(.+)$/i
    );
    if (!match) {
        return { message: trimmed };
    }

    const [, kindRaw, lineRaw, colRaw, message] = match;
    const kind = (kindRaw || '').toLowerCase();
    let severity = vscode.DiagnosticSeverity.Error;
    if (kind.includes('semantique')) {
        severity = vscode.DiagnosticSeverity.Error;
    } else if (kind.includes('execution')) {
        severity = vscode.DiagnosticSeverity.Warning;
    }

    return {
        message: message.trim(),
        line: lineRaw ? Number(lineRaw) : undefined,
        column: colRaw ? Number(colRaw) : undefined,
        severity
    };
}

function updateDiagnosticsForDocument(document, diagnosticCollection) {
    if (!document || document.languageId !== 'algolab') {
        return;
    }

    const executablePath = getExecutablePath();
    if (!canExecuteAlgoLab(executablePath)) {
        vscode.window.showErrorMessage(
            "Impossible d'exécuter AlgoLab. Vérifiez `algolab.executablePath` et votre PATH."
        );
        return;
    }

    const timeoutMs = getDiagnosticsTimeoutMs();
    const result = runCommand(executablePath, [document.uri.fsPath], timeoutMs);
    if (result.error && result.error.code === 'ETIMEDOUT') {
        vscode.window.showWarningMessage(
            "Validation AlgoLab interrompue (timeout). Augmente `algolab.diagnosticsTimeoutMs` ou vérifiez les entrées LIRE."
        );
        return;
    }

    if (result.status === 0) {
        diagnosticCollection.delete(document.uri);
        return;
    }

    const combinedOutput = `${result.stderr || ''}\n${result.stdout || ''}`.trim();
    const parsed = parseAlgoLabError(combinedOutput);
    const lineIndex = Math.max((parsed && parsed.line ? parsed.line : 1) - 1, 0);
    const columnIndex = Math.max((parsed && parsed.column ? parsed.column : 1) - 1, 0);
    const safeLine = Math.min(lineIndex, Math.max(document.lineCount - 1, 0));
    const lineLength = document.lineAt(safeLine).text.length;
    const startCol = Math.min(columnIndex, lineLength);
    const endCol = Math.min(startCol + 1, lineLength);
    const range = new vscode.Range(safeLine, startCol, safeLine, endCol);

    const diagnostic = new vscode.Diagnostic(
        range,
        (parsed && parsed.message) || combinedOutput || 'Erreur AlgoLab',
        (parsed && parsed.severity) || vscode.DiagnosticSeverity.Error
    );
    diagnostic.source = 'AlgoLab';
    diagnosticCollection.set(document.uri, [diagnostic]);
}

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('algolab');
    context.subscriptions.push(diagnosticCollection);

    const runCommandDisposable = vscode.commands.registerCommand('algolab.run', function () {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage("Aucun fichier ouvert.");
            return;
        }

        const document = editor.document;
        if (document.languageId !== 'algolab') {
            vscode.window.showErrorMessage("Le fichier actif n'est pas un fichier AlgoLab (.algo).");
            return;
        }

        document.save().then(() => {
            const filePath = document.uri.fsPath;
            const executablePath = getExecutablePath();

            if (!canExecuteAlgoLab(executablePath)) {
                vscode.window.showErrorMessage(
                    "Impossible d'exécuter AlgoLab. Vérifiez `algolab.executablePath` et votre PATH."
                );
                return;
            }

            let terminal = vscode.window.terminals.find(t => t.name === 'AlgoLab execution');
            if (!terminal) {
                terminal = vscode.window.createTerminal('AlgoLab execution');
            }

            terminal.show();
            terminal.sendText(`${quoteArg(executablePath)} ${quoteArg(filePath)}`);
        });
    });

    const validateCommandDisposable = vscode.commands.registerCommand('algolab.validate', function () {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage("Aucun fichier ouvert.");
            return;
        }

        const document = editor.document;
        if (document.languageId !== 'algolab') {
            vscode.window.showErrorMessage("Le fichier actif n'est pas un fichier AlgoLab (.algo).");
            return;
        }

        document.save().then(() => {
            updateDiagnosticsForDocument(document, diagnosticCollection);
            vscode.window.showInformationMessage("Validation AlgoLab terminée.");
        });
    });

    const onSaveDisposable = vscode.workspace.onDidSaveTextDocument((document) => {
        const enabled = vscode.workspace.getConfiguration('algolab').get('diagnosticsOnSave', true);
        if (enabled) {
            updateDiagnosticsForDocument(document, diagnosticCollection);
        }
    });

    const onCloseDisposable = vscode.workspace.onDidCloseTextDocument((document) => {
        diagnosticCollection.delete(document.uri);
    });

    context.subscriptions.push(
        runCommandDisposable,
        validateCommandDisposable,
        onSaveDisposable,
        onCloseDisposable
    );
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
}
