#!/usr/bin/python
import time
import thread
def one():
	while True:
		print "hello"
		time.sleep(1)
def two():
	while True:
		print "word"
		time.sleep(1)
thread.start_new_thread(one,())
thread.start_new_thread(two,())
while True:
	time.sleep(2)
	pass
