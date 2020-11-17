import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'Torcs_5'
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[('share/ament_index/resource_index/packages', ['resource/' + package_name]), ('share/' + package_name, ['package.xml']), (os.path.join('share', package_name), glob('launch/*.launch.py'))],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TODO: Your name',
    maintainer_email='TODO: Your email',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={'console_scripts': ['splash_server = Torcs_5.__init__:main', 'default_build_unit = Torcs_5.default_build_unit_exec:main'],},
)
