from setuptools import setup, find_packages

setup(
    name="nmigen_cocotb",
    version="0.1",
    author='Andres Demski',
    py_modules=['nmigen_cocotb'],
    setup_requires=['cocotb'],
    install_requires=[
        'cocotb-test',
        'nmigen'
    ]
)
