import os
from typing import List
from objects.importdict import ImportDict
from objects.filedict import FileDict

class Project():
    def __init__(self, directory) -> None:
        all_files = []
        for parent_path, _, filenames in os.walk(directory):
            for f in filenames:
                all_files.append(os.path.join(parent_path, f))
        self.file_paths = [x for x in all_files if x.endswith('.py')]
        self.import_names = [x.split('\\')[-1].split('.')[0] for x in self.file_paths]

    def _get_file_imports(self, file_path: str) -> List[str]:
        with open(file_path, 'r') as pythonfile:
            imports = [
                line.strip().split(' ')[1] 
                for line in pythonfile.readlines() 
                if line.startswith('import') or line.startswith('from')
            ]
        file: FileDict = {
            'file_name': file.split('\\')[-1].split('.')[0],
            'imports': [
                ImportDict(
                    import_name=import_name, 
                    import_type= 'internal' 
                    if import_name in self.import_names else 'external')
                for import_name in imports
                ],
            'file_path': file_path
            }
    