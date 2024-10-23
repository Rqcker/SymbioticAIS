from setuptools import setup, find_packages


setup(
    name='sais',
    version='0.3.3',
    packages=find_packages(),
    description='Symbiotic Artificial Immune Systems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Junhao',
    author_email='junhao.song23@imperial.ac.uk',
    url='https://github.com/Rqcker/SymbioticAIS',
    install_requires=[
        # requires list and version
        'numpy>=1.23.5'
    ]
)
