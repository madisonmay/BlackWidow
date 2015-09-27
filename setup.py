from setuptools import setup
setup(
    name="blackwidow",
    version="0.1.4",
    author="Madison May",
    author_email="madison@indico.io",
    packages=["blackwidow"],
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
    url="https://github.com/madisonmay/spider"
)
