import io
import os
import re

import setuptools



###############################################################################

META_PATH = os.path.join("src", "qutty", "__init__.py")
KEYWORDS = ["gui", "applications"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
INSTALL_REQUIRES = [
    "importlib-metadata==4.11.4",
    "PyQt5==5.15.6",
    "PyQt5-Qt5==5.15.2",
    "PyQt5-sip==12.10.1",
    "zipp==3.8.0",
]
EXTRAS_REQUIRE = {
    "docs": [
    ],
    "tests": [
    ],
    "release": [
    ],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"]



###############################################################################

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with io.open(os.path.join(HERE, *parts), encoding="utf-8") as f:
        return f.read()



META_FILE = read(META_PATH)

def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))



if __name__ == "__main__":
    setuptools.setup(
        name=find_meta("title"),
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("uri"),
        version=find_meta("version"),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        long_description=read("README.rst"),
        long_description_content_type='text/x-rst',
        packages=setuptools.find_packages(where="src"),
        package_dir={"": "src"},
        package_data={
            "": ["*.png"],
        },
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        entry_points={                                                                    
            'console_scripts': [
                'qutty=qutty.__main__:main',
            ],
        },
    )

