from setuptools import find_packages, setup

package_name = 'tdmpc2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[],
    install_requires=[
        'setuptools',
        'gymnasium'
        ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
