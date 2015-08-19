from setuptools import setup

import os


def Readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), "r").read()

setup(
    name='pycache',
    packages=['pycache'],
    version='0.5',
    description='Pythonic way of Caching Computations',
    long_description = Readme(),
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/pyhttp.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    install_requires = ['six'],
    include_package_data=True,
    license='MIT License',
)