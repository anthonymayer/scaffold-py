from setuptools import find_packages
from setuptools import setup

setup(
    name='Scaffold',
    description='Simple project scaffolding for Python',
    url='https://github.com/anthonymayer/scaffold-py',
    version='0.1.6',

    platforms='all',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'pyscaffold = scaffold.__main__:main',
        ],
        'virtualenvwrapper.project.template': [
            'base = scaffold.virtualenvwrapper:template',
        ],
    },
)
