from setuptools import setup, find_packages

setup(
    name="clag",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[
        "textx>=4.0.1",
        "jinja2>=3.1.4",
        "click>=8.1.7",
        "antlr4-python3-runtime>=4.13.2",
        "maspy-ml>=0.5.6",
    ],
    entry_points={
        'console_scripts': [
            'clag=clag.cli:build',
        ],
    },
    python_requires=">=3.10",
) 