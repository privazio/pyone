import unittest
import ssl
import pyone

testSession = "oneadmin:onepass"
testEndpoint = 'https://192.168.121.93/RPC2'
one = pyone.OneServer(testEndpoint, session=testSession, context=ssl._create_unverified_context())

class TestPyOne(unittest.TestCase):

    def test_pool_info(self):
        hostpool = one.hostpool.info()
        self.assertGreater(len(hostpool.HOST), 0)
        host0 = hostpool.HOST[0]
        self.assertEqual(host0.ID, 0)

    def test_auth_error(self):
        with self.assertRaises(pyone.OneAuthenticationException):
            xone = pyone.OneServer(testEndpoint,session="oneadmin:invalidpass",context=ssl._create_unverified_context())
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
        one.host.update(0,  {"LABELS": "HD"}, 1)

    def test_xml_template_parameter(self):
        one.host.update(1,
            {
                'TEMPLATE': {
                    'LABELS': 'SSD',
                    'MAX_CPU': '176'
                }
            }, 1)

    def test_empty_dictionary(self):
        with self.assertRaises(pyone.OneException):
            one.host.update(0, {}, 1)
