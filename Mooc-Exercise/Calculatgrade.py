try:
    score = eval(input())
    if score>100 or score<0:
        print("输入有误！")
    else:
        a = int(100 / 10)
        if a == 10 or a == 9:
            print("输入成绩属于A级别。")
            print("祝贺你通过考试！")
        elif a == 8:
            print("输入成绩属于B级别。")
            print("祝贺你通过考试！")
        elif a == 7:
            print("输入成绩属于C级别。")
            print("祝贺你通过考试！")
        elif a == 6:
            print("输入成绩属于D级别。")
            print("祝贺你通过考试！")
        else:
            print("输入成绩属于E级别。")
except:
    print("输入有误！")
finally:
    print("好好学习，天天向上！")
