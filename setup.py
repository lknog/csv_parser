from setuptools import setup

setup(
    name='CSV Parser',
    version='0.0.1',
    py_modules=['csv_parser'], # no .py
    install_requires=['Click', 'pandas'],
    entry_points='''
        [console_scripts]
        csv_parser=csv_parser:cli
    ''',
)