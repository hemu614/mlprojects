from setuptools import find_packages, setup
from typing import List

def get_requiremnts(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements




setup(
name = 'mlproject',
version = '0.0.1',
author = 'Hemant Mishra',
author_email= 'hemantmishra614@gmail.com',
packages=find_packages(),
install_requires=get_requiremnts('requirements.txt')
)