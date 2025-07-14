from setuptools import setup, find_packages

def get_requirements():
    requirement_lst = []
    try:
        with open("requirements.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e':
                    requirement_lst.append(requirement)
        return requirement_lst
    except FileNotFoundError:
        print("requirements.txt file not found")

setup(
    name='phising-detection',
    version='0.0.1',
    author='Kishore',
    author_email='kishore007008ya@gmail.com',
    packages=find_packages(),
    requires=get_requirements()
)
