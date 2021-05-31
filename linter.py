from SublimeLinter.lint import Linter
from SublimeLinter.lint import const


class CSpell(Linter):
    default_type = const.WARNING
    cmd = ('cspell', '--no-color', '--no-summary', '${args}', 'stdin')
    defaults = {'selector': 'source'}
    regex = r'(?P<filename>[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)'
