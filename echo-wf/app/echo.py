import sys, os

for i, argv in enumerate(sys.argv):
	print('XXXXX ' + str(i) + ":" + argv)

if 'TS' in os.environ:
	print('XXXXX TS=' + os.environ['TS'])
else:
	print('XXXXX no TS in env')

