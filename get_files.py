import os
from typing import List

def get_files(directory: str) -> List[str]:
    all_files = []
    for parent_path, _, filenames in os.walk(directory):
        for f in filenames:
            all_files.append(os.path.join(parent_path, f))
    return [x for x in all_files if x.endswith('.py')]