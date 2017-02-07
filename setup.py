#!/usr/bin/env python3

from setuptools import setup


setup(
    name='plover_palantype_system',
    version='0.2.0',
    description='Palantype system for Plover',
    author='Ted Morin',
    author_email='morinted@gmail.com',
    license='GNU General Public License v2 or later (GPLv2+)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop'
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'plover>=4.0.0.dev0',
    ],
    packages=[
        'plover_palantype_system',
    ],
    include_package_data=True,
    py_modules=[
        'plover_palantype_machine'
    ],
    entry_points='''
    [plover.system]
    Possum Palantype=plover_palantype_system.system

    [plover.machine]
    Palantype=plover_palantype_machine:Palantype

    ''',
    zip_safe=True,
)
