
import sys

print (sys.version_info)
print (sys.version_info[:2])

if sys.version_info[:2] == (2, 7):
	print ('y')
sys.exit()
