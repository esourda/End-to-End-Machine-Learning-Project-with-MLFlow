import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desription = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Project-with-MLFlow"
AUTHOR_USER_NAME = "esourda"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "sourav.das.besu@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for ml app",
    long_description=long_desription,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)