from setuptools import setup, find_packages

setup(
    name='vorteex',
    packages=find_packages(),
    version='0.0.1',
    license='gpl-3.0',
    author='Adrian',
    author_email='adrian@syberfy.com',
    description='Python library and CLI tool for Vorteex (https://vorteex.io)',
    url='https://github.com/SYBERFY/vorteex-cli',
    scripts=['./scripts/vorteex'],
    install_requires=[
        'pyinquirer',
        'requests',
        'validators'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)
