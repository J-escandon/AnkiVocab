from setuptools import setup, find_packages\n\nsetup(\n    name='ankivocab',\n    version='0.1',\n    packages=find_packages(where='src'),\n    package_dir={'': 'src'},\n    install_requires=[\n        # Add dependencies here\n    ],\n)\n