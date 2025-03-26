from setuptools import setup, find_packages

setup(
    name='BZI', 
    version='0.1',
    packages=find_packages(),
    description='A simple DS package for some simple tasks.',
    author='Zherong Ye',
    author_email='danielsye@hearts-science.com',
    url='https://github.com/danielsye',
    install_requires=[
        'pandas',  
        'openpyxl',  
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
