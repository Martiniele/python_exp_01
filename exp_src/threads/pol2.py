import time
import threadpool


def sayhello(str):
    print "Hello ", str
    time.sleep(2)


if __name__ == "__main__":
    name_list = ['xiaozi', 'aa', 'bb', 'cc''xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa', 'bb', 'xiaozi', 'aa']
    start_time = time.time()
    pool = threadpool.ThreadPool(20)
    requests = threadpool.makeRequests(sayhello, name_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    print '%d second' % (time.time() - start_time)
