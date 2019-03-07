============
Installation
============

The project is developed in Python using the `Django framework`_. You can 
either install the project locally for development, or use Docker to get it up
and running quickly

.. _Django framework: https://www.djangoproject.com/


Development
===========


Prerequisites
-------------

You need the following libraries and/or programs:

* `Python`_ 3.4 or above
* Python `Virtualenv`_ and `Pip`_
* `PostgreSQL`_ 9.1 or above
* `Redis`_ 3.0 or above
* `Node.js`_
* `npm`_

.. _Python: https://www.python.org/
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/
.. _Pip: https://packaging.python.org/tutorials/installing-packages/#ensure-pip-setuptools-and-wheel-are-up-to-date
.. _PostgreSQL: https://www.postgresql.org
.. _Node.js: http://nodejs.org/
.. _npm: https://www.npmjs.com/
.. _Redis: https://redis.io/


Getting started
---------------

Developers can follow the following steps to set up the project on their local
development machine.

1. Navigate to the location where you want to place your project.

2. Get the code:

   .. code-block:: bash

       $ git clone git@github.com:VNG-Realisatie/gemma-zaken-demo.git
       $ cd gemma-zaken-demo

3. Install all required libraries.

   .. code-block:: bash

       $ virtualenv env
       $ source env/bin/activate
       $ pip install -r requirements.txt

   **Windows users**

   .. code-block:: bash

       $ pip install pypiwin32

4. Install the `npm`_ package if you've never installed them before and
   install the frontend libraries:

   .. code-block:: bash

       $ npm install

5. Activate your virtual environment and create the statics and database:

   .. code-block:: bash

       $ source env/bin/activate
       $ python src/manage.py collectstatic --link
       $ python src/manage.py migrate

6. Create a superuser to access the management interface:

   .. code-block:: bash

       $ python src/manage.py createsuperuser

7. You can now run your installation and point your browser to the address
   given by this command:

   .. code-block:: bash

       $ python src/manage.py runserver

8. Continue to the configuration section.

**Note:** If you are making local, machine specific, changes, add them to
``src/zac/conf/local.py``. You can base this file on the
example file included in the same directory.

**Note:** You can run watch-tasks to compile `Sass`_ to CSS and `ECMA`_ to JS
using `gulp`_. By default this will compile the files if they change.

.. _ECMA: https://ecma-international.org/
.. _Sass: https://sass-lang.com/
.. _gulp: https://gulpjs.com/


Update installation
-------------------

When updating an existing installation:

1. Activate the virtual environment:

   .. code-block:: bash

       $ cd gemma-zaken-demo
       $ source env/bin/activate

2. Update the code and libraries:

   .. code-block:: bash

       $ git pull
       $ pip install -r requirements.txt
       $ npm install
       $ gulp sass

3. Update the statics and database:

   .. code-block:: bash

       $ python src/manage.py collectstatic --link
       $ python src/manage.py migrate


Testsuite
---------

To run the test suite:

.. code-block:: bash

    $ python src/manage.py test zac


Docker
======

The easiest way to get the project started is by using `Docker Compose`_.

1. Clone or download the code from `Github`_ in a folder like
   ``gemma-zaken-demo``:

   .. code-block:: bash

       $ git clone git@github.com:VNG-Realisatie/gemma-zaken-demo.git
       Cloning into 'gemma-zaken-demo'...
       ...

       $ cd gemma-zaken-demo

2. Start the database, redis and web-application:

   .. code-block:: bash

       $ docker-compose up --build -d
       Starting gemmazakendemo_redis_1 ... done
       Starting gemmazakendemo_db_1 ... done
       Starting gemmazakendemo_web_1 ... done

   It can take a while before everything is done. Even after starting the web
   container, the database might still be migrating. You can always check the
   status with:

   .. code-block:: bash

       $ docker logs -f gemmazakendemo_web_1

3. Create an admin user and load initial data. If different container names
   are shown above, use the container name ending with ``_web_1``:

   .. code-block:: bash

       $ docker exec -it gemmazakendemo_web_1 /app/src/manage.py createsuperuser
       Username: admin
       ...
       Superuser created successfully.

4. Point your browser to ``http://localhost:8080/admin/`` to access the
   project's management interface with the credentials used in step 3.

   If you are using ``Docker Machine``, you need to point your browser to the
   Docker VM IP address. You can get the IP address by doing
   ``docker-machine ip`` and point your browser to
   ``http://<ip>:8080/`` instead

5. Continue to the configuration section.


To shutdown the services, use ``docker-compose down`` and to remove
everything, you can run ``docker rmi gemmazakendemo_web``.

.. _Docker Compose: https://docs.docker.com/compose/install/
.. _Github: https://github.com/VNG-Realisatie/gemma-zaken-demo/


More Docker
-----------

If you just want to run the project as a Docker container and connect to an
external database, you can build and run the ``Dockerfile`` and pass several
environment variables. See ``src/zac/conf/docker.py`` for
all settings.

.. code-block:: bash

    $ docker build -t vngr/gemma-zaken-demo .
    $ docker run \
        -p 8000:8000 \
        -e UWSGI_PORT=8000 \
        -e DJANGO_SETTINGS_MODULE=zac.conf.docker \
        -e DATABASE_USERNAME=... \
        -e DATABASE_PASSWORD=... \
        -e DATABASE_HOST=... \
        -e REDIS_HOST=... \
        -e REDIS_PORT=... \
        --name gemma-zaken-demo \
        vngr/gemma-zaken-demo

    $ docker run gemma-zaken-demo /app/src/manage.py createsuperuser


Configuration
=============

This section assumes you have the demo site up and running (either on your
local machine, or as Docker container, or otherwise).

1. Start the components (ZRC, DRC, ZTC). See the ``infra`` section in the
   `GEMMA Zaken repository on Github`_ (via Docker, or otherwise).

2. Take note of their URLs (scheme, IP address, port).

3. Navigate to the ZTC management interface and login. Typically:
   ``http://localhost:8002/admin/``. Create the following objects:

   * Catalogus
   * ZaakType: Melding Openbare Ruimte
   * StatusType: Nieuw

4. Make sure you have the UUIDs of all entities created above.

5. Navigate to the management interface of the demo application (this
   project) and login. Typically: ``http://localhost:8080/admin/``

6. Go to the *Demo* section, and click on *Configuratie*

7. Fill in all settings.

8. Navigate to the root URL of the demo application (``/``).

9. Now you can access all demo applications.

.. _GEMMA Zaken repository on Github: https://github.com/VNG-Realisatie/gemma-zaken/


Settings
========

All settings for the project can be found in
``src/zac/conf``.
The file ``local.py`` overwrites settings from the base configuration.


Commands
========

Commands can be executed using:

.. code-block:: bash

    $ python src/manage.py <command>

There are no specific commands for the project. See
`Django framework commands`_ for all default commands, or type
``python src/manage.py --help``.

.. _Django framework commands: https://docs.djangoproject.com/en/dev/ref/django-admin/#available-commands
