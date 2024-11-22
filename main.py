def initAPI(api):
    VtAPI = api
    global OpenDirCommand, onDoubleClick

    class OpenDirCommand(VtAPI.Plugin.WindowCommand):
        def run(self, dir=None):
            if not dir:
                dir = self.api.Dialogs.openDirDialog()
            self.window.setTreeWidgetDir(dir)

    def onDoubleClick(item):
        fp = VtAPI.activeWindow.getModelElement(item)
        if fp:
            VtAPI.activeWindow.openFiles([fp])
        else:
            VtAPI.activeWindow.setLogMsg("Command 'openFile' not found. Install Open&Save plugin")

    VtAPI.activeWindow.signals.treeWidgetDoubleClicked.connect(onDoubleClick)