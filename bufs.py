import sys
import time

sys.stdout.flush()
#Flushes buffers

# https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method

remove_time = '\b\b\b\b\b'
start_time = time.time()

print(sys.stdout.write('%.5s%s'% (time.time() - start_time,remove_time)))

#sys.path.append()
print (sys.argv)

sys.stderr.write('stderr\n')
sys.stdout.write('stdout\n')
