import json
from functools import partial
from pathlib import Path

from SublimeLinter.lint import Linter, const
from SublimeLinter.lint.quick_fix import (QuickAction, add_at_eol,
                                          line_error_is_on, quick_actions_for)


class CSpell(Linter):
    default_type = const.WARNING
    cmd = ('cspell', '--no-color', '--no-summary', '${args}', 'stdin')
    defaults = {'selector': 'source'}
    regex = r'([^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)'


@quick_actions_for('cspell')
def cspell_fix(errors, view):
    for error in errors:
        yield QuickAction(
            '{linter}: Add word "{offending_text}" to dictionary'.format(
                **error),
            partial(fix_cspell_error, error),
            '',
            solves=error,
        )
        yield QuickAction(
            '{linter}: Disable line with word "{offending_text}"'.format(
                **error),
            partial(fix_disable_cspell_error, error),
            '',
            solves=error,
        )


def fix_cspell_error(error, view):
    word = error.get('offending_text')
    if word:
        path = Path(next(iter(view.window().folders()), None), 'cspell.json')
        cspell = json.load(path.open('r', encoding='utf8'))
        words = set(cspell['words'])
        words.add(word.lower())
        cspell['words'] = sorted(words)
        json.dump(
            cspell,
            path.open('w', encoding='utf8'),
            ensure_ascii=False,
            indent=2,
        )
    yield line_error_is_on(view, error)


def fix_disable_cspell_error(error, view):
    line = line_error_is_on(view, error)
    yield add_at_eol(
        ('  # cspell:disable-line'
         if '#' not in line.text.rstrip() else ' cspell:disable-line'),
        line,
    )
