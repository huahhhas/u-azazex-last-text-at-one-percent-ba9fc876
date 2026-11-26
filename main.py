#!/usr/bin/env python3
"""Last Text at One Percent — the final text a dying phone sends at 1% battery."""

# Revise 2 (fix): restore the line constant the helper returns.
LINE = "Battery at 1%. Tell the group chat I left them on read on purpose \u2014 I did. Delete my search history. It's been an honour. Goodbye, cruel pocket."


# Revise 2: move the print behind a helper; behaviour and output unchanged.
def get_line():
    return LINE


print(get_line())
