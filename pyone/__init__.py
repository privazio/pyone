# Copyright 2018 www.privaz.io Valletech AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bindings
import pyxb
import xmlrpclib
import xml.dom.minidom as dom
import socket
import logging

from util import dict2one

#
# Exceptions as defined in the XML-API reference
#

class OneException(Exception):
    pass
class OneAuthenticationException(OneException):
    pass
class OneAuthorizationException(OneException):
    pass
class OneNoExistsException(OneException):
    pass
class OneActionException(OneException):
    pass
class OneApiException(OneException):
    pass
class OneInternalException(OneException):
    pass

# Prevent warnings from PyXB about missing logger handler:
# No handlers could be found for logger "pyxb.binding.basis"
logging.getLogger("pyxb.binding.basis").addHandler(logging.NullHandler())

#
# Set the default namespace to make DOM easier to handle.
#

pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(bindings.Namespace)

##
#
# XML-RPC OpenNebula Server
# Slightly tuned ServerProxy
#
class OneServer(xmlrpclib.ServerProxy):

    #
    # Override the constructor to take the authentication or session
    # Will also configure the socket timeout
    #

    def __init__(self, uri, session, timeout=None, **options):
        self.__session = session
        if timeout:
            # note that this will affect other classes using sockets too.
            socket.setdefaulttimeout(timeout)
        xmlrpclib.ServerProxy.__init__(self, uri, **options)

    #
    # Override/patch the (private) request method to:
    # - structured parameters will be casted to attribute=value or XML
    # - automatically prefix all methodnames with "one."
    # - automatically add the authentication info as first parameter
    # - process the response
    def _ServerProxy__request(self, methodname, params):

        # cast parameters, make them one-friendly
        lparams = list(params)
        for i,param in enumerate(lparams):
            lparams[i] = dict2one(param)
        params = tuple(lparams)

        params = ( self.__session, ) + params
        methodname = "one." + methodname
        try:
            ret = xmlrpclib.ServerProxy._ServerProxy__request(self, methodname, params)
        except xmlrpclib.Fault as e:
            raise OneException(e)

        return self.__response(ret)

    #
    # Process the response from one XML-RPC server
    # will throw exceptions for each error condition
    # will bind returned xml to objects generated from xsd schemas
    def __response(self, rawResponse):
        sucess = rawResponse[0]
        code = rawResponse[2]

        if sucess:
            ret = rawResponse[1]
            if isinstance(ret, basestring):
                # detect xml
                if ret[0] == '<':
                    # PyXB won't recognize the type if the namespace is not present
                    # preliminary parsing to do the checks and add it
                    doc = dom.parseString(ret)
                    doc.documentElement.setAttribute('xmlns', 'http://opennebula.org/XMLSchema')
                    # toDOM and CD_DATA is broken in PyXB until 1.2.7, so, will force SAX parsing
                    return bindings.CreateFromDocument(doc.toxml())
            return ret;

        else:
            message = rawResponse[1]
            if code == 0x0100:
                raise OneAuthenticationException(message)
            elif code == 0x0200:
                raise OneAuthorizationException(message)
            elif code == 0x0400:
                raise OneNoExistsException(message)
            elif code == 0x0800:
                raise OneActionException(message)
            elif code == 0x1000:
                raise OneApiException(message)
            elif code == 0x2000:
                raise OneInternalException(message)
            else:
                raise OneException(message)


