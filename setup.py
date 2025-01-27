import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.2.6'
PACKAGE_NAME = 'shap-hypetune-atpe'
AUTHOR = 'Sergey Bondarkov'
AUTHOR_EMAIL = 'rosebush@duck.com'
URL = 'https://github.com/sergey-bondarkov/shap-hypetune_atpe'

LICENSE = 'MIT'
DESCRIPTION = "Fork of Marco Cerliani's shap-hypetune package to use ATPE in feature selection"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'numpy',
    'scipy',
    'scikit-learn>=0.24.1',
    'shap>=0.39.0',
    'hyperopt==0.2.5',
    'fasttreeshap'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      python_requires='>=3',
      packages=find_packages()
      )
