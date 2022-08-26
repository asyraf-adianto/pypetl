import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="pypetl",
    version="0.0.3",
    author="asyraf-adianto",
    author_email="asyraf.adianto@gmail.com",
    packages=["pypetl"],
    description="Python ETL Tools",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/asyraf-adianto/pypetl",
    license='MIT',
    python_requires='>=3.9',
    install_requires=[
        'petl',
        'redshift-connector',
        'psycopg2-binary',
        'paramiko',
        'sshtunnel'
    ]
)