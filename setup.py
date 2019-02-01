from distutils.core import setup

setup(
    name='VPN Connect',
    version='0.0.1',
    description='VPN Connect',
    packages=['vpnconnect'],
    entry_points = {
        'console_scripts': [
            'vpnc = vpnconnect.__main__:main'
        ]
    }
)
