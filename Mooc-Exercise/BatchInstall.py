import os

#分别列出需要安装的第三方库
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests",
        "jieba", "beautifulsoup4", "wheel", "networkx", "sympy",
        "pyinstaller", "django", "flask", "werobot", "pyqt5",
        "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}


#利用try-except异常处理进行安装
try:
    for lib in libs:
        os.system("pip3 install " + lib)   #逐一取出libs中的库名，逐一安装
    print("Successful")
except:
    print("Failed Somehow")

