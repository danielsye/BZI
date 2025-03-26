from setuptools import setup, find_packages

setup(
    name='file_merger',
    version='0.1',
    packages=find_packages(),
    description='A simple package to merge CSV and Excel files from a directory.',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    url='https://github.com/BZI/BZI/utils/file_merger',  # Your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
