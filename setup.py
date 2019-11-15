"""Setup script for extension."""

from setuptools import setup


setup(
    name='grow-ext-translation',
    version='1.0.0',
    license='MIT',
    author='Grow Authors',
    author_email='hello@grow.io',
    include_package_data=True,
    packages=[
        'translation',
    ],
    package_data={
        'translation': ['dist/*.js', 'dist/*.css']
    }
)
