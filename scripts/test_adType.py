import requests,json

from api.adType_API import ad_type_api
from common.login import login

def analyze_data():
    with open("./data/adType.json","r",encoding="utf-8") as f:
        print(json.load(f))

class Test_adType:

    def setup(self):
        self.session = requests.Session()
        headers = {
            "token":login.get_token()
        }
        self.session.headers.update(headers)
        self.api = ad_type_api(self.session)

    def teardown(self):
        self.session.close()

    def test_select(self):
        json = {
            "ascdesc": "",
            "bsDictType":"adType",
            "page": 1,
            "rows": 30,
            "sortBy": ""
        }
        response = self.api.select_api(json)

        assert response.status_code == 200
        assert response.json()["msg"] == "操作成功"
