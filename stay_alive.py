import time
import urllib


def stay_alive():
	while True:
		start = time.time()
		
		while True:
			end = time.time()

			# This 15 is for the amount of minutes you change it and take it upto 30 minutes at most
			if ((end - start) >= (15 * 60)):
				urllib.requests.urlopen("the repl web url which you will get after running goes here")
				break
