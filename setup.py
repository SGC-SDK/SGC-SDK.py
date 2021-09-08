from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="SGC-SDK",
    version="0.0.1",
    install_requires=requirements,
    description="Super Global Chat Library for Discord.py",
    long_description=readme,
    author="SGC Development Team",
    url="https://github.com/SGC-SDK/SGC-SDK.py",
    project_urls={
        "Issue tracker": "https://github.com/SGC-SDK/SGC-SDK.py/issues"
    },
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Development Status :: 1 - Planning"
    ]
)
