import setuptools
import easynewsletter as enl


long_description = open("README.md").read()
install_requires = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name="easynewsletter",
    packages=["easynewsletter"],
    version=enl.__version__,
    description=enl.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=enl.__source__,
    author=enl.__author__,
    author_email=enl.__contact__,
    license=enl.__license__,
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Database",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=install_requires,
    platforms=["Linux", "Windows", "MacOS"],
    keywords=["newsletter scheduler red-mail"],
    project_urls={
        "Docs": "https://easynewsletter.readthedocs.io",
    },
)
