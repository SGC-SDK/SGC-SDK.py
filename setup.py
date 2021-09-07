from setuptools import setup

setup(
    name='SGC-SDK.py',
    version="0.0.1",
    install_requires=["discord.py @ git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]"],
    description="Super Global Chat Library for Discord.py",
    long_description="",
    author='Tsukikoh',
    url="https://github.com/SGC-SDK/SGC-SDK.py",
    license='Apache License 2.0',
    classifiers=[
        "Development Status :: 1 - Planning"
    ]
)