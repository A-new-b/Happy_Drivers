from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import os

# spath = "\"C:\\\\Users\\\\krusl\\\\tempk.jpg\""

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(path, "img", "temp.jpg")
# print(file_path)


def Generate(s):
    k = WolframLanguageSession()
    print(k.evaluate(wlexpr("Export[" + file_path + "," + s + "]")))
    k.stop()
    return file_path
