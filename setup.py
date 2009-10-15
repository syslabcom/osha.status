from setuptools import setup, find_packages
import os

version = '1.0.4'

tests_require = [
    'zc.testbrowser', 
    'osha.theme', 
    'slc.alertservice', 
    ]

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('src', 'osha', 'status', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n'
    )

setup(name='osha.status',
      version=version,
      description="Small status page",
      long_description = long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Patrick Gerken (syslab.com)',
      author_email='gerken@syslab.com',
      url='http://www.syslab.com',
      license='GPL',
      packages=['osha', 'osha.status'],
      package_dir = {'' : 'src'},
      namespace_packages=['osha'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
