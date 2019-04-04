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

		self.theprompt()

	def do_clr(self, args):
		os.system('clear')

	def do_dir(self, args):
		if '>' not in args:
			path = '.'
			files = os.listdir(path)
			for name in files:
				print(name)

		else:
			self.default('dir ' + args)

	def do_environ(self, args):
		if '>' in args:
			out_file = args.split()[-1]
			with open(out_file, 'w') as f:
				environ = os.environ
				for key,value in environ.items():
					f.write(key + "=" + value + "\n")
				f.close()
		else:
			environ = os.environ
			for key,value in environ.items():
				print(RED + key + RED + WHITE +"=" + value + WHITE + '\n')

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
		self.prompt = CYAN + os.getcwd() + '/myshell>' + WHITE
	
	def file(self):
		with open(sys.argv[1], 'r') as f:
			prompt.cmdqueue.extend([line.strip() for line in f.readlines()])
			prompt.cmdqueue.append('quit')

	def background(self, args):
		if "<" in args and ">" in args:
			self.inside_outside(args)
		elif "<" in args:
			args = args[:-1]
			self.inside(args)
		elif ">>" in args:
			args = args[:-1]
			self.double_outside(args)
		elif ">" in args:
			args = args[:-1]
			self.outside(args)
		else:
			complete = Popen([arg for arg in args.split()])
		self.cmdloop()

	def stdin_file(self, args, file):
		""" < stdin file (input redirection)"""
		p = Popen([args[0], args[1]], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
		grep_stdout = p.communicate(input=Popen(['cat', file], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0])[0]
		print(grep_stdout.decode())
		if len(args) - 1 > 1:
			current = args[0:1] + args[2:]
			self.default(" ".join(current))

		return p

	def overwrite_file(self, args, file):
		""" > stdout file (output redirection)"""
		with open(file, "w") as f:
			for i in range(1,len(args)):
				p = Popen([args[0], args[i]],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
				grep_stdout = p.communicate()[0]
				f.write(grep_stdout.decode())
		f.close()

		return p

	def append_file(self, args, file): 
		""">> redirection token, appends to the output file if file exists in the current directory, otherwise creates output file if file does not exist in the current directory."""

		with open(file,"a") as f:
			for i in range(1,len(args)):
				p = Popen([args[0], args[i]],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
				grep_stdout = p.communicate()[0]
				f.write(grep_stdout.decode())
		f.close()
		return p

	def stdin_stdout(self, args):
		args = shlex.split(args)
		program = args[0]

		index_out = args.index(">")+1
		index_in = args.index("<")+1
		out = args[index_out]
		in_ = args[index_in]

		with open(out, 'w') as f:
			for i in range(1,min(index_out-1, index_in-1)):
				p = Popen([program, args[i]], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
				grep_stdout = p.communicate(input=Popen(['cat',in_], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0])[0]
				f.write(grep_stdout.decode())
		f.close()
		return p
		
	def default(self, args):
		if '&' in args:
			self.background(args)
		else:
			if (">"in args) and ("<" in args):
				p = self.stdin_stdout(args)
				p.wait()
			elif "<" in args:
				args = args.split()
				index_in = args.index("<")
				file = args[index_in + 1]
				p = self.stdin_file(args[:index_in], file)
				p.wait()
			elif ">>" in args:
				args = args.split()
				index_append = args.index(">>")
				file = args[index_append + 1]
				p = self.append_file(args[:index_append], file)
				p.wait()
			elif ">" in args:
				args = args.split()
				index_out = args.index(">")
				file = args[index_out + 1]
				p = self.overwrite_file(args[:index_out], file)
				p.wait()
			else:
				files = args.split()
				programmename = files[0]
				files = files[1:]
				length = len(files)
				for i in range(0,len(files)):
					p = Popen([programmename, files[i]])
					p.wait()
	
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
