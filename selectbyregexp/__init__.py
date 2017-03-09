from fman import DirectoryPaneCommand, show_alert, show_prompt
import os, re

class SelectByRegExp(DirectoryPaneCommand):
    def __call__(self):
        regexp,okay = show_prompt("Your Regular Expression for Selection:")
        pattern = re.compile(regexp)
        currentDir = self.pane.get_path()
        filesInDir = os.listdir(currentDir)
        for filep in filesInDir:
            if pattern.search(filep):
                self.pane.toggle_selection(currentDir + os.sep + filep)