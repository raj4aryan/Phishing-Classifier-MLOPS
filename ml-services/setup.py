from setuptools import find_packages, setup
from typing import List

def get_requirements()->List:
    try:
        reqrList:List[str] = []
        with open("requirements.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if(requirement and requirement != "-e ."):
                    reqrList.append(requirement)
        return reqrList
    except FileNotFoundError:
        print("Error: requirements.txt file is missing")


setup(
    name="setup-network-security",
    version="0.0.1",
    author="Raj",
    packages=find_packages(),
    install_requires=get_requirements()    
)