PyONE: Open Nebula Python Bindings
==================================

Description
-----------

PyOne is an implementation of Open Nebula XML-RPC bindings in Python.

The main goals of this library are **completeness and maintainability**.

Proxies and generators have been used whenever possible to minimize the impact of
API updates, ensuring that the distributed xsd files are the only update required
when new API versions are released.

This library is meant to be used together with OpenNebula API documentation:

The `XML-RPC API <http://docs.opennebula.org/5.4/integration/system_interfaces/api.html>`_ must
be used to know which calls to make.

Development
-----------

To contribute enhancements or fixes use GitHub tools: Pull requests and issues.
Please note that by contributing to this project you accept that your contributions
are under the Apache License 2.0, just like the rest of this project. Please take
some time to read and understand the license terms and ensure that you are happy with it.

Authors
-------

* Rafael del Valle (rvalle@privaz.io)

Compatibility
-------------

* PyONE is compatible with OpenNebula v5.4
* It should be easy to backport PyOne to any OpenNebula version with XML-RPC API that includes XML Schema Definition (XSD) files.

Requirements
------------

* Connectivity and Credentials to OpenNebula XML-RPC Server.

Installation
------------

PyONE is distributed as a python package, it can be installed as:

.. code:: shell

  pip install pyone

Configuration
-------------

You can configure your XML-RPC Server endpoint and credentials in the constructor:

.. code:: python

  import pyone
  one = pyone.OneServer("http://one/RPC2", session="oneadmin:onepass" )

If you are connecting to a test platform with a self signed certificate you can disable
certificate verification as:

.. code:: python

  import pyone
  import ssl
  one = pyone.OneServer("http://one/RPC2", session="oneadmin:onepass", context=ssl._create_unverified_context() )

It is also possible to modify the default connection timeout, but note that the setting
will modify the TCP socket default timeout of your Python VM, ensure that the chosen timeout
is suitable to any other connections runing in your project.

Usage
-----

**Making Calls**

Calls match the API documentation provided by Open Nebula:

.. code:: python

  import pyone

  one = pyone.OneServer("http://one/RPC2", session="oneadmin:onepass" )
  hostpool = one.hostpool.info()
  host = hostpool.HOST[0]
  id = host.ID

Note that the session parameter is automatically included as well as the "one." prefix to the method.

**Returned Objects**

The returned types have been generated with PyXB and closely match the XSD specification.
You can use the XSD specification as primary documentation while your IDE will
offer code completion as you code or debug.

.. code:: python

   marketpool = one.marketpool.info()
   m0 = marketpool.MARKETPLACE[0]
   print "Markeplace name is " + m0.NAME

**Structured Parameters**

When making calls, the library will translate flat dictionaries into attribute=value
vectors. Such as:

.. code:: python

  one.host.update(0,  {"LABELS": "HD"}, 1)

When the provided dictionary has a "root" dictionary, it is considered to be root
element and it will be translated to XML:

.. code:: python

  one.vm.update(1,
    {
      'TEMPLATE': {
        'NAME': 'abc',
        'MEMORY': '1024',
        'ATT1': 'value1'
      }
    }, 1)

**Building from Source**

Note that a Makefile is provided to generate the python bindings

References
----------

PyONE started as part of the `Privazio <http://privaz.io>`_ project.

Privazio is a private cloud for residential users,
startups or workgroups with a special focus on privacy.

PyONE is meant to be a key component to implement an Ansible module for
managing Open Nebula.

License
-------

PyONE is licensed under Apache License 2.0
