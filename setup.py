from setuptools import setup, find_packages

setup(
    name="expense-tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "expense-tracker=expense_tracker.expense_tracker:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple command-line expense tracker application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/expense-tracker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)