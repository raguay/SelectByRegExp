from fman import DirectoryPaneCommand, show_alert, show_prompt
import os, re

class SelectByRegExp(DirectoryPaneCommand):
    def __call__(self):
        regexp,okay = show_prompt("Your Regular Expression for Selection:")
        if not okay:
            return
        try:
            pattern = re.compile(regexp)
        except Exception as e:
            show_alert('Your Regular Expression statement is not valid.')
            self.__call__()
            return
        currentDir = self.pane.get_path()
        filesInDir = os.listdir(currentDir)
        for filep in filesInDir:
            if pattern.search(filep):
                self.pane.toggle_selection(currentDir + os.sep + filep)