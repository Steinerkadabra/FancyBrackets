import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open("requirements.txt", "r") as fh:
#     requirements = fh.read().splitlines()

setuptools.setup(
    name="FancyBrackets", # Replace with your own username
    version="0.0.1",
    author="Thomas Steindl",
    author_email="thomas.steindl95@gmx.at",
    description="Python package to plot fancy brackets in Matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
