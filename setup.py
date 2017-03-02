import os

from setuptools import find_packages
from setuptools import setup

setup(
    name='deep-learning-utils',
    version='0.0.1',
    description='A common utils and tools for deep learning projects.',
    url='https://github.com/datasart/deep-learning-utils.git',
    author='Trang Mai Xuan',
    keywords='Deep Learning Utils',
    packages=find_packages(exclude=["tests.*", "tests"])
)
