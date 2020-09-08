from distutils.core import setup


setup(
    name='spell-checker',
    version='1.0',
    description='Simple spell checking API',
    author='Ellis Andrews',
    packages=['spell-checker'],
    install_requires=[
        'Flask'
    ]
)
