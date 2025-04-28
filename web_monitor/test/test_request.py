import unittest

from src.request import send_request

class TestSendRequest(unittest.TestCase):
    # These tests depend on radionimbus.wl.r.appspot.com being online.

    def test_successful_regex(self):
        url = "https://radionimbus.wl.r.appspot.com/"
        regex = "body"
        response = send_request(url, regex)

        self.assertTrue(response["regex_match"])
        self.assertEqual(200, response["status_code"])

    def test_successful_no_regex(self):
        url = "https://radionimbus.wl.r.appspot.com/"
        response = send_request(url)

        self.assertFalse(response["regex_match"])
        self.assertEqual(200, response["status_code"])

    def test_unsuccessful(self): 
        url = "not a url"
        response = send_request(url)

        self.assertTrue("error" in response)
        
    