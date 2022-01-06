import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrmanent",
    version="1.1.0",
    author="Sergio Abad",
    author_email="sergio.abad@bytelix.com",
    description="Make all your classes permanent in a flash",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/sergioteula/pyrmanent",
    keywords=["python", "persistence", "class", "permanent"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.0",
)
