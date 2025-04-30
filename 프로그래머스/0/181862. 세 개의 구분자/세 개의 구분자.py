def solution(myStr):
    for x in ["a", "b", "c"]:
        myStr = myStr.replace(x, " ")
    myStr = myStr.split()
    return myStr if myStr else ["EMPTY"]