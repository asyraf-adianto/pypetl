import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="pypetl-canary",
    version="0.0.10",
    author="asyraf-adianto",
    author_email="asyraf.adianto@gmail.com",
    packages=["pypetl_canary"],
    description="Python ETL Tools",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/asyraf-adianto/pypetl",
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'petl',
        'redshift-connector',
        'psycopg2-binary',
        'paramiko',
        'sshtunnel'
    ]
)