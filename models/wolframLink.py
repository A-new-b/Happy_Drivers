from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import os

# spath = "\"C:\\\\Users\\\\krusl\\\\tempk.jpg\""
# spath = "\"C:\\\\Users\\\\Administrator\\\\Desktop\\\\Happy_Drivers\\\\img\\\\temp.jpg\""

Num = 0
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(path, "img", "temp.jpg")


def createPath():
    global Num
    Num += 1
    return "\"C:\\\\Users\\\\Administrator\\\\Desktop\\\\Happy_Drivers\\\\img\\\\temp" + str(Num) + ".jpg\""


# print(file_path)
k = WolframLanguageSession()


def Generate(s):
    print(k.evaluate(wlexpr("Export[" + createPath() + "," + s + "]")))
    # print(k.evaluate(wlexpr("Export[" + spath + "," + s + "]")))
    return {"path": "temp"+str(Num)+".jpg"}


def endSession():
    k.stop()
