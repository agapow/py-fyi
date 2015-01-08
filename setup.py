from setuptools import setup, find_packages
import sys, os

from fyi import __version__



setup(
   name='fyi',
   version=__version__,
   description="'Simple commandline notifications and logging'",
   long_description="""\
   A common need in commandline programs and scripts is notifications, informning the user of progress including errors. Ideally, the level of notification should be configurable, allowing different levels of verbosity e.g. only displaying critical messages or including debug information. The Python logging module offers a central and cpowerful mechanism for doing this, but is slightly ornate. This package provides a thin skin around the logging module, to allow for most common use cases while providing a simpler interface tfor customizing logger behaviour.""",
   classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
   keywords='logging, notifications, progress',
   author='Paul Agapow',
   author_email='paul@agapow.net',
   url='http://www.agapow.net/software/py-fyi',
   license='MIT',
   packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
   include_package_data=True,
   zip_safe=False,
   install_requires=[
      # -*- Extra requirements: -*-
   ],
   entry_points="""
      # -*- Entry points: -*-
   """,
)
