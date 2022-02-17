import os
from setuptools import setup

LONG_DESCRIPTION = """
The wq command line tool.
"""


def readme():
    try:
        readme = open("README.md")
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()


def create_wq_namespace():
    """
    Generate the wq namespace package
    (not checked in, as it technically is the parent of this folder)
    """
    if os.path.isdir("wq"):
        return
    os.makedirs("wq")
    init = open(os.path.join("wq", "__init__.py"), "w")
    init.write("__import__('pkg_resources').declare_namespace(__name__)")
    init.close()


create_wq_namespace()

setup(
    name="wq.build",
    use_scm_version=True,
    author="S. Andrew Sheppard",
    author_email="andrew@wq.io",
    url="https://wq.io/",
    license="MIT",
    packages=[
        "wq",
        "wq.build",
        "wq.build.commands",
        "wq.build.management",
        "wq.build.management.commands",
    ],
    package_dir={
        "wq.build": ".",
        "wq.build.commands": "./commands",
        "wq.build.management": "./management",
        "wq.build.management.commands": "./management/commands",
    },
    install_requires=[
        "click>8",
        "django-click",
        "PyYAML",
        "Pillow",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
    namespace_packages=["wq"],
    entry_points="""
       [console_scripts]
       wq=wq.build:wq
       [wq]
       wq.build=wq.build.commands
    """,
    description=LONG_DESCRIPTION.strip(),
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Build Tools",
    ],
)
