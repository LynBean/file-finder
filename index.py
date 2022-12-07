"""Walks through the root directory and returns a list of files that match the filename."""

import os
import platform
import time

def walk(root: str, filename: str, debug: bool = False) -> list:
    """Walks through the root directory and returns a list of files that match the filename.

    Args:
        root (str): root directory to walk through
        debug (bool, optional): Defaults to False.

    Returns:
        list: List of paths of files that match the filename
    """
    javaw: list = []
    for path, _, files in os.walk(root):
        for file in files:
            if debug:
                print(os.path.join(path, file))

            if filename not in file:
                continue

            javaw.append(os.path.join(path, file))

    return javaw

FILENAME = 'javaw.exe'
root_list = [rf'{i}:\\' for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] if platform.system() == 'Windows' \
    else ['/']

for item in root_list:
    if not os.path.exists(item):
        continue

    start_time = time.time()
    print(f'\nSearching for {FILENAME} in: {item}\n')
    print('\n'.join(walk(item, FILENAME, debug=False)))
    print(f'\nFinished: {item} in {time.time() - start_time:,.2f} seconds\n')
