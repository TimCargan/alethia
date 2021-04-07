from setuptools import find_packages, setup

setup(
    name="aletheia",
    packages=[package for package in find_packages() if package.startswith("aletheia")],
    install_requires=["google-cloud-firestore", "protobuf"],
    version="0.0.1-alpha",
    description="Experiment tracking library",
    author="timcargan",
    license="None"
)