from setuptools import setup
import setuptools

setup(
	name="diffusion2D_sod",
	version="1.1",
	author="Sinan Ozgun Demir",
	description="2D thermal diffusion simmulation",
	url="https://github.com/sozgundemir/diffusion2D",
	package_dir={"": "diffusion2D_sod"},
	packages=setuptools.find_packages(where="diffusion2D_sod"),
	install_requires=["<dependencies>"]
	entry_points={
	  'console_scripts': ['diffusion2D_sod = ./src/diffusion2D.py']
	}
)