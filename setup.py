from setuptools import setup, find_packages

setup(
    name='qbot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy'
    ]
)