import os, platform
os.system("cd $HOME/")
#os.system("termux-setup-storage")
#os.system("xdg-open https://www.facebook.com/100346185630243/posts/248205137511013/?app=fbl")
os.system("clear")
print("\t Tool updating please wait..")
try:
    import requests
except ImportError:
    os.system("pip install requests")


rana=platform.architecture()[0]
if rana=="32bit":
    __import__("rsa32").mysec()
elif rana=="64bit":
    __import__("rsa").mysec()