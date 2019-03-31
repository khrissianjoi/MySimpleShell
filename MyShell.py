# name: Khrissian Joi Neuda
# student number: 17339711

"""A simple command line shell enforced on Linux"""

from __future__ import print_function
from cmd import Cmd
from subprocess import Popen, PIPE, STDOUT
import os, sys, subprocess, shlex

WHITE = '\033[37;0m'
RED = '\033[31;1m'
CYAN = '\033[36;1m'
BOLD = '\033[37;1m'

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
			print(RED + key + RED + WHITE +" - " + value + WHITE + '\n')

	def do_echo(self, args):
		print(args)

	def do_pause(self, args):
		press = input("Please press Enter to continue")
		while press != "":
			press = input("Please press Enter to continue")

	def do_quit(self, args):
		"""Quits the program"""
		print('Quitting')
		raise SystemExit

	def theprompt(self):
		prompt.prompt = CYAN + os.getcwd() + CYAN + '/myshell>' + WHITE
	
	def file(self):
		with open(sys.argv[1], 'r') as f:
			prompt.cmdqueue.extend([line.strip() for line in f.readlines()])
			prompt.cmdqueue.append('quit')


	def background(self, args):
		try:
				pid = os.fork()
				if pid > 0:
					self.cmdloop()
		except OSError:
			self.cmdloop()
		if "<" in args:
			args = args[:-1]
			self.inside(args)
		elif ">>" in args:
			args = args[:-1]
			self.double_outside(args)
		elif ">" in args:
			args = args[:-1]
			self.outside(args)
		else:
			complete = subprocess.run([arg for arg in args.split()])
		self.cmdloop()

	def inside(self, args):
		args = shlex.split(args)
		p = Popen(args[:-2], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
		grep_stdout = p.communicate(input=Popen(['cat',args[-1]], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0])[0]
		print(grep_stdout.decode())

	def outside(self, args):
		file = shlex.split(args)
		with open(file[-1], "w") as f:
			p = Popen([arg for arg in args.split()][:-2],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
			grep_stdout = p.communicate()[0]
			f.write(grep_stdout.decode())
			f.close()

	def double_outside(self, args):
		""">> redirection token, appends to the output file if file exists in the current directory, otherwise creates output file if file does not exist in the current directory."""
		curr = os.getcwd()
		file = shlex.split(args)

		with open(file[-1],"a") as f:
			p = Popen([arg for arg in args.split()][:-2],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
			grep_stdout = p.communicate()[0]
			f.write(grep_stdout.decode())
			f.close()

	def default(self, args):
		if '&' in args:
			self.background(args)
		else:
			if (">"in args) and ("<" in args):
				pass
			elif "<" in args:
				self.inside(args)
			elif ">>" in args:
				self.double_outside(args)
			elif ">" in args:
				self.outside(args)
			elif len(args.split()) <= 2:
				print("h")
				complete = subprocess.run([arg for arg in args.split()])
			else:
				files = args.split()
				programmename = files[0]
				files = files[1:]
				length = len(files)
				for i in range(0,len(files)):
					complete = subprocess.run([programmename, files[i]])

	
	def help_echo(self):
		print(RED+ "ECHO <comment>" +RED + WHITE +" - echo command displays <comment> on the display followed by a new line"+WHITE)
	
	def help_environ(self):
		print(RED+"ENVIRON"+ RED + WHITE + " - environ command list all the environment strings" + WHITE)

	def help_clr(self):
		print(RED + "CLR" + RED + WHITE + " - clears the shell" + WHITE)

	def help_quit(self):
		print(RED + "QUIT" + RED + WHITE + " - quit command raises the SystemExist and stops the execution of this script." + WHITE)

	def help_cd(self):
		print(RED + "CD <directory>" + RED + WHITE + " - cd command changes the current default directory to <directory>. If the <directory> argument is not present, report the current directory. If the directory does not exist an appropriate error should be reported." + WHITE)

	def help_pause(self):
		print(RED + "PAUSE" + RED + WHITE + " - pause command suspends the operation of the shell until 'Enter' is pressed by the user." + WHITE)

	def help_dir(self):
		print(RED + "DIR <directory>" + RED + WHITE + " - dir command lists the contents of directory <directory>." + WHITE)

if __name__ == '__main__':
	prompt = MyShell()
	if len(sys.argv) > 1:
		prompt.file()
	prompt.theprompt()
	print('Starting MyShell...')
	prompt.cmdloop()
