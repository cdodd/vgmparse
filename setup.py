from setuptools import setup, find_packages

setup(
    name='vgmparse',
    version='1.0.0',
    description='VGM (Video Game Music) file parser',
    url='https://github.com/cdodd/vgmparse',
    author='Craig Dodd',
    author_email='craig@dodd.io',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
)
