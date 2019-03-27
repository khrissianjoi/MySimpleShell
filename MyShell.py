from __future__ import print_function
from cmd import Cmd
import os, sys, subprocess
class MyShell(Cmd):

	def do_cd(self, args):
		if len(args) == 0:
			cwd = os.getcwd()
			print(cwd)
		else:
			try :
				path = args
				os.chdir(path)
			except:
				print('cd: no such file or directory: ' + args)
		self.theprompt()

	def do_clr(self, args):
		os.system('clear') 

	def do_dir(self, args):
		path = '.'
		files = os.listdir(path)
		for name in files:
			print(name)

	def do_environ(self, args):
		environ = os.environ
		for key,value in environ.items():
			print(key +":"+ value + '\n')

	def do_echo(self, args):
		print(args)

	def do_pause(self, args):
		os.system("read -p 'Press Enter to continue...' var");

	def do_quit(self, args):
		"""Quits the program"""
		print('Quitting')
		raise SystemExit

	def theprompt(self):
		prompt.prompt = os.getcwd() + '/myshell>'
	
	def file(self):
		with open(sys.argv[1], 'r') as f:
			prompt.cmdqueue.extend([line.strip() for line in f.readlines()])
			prompt.cmdqueue.append('quit')

	# def do_help(self, args):

	def amperstand(self, args):
		complete = subprocess.run([args[0], args[1]])

	def default(self, args):
		args = args.split()

		if '&' in args:
			try:
				pid = os.fork()
				if pid > 0:
					self.cmdloop()
			except OSError:
				self.cmdloop()
			self.amperstand(args)

		else:
			complete = subprocess.run([args[0], args[1]])
if __name__ == '__main__':
	prompt = MyShell()
	if len(sys.argv) > 1:
		prompt.file()
	prompt.theprompt()
	print('Starting MyShell...')
	prompt.cmdloop()