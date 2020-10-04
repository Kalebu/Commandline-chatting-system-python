import socket 
import time
import os
import platform 
import threading


class client():
	''' node for sending request to server
		to iniate a communication '''


	#__________initializing a node for TCP communication___________

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#__________ Our node server information _______________


	def __init__(self):
		while True:
			self.server_ip = input('Enter server_ip: ')
			self.server_port = 12345
			if len(self.server_ip.split('.'))<4:
				continue
			break
		print('Finding connection')
		time.sleep(1)


	@property
	def make_connection(self):
		''' Sending connection request to the server node '''
		while True:
			try:
				server = (self.server_ip, self.server_port)
				self.client_socket.connect(server)
				print('Connection succesful made to the server')
				return True
			except:
				print('..');time.sleep(0.1)
				print('..'*2);time.sleep(0.1)
				print('..'*6);time.sleep(0.1)
				if platform.system().lower().startswith('win'):
					os.system('cls')
					continue
				os.system('clear')

	def send_sms(self, msg):
		''' Sending the message to the connected
			Sever '''	
		self.client_socket.send(msg.encode())

	def receive_sms(self):
		''' Receiving message from the node server'''
		while True:
			data = ''
			data = self.client_socket.recv(1024).decode()
			'''Printing sms received from the server '''
			time.sleep(0.001)
			print(data)

	def chat_room(self):
			if self.make_connection:
				Receiving_cio = threading.Thread(target=self.receive_sms)
				Receiving_cio.daemon = True
				Receiving_cio.start()
				while True:	
						message = input()
						message = "\nclient:{}\n".format(message)
						self.send_sms(message)#Client replying 
						continue

if __name__ == '__main__':
	Client = client()
	Client.chat_room()

