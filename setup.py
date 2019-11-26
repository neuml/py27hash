# pylint: disable = C0111
from setuptools import setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(name="py27hash",
      version="1.0.1",
      author="David Mezzetti",
      description="Python 2.7 hashing and iteration in Python 3+",
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://davidmezzetti.github.io/py27hash",
      project_urls={
          "Documentation": "https://davidmezzetti.github.io/py27hash",
          "Issue Tracker": "https://github.com/davidmezzetti/py27hash/issues",
          "Source Code": "https://github.com/davidmezzetti/py27hash",
      },
      download_url="https://pypi.org/project/py27hash/",
      license="MIT License: http://opensource.org/licenses/MIT",
      packages=["py27hash"],
      package_dir={"": "src/python/"},
      keywords="python hash iteration migration",
      python_requires=">=2.7",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Libraries"
      ])
