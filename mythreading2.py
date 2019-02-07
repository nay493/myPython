import threading
import time


def sleeper(n, name):
    print("Hi {} sleeping for {} secs".format(name, n))
    time.sleep(n)
    print("Hello! got woke up\n")


start = time.time()
for i in range(4):
    sleeper(i, 'thread{}'.format(i))

end = time.time()
print('Time taken is {}'.format(end - start))


