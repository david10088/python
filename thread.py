#!/usr/bin/env python
# -*-coding:UTF-8-*-
import time
import  multiprocessing 

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"
    return "done" + msg

def ab():
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(8):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print ":::", res.get()
    print "Sub-process(es) done."


ab()