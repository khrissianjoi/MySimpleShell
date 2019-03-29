from __future__ import print_function
from cmd import Cmd
import os, sys, subprocess, shlex
from subprocess import Popen, PIPE, STDOUT
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
		self.cmdloop()

	def open(self, args):
		args = shlex.split(args)
		p = Popen(args[:-2], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
		grep_stdout = p.communicate(input=Popen(['cat',args[-1]], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0])[0]
		print(grep_stdout.decode())

	def default(self, args):
		if '&' in args:
			try:
				pid = os.fork()
				if pid > 0:
					self.cmdloop()
			except OSError:
				self.cmdloop()
			if "<" in args:
				args = args[:-1]
				self.open(args)
			else:
				complete = subprocess.run([arg for arg in args.split()])
			self.cmdloop()

		else:
			if "<" in args:
				self.open(args)
			else:
				complete = subprocess.run([arg for arg in args.split()])
			

if __name__ == '__main__':
	prompt = MyShell()
	if len(sys.argv) > 1:
		prompt.file()
	prompt.theprompt()
	print('Starting MyShell...')
	prompt.cmdloop()
