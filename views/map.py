import flask
import json
import random
import os
import copy
from models import wolframLink

Map = flask.Blueprint("Map", __name__)


def json_decode(map_list_k):
    point_list = []
    for i in map_list_k:
        if i["p1"] not in point_list:
            point_list.append(i["p1"])
        if i["p2"] not in point_list:
            point_list.append(i["p2"])
        "Labeled[1 -> 2, \"1\"]"
    last_part = ", VertexLabels -> {"
    for i in range(0, len(point_list)):
        item = str(i + 1) + " -> \"" + point_list[i] + "\", "
        last_part += item
    last_part = last_part[:-2]
    last_part += "}]"
    header_part = "Graph[{"
    for i in map_list_k:
        label = "Labeled[" + str(point_list.index(i["p1"]) + 1) + " -> " + str(
            point_list.index(i["p2"]) + 1) + ", \"" \
                + str(i["linkId"]) + ",len:" + str(i["len"]) + "\"], "
        header_part += label
    header_part = header_part[:-2]
    header_part += "}"
    return header_part + last_part


def rand_position(list_data, nums):
    map_list_r = copy.deepcopy(map_list[::-1])
    # print(map_list_r)
    print(map_list)
    map_list_k = []
    position_list = []
    for i in list_data:
        position = random.randint(0, nums)
        while position in position_list:
            position = random.randint(0, nums)
        position_list.append(position)
        l = random.randint(10, 21)
        map_list_r[position]["linkId"] = i['linkId']
        map_list_r[position]['len'] = l
    for i in map_list_r:
        if "linkId" in i.keys():
            map_list_k.append(i)
    return json_decode(map_list_k)


def switch_nums(list_data):
    if len(list_data) <= 2:
        return rand_position(list_data, 1)
    elif len(list_data) <= 6:
        return rand_position(list_data, 5)
    elif len(list_data) <= 12:
        return rand_position(list_data, 11)
    elif len(list_data) <= 20:
        return rand_position(list_data, 19)
    elif len(list_data) <= 30:
        return rand_position(list_data, 29)
    elif len(list_data) <= 42:
        return rand_position(list_data, 41)
    elif len(list_data) <= 56:
        return rand_position(list_data, 55)
    elif len(list_data) <= 72:
        return rand_position(list_data, 71)


@Map.route('/api/map', methods=['Post'])
def upload():
    try:
        post_data = json.loads(flask.request.get_data(as_text=True))
        length = len(post_data)
        res = rand_position(post_data, length)
        path = wolframLink.Generate(res)
        return path
    except Exception as e:
        print(e)
        return 500


map_list = [
    {'p1': '金门大桥', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '金门大桥'},
    {'p1': '金门大桥', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '金门大桥'},
    {'p1': '帝国大厦', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '帝国大厦'},
    {'p1': '帝国大厦', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '帝国大厦'},
    {'p1': '水晶宫', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '水晶宫'},
    {'p1': '水晶宫', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '水晶宫'},
    {'p1': '洛克菲勒中心', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '洛克菲勒中心'},
    {'p1': '洛克菲勒中心', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '洛克菲勒中心'},
    {'p1': '白宫', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '白宫'},
    {'p1': '白宫', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '白宫'},
    {'p1': '总统山', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '总统山'},
    {'p1': '总统山', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '总统山'},
    {'p1': '自由女神像', 'p2': '圣路易斯拱门'},
    {'p1': '圣路易斯拱门', 'p2': '自由女神像'},
    {'p1': '自由女神像', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '自由女神像'},
    {'p1': '圣路易斯拱门', 'p2': '布鲁克林桥'},
    {'p1': '布鲁克林桥', 'p2': '圣路易斯拱门'}
]
