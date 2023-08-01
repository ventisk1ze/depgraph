import os
import json
from project import Project

p = Project(r'C:\Users\User\Desktop\Programming\rosreestr2coord')

with open('./test.json', 'a') as file:
    json.dump(p.get_imports(), file)