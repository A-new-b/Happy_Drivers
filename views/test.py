# list_s = ["金门大桥", "帝国大厦", "水晶宫", "洛克菲勒中心", "白宫", "总统山", "自由女神像", "圣路易斯拱门", "布鲁克林桥"]
#
# for i in range(0, len(list_s)-1):
#     for j in range(i+1, len(list_s)):
#         print("{'p1':'" + list_s[i] + "','p2':'" + list_s[j] + "'},")
#         print("{'p1':'" + list_s[j] + "','p2':'" + list_s[i] + "'},")

from views import map
import json

list_data = [
    {"linkId": 1234},
    {"linkId": 2341},
    {"linkId": 234}
]


print(json.loads(map.switch_nums(list_data)))
