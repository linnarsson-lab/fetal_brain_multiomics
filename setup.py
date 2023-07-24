from setuptools import setup, find_packages

__version__ = "0.0.1"
setup(
	name="fetalxbrainxmultiomics",
	version=__version__,
	packages=find_packages(),
	install_requires=[
		'loompy',
		'numpy',
		'scikit-learn',
		'seaborn',
		'numba==0.51.0',
                'deeplift',
                'twobitreader',
		'captum',
                'scipy',
		'statsmodels',
		'torch',
                'pytorch-lightning',
                'pybedtools',
                'biopython'
		## Install through bioconda ucsc-bedgraphtobigwig ucsc-genepredtobed ucsc-gtftogenepred ucsc-bigwigaverageoverbed
		],
	include_package_data=True,
	author="Linnarsson Lab",
	author_email="camiel.mannens@ki.se",
	description="Notebooks and data accompanying the 'Dynamics of chromatin accessibility during human first-trimester neurodevelopment' paper",
	license="MIT",
	url="https://github.com/linnarsson-lab/fetal_brain_multiomics",
)
