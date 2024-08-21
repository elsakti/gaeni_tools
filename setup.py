from setuptools import setup, find_packages

setup(
    name="gaeni_tools",
    version="0.0.1",
    description="Gaeni Toolkit For Us",
    url="https://github.com/elsakti/gaeni_tools",
    long_description_content_type="text/markdown",
    author="ggusakti",
    packages=find_packages(),
    install_requires=['crewai', 'crewai-tools'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)