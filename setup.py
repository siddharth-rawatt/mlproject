# It is resposible in creating my machine learning applications as a package and eveen deploy in python pypy
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requiremnts = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


# it is the metadata information about the entire project
setup(
    name="ML-PROJECT",
    version="0.0.1",
    author="Siddharth",
    author_email="siddharth.rawatt@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

# whenever, find package is running it goes and sees in how many folders do we have the file __init__.py,
# so it starts considering src as a package itself and then we can import this and use it wherever we want
