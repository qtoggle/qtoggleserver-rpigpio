
from setuptools import setup, find_namespace_packages


setup(
    name='qtoggleserver-rpigpio',
    version='1.0.0',
    description='qToggleServer driver for Raspberry Pi GPIOs',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages(),

    install_requires=[
        'RPi.GPIO'
    ]
)
