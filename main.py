import os
import json
import argparse
from project import Project

parser = argparse.ArgumentParser(
    prog='Depgraph',
    description='Python module for drawing graph dependencies',
    epilog='Have fun'
)

parser.add_argument('project_path')

p = Project(r'C:\Users\User\Desktop\Programming\pm4py-core')

with open('./test.json', 'w') as file:
    json.dump(p.get_imports(), file, indent=4, ensure_ascii=False)