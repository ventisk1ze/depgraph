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
        self.file_paths = [x for x in all_files if x.endswith('.py') and 'env' not in x]
        self.import_names = [self._get_file_name(x) for x in self.file_paths]

    @staticmethod
    def _get_file_name(file):
        return file.split('\\')[-1].split('.')[0]
    
    def _get_file_imports(self, file_path: str) -> FileDict:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as pythonfile:
            imports = [
                line.strip().split(' ')[1]
                for line in pythonfile.readlines() 
                if line.startswith('import ') or line.startswith('from ')
            ]
            imports = [x.split('.')[-1] if '.' in x else x for x in imports]
        
        file: FileDict = {
            'file_name': self._get_file_name(file_path),
            'imports': [
                ImportDict(
                    import_name=import_name, 
                    import_type= 'internal' 
                    if import_name in self.import_names else 'external')
                for import_name in imports
                ],
            'file_path': file_path
            }
        
        return file
    
    def get_imports(self) -> dict:
        self.imports = {self._get_file_name(path):self._get_file_imports(path) for path in self.file_paths}
        return self.imports