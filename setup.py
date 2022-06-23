from setuptools import setup, find_packages

setup(
    name="bottest",
    version="0.22.8",
    packages=find_packages(),
    package_data={
        "bottest": ['data/licences/*.lcs', "data/*"]
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bottest=bottest:main',
        ]
    }

)
