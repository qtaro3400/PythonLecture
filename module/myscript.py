# 標準ライブラリ、サードパーティーのライブラリ、自分たちのライブラリ、ローカルのライブラリ
import sys
sys.path.append("C:\\Users\\poohm\\Desktop\\PythonLecture\\function")
import docstring

import mymodule as mm
# from mymodule import myfunc, myvariable, anotherfunc
# from mymodule import *

# mymodule.myfunc()
mm.myfunc()
mm.anotherfunc()
print(mm.myvariable)
# print(mymodule.myvariable)

print(sys.path)
print(docstring.multiply(3, 4))