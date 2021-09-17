# import myfirstpackage.module1
# import myfirstpackage.module2
#
# myfirstpackage.module1.myfunc()
# myfirstpackage.module2.myfunc()


# from myfirstpackage import module1, module2
#
# module1.myfunc()
# module2.myfunc()


# from myfirstpackage.module1 import myfunc
# from myfirstpackage.subdir.module2 import myfunc

# import myfirstpackage
# import myfirstpackage.module1
#
# myfirstpackage.myfunc()
# myfirstpackage.module1.myfunc()



# from myfirstpackage.subdir import *
# myfunc()


import myfirstpackage.subdir.module2

myfirstpackage.subdir.module2.myfunc2()