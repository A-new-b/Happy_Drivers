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

dll.itf_DataSearch.restype = c_char_p
dll.itf_DataSearch.argtype = [c_int]


def Init(path):
    szBufferIn = create_unicode_buffer(path)
    szBufferOut = c_char_p(dll.itf_Init(szBufferIn))
    return str(szBufferOut.value, encoding="gb2312")


def DataGet():
    szBuffer = c_char_p(dll.itf_DataGet())
    return str(szBuffer.value, encoding="gb2312")


def SortMethodGet():
    szBuffer = c_char_p(dll.itf_SortMethodGet())
    return str(szBuffer.value, encoding="gb2312")


def ExecSort(id):
    return dll.itf_ExecSort(id)


def GetRecordCount():
    return dll.itf_GetCount()


def DataGetEx(begin, end):
    szBuffer = c_char_p(dll.itf_DataGetEx(begin, end))
    return str(szBuffer.value, encoding="gb2312")


def DataSearch(id):
    szBuffer = c_char_p(dll.itf_DataSearch(id))
    return str(szBuffer.value, encoding="gb2312")


print(Init(path + "\GTBL.dat"))
# #print(DataGet())
# print(GetRecordCount())
# print(SortMethodGet())
# print(DataGetEx(0, 5))

print(DataSearch(11852))
