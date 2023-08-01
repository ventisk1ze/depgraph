from typing import TypedDict, List
from importdict import ImportDict


class FileDict(TypedDict):
    file_name: str
    imports: List[ImportDict]
    file_path: str