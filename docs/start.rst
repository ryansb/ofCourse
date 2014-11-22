.. Getting started docs

Get started with ofcourse
=========================

This tutorial will help you install the ofcourse tools, create a
site, and deploy your site on OpenShift.

Installing ofcourse
-------------------

Before you can do anything with this (run the webserver locally, or any of the
scripts) you'll need to setup and activate a python `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_.  Run the following at the command
prompt...

On Linux/Mac OS X
+++++++++++++++++

If you don't have virtualenv installed yet, try::

 $ sudo pip install virtualenv virtualenvwrapper

If you're using a distro like Fedora or Ubuntu, you should try this instead::

 Fedora:
 $ sudo yum install python-virtualenv

 Ubuntu/Debian:
 $ sudo apt-get install python-virtualenv

Once you have virtualenv installed, you should be able to run::

 $ virtualenv --no-site-packages -p python2 ofcourse_environment
 $ source ofcourse_environment/bin/activate
 $ pip install ofcourse

To actively develop ofcourse, try this instead::

 $ git clone https://github.com/ryansb/ofCourse ofcourse
 $ cd ofcourse
 $ virtualenv --no-site-packages -p python2 ofcourse_environment
 $ source ofcourse_environment/bin/activate
 $ python setup.py develop


On Windows
++++++++++

At the windows command prompt::

 $ virtualenv --no-site-packages -p python2 ofcourse_environment
 $ ofcourse_environment/Scripts/activate.bat

In msysGit or git-bash::

 $ git clone https://github.com/ryansb/ofCourse.git

Back in the windows command prompt::

 $ cd ofCourse
 $ python setup.py develop

On Both Platforms
+++++++++++++++++

After completing these instructions you should be able to see the CLI tool
documentation by typing into your prompt::

  $ ofcourse
