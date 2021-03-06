import time
from multiprocessing import Pool, Manager

import threadpool


def do(str):
    print "Hello ", str
    time.sleep(20)


def sayhello(que):
    name_list = que.get()
    pool = threadpool.ThreadPool(400)
    requests = threadpool.makeRequests(do, name_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()


if __name__ == "__main__":
    name_list = ['xiaozi', 'aa', 'bb', 'cc''xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa',
                 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb']
    start_time = time.time()
    pool = Pool(processes=100)
    # que = Manager().Queue(20)
    for i in name_list:
        # while que.full():
        #     time.sleep(20)
        # que.put(name_list)
        pool.apply_async(do, (i, ))
    pool.close()
    pool.join()
    print '%d second' % (time.time() - start_time)
