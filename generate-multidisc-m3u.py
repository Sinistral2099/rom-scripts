#! /usr/bin/env python3

from natsort import os_sorted
from pathlib import Path

"""
This is a script to create m3u playlists for multiple discs in pre-existing folders.
"""

multi_disc_game_dirs = Path("./").glob("*")

# Sort the directories by name

for dir in os_sorted(multi_disc_game_dirs):
    if dir.is_dir():
        print("Processing " + dir.name)
        roms = Path(dir).glob("*")

        playlist_name = dir.name + ".m3u"

        with open(dir / playlist_name, "w") as playlist:
            for rom in os_sorted(roms):
                if not rom.name == playlist_name:
                    playlist.write(rom.name + "\n")

print("Done.")
