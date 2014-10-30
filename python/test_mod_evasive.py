import sys

import human_curl as hurl

target = ''
count  = 200


def spamspamspam(url,tries):
	for i in range(tries):
		if "http" in url:
			c = hurl.get(url)
		else:
			c = hurl.get('http://'+url)
		if c.status_code is not "302":
			print " Returned a {} status code. Not blocking yet. ".format(c.status_code)
		else:
			print " Blocking! (Code {}) ".format(c.status_code)

if __name__ == '__main__':
	if sys.argv[1]:
		target = sys.argv[1]
		if sys.argv[2]:
			count = int(sys.argv[2])
		print " Running {} attempts against {} ".format(count,target)
		spamspamspam(target,count)
	else:
		print " Usage: test_mod_evasive.py targeturl.com [iteration_count] "
