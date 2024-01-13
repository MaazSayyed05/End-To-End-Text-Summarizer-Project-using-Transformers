
import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'

REPO_NAME = "End-to-End-Text-Summarizer-using-Transformers"
AUTHOR_USER_NAME = "Maaz Sayyed"
SRC_REPO = "Text_Summarizer"
AUTHOR_EMAIL = "maazsayyed05@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "End-to-End Text Summarizer Project using Transformers.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/MaazSayyed05/End-To-End-Text-Summarizer-Project-using-Transformer",
    project_urls={
        "Bug Tracker": "https://github.com/MaazSayyed05/End-To-End-Text-Summarizer-Project-using-Transformer/issues",
    },
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where='src')
)





