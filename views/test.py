# list_s = ["金门大桥", "帝国大厦", "水晶宫", "洛克菲勒中心", "白宫", "总统山", "自由女神像", "圣路易斯拱门", "布鲁克林桥"]
from views import map
from models import wolframLink

list_data = [
    {"linkId": 1234},
    {"linkId": 2341},
    {"linkId": 234}
]

info = map.switch_nums(list_data)
wolframLink.Generate(info)