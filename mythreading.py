import threading
import time


def sleeper(n, name):
    print("Hi {} sleeping for {} secs".format(name, n))
    time.sleep(n)
    print("Hello! got woke up\n")


t1 = threading.Thread(target=sleeper, name='t1', args=(5, 'thread1'))
t1.start()
#t1.join()
# uncomment the above see the change
# join makes t1 to wait until t1 is done

print ('main thread')
print ('main thread')
print ('main thread')

