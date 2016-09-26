from setuptools import find_packages, setup

setup(
    name='hotelspro_client',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/huseyinkabil/hotelspro-client',
    license='MIT',
    author='Hüseyin Kabil',
    author_email='hsynkabil@gmail.com',
    description='Hotelspro.com api client',
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
