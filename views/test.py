# list_s = ["金门大桥", "帝国大厦", "水晶宫", "洛克菲勒中心", "白宫", "总统山", "自由女神像", "圣路易斯拱门", "布鲁克林桥"]
from views import map
from models import wolframLink

list_data = [{"linkId": 811},
             {"linkId": 846},
             {"linkId": 2133},
             {"linkId": 2134},
             {"linkId": 11583},
             {"linkId": 11852}]

info = map.switch_nums(list_data)
print(info)
# wolframLink.Generate(info)
