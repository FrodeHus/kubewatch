import setuptools

from os import path
dir = path.abspath(path.dirname(__file__))
with open(path.join(dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="kubewatch",
    version="1.0b1",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'kwatch=kubewatch.__main__:main'
        ]
    },
    author="Frode Hus",
    author_email="frode.hus@outlook.com",
    description="Simple utility for getting an overview of what is running in a kubernetes cluster",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frodehus/kubewatch",
    python_requires='>=3.6',
    install_requires=[
        "kubernetes>=11.0.0b2",
        "pyinquirer",
        "prettytable",
        "adal",
        "colorama",
    ],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
