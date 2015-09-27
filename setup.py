from setuptools import setup, find_packages

setup(
    name="blackwidow",
    version="0.1.5",
    author="Madison May",
    author_email="madison@indico.io",
    packages=find_packages(),
    install_requires=[
        "networkx==1.10"
    ],
    package_dir={"blackwidow": "blackwidow"},
    package_data={
        "blackwidow": ["viz/static/*"]
    },
    description="""
        Visualizing and refactoring python project import graphs.
    """,
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/madisonmay/blackwidow"
)
