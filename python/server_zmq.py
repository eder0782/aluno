import time
import zmq
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
	try:
		#  Wait for next request from client
		message = socket.recv()
		print("Received request: %s" % message)
		print(datetime.now())

		#  Do some 'work'
		time.sleep(1)

		#  Send reply back to client
		socket.send(b"Mundo Novo")
	except:
		break