from main import *

test1 = string("Hej")
test2 = string(152)
print(test1 + " " + test2)

test3 = intnum(43)
test4 = intnum("Hej")
print(str(test3) + " " + str(test4))

test5 = floatnum(56.94)
test6 = floatnum(93)
test7 = floatnum("Hej")
print(str(test5) + " " + str(test6) + " " + str(test7))

test8 = boolean(True)
test9 = boolean("false")
test10 = boolean("Hej")
test11 = boolean(0)
test12 = boolean(205)
print(str(test8) + " " + str(test9) + " " + str(test10) + " " + str(test11) + " " + str(test12))

test13 = table(9, 7, 9 , 15, 189, 90, 89, 12, 182, 95)
test14 = table(1, test13)
test15 = test14[0]
test16 = table(9, test13)
print(str(test13) + " " + str(test14) + " " + str(test15) + " " + str(test16))