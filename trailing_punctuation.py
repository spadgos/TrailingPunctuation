"""
TrailingPunctuation v1.0.0
by Nick Fisher
"""
import sublime_plugin
import sublime
import re

class TrailingPunctuationCommand(sublime_plugin.TextCommand):
    def run(self, edit, char = ";"):
        v = self.view
        for sel in reversed(v.sel()):
            for line in reversed(v.lines(sel)):
                eol = line.end()
                scope = v.scope_name(eol)
                if v.match_selector(eol, 'comment'):
                    commentRegion = v.extract_scope(eol)
                    eol = max(line.begin(), commentRegion.begin())

                while eol > line.begin() and v.substr(eol - 1) == ' ':
                    eol = eol - 1

                if eol > line.begin():

                    lastCharRegion = sublime.Region(eol - 1, eol)
                    lastChar = v.substr(lastCharRegion)
                    if lastChar == char:  # toggle
                        v.erase(edit, lastCharRegion)
                    else:                 # add char, but remove other trailing chars
                        v.replace(edit, lastCharRegion, re.sub(r'[;,]?$', char, lastChar))

# fff
         # bbb

# aa
