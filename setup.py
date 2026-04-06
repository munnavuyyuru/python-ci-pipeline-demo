"""Setup configuration for python-ci-pipeline-demo package."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-ci-pipeline-demo",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Production-grade CI pipeline demonstration with comprehensive testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/python-ci-pipeline-demo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "pytest-html>=4.1.1",
            "black>=23.12.1",
            "isort>=5.13.2",
            "flake8>=7.0.0",
            "pylint>=3.0.3",
            "mypy>=1.8.0",
            "bandit>=1.7.6",
            "safety>=2.3.5",
        ],
    },
)
