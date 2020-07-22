from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import os

# spath = "\"C:\\\\Users\\\\krusl\\\\tempk.jpg\""
# spath = "\"C:\\\\Users\\\\Administrator\\\\Desktop\\\\Happy_Drivers\\\\img\\\\temp.jpg\""
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(path, "img", "temp.jpg")


# print(file_path)
k = WolframLanguageSession()


def Generate(s):
    print(k.evaluate(wlexpr("Export[" + file_path + "," + s + "]")))
    # print(k.evaluate(wlexpr("Export[" + spath + "," + s + "]")))
    return {"path": "temp.jpg"}

def endSession():
    k.stop()
