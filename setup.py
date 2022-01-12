from setuptools import find_packages, setup
setup(
    name='honeygain',
    packages=find_packages(),
    version='0.0.1',
    description='A python library to interact with the Honeygain API',
    author='Woodie',
    url='https://github.com/Woodie-07/honeygain.py',
    install_requires=['requests'],
)