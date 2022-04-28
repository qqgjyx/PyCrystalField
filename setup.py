import setuptools

setuptools.setup(
    name='PyCrystalField',
    version='2.3.4',    
    description='Code to calculate the crystal field Hamiltonian of magnetic ions.',
    url='https://github.com/asche1/PyCrystalField/tree/for_PyPi',
    author='Allen Scheie',
    author_email='scheieao@ornl.gov',
    license='GNU GPL',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['matplotlib',
                      'scipy',
                      'numba', 'numpy'   
                      ],
    package_data={'pcf_lib':['*',]}
)