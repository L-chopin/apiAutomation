from app import BASE_URL

class taotuanProduct_api:

    def __init__(self,session):
        self.session = session
        self.select_url = BASE_URL + "/tpp/tppd/select"
        self.insert_url = BASE_URL + "/tpp/tppd/add"
        self.update_url = BASE_URL + "/tpp/tppd/update"
        self.delete_url = BASE_URL + "/tpp/tppd/delete/"


    def select_api(self,params):
        response = self.session.get(self.select_url,params=params)
        return response

    def insert_api(self,json):
        response = self.session.post(self.insert_url,json=json)
        return response

    def update_api(self,json):
        response = self.session.put(self.update_url,json=json)
        return response

    def delete_api(self,delete_id):
        response = self.session.delete(self.delete_url + delete_id)
        return response