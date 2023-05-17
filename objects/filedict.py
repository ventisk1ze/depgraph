from typing import TypedDict, Tuple


class FileDict(TypedDict):
    file_name: str
    imports: Tuple(str, str)
    file_path: str