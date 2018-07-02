#文本进度条 简单的开始
import time

scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")









#文本进度条 单行动态刷新
import time

for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)








#文本进度条 实例完整效果
import time

scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()

for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)

print("\n"+"执行结束".center(scale//2,'-'))


