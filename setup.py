# encoding: utf-8
from setuptools import setup

import vcd


setup(
    name='pyvcd',
    version=vcd.__version__,
    author='Peter Grayson',
    author_email='jpgrayson@gmail.com',
    description='Python VCD file support.',
    long_description='\n\n'.join(
        open(f, 'rb').read().decode('utf-8')
        for f in ['README.rst', 'LICENSE.txt']),
    # url='https://',
    # download_url='https://',
    # license='',
    install_requires=['six'],
    packages=['vcd'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        # 'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Electronic Design Automation '
        '(EDA)',
    ],
)