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
    'django-guardian>=2.0',
    'html2text',
    'Django>=2.2',
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
      python_requires='>=3.6',
      test_suite='tests.main',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 2.2',
          'Framework :: Django :: 3.1',
          'Framework :: Django :: 3.2',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Utilities'
      ],
      )
