from SublimeLinter.lint import Linter, STREAM_STDOUT


class CSpell(Linter):
    cmd = 'cspell ${file_on_disk}'
    defaults = {'selector': 'source'}
    regex = r'^(?P<filename>[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)$'
    tempfile_suffix = '-'
    error_stream = STREAM_STDOUT
