const vscode = require('vscode');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    let disposable = vscode.commands.registerCommand('algolab.run', function () {
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

        // Sauvegarder le fichier avant de lancer
        document.save().then(() => {
            const filePath = document.uri.fsPath;
            
            // Trouver ou créer un terminal
            let terminal = vscode.window.terminals.find(t => t.name === 'AlgoLab execution');
            if (!terminal) {
                terminal = vscode.window.createTerminal('AlgoLab execution');
            }
            
            terminal.show();
            // Lancer la commande algolab sur le fichier
            terminal.sendText(`algolab "${filePath}"`);
        });
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
}
