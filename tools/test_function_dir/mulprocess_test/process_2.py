# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: process_2.py
@time: 2019/2/27
"""
# from datetime import time
import time
from multiprocessing import Process
import os
from multiprocessing import Pool

# 子进程要执行的代码
def run_proc(name):
    print('进程1等待10秒')
    time.sleep(10)

    print ('Run child process %s (%s)...' % (name, os.getpid()))


def run_proc2():
    print("进程2，等待10秒")
    time.sleep(10)


if __name__=='__main__':
    # print ('Parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test',))
    # print ('Process will start.')
    #
    # p.start()
    # p.join()
    #
    # print(p.is_alive())
    # p2 = Process(target=run_proc2)
    # p2.start()
    #     # p2.join()
    # print( 'Process end.')
    # print('11111111111111111111111111111111111')

    # p = Pool(process_nums)