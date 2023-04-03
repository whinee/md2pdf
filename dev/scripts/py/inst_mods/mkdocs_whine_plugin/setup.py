from setuptools import find_packages, setup

setup(
    name="mkdocs_whine_plugin",
    packages=find_packages(),
    entry_points={"mkdocs.plugins": ["whine = main:MainPlugin"]},
)
