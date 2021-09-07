import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

setuptools.setup(
    name="SGC-SDK.py",
    version="0.0.1",
    author="Tsukikoh",
    description="This is for super global chat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SGC-SDK/SGC-SDK.py",
    install_requires=_requires_from_file('rqs.txt'),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
