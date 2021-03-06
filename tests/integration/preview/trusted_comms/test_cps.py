# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class CpsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.trusted_comms.cps().fetch(twilio_sandbox_mode="twilio_sandbox_mode", x_xcnam_sensitive_phone_number="x_xcnam_sensitive_phone_number")

        headers = {
            'Twilio-Sandbox-Mode': "twilio_sandbox_mode",
            'X-Xcnam-Sensitive-Phone-Number': "x_xcnam_sensitive_phone_number",
        }
        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/TrustedComms/CPS',
            headers=headers,
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "cps_url": "https://preview.twilio.com/TrustedComms/CurrentCall",
                "phone_number": "+1500123",
                "url": "https://preview.twilio.com/TrustedComms/CPS"
            }
            '''
        ))

        actual = self.client.preview.trusted_comms.cps().fetch()

        self.assertIsNotNone(actual)
