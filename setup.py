import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
    name='copyscape_api',  
    version='0.1',
    scripts=[],
    author="Vladimir Kadalashvili",
    author_email="Kadalashvili.Vladimir@gmail.com",
    description="Python client for Copyscape API",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/selentium/copyscape-api-client",
    license="MIT",
    packages=['copyscape_api'],
    install_requires=[
        "requests",
        "xmltodict",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )