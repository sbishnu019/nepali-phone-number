import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepali-phone-number",
    version="0.0.2",
    author="Bishnu Sharma",
    author_email="sbishnu019@gmail.com",
    description="A package for nepali mobile number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbishnu019/nepali-phone-number",
    download_url='https://github.com/sbishnu019/nepali-phone-number/archive/v0.0.2.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
