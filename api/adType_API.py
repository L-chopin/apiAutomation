from app import BASE_URL


class ad_type_api:

    def __init__(self,session):
        self.session = session
        self.select_url = BASE_URL + "bsDict/selectByType"
        self.insert_url = BASE_URL + "bsDict/insertBsDict"
        self.update_url = BASE_URL + "bsDict/update"

    # 请求查询接口
    def select_api(self,json):
        response =self.session.post(self.select_url,json=json)
        return response

    # 请求新增接口
    def inser_api(self,json):
        response = self.session.post(self.insert_url,json=json)
        return response

    # 请求更新接口
    def update_api(self,json):
        response = self.session.post(self.update_url,json=json)
        return response