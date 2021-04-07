from setuptools import find_packages, setup

pkgs = [package for package in find_packages() if package.startswith("aletheia")]
setup(
    name="aletheia",
    packages=pkgs,
    install_requires=["google-cloud-firestore", "protobuf"],
    version="0.0.1-alpha",
    description="Experiment tracking library",
    author="timcargan",
    license="None",
    python_requires='>3.7.0'
)