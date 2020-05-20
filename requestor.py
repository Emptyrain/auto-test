import pytest
import requests

class Test_httpbin():

    def test_get_ip(self):
        IP = "183.228.8.141"
        url = "http://httpbin.org//ip"
        r = requests.get(url)
        print(r.headers)
        response_data = r.json()
        print(response_data)
        assert 200 == r.status_code
        assert IP == response_data["origin"]

    def test_post_method(self):
        url = "http://httpbin.org//post"
        post_data = {"name":"yourname","pwd":"123456"}
        r = requests.post(url,data = post_data)
        print(r.headers)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == response_data["form"]["name"]
        assert post_data["pwd"] == response_data["form"]["pwd"]

    if __name__ == '__main__':
        # url_get = "http://httpbin.org//ip"
        # url_post = "http://httpbin.org//post"
        # test_get_ip(url_get)
        # test_post_method(url_post)

        pytest.main(["-s", "requestor.py", "--html=report.html"])
