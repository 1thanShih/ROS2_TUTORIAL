from setuptools import find_packages, setup

package_name = 'ros_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ethan_Shih',
    maintainer_email='smartshithan1620.en12@nycu.edu.tw',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'draw_circle = ros_test.draw_circle:main',
            'hello_node = ros_test.hello_ros:main',
       ],
    },
)
