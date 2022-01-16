from setuptools import setup, find_packages

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version = "0.0.1",
    author = "GuptAmit725",
    description = "A basic simple project for DVC ML pipeline.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/GuptAmit725/simple-dvc-project",
    author_email="amitinger19@gmail.com",
    package_dir= {"":"src"},
    packages = find_packages(where="src"),license="GNU",
    python_requires = ">=3.7",
    install_requires = [
        'dvc',
        'dvc[gdrive]',
        'dvc[s3',
        'pandas',
        'scikit-learn'
    ]
)