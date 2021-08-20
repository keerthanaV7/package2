import setuptools
import os

setuptools.setup(
	name = "check2",
	version="2.0",
	author="Keerthana",
	description="Package 2",
	classifiers = [
		"Programming Languages :: Python :: 3",
		"Operating System :: OS Independent"],
	python_requires ='>=3.6',
	install_requires=['pandas==1.1.5'],
	dependency_links=""
	
)