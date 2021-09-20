from setuptools import setup

setup(name='valve-casual-api',
      version='0.1.0',
      description='Valve Casual Wrapper',
      author='kritanta',
      url='https://github.com/kritantadev/valve-casual-api',
      install_requires=['python-a2s'],
      packages=['vcapi'],
      package_dir={
          'vcapi': 'src/vcapi'
      },
      package_data={
          'vcapi': ['data/*'],
      }
      )
