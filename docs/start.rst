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


Creating a New Course
---------------------

Before you can follow these instructions, you'll need to setup and activate a
python `virtualenv <http://pypi.python.org/pypi/virtualenv>`_.  Run the
following at the command prompt...

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

 $ cd code
 $ virtualenv --no-site-packages -p python2 ofcourse_environment
 $ . ./ofcourse_environment/bin/activate
 $ pip install ofcourse
 $ mkdir YOUR_COURSENAME
 $ cd YOUR_COURSENAME
 $ ofcourse new

Once you've done that you'll probably want to edit some of the
pre-generated files for the course. That way the website will
reflect your course's information. Check your course out locally with::

  $ ofcourse run

And go to http://localhost:5000 in your browser to see what you have.

After you're satisfied with your content, create a GitHub repository and add
your files.::

  $ git init
  $ git add .
  $ git commit -m 'initial commit'
  $ git remote add origin git@github.com:YOUR_USERNAME/YOUR_COURSENAME.git
  $ git push origin master

And now your course is published on GitHub!

On Windows
++++++++++

At the windows command prompt::

 $ virtualenv --no-site-packages -p python2 ofcourse_environment
 $ ofcourse_environment/Scripts/activate.bat
 $ pip install ofcourse

Make the repository on GitHub, then use msysGit or git-bash::

 $ git clone git@github.com:YOUR_USERNAME/YOUR_COURSENAME-content.git

Back in the windows command prompt::

 $ cd YOUR_COURSENAME-content
 $ ofcourse new

Once you've done that you'll probably want to edit some of the
pre-generated files for the course. That way the website will
reflect your course's information. Check your course out locally with::

  $ ofcourse run

When you're ready, add the files and push them to GitHub with git-bash or
msysGit::

  $ git add .
  $ git commit -m 'Add ofcourse templates'
  $ git push origin master

And now your course is published on GitHub!

Deploying to OpenShift
++++++++++++++++++++++

Deploying to OpenShift is fairly simple once you have your local instance up and
running. Before deploying you need to make sure that you have an openshift
account and a few extra things configured.

If you don't yet have an account feel free to go to openshifts account creation
page which can be found `here <https://www.openshift.com/app/account/new>`__.

Once you have an account created, you then need to go to your
`settings page <https://openshift.redhat.com/app/console/settings>`_ and set
the domain name for the app that you will be using. This creates a url which
will look similar to the following where {{domain-name}} is substituted with
what you enter.

  http://{{application-name}}-{{domain-name}}.rhcloud.com

After you have your domain name set, the last think you need to do is submit
ssh key which will allow you to push your newly created code to OpenShift's
servers. Github provides a fantastic guide on setting up your SSH keys
`here <https://help.github.com/articles/generating-ssh-keys/>`__, if you have
already created your SSH key, simply paste them into the text box
`here <https://openshift.redhat.com/app/console/keys/new>`__.

Lastly you'll need to choose an app name. Lets say for this example we will be
calling our app `SuperAwesomeApp`. Simply run the following::

  ofcourse openshift --app SuperAwesomeApp

Follow the instructions on the screen and your app should be deployed now!
