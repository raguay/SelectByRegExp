from core.quicksearch_matchers import contains_chars
from fman import DirectoryPaneCommand, show_alert, show_prompt, show_quicksearch, QuicksearchItem, show_status_message, clear_status_message
import os
import re
from fman.url import as_human_readable
from fman.url import as_url


REGULAREXPRESSIONHIST = os.path.expanduser("~") + "/.regexphist"

class SelectByRegExp(DirectoryPaneCommand):
    def __call__(self):
        show_status_message('Regular Expressions Selection')
        result = show_quicksearch(self._suggest_projects)
        if result:
            query, regexp = result
            try:
                pattern = re.compile(regexp)
            except Exception as e:
                show_alert('Your Regular Expression statement is not valid.' + e)
                self.__call__()
                return
            used = False
            lines = [""]
            if os.path.isfile(REGULAREXPRESSIONHIST):
                with open(REGULAREXPRESSIONHIST, "r") as f:
                    lines = f.readlines()
            for line in lines:
                if line.strip() == regexp:
                    used = True
            if not used:
                with open(REGULAREXPRESSIONHIST, "a") as f:
                    f.write(regexp + "\n")
            currentDir = as_human_readable(self.pane.get_path())
            filesInDir = os.listdir(currentDir)
            for filep in filesInDir:
                if pattern.search(filep):
                    self.pane.toggle_selection(as_url(currentDir + os.sep + filep))
        clear_status_message()

    def _suggest_projects(self, query):
        regexs = ["No Regular Expression History."]
        if os.path.isfile(REGULAREXPRESSIONHIST):
            with open(REGULAREXPRESSIONHIST, "r") as f:
                regexs = f.readlines()
        found = False
        for regex in regexs:
            regex = regex.strip()
            if not regex == "":
                match = contains_chars(regex.lower(), query.lower())
                if match or not query:
                    found = True
                    yield QuicksearchItem(regex, highlight=match)
        if not found:
            yield QuicksearchItem(query)

class SelectRegExpToRemove(DirectoryPaneCommand):
    def __call__(self):
        show_status_message('Remove Regular Expressions Selection')
        result = show_quicksearch(self._suggest_projects)
        if result:
            query, regexp = result
            lines = [""]
            if os.path.isfile(REGULAREXPRESSIONHIST):
                with open(REGULAREXPRESSIONHIST, "r") as f:
                    lines = f.readlines()
                with open(REGULAREXPRESSIONHIST, "w") as f:
                    for line in lines:
                        if line.strip() != regexp:
                            f.write(line + "\n")
        clear_status_message()

    def _suggest_projects(self, query):
        regexs = ["No Regular Expression History."]
        if os.path.isfile(REGULAREXPRESSIONHIST):
            with open(REGULAREXPRESSIONHIST, "r") as f:
                regexs = f.readlines()
        for regex in regexs:
            if not regex.strip() == "":
                match = contains_chars(regex.lower().strip(), query.lower().strip())
                if match or not query:
                    yield QuicksearchItem(regex.strip(), highlight=match)