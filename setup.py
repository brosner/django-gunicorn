import codecs
import os

from setuptools import find_packages, setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    name="django-gunicorn",
    version="0.1",
    description="simple Django app to replace runserver with Gunicorn",
    long_description=read("README.md"),
    url="https://github.com/brosner/django-gunicorn",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "gunicorn>=19.0.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
