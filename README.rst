fyi
===
Simple commandline notifications and logging
--------------------------------------------

:authors: Paul Agapow <paul@agapow.net>


Background
----------

A common need in commandline programs and scripts is notifications, informming (or reassuring!) the user of progress, issuing warnings and recording information for debugging. Ideally, verbosity should be configurable, showing only certain levels of notifications e.g. normally only displaying critical messages but allowing the display of debug information. The Python logging module offers a central and powerful mechanism for doing this, but is slightly ornate and longwinded, especially for common use cases.


Features
--------

This package provides a thin skin around the logging module, providing simple notification and logging capbilities. These mostly work 'straight from the box', covering many common use cases with little or no configuration. At the same time, notification and logger behaviour can still be configured.

Features include:

* Simple and sensible notification behaviour provided by a simple import and setup call.

* Functions for controlling verbosity from commandline arguments

* Easy setting of more complex behaviour (e.g. logging to files)

* Pythonification of the slightly strange logging interface


Design & limitations
--------------------

This package was prompted by repeatedly having to repeatedly implement same set of functions over many programs: print out informational messages, log information during development, allow these to be tuned as needs. So fyi is setup to allow these tasks to be easily and quickly done.

To do this, I've made a few assumptions:

* The desired levels of logging and their behaviour are configured at the start of the program and not expected them to change during the program.

* If a level is set, it is assumed you want to use it, i.e. you don't define output for debug messages and set the level higher.

* Normally only one logger - the root logger - will be used and all calls default to this one.

The concept and features of this package have evolved considerably during development. Arguably,

While the necessary setup for the standard logging package is commonly seen as verbose [mechcat_], the simplfication this package offers is arguably minimal.


References
----------

.. _mechcat:: "Simple usage of Python's logging module" http://www.mechanicalcat.net/richard/log/Python/Simple_usage_of_Python_s_logging_module
