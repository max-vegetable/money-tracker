const { app, BrowserWindow } = require('electron');
const path = require('path');

app.whenReady().then(() => {
    const win = new BrowserWindow({
        width: 420,
        height: 700,
        minWidth: 380,
        minHeight: 600,
        x: 100,
        y: 100,
        alwaysOnTop: true,
        resizable: true,
        backgroundColor: '#0a0e17',
        title: '老子今天又赚 200',
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    win.loadFile('index.html');
    win.setMenuBarVisibility(false);
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        app.whenReady();
    }
});