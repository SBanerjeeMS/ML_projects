from setuptools import find_packages,setup
from typing import List
HYP_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    # returns list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ch.replace("\n","") for ch in requirements]
        if HYP_E_DOT in requirements:
            requirements.remove(HYP_E_DOT)
            
    return requirements
    
setup(
name = 'ML_projects',
version = '0.0.1',
author = 'Subhankar Banerjee',
author_email = 'sbannerd@Gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)