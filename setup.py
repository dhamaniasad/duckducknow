from setuptools import setup
import duckducknow

setup(
    name='duckducknow',
    version=duckducknow.__version__,
    description='Search DuckDuckGo right from your terminal',
    author='Asad Dhamani',
    author_email='dhamaniasad+code@gmail.com',
    url='https://github.com/dhamaniasad/duckducknow',
    license='Unlicense',
    py_modules=['duckducknow'],
    entry_points={
        'console_scripts': [
            'duck = duckducknow:command_line_runner',
        ]
    }
)
