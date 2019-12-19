
from setuptools import setup, find_namespace_packages

from qtoggleserver.rpigpio import VERSION


setup(
    name='qtoggleserver-rpigpio',
    version=VERSION,
    description='qToggleServer driver for Raspberry Pi GPIOs',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages(),

    install_requires=[
        'RPi.GPIO'
    ]
)
