import os
from ctypes import *

dll = cdll.LoadLibrary(".\DllGIS1.dll")

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

dll.itf_DataSearch2.restype = c_char_p
dll.itf_DataSearch2.argtype = [c_int]

dll.itf_GetLastTick.restype = c_int
dll.itf_GetLastTick.argtype = []

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
    return szBuffer.value
    #return str(szBuffer.value, encoding="gb2312")

def DataSearch2(id):
    szBuffer = c_char_p(dll.itf_DataSearch2(id))
    return szBuffer.value

def GetLastTick():
    return dll.itf_GetLastTick()

print(Init("C:\\Users\\krusl\\Documents\\实习\\2020_07_13\\东大项目参考资料\\需求\\GTBL.dat"))
#print(DataGet())
print(GetRecordCount())
print(SortMethodGet())
print(DataGetEx(0, 5))
print(DataSearch(2132))

