from SublimeLinter.lint import Linter
import re


class SpellCheckLinter(Linter):
    cmd = 'cspell ${file}'
    defaults = {'selector': 'source'}
    regex = re.compile(
        r'^(?P<filename>[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)$'
    )
