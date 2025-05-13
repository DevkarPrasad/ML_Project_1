from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str) -> list[str]:
    """
    This function returns a list of requirements from the given file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Prasad',
    author_email = 'devkarprasad00@gmmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'seaborn']
)