"""
解析json数据文件
"""

import json

class json_analyze:

    def analyze(self,file):
        with open("./data/%s" % file,"r",encoding="utf-8") as f:
            data_list = []
            data_dict = json.load(f)
            for value in data_dict.values():
                data_list.append(value)
                return data_list
