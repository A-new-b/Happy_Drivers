import flask
import json
import random
import os

Map = flask.Blueprint("Map", __name__)


def rand_position(list_data, nums):
    map_list_r = map_list[::-1]
    # print(map_list_r)
    map_list_k = []
    for i in list_data:
        position = random.randint(0, nums)
        l = random.randint(10, 21)
        map_list_r[position]["linkId"] = i['linkId']
        map_list_r[position]['len'] = l
    for i in map_list_r:
        if "linkId" in i.keys():
            map_list_k.append(i)
    return json.dumps(map_list_k)


def switch_nums(list_data):
    if len(list_data) <= 2:
        return rand_position(list_data, 2)
    elif len(list_data) <= 6:
        return rand_position(list_data, 6)
    elif len(list_data) <= 12:
        return rand_position(list_data, 12)
    elif len(list_data) <= 20:
        return rand_position(list_data, 20)
    elif len(list_data) <= 30:
        return rand_position(list_data, 30)
    elif len(list_data) <= 42:
        return rand_position(list_data, 42)
    elif len(list_data) <= 56:
        return rand_position(list_data, 56)
    elif len(list_data) <= 72:
        return rand_position(list_data, 72)


@Map.route('/api/map', methods=['Post'])
def upload():
    try:
        map_list_r = map_list[::-1]
        post_data = json.loads(flask.request.get_data(as_text=True))
        length = len(post_data)
        # if length<=2:
        #     for i in
        # for i in post_data:
        #
        return {"message": "success"}
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
