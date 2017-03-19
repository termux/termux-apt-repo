from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name = 'termux-apt-repo',
    version = '0.2',
    license = 'MIT',
    description = 'Script to create Termux apt repositories',
    long_description = readme(),
    author = 'Fredrik Fornwall',
    author_email = 'fredrik@fornwall.net',
    url = 'https://github.com/termux/termux-apt-repo',
    scripts = ['termux-apt-repo'],
    classifiers = (
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    )
)
