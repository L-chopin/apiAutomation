import requests
from common.login import login
from common.product_data import get_product
from api.taotuanProduct_API import taotuanProduct_api


class Test_taotuanProduct:


    def setup(self):
        self.session = requests.Session()
        headers = {
            "token":login.get_token()
        }
        self.session.headers.update(headers)
        self.api = taotuanProduct_api(self.session)
        

    def teardown(self):
        self.api.delete_api()



    def test_insert001(self):
        # 新增一条数据，只填写必填项

        insert_json = {
            "shopId":"1CK00001",
            "productNo":"1C01A001",
            "censusDate":"2021-01-01",
            "clicks":"",
            "paymentsNumber":"",
            "gvm":"",
            "receiptNumber":"",
            "receiptAmount":"",
            "commission":"",
            "serviceFee":"",
            "couponsUsed":""
    }
        select_json = {
            "page": 1,
            "rows": 30,
            "sortBy": "census_date",
            "ascdesc": "desc",
            "startTime": "2021-01-01",
            "endTime": "2021-01-01",
            "shopName": "colorkey天猫",
            "productName": "空气唇釉 丝绒系列"
        }

        response1 = self.api.insert_api(json=insert_json)
        response2 = self.api.select_api(params=select_json)


        for i in list(insert_json.keys()):
            if response2.json()["data"]["tppds"]["list"]["shopId"] != insert_json[i]:
                print("%s不正确" % i)
                assert 0
        assert 1

        if response1.json()["msg"] == "操作成功":

            # 判断新增后数据是否存在
            if len(response2.json()["data"]["tppds"]["list"]) > 0:

                # 遍历每个值，校验系统的数据是否与新增时传入的数据匹配
                for i in list(insert_json.keys()):
                    if response2.json()["data"]["tppds"]["list"]["shopId"] != insert_json[i]:
                        print("%s不正确" % i)
                        assert 0
                assert 1
            else:
                print("新增提示“操作成功”，但是查询结果为失败")
                assert 0
        else:
            assert 0


        # if response2.json()["data"]["tppds"]["list"]["shopId"] == insert_json["shopId"]:
        #     if response2.json()["data"]["tppds"]["list"]["productNo"] == insert_json["productNo"]:
        #         if response2.json()["data"]["tppds"]["list"]["censusDate"] == insert_json["censusDate"]:
        #             if response2.json()["data"]["tppds"]["list"]["clicks"] == insert_json["clicks"]:
        #                 if response2.json()["data"]["tppds"]["list"]["paymentsNumber"] == insert_json["paymentsNumber"]:
        #                     if response2.json()["data"]["tppds"]["list"]["gvm"] == insert_json["gvm"]:
        #                         if response2.json()["data"]["tppds"]["list"]["receiptNumber"] == insert_json["receiptNumber"]:
        #                             if response2.json()["data"]["tppds"]["list"]["receiptAmount"] == insert_json["receiptAmount"]:
        #                                 if response2.json()["data"]["tppds"]["list"]["commission"] == insert_json["commission"]:
        #                                     if response2.json()["data"]["tppds"]["list"]["serviceFee"] == insert_json["serviceFee"]:
        #                                         if response2.json()["data"]["tppds"]["list"]["couponsUsed"] == insert_json["couponsUsed"]:
        #                                             assert 1
        #                                         else:
        #                                             print("优惠券使用张数不正确")
        #                                             assert 0
        #                                     else:
        #                                         print("服务费不正确")
        #                                         assert 0
        #                                 else:
        #                                     print("佣金费用不正确")
        #                                     assert 0
        #                             else:
        #                                 print("结算金额不正确")
        #                                 assert 0
        #                         else:
        #                             print("结算笔数不正确")
        #                             assert 0
        #                     else:
        #                         print("成交金额不正确")
        #                         assert 0
        #                 else:
        #                     print("支付笔数不正确")
        #                     assert 0
        #             else:
        #                 print("点击量不正确")
        #                 assert 0
        #         else:
        #             print("日期不正确")
        #             assert 0
        #     else:
        #         print("商品ID不正确")
        #         assert 0
        # else:
        #     print("店铺ID不正确")
        #     assert 0


