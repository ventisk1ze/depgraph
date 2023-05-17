from typing import TypedDict, Tuple


class ImportDict(TypedDict):
    import_name: str
    import_type: str
    full_path: str

class FileDict(TypedDict):
    file_name: str
    imports: Tuple(str, str)
    file_path: str