.. A tour of the ofcourse internals

Under the Hood
==============

The Web App
-----------

`Flask`_ powers the web site, rendering all the page templates and handling
requests.

.. _Flask: http://flask.pocoo.org/

The CLI Tool
------------

The CLI tool is a `Click`_ application that uses `dulwich`_ and the OpenShift
API to deploy your course seamlessly.

.. _Click: http://click.pocoo.org/
.. _dulwich: https://www.samba.org/~jelmer/dulwich/
