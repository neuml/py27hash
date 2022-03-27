# pylint: disable = C0111
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    DESCRIPTION = f.read()

setup(
    name="py27hash",
    version="1.1.0",
    author="NeuML",
    description="Python 2.7 hashing and iteration in Python 3+",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/neuml/py27hash",
    project_urls={
        "Documentation": "https://github.com/neuml/py27hash",
        "Issue Tracker": "https://github.com/neuml/py27hash/issues",
        "Source Code": "https://github.com/neuml/py27hash",
    },
    download_url="https://pypi.org/project/py27hash/",
    license="MIT License: http://opensource.org/licenses/MIT",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    keywords="python hash iteration migration",
    python_requires=">=2.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries"
    ])
