import sys

def example():
	if sys.platform == 'win32':
		if sys.version_info.minor == 7:
			print('Running python 3.7 on windows.')
		else:
			print('Running python 3.9 on windows.')
	elif sys.platform.startswith('linux'):
		if sys.version_info.minor == 7:
			print('Running python 3.7 on linux.')
		else:
			print('Running python 3.9 on linux.')
	elif sys.platform.startswith('darwin'):
		if sys.version_info.minor == 7:
			print('Running python 3.7 on OSX.')
		else:
			print('Running python 3.9 on OSX.')
