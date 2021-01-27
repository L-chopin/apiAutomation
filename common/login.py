"""
登录接口

"""

# 请求数据中台测试地址登录接口，并返回token
import requests

class login:

    @classmethod
    def get_token(cls):

        json = {
            "password": "123456",
            "type": "pc",
            "username": "admin"
        }

        login_headers = {
            "Content-Type":"application/json;charset=UTF-8"
        }

        response = requests.post(
            "http://14.23.109.84:9092/sys/login",
            headers = login_headers,
            json = json
        )

        # 调用.json()方法，将响应信息转变为python字典，不然没法用字典的方式获取响应信息中的token
        # 获取token,并返回
        return response.json()["data"]["accessToken"]
