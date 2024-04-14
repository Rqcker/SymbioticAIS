from setuptools import setup, find_packages


setup(
    name='sais',
    version='0.1.0',
    packages=find_packages(),
    description='Symbiotic Artificial Immune Systems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Junhao',
    author_email='junhao.song23@imperial.ac.uk',
    url='https://github.com/Rqcker/SymbioticAIS',
    install_requires=[
        # requires list and version
        'requests>=2.23.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: CC-BY-4.0 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
