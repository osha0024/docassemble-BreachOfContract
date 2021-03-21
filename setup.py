import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.BreachOfContract',
      version='0.0.1',
      description=('LLAW3301 Law in a Digital Age - Docassemble teaching materials'),
      long_description='# LLAW3301: Law in a Digital Age\r\n\r\n### Teaching materials\r\n\r\nThis Docassemble package contains the source code and other resources used\r\nto teach students Docassemble, YAML and Python.\r\n\r\nLaw in a Digital Age is a topic taught by the \r\n[College of Business, Government and Law](https://www.flinders.edu.au/college-business-government-law)\r\nat [Flinders University](https://flinders.edu.au).  From 2020 it will form part of\r\nthe core Bachelor of Laws degrees taught at Flinders.\r\n\r\nFor any enquirires please contact [Mark Ferraretto](mailto:mark.ferraretto@flinders.edu.au) or on +61 8 7421 9816.\r\n',
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/BreachOfContract/', package='docassemble.BreachOfContract'),
     )

