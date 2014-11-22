ofCourse -- Open, Free Course(ware)
===================================

.. image:: https://api.travis-ci.org/ryansb/ofCourse.svg
    :target: https://travis-ci.org/ryansb/ofCourse
.. image:: https://pypip.in/v/ofcourse/badge.png
    :target: https://pypi.python.org/pypi/ofcourse/
.. image:: https://pypip.in/download/ofcourse/badge.svg
    :target: https://pypi.python.org/pypi/ofcourse/

Warning
=======

This is an enormous cleanup and rename of HFLOSSK, and things will break at
least temporarily. Old history will disappear. Just be aware. - ryansb 11/21/14

Wat?
----
This repository is an experiment to use Flask, Mako, and Bootstrap to make a
website for the Humanitarian Free/Open Source Software Course at RIT. This
repository is a work in progress (as any FOSS project is), and will be open for
contributions.

The content shown here is a compilation of course materials from 4 previous
professors, who've run the course 5 separate times. Those profs are:
    - Stephen Jacobs
    - Dave Shein (x2)
    - Ralph Bean
    - Justin Sherrill

Docs
----

Docs are available on `ReadTheDocs`_
.. image:: https://readthedocs.org/projects/ofcourse/badge/?version=latest
    :target: http://ofcourse.readthedocs.org/en/latest

.. _ReadTheDocs:: http://ofcourse.readthedocs.org/


Tests
-----

All tests are run using tox. To run the tests::

$ virtualenv --no-site-packages -p python2 ofcourse_env
$ . ofcourse_env/bin/activate
$ pip install tox
$ tox

Tests check validity of all yaml, and the keys in any student yaml files. Tests
also checks that code conforms to PEP8.

License
=======

Copyright 2013 Remy DeCausemaker

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
