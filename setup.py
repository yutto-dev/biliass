import os
import sys
from shutil import rmtree

from biliass.__version__ import VERSION as biliass_version
from setuptools import setup, Command, find_packages

here = os.path.abspath(os.path.dirname(__file__))


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s: str):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Generating stub files...")
        os.system("touch biliass/py.typed")
        os.system("stubgen ./biliass/biliass.py -o .")

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(biliass_version))
        os.system("git push --tags")

        sys.exit()


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        desc = f.read()
    return desc


setup(
    name="biliass",
    version=biliass_version,
    description="将 B 站 XML 弹幕转换为 ASS 弹幕",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="bilibili danmaku xml ass",
    author="m13253, Nyakku Shigure",
    url="https://github.com/ShigureLab/biliass",
    license="GPLv3",
    packages=find_packages(),
    package_data={"biliass": ["py.typed", "*.pyi", "**/*.pyi"]},
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.6.0",
    setup_requires=["wheel"],
    install_requires=["protobuf"],
    entry_points={"console_scripts": ["biliass = biliass.__main__:main"]},
    cmdclass={
        "upload": UploadCommand,
    },
)
