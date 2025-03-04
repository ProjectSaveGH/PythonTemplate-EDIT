from setuptools import setup, find_packages

setup(
    name='TCPYLib',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        "requests", #==2.26.0
        "asciimatics", #==1.12.0
        "rich" #==10.12.0
    ],
    author='Alexander Schwarz',
    author_email='alexanderschwarz148@gmail.com',
    description='A collection of utilities and functions for various tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrcool7387/TCPYlib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)