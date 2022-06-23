# coding = utf-8
import requests

URL = "http://127.0.0.1:5015"


class TestCase:
    def request_get(self, url, data):
        send_url = f"{URL}{url}"
        res = requests.get(send_url, data)
        return res.content.decode()

    def test_write_table(self):
        """
        写入table
        """
        pass
