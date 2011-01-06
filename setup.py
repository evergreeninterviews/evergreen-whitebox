from setuptools import setup, find_packages


setup(
    name = "evergreeninterviews.com",
    version = "1.0",
    author = "ElevenCraft Inc. and contributors",
    author_email = "matt@11craft.com",
    description = "",
    long_description = open("README").read(),
    license = "GPLv3",
    url = "http://evergreeninterviews.com/",
    packages = find_packages(exclude=[
        'bin',
    ]),
    classifiers = [
    ]
)
