import setuptools

install_requires = [
    'con-fu',
]

extras_require = {
    'tests': [
        'pytest >=2.5.2,<2.6',
        'pytest-cov >=1.7,<2.0',
    ],
}

scripts = []

data_files = []

packages = []

setuptools.setup(
    name='infra-bp',
    version='1.0',
    url='https://github.com/balanced-ops/infra-bp',
    author='Balanced',
    author_email='dev@balancedpayments.com',
    description='Sets up Balanced infrastructure',
    long_description='',
    platforms='any',
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require['tests'],
    packages=packages,
    scripts=scripts,
    data_files=data_files,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    cmdclass={},
)
