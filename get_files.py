import os
from typing import List
from objects.importdict import ImportDict

def get_files(directory: str) -> List[str]:
    '''
    Get all .py files in project directory
    '''
    all_files = []
    for parent_path, _, filenames in os.walk(directory):
        for f in filenames:
            all_files.append(os.path.join(parent_path, f))
    return [x for x in all_files if x.endswith('.py')]

def get_preliminary_dict(directory: str) -> ImportDict:
    '''
    Yield ImportDicts with full path and module
    '''
    for file in get_files(directory):
        yield ImportDict(import_name = file.split('\\')[-1].split('.')[0], import_type = "", full_path = file)