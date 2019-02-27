# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: multiprocess_test.py
@time: 2019/2/27
"""
from multiprocessing import Process,Pipe
import time,os


if __name__ == '__main__':
    # 创建管道对象
    fd1, fd2 = Pipe()

    def fun(name):
        time.sleep(1)
        fd2.send(os.getppid())

    jobs = []
    # 创建5个子进程
    for i in range(5):
        p = Process(target = fun,args = (i,))
        jobs.append(p)
        p.start()

    for i in range(5):
        data = fd1.recv()
        print(data)

    for i in jobs:
        i.join()