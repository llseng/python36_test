# -*- coding: utf-8 -*-
# @Author: llseng
# @Date:   2021-01-12 11:17:57
# @Last Modified by:   llseng
# @Last Modified time: 2021-01-12 14:36:06

import _thread, time, json

class ThreadPool():
    """线程池对象"""

    def __init__(self):
        self.ids = []
        self.thread_count = 4
        self.task_queue = []
        self.lock = _thread.allocate_lock()
        self.task_func = None

    def __repr__(self):
        return json.dumps( {
            'ids': self.ids,
            'thread_count': self.thread_count,
            'task_queue': self.task_queue,
            # 'lock': self.lock,
            # 'task_func': self.task_func
        })
    
    def en_task(self, **args):
        with self.lock:
            self.task_queue.append( args )

    def de_task(self):
        task_args = None
        with self.lock:
            if len( pool.task_queue ):
                task_args = self.task_queue.pop( 0 )
        return task_args

    def set_task_func(self, func):
        if not callable( func ): return
        self.task_func = func

    @staticmethod
    def __manager( pool ):
        tid = _thread.get_ident()
        pool.ids.append( tid )
        while True:
            task_args = pool.de_task()
            if task_args == None:
                print( "T %d: sleep 1" % tid )
                time.sleep( 1 )
                continue

            print( "T %d: task start" % tid )
            pool.task_func( task_args )
            print( "T %d: task end" % tid )

    def run(self):
        if self.task_func == None:
            raise Exception( 'task_func is None! Use "pool.set_task_func( func )" specify' )
        for i in range( self.thread_count ):
            _thread.start_new_thread( ThreadPool.__manager, (self,) )


def tfunc( parems ):
    sleep_time = parems.get( 'sleep', 1 )
    time.sleep( sleep_time )
    print( repr( parems ) )


pool = ThreadPool()
pool.set_task_func( tfunc )
pool.run()

pool.en_task( sleep = 5, task = 1 )
pool.en_task( sleep = 3, task = 2 )
pool.en_task( sleep = 5, task = 3 )
pool.en_task( sleep = 8, task = 4 )
pool.en_task( sleep = 7, task = 5 )
pool.en_task( sleep = 6, task = 6 )
pool.en_task( sleep = 5, task = 7 )
pool.en_task( sleep = 1, task = 8 )

i = 40
while i:
    i -= 1
    time.sleep( 1 )
    print( pool )