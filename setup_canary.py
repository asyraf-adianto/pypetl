from setuptools import setup, find_packages
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setup(
    name="pypetl-canary",
    version="0.0.13",
    author="asyraf-adianto",
    author_email="asyraf.adianto@gmail.com",
    package_dir={'': '.'},
    packages=find_packages('.'),
    description="Python ETL Tools",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/asyraf-adianto/pypetl",
    license='MIT',
    python_requires='>=3.0',
    install_requires=[
        'petl',
        'redshift-connector',
        'psycopg2-binary',
        'paramiko',
        'sshtunnel'
    ]
)