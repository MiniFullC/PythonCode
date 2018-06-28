#这个程序模拟两个选手A和B的某种竞技比赛
from random import random

#打印程序的介绍性信息
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0-1之间的小数表示)")


#获得程序运行参数
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1)"))
    b = eval(input("请输入选手B的能力值(0-1)"))
    n = eval(input("模拟比赛的场次："))
    return a,b,n


#输出球员A和球员B获胜比赛的场次及概率。
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，功模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))



def gameOver(a,b):
    return a==15 or b==15



#模拟一场比赛
def simoOneGame(probA, probB):
    scoreA, scoreB = 0,0
    serving = "A"
    while not gameOver(scoreA,scoreB):   #使用随机函数比较AB能力与获得分数之间的关系
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB        #返回调用函数


#模拟N局比赛
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):    #每次用simOneGames函数所产生胜利场数，循环累加
        scoreA, scoreB = simoOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def main():
    printIntro()
    probA ,probB ,n = getInputs()
    winsA,winsB = simNGames(n, probA,probB)
    printSummary(winsA, winsB)


main()

