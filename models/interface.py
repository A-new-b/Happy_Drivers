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


def Init(path):
    szBufferIn = create_unicode_buffer(path)
    szBufferOut = c_char_p(dll.itf_Init(szBufferIn))
    return str(szBufferOut.value, encoding="utf-8")


def DataGet():
    szBuffer = c_char_p(dll.itf_DataGet())
    return szBuffer.value.decode(encoding='gb2312')


def SortMethodGet():
    szBuffer = c_char_p(dll.itf_SortMethodGet())
    return szBuffer.value.decode(encoding='gb2312')


def ExecSort(id):
    return dll.itf_ExecSort(id)


# def init_r():
#     Init(path + "\GTBL.dat")
print(Init(path + "\GTBL.dat"))
# print(SortMethodGet())
