from SublimeLinter.lint import Linter


class CSpell(Linter):
    cmd = 'cspell --no-color stdin'
    defaults = {'selector': 'source'}
    regex = r'(?P<filename>[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)'