#! /usr/bin/env python3

"""
This is a simple script to sort games with multiple discs into folders.
"""

import re

from natsort import os_sorted
from pathlib import Path

multi_disc_games = Path("./").glob("*(Disc*")

for game in os_sorted(multi_disc_games):
    print("Processing " + game.name)
    _dir_name = Path(re.sub(r".\(Disc.[0-9]\)", "", game.stem))
    _dir_name.mkdir(exist_ok=True)
    game.rename(_dir_name / game)
