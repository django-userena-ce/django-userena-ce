import sys

from setuptools import setup, find_packages

userena = __import__('userena')

readme_file = 'README.md'
try:
    long_description = open(readme_file).read()
except IOError:
    sys.stderr.write(
        "[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file
    )
    sys.exit(1)

install_requires = [
    'easy_thumbnails',
    'django-guardian>=1.4.2,<=1.4.9',
    'html2text==2014.12.29',
    'Django>=1.8',
]

try:
    from collections import OrderedDict
except ImportError:
    install_requires.append('ordereddict')

setup(name='django-userena-ce',
      version=userena.get_version(),
      description='Complete user management application for Django',
      long_description=long_description,
      zip_safe=False,
      author='James Meakin',
      author_email='jamesmeakin@gmail.com',
      url='https://github.com/django-userena-ce/django-userena-ce/',
      download_url='https://github.com/django-userena-ce/django-userena-ce/downloads',
      packages=find_packages(exclude=['demo', 'demo.*']),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='tests.main',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.11',
          'Framework :: Django :: 2.0',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Utilities'
      ],
      )
