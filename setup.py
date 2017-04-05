import os
from setuptools import setup

# if you are not using vagrant, just delete os.link directly,
# The hard link only saves a little disk space, so you should not care
if os.environ.get('USER', '') == 'vagrant':
    del os.link

try:
    with open('README.txt') as file:
        long_description = file.read()
except:
    long_description = "Bad Ideas for Python!"

setup(name='bad-ideas',
      version='0.0.1',
      description='Pythonic Redis Client.',
      url='https://github.com/seperman/bad-ideas',
      download_url='https://github.com/seperman/bad-ideas/tarball/master',
      author='Seperman',
      author_email='sep@zepworks.com',
      license='MIT',
      packages=['bad'],
      zip_safe=False,
      test_suite="tests",
      long_description=long_description,
      classifiers=[
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Topic :: Software Development",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License"
      ],
      )
