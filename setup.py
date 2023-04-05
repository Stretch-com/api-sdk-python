import os
from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

module = SourceFileLoader("version", os.path.join("stretch", "version.py")).load_module()

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
install_requires = ["fastapi >=0.85", "tortoise-orm[asyncpg]>=0.19.2"]


# with open('requirements.txt') as fp:
#    for line in fp.readlines():
#        if (line != ''):
#            install_requires.append(line)

# print(install_requires)


setup(
    name="stretchcore",
    version=module.__version__,
    author=module.__author__,
    author_email=module.team_email,
    license=module.package_license,
    description=module.package_info,
    long_description="""
# Stretch API support library (development)
""",
    platforms="all",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    project_urls={
        "Documentation": "https://api.stretch.com/",
        "Tracker": "https://api.stretch.com/issues/",
    },
    packages=find_packages(exclude=["tests"]),
    # package_data={'stretchcore': ['py.typed']},
    install_requires=install_requires,
    python_requires=">=3.9, <4",
    extras_require={
        "develop": [
            "pytest",
            "flake8",
            "isort",
            "black",
        ]
    },
)
