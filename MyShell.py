# name: Khrissian Joi Neuda
# student number: 17339711

"""A simple command line shell enforced on Linux"""

from __future__ import print_function
from cmd import Cmd
from subprocess import Popen, PIPE, STDOUT
from MyHelp import MyShellHelp, help_dic
import os, sys, subprocess, shlex

WHITE = '\033[37;0m'
RED = '\033[31;1m'
CYAN = '\033[36;1m'
BOLD = '\033[37;1m'

class MyShell(Cmd):
	def do_cd(self, args):
		"""Changes the current directory to the argument given <directory>, if not given, error is given."""
		if len(args) == 0:
			cwd = os.getcwd()
			print(cwd)
		else:
			try :
				path = args
				os.chdir(path)
			except:
				print('cd: no such file or directory: ' + args)
		"""updates the pathname of the shell environment"""
		self.theprompt()

	def do_clr(self, args):
		"""clears the screen"""
		os.system('clear')

	def do_dir(self, args):
		"""Lists the contents of the current directory"""
		path = '.'
		files = os.listdir(path)
		if '>' not in args:
			for name in files:
				print(name)
		else:
			"""call default function if stdout file '>' is given"""
			args = args.split()
			with open(args[-1],'w') as f:
				for name in files:
					f.write(name+"\n")
				f.close()

	def do_environ(self, args):
		"""Environ lists out the environemnt strings"""
		"""given as a dictionary"""
		environ = os.environ
		if '>' in args:
			"""if stdout file '>' is given"""
			out_file = args.split()[-1]
			with open(out_file, 'w') as f:
				for key,value in environ.items():
					f.write(key + "=" + value + "\n")
				f.close()
		else:
			"""prints out environment strings"""
			for key,value in environ.items():
				print(RED + key + RED + WHITE +"=" + value + WHITE + '\n')

	def do_echo(self, args):
		"""display comment/args"""
		if ">" in args:
			"""stout file is given '>', writes comment/args in file"""
			args = args.split(">")
			file = args[-1].strip()
			content = args[0].strip()
			with open(file, 'w') as f:
				f.write(content)
			f.close()
		else:
			"""prints out comment/args"""
			print(args)

	def do_help(self, args=''):
		if args == '':
			print("Documented commands (type help <topic>):\n========================================\ncd  clr  dir  echo  environ  help  pause  quit")
			print('\n')
			press = input("Please press Enter to view help commands and space to exit and return to MyShell")
			print("\n")
			if press == "":
				for k,v in help_dic.items():
					eval(v)
					self.do_pause('pause', True)
		else:
			check = args.split()[0]
			if '(' and ')' in check:
				check = check[1:-1]
			if check in help_dic:
				"""if help <command> is given where <command> is a valid MyShell command"""
				print("\n")
				"""MyShellHelp class is called, which contains help command documents"""
				call = 'MyShellHelp.help_' + check + '()'
				eval(call)
				print("\n")
			else:
				print("Name " + check + " is not defined")
			
	def do_pause(self, args, help=False):
		""" Pauses operation until 'Enter' is pressed """
		if help == False:
			press = input("Paused, please press Enter to continue")
			while press != "":
				press = input("Please press Enter to continue")
		elif help == True:
			"""Used to pause help command documentation printing, user is asked to press Enter"""
			""" to continue seeing more of the help documentation, or Space to exit and return to MyShell"""
			press = input()
			if press == " ":
				print("Exiting help")
				self.cmdloop()

	def do_quit(self, args):
		"""Quits the program"""
		print('Quitting')
		raise SystemExit

	def theprompt(self):
		"""shell environment path name shell=<pathname>/myshell>"""
		self.prompt = CYAN + os.getcwd() + '/myshell>' + WHITE
	
	def batchfile(self):
		"""shell command line input from file(myshell batchfile)"""
		"""the shell exits after reading the file and running each command that the file contains"""
		with open(sys.argv[1], 'r') as f:
			prompt.cmdqueue.extend([line.strip() for line in f.readlines()])
			prompt.cmdqueue.append('quit')

	def background(self, args):
		"""background processes (&), after launching the process(es)"""
		"""cmdloop() is called so user can return to the command line prompt"""
		complete = Popen([arg for arg in args.split()])
		# self.cmdloop()

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
		""">> redirection token, appends to the output file if file exists in the current directory,"""
		"""otherwise creates output file if file does not exist in the current directory."""

		with open(file,"a") as f:
			for i in range(1,len(args)):
				p = Popen([args[0], args[i]],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
				grep_stdout = p.communicate()[0]
				f.write(grep_stdout.decode())
		f.close()
		return p

	def stdin_stdout(self, args):
		"""> stdin file and < stdout file, reading input from a (< redirectioninput)"""
		"""file that is given, then outputing the file to the (> redirection) file"""
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
			"""if the user input contains '&' (amperstand), program is launched"""
			"""as a background process and return to MyShell command line prompt"""
			self.background(args)
		else:
			"""checks if the users input contains a redirection token"""
			"""wait for the process to end before returning to command line prompt"""
			if (">"in args) and ("<" in args):
				"""stdin and stdout, output and input redirection"""
				p = self.stdin_stdout(args)
				p.wait()
			elif "<" in args:
				"""stdin, input redirection"""
				args = args.split()
				index_in = args.index("<")
				file = args[index_in + 1]
				p = self.stdin_file(args[:index_in], file)
			elif ">>" in args:
				"""output redirection, append to file if exists"""
				args = args.split()
				index_append = args.index(">>")
				file = args[index_append + 1]
				p = self.append_file(args[:index_append], file)
			elif ">" in args:
				"""stdout, output redirection"""
				args = args.split()
				index_out = args.index(">")
				file = args[index_out + 1]
				p = self.overwrite_file(args[:index_out], file)
			else:
				"""the process will execute and run"""
				files = args.split()
				programmename = files[0]
				files = files[1:]
				length = len(files)
				for i in range(0,len(files)):
					p = Popen([programmename, files[i]])
					p.wait()
	
if __name__ == '__main__':
	prompt = MyShell()
	if len(sys.argv) > 1:
		prompt.batchfile()
	prompt.theprompt()
	print('Starting MyShell...')
	prompt.cmdloop()
