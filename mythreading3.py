import threading
import time


def sleeper(n, name):
    print("Hi {} sleeping for {} secs".format(name, n))
    time.sleep(n)
    print("Hello! got woke up\n")


start = time.time()


thread_list = []
for i in range(4):
    t = threading.Thread(target=sleeper, name='thread{}'.format(i), args=(5, 'thread'))
    thread_list.append(t)
    t.start()

t.join()

end = time.time()
print('Time taken is {}'.format(end - start))


