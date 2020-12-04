import unittest
from unittest import mock
from unittest.mock import patch, Mock
from cli.ip_in_subnetwork import ip_in_subnetwork, ip_to_integer, subnetwork_to_ip_range, check_if_ip_in_subnetwork
from cli.helpers import get_list_of_CIDRs



CONTENT = {
    "data": {
        "resources": {
            "asn": [
                "1",
                "2"
            ],
            "ipv4": [
                "68.32.0.0/11"
            ],
            "ipv6": [
                "2001:400::/32"
            ]
        }
    },
    "status": "ok",
    "status_code": 200,
}


class TestIpInSubnetwork(unittest.TestCase):

    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):

        mock_resp = Mock()
        json_data = CONTENT

        mock_resp.raise_for_status = Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status

        mock_resp.status_code = status
        mock_resp.content = content

        if json_data:
            mock_resp.json = Mock(return_value=json_data)
        return mock_resp



    @mock.patch('requests.get')
    def test_get_list_of_CIDRs(self, mock_get):
        mock_resp = self._mock_response(content=CONTENT)
        mock_get.return_value = mock_resp
        mock_result = get_list_of_CIDRs()
        status_code = mock_result['status_code']

        self.assertTrue(status_code == 200)
        self.assertEqual(mock_result, CONTENT)
        self.assertFalse(mock_resp.raise_for_status.called)


    @mock.patch('requests.get')
    def test_check_if_ip_in_subnetwork(self, mock_get, host_ip="68.52.38.81"):
        subnetwork = '68.32.0.0/11'
        matches = ['68.32.0.0/11']

        mock_resp = self._mock_response(content=CONTENT)
        mock_get.return_value = mock_resp
        mock_check_ip_in_subnetwork = check_if_ip_in_subnetwork(host_ip)


        self.assertEqual(matches, ['68.32.0.0/11'])
        self.assertTrue(len(mock_check_ip_in_subnetwork) > 0)



    def test_ip_in_subnetwork(self, host_ip='68.52.38.81', subnetwork='68.32.0.0/11'):
        match = ip_in_subnetwork(host_ip, subnetwork)
        self.assertTrue(match == '68.32.0.0/11')



    def test_ip_to_integer(self, ip_address='68.52.38.81'):
        self.assertEqual(ip_to_integer(ip_address), (1144268369, 4))



    def test_subnetwork_to_ip_range(self, subnetwork='68.32.0.0/11'):
        self.assertEqual(subnetwork_to_ip_range(subnetwork), (1142947840, 1145044991, 4))


if __name__ == '__main__':
    unittest.main()
