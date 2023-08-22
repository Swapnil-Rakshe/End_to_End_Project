# Import necessary functions from the setuptools library

from setuptools import find_packages,setup
from typing import List

# Define a constant string '-e .' used for local editable installation in requirements
HYPEN_E_DOT='-e .'

# Define a function to retrieve the list of requirements from a file
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    
    # Open the requirements file and read its content line by line
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        
        # Remove newline characters from each requirement and create a list
        requirements=[req.replace("\n","") for req in requirements]

        # If '-e .' exists in requirements, remove it from the list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Define project details and dependencies using the setup function
setup(
    name='END_END_PROJECT',            # Set the name of the project
    version='0.0.1',                   # Set the project version
    author='Swapnil',                  # Set the author's name
    author_email='swapnil.rakshe1997@gmail.com',  # Set the author's email
    packages=find_packages(),          # Automatically find and include all project packages
    install_requires=get_requirements('requirements.txt')  # Retrieve requirements from file
)