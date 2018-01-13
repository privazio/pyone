Open Nebula Python Bindings
===========================

This is an implementation of Open Nebula XML-RPC bindings in Python.

The main goals of this library are **completeness and maintainability**.

Proxies and generators have been used whenever possible to minimize the impact of API updates, ensuring that the distributed xsd files are the only update required when new API versions are released.

This library is meant to be used together with OpenNebula API documentation:

The `XML-RPC API <http://docs.opennebula.org/5.4/integration/system_interfaces/api.html>`_ must be used to know which calls to make.

How to use it
=============

Installation
------------

The code is distributed as a package:

.. code:: shell

  pip install pyone

Making Calls
------------

Calls match the API documentation provided by Open Nebula:

.. code:: python

  import pyone

  one = pyone.OneServer("http://one/RPC2", session="oneadmin:onepass" )
  hostpool = one.hostpool.info()
  host = hostpool.HOST[0]
  id = host.ID

Note that the session parameter is automatically included as well as the "one." prefix to the method.

Returned Objects
----------------

The returned types have been generated with PyXB and closely match the XSD specification. You can use the XSD specification as primary documentation while your IDE will offer code completion as you code

.. code:: python

   marketpool = one.marketpool.info()
   m0 = marketpool.MARKETPLACE[0]
   print "Markeplace name is " + m0.NAME

Structured Parameters
---------------------

When making calls, the library will translate flat dictionaries into attribute=value vectors. Such as:

.. code:: python

  one.host.update(0,  {"LABELS": "HD"}, 1)


When the provided dictionary has a "root" dictionary, it is considered to be root element and it will be translated to XML:

.. code:: python

  one.vm.update(1,
    {
      'TEMPLATE': {
        'NAME': 'abc',
        'MEMORY': '1024',
        'ATT1': 'value1'
      }
    }, 1)

Building from Source
====================

Note that a Makefile is provided to generate the python bindings
