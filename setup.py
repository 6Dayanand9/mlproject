from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT_E='-e .'
def get_requirements(file_path:str)-> List[str]:
    # this will rwturn the list of requiremnts
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)

setup(
    name="mlproject",
    version='0.0.1',
    author="Dayanand Nimbalkar",
    author_email="6nimbalkardayanand9@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
    )