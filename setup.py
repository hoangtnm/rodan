import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

REQUIRED_PACKAGES = [
    "torch>=1.8",
    "torchvision>=0.9",
    "torchaudio",
    "scikit-learn",
    "scipy",
    "jupyterlab",
    "matplotlib",
    "Cython",
]

setup(
    name="rodan",
    version="0.0.1",
    description="An Open Source AI Toolkit for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hoangtnm/rodan",
    author="Tran N.M. Hoang",
    author_email="hoangtnm.cse@gmail.com",
    license="Apache License, Version 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=find_packages("src"),
)
