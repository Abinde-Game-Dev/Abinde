from setuptools import setup

with open("README.md").read() as l:
    long_description = l

setup(
    name='Firestorm',
    version='0.0.1',
    install_requires=[
        'pygame>=2.1.2',
	'pyopengl',
	'threading',
        'importlib-metadata; python_version == "3.8"',
    ],
    long_description=long_description,
    url="https://github.com/desvasicek/Firestorm",
    author="desvasicek",
    keywords="OpenGL pygame python game-engine module easy",
    license="MIT",
    description="Firestorm is an easy-to-use python module for pygame.",
    long_description_context_type="text/markdown",
    classifiers=[
	    "Development Status :: 2 - Pre-Alpha",
	    "License :: OSI Approved :: MIT License",
	    "Natural Language :: English",
	    "Programming Language :: Python :: 3 :: Only",
	    "Topic :: Games/Entertainment",
	    "Topic :: Utilities",
	    "Intended Audience :: Developers",
    ]
)
