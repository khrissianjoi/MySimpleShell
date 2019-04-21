# name: Khrissian Joi Neuda
# student number: 17339711

"""A simple command line shell enforced on Linux"""

from __future__ import print_function
from cmd import Cmd
from subprocess import Popen, PIPE, STDOUT
from MyHelp import MyHelp, help_dic
from MyRedirection import MyRedirection
import os, sys, subprocess, shlex
import time



WHITE = '\033[37;0m'
RED = '\033[31;1m'
CYAN = '\033[36;1m'
BOLD = '\033[37;1m'


"""io mode as keys, providing token and necessary function"""
io = {
	'a':('>>', 'MyRedirection.append_file'),
	'w': ('>', 'MyRedirection.overwrite_file'),
	'r': ('<', 'MyRedirection.stdin_file')
	}
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
		mode = self.io_parse(args)	
		if not mode:
			for name in files:
				print(name)
		else:
			"""call default function if stdout file '>' is given"""	
			args = args.split()
			with open(args[-1],mode) as f:
				for name in files:
					f.write(name+"\n")
				f.close()

	def do_environ(self, args):
		"""Environ lists out the environemnt strings"""
		"""given as a dictionary"""
		environ = os.environ
		mode = self.io_parse(args)
		if mode:
			out_file = args.split()[-1]
			with open(out_file, mode) as f:
				for key,value in environ.items():
					f.write(key + "=" + value + "\n")
				f.close()
		else:
			"""prints out environment strings"""
			for key,value in environ.items():
				print(RED + key + RED + WHITE +"=" + value + WHITE + '\n')

	def do_echo(self, args):
		"""display comment/args"""
		mode = self.io_parse(args)
		if mode:
			"""stout file is given '>' or '>>', writes comment/args in file"""
			token = io[mode][0]
			args = args.split(token)
			file = args[-1].strip()
			content = args[0].strip()
			print(content)
			with open(file, mode) as f:
				f.write(content)
			f.close()
		else:
			"""prints out comment/args"""
			print(args)

	def do_help(self, args=''):
		mode = self.io_parse(args)
		if args == '':
			print("Documented commands (type help <topic>):\n========================================\ncd  clr  dir  echo  environ  help  pause  quit")
			print('\n')
			press = input("Please press Enter to view help commands and space to exit and return to MyShell")
			print("\n")
			if press == "":
				for k,v in help_dic.items():
					eval(v[0])
					self.do_pause('pause', True)
				print("All commands have been viewed")
				time.sleep(1)
				print("Exiting help")
				time.sleep(1)
		elif mode:
			mode = self.io_parse(args)
			args = args.split()
			with open(args[-1], mode) as f:
				for k,v in help_dic.items():
					view = v[1]
					f.write(view+"\n")
			f.close()
		else:
			check = args.split()[0]
			if '(' and ')' in check:
				check = check[1:-1]
			if check in help_dic:
				"""if help <command> is given where <command> is a valid MyShell command"""
				print("\n")
				"""MyShellHelp class is called, which contains help command documents"""
				call = 'MyHelp.help_' + check + '()'
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

	def io_parse(self, args):
		"""this differentiate as to what redirection token (ie. '>', '>>' or '<') is given"""
		"""or if there was any given"""
		"""the correct mode is then returned"""
		if '>' in args and '<' in args:
			return 'both'
		if '>>' in args:
			return 'a'
		elif '>' in args:
			return 'w'
		elif '<' in args:
			return 'r'
		return None

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
		
	def default(self, args):
		if '&' in args:
			"""if the user input contains '&' (amperstand), program is launched"""
			"""as a background process and return to MyShell command line prompt"""
			self.background(args)
		else:
			"""checks if the users input contains a redirection token"""
			"""wait for the process to end before returning to command line prompt"""
			mode = self.io_parse(args)
			if mode:
				if mode == 'both':
					"""stdin and stdout, output and input redirection"""
					p = MyRedirection.stdin_stdout(args)
				else:
					"""parses the command line args"""
					args = args.split()
					mode_index = io[mode][0]
					mode_index = args.index(mode_index)
					file = args[mode_index + 1]
					"""io dictionary provides the necessary function name to call"""
					p = eval(io[mode][1]+'(args[:mode_index], file)')
				p.wait()
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
	while True:
		try:
			prompt.cmdloop()
		except Exception as e:
			print('Error invalid operation')
			continue
