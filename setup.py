from setuptools import setup, find_packages

setup(
    name="spider",
    version="0.1.0",
    author="Madison May",
    author_email="madison@indico.io",
    packages=find_packages(),
    install_requires=[],
    description="""
        Visualizing and refactoring python project import graphs.
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/madisonmay/spider"
)