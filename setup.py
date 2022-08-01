from setuptools import setup

setup(
    name='Pytine',
    version='0.0.2',
    install_requires=[
        'pygame>=2.1.2',
	'pyopengl',
        'importlib-metadata; python_version == "3.8"',
    ],
    long_description=open("README.md").read(),
    url="https://github.com/desvasicek/Pytine",
    author="desvasicek",
    keywords="OpenGL pygame python game-engine module easy",
    license="MIT",
    description="Firestorm is an easy-to-use python module for pygame.",
    long_description_context_type="markdown",
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
