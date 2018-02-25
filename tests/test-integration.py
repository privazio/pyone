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

import unittest
import ssl
import pyone

from pyone.util import one2dict

testSession = "oneadmin:onepass"
testEndpoint = 'https://192.168.121.55/RPC2'
one = pyone.OneServer(testEndpoint, session=testSession, context=ssl._create_unverified_context())

class IntegrationTests(unittest.TestCase):

    def test_pool_info(self):
        hostpool = one.hostpool.info()
        self.assertGreater(len(hostpool.HOST), 0)
        host0 = hostpool.HOST[0]
        self.assertEqual(host0.ID, 0)

    def test_auth_error(self):
        with self.assertRaises(pyone.OneAuthenticationException):
            xone = pyone.OneServer(testEndpoint, session="oneadmin:invalidpass", context=ssl._create_unverified_context())
            xone.hostpool.info()

    def test_market_info(self):
        marketpool = one.marketpool.info()
        self.assertGreater(len(marketpool.MARKETPLACE), 0)
        m0 = marketpool.MARKETPLACE[0]
        self.assertEqual(m0.NAME, "OpenNebula Public")

    def test_invalid_method(self):
        with self.assertRaises(pyone.OneException):
            one.invalid.api.call()

    def test_template_attribute_vector_parameter(self):
        one.host.update(0,  {"LABELS": "HD,LOWPOWER"}, 1)

    def test_xml_template_parameter(self):
        one.host.update(1,
            {
                'TEMPLATE': {
                    'LABELS': 'SSD',
                    'MAX_CPU': '176'
                }
            }, 1)

    def test_empty_dictionary(self):
        with self.assertRaises(Exception):
            one.host.update(0, {}, 1)

    def test_retrieve_template_as_DOM(self):
        host = one.host.info(0)
        template = host.TEMPLATE.toDOM()
        arch = template.getElementsByTagName('ARCH')[0].firstChild.nodeValue
        self.assertEqual(arch, 'x86_64')

    def test_retrieve_template_as_dict(self):
        host = one.host.info(0)
        tdict = one2dict(host.TEMPLATE)
        arch = tdict['TEMPLATE']['ARCH']
        self.assertEqual(arch, 'x86_64')
