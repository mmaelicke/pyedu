PyEDU
=====

The Python Educational Suite (PyEDU) is a flask application for guided Python exercise creation and completion. It
was created for the Python I and Python II lectures at the Chair for remote sensing and landscape information systems
at the Univeristy of Freiburg, but will however work with other exercises as well.

The application is meant to be run from the localhost so that the exercise code is run in a local Python environement.
Before running it on a remote server, one has to make sure that no harmful code is included in the exercises before
running the code. However, the local application can connect to a local or remote database. For Python I and II these
remote connections are already included in an encrypted file. As the user has the decryption key, the connection can
be used. In the supplementary folder is Jupyter notebook which can create such a file for other remote locations.

Installation
~~~~~~~~~~~~

Although the project will be on PyPI, the installation using git favored. One of the next updates will included
a version check and auto-update function, which will be based on git and might not work when PyEDU is installed
using pip. It can be installed using:

.. code-block:: bash

    git clone https://github.com/mmaelicke/pyedu.git
    cd pyedu
    pip install -r requirements.txt
    python setup.py install


Using remote connections
~~~~~~~~~~~~~~~~~~~~~~~~

In order to use a remote connection you'll need a file with the decryption key in it. The connection and keys are in the
pyedu/enc folder. To use a remote connection as default, rename the .enc file you wish to use to 'remote.enc' and
place the key as 'remote.key' into the enc folder. Then the default flask settings will use this connection as
the default connection.
For one of the next updates, there will be the possibility to enter the cleartext key during the start process. Then
the user cannot manually decrypt the enc file anymore.

Starting the application
~~~~~~~~~~~~~~~~~~~~~~~~

In order to start the application, in the pyedu/pyedu folder use:

.. code-block:: bash

    python manage.py runserver

If you like to use another flask configuration, like with enabled debug mode or a local connection, you can use the -c
(--config) flag:

.. code-block:: bash

    python manage.py -c local_dev runserver

Once the server is running, the application can be accessed with your browser and activated Javascript at:

.. code-block::

    http://locahost:5000

With one of the next versions, the application will be able to create a shortcut on Windows or a executable symlink on
Linux for starting the application.


Security
~~~~~~~~

Please note, that this application is not made for remote usage and still under active development. If you decide to
run this application with a remote database, please note that it is possbile to read the database connection and
connect externally. To come around external assingment injection, the application will include a different assign
route with a future release, that will shift the solution check to a remote REST API and therefore make the student
db user a read only db user.