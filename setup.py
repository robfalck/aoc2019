from distutils.core import setup
from setuptools import find_packages


setup(name='aoc2019',
    version='0.0.1',
    description='Solutions to the Advent of Code - 2019',
    url='https://github.com/robfalck/aoc2019',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    license='Apache License',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.14.1',
        'scipy>=0.19.1',
        'networkx'
    ],
    zip_safe=False,
)
