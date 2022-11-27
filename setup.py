from setuptools import setup, find_packages
import pathlib

# The directory containing this file
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# setup.py
setup(
    name='pycurtain',
    url='https://github.com/bin2ai/pycurtain',
    author='bin2ai',
    license='MIT',
    keywords='art, ai, deep learning, upscaling, img2img, text2img, style transfer, rest, rest api, wrapper',
    version='0.0.0',
    include_package_data=True,
    description='A community-maintained Python package for wrapping a variety of REST API calls for different AI art models.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'pillow>=9.3.0',
        'requests>=2.28.1',
        'stability-sdk>=0.2.9',
    ],
    extras_require={
        'dev': [
            'pytest>=7.2.0',
            'check-manifest>=0.48',
        ],
    },
    package_dir={'': 'src'},
    packages=find_packages(where="src"),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
