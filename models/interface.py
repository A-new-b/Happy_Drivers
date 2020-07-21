import os
from ctypes import *

path = os.path.dirname(os.path.abspath(__file__))

# print(path)
dll = cdll.LoadLibrary(path + "\DLLGIS1.dll")

dll.itf_Init.restype = c_char_p
dll.itf_Init.argtype = [c_wchar_p]

dll.itf_DataGet.restype = c_char_p
dll.itf_DataGet.argtype = []

dll.itf_SortMethodGet.restype = c_char_p
dll.itf_SortMethodGet.argtype = []

dll.itf_ExecSort.restype = c_int
dll.itf_ExecSort.argtype = [c_int]

dll.itf_GetCount.restype = c_int
dll.itf_GetCount.argtype = []

dll.itf_DataGetEx.restype = c_char_p
dll.itf_DataGetEx.argtype = [c_int, c_int]



def Init(path):
    szBufferIn = create_unicode_buffer(path)
    szBufferOut = c_char_p(dll.itf_Init(szBufferIn))
    return str(szBufferOut.value, encoding="gb2312")


def DataGet():
    Init(path + "\GTBL.dat")
    szBuffer = c_char_p(dll.itf_DataGet())
    return szBuffer.value.decode(encoding='gb2312')


def SortMethodGet():
    szBuffer = c_char_p(dll.itf_SortMethodGet())
    return szBuffer.value.decode(encoding='gb2312')


def ExecSort(id):
    Init(path + "\GTBL.dat")
    return dll.itf_ExecSort(id)


def GetRecordCount():  # 获取记录总数
    Init(path + "\GTBL.dat")
    return dll.itf_GetCount()


def DataGetEx(begin, end):  # 从某个位置开始获取
    Init(path + "\GTBL.dat")
    szBuffer = c_char_p(dll.itf_DataGetEx(begin, end))
    return str(szBuffer.value, encoding="gb2312")


# def init_r():
#     Init(path + "\GTBL.dat")


# print(Init(path + "\GTBL.dat"))
# print(SortMethodGet())

# print(DataGetEx(1, 20))
