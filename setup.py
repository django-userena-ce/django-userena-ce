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


def django_guardian_version():
    if sys.version_info < (3,5):
        # Django Guardian does not support Python < 3.5 after version 2
        return 'django-guardian>=1.4.2,<2'
    else:
        return 'django-guardian>=1.4.2'

install_requires = [
    'easy_thumbnails',
    django_guardian_version(),
    'html2text',
    'Django>=1.11',
]

setup(name='django-userena-ce',
      version=userena.get_version(),
      description='Complete user management application for Django',
      long_description=long_description,
      long_description_content_type='text/markdown',
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
          'Framework :: Django :: 1.11',
          'Framework :: Django :: 2.1',
          'Framework :: Django :: 2.2',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Utilities'
      ],
      )
