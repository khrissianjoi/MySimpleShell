"""A simple command line shell enforced on Linux"""

from __future__ import print_function
from cmd import Cmd
from subprocess import Popen, PIPE, STDOUT
from MyHelp import MyHelp, help_dic
from MyRedirection import MyRedirection
import os, sys, subprocess, shlex
import time
import re

WHITE = '\033[37;0m'
RED = '\033[31;1m'
CYAN = '\033[36;1m'
BOLD = '\033[37;1m'

"""io mode as keys, providing a tuple with token (index 0) and necessary function (index 1)"""
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
		mode = self.io_parse(args)
		args = args.split()
		try:
			if mode:
				"""output redirection"""
				with open(args[-1], mode) as f:
					args = args[:-2]
					if  not len(args):
						path = '.'
					else:
						"""if directory argument is given"""
						path = os.getcwd() +'/'+args[0]
					files = os.listdir(path)					
					for name in files:
						f.write(name+'\n')
				f.close()
			else:
				if len(args):
					"""if directory argument is given"""
					path = os.getcwd() + '/'+args[0]
				else:
					path = '.'
				files = os.listdir(path)
				"""standard output to the screen"""
				for name in files:
					print(name)
		except:
			print('cd: no such file or directory: ' + args)
			
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
			"""get rid of tabs"""
			content = " ".join(args[0].split())

			with open(file, mode) as f:
				f.write(content)
			f.close()
		else:
			"""prints out comment/args"""
			"""removes tabs"""
			args = " ".join(args.split())
			print(args)

	def do_help(self, args=''):
		man = 'readme'
		mode = self.io_parse(args)
		if args == '':
			print("Welcome to MyShell help!\n")
			"""display the user manual using ENTER to see more"""
			with open(man, 'r') as f:
				lines = f.readlines()
				i = 0
				for line in lines:
					i += 1
					print(line.rstrip())
					if i % 20 == 0:
						press= input()
						if press == ' ':
							break
				
		elif mode:
			args = args.split()
			if '>' not in args[0]:
				"""specific command descritpion output redirection"""
				with open(args[-1], mode) as f:
					f.write(help_dic[args[0]][1])
				f.close()
			else:
				"""user manual output"""
				with open(args[-1], mode) as f:
					with open(man, 'r') as h:
						lines = h.readlines()
						for line in lines:
							f.write(line)
						h.close()
				f.close()
		else:
			check = args.split()[0]
			if check in help_dic:
				"""if help [COMMAND]is given where [COMMAND] is a valid MyShell command"""
				print("\n")
				"""MyShellHelp class is called, which contains help command documents"""
				call = 'MyHelp.help_' + check + '()'
				eval(call)
				print("\n")
			else:
				print("Name " + check + " is not defined")
			
	def do_pause(self, args):
		""" Pauses operation until 'Enter' is pressed """
		press = input("Please press Enter to continue")
		while press != "":
			press = input("Please press Enter to continue")

	def do_quit(self, args):
		"""Quits the program"""
		print('Quitting')
		raise SystemExit

	def io_parse(self, args):
		"""this differentiate as to what redirection token (ie. '>', '>>' or '<') is given"""
		"""or if there was any given"""
		"""the correct mode is then returned"""
		if ('>' in args) and ('<' in args):
			return 'both'
		# elif re.search(r'[^>]+>>[^>]+', args):
		elif '>>' in args:
			return 'a'
		# elif re.search(r'[^>]+>[^>]+', args):
		elif '>' in args:
			return 'w'
		elif re.search(r'[^<]+<[^<]+', args):
		# elif '<' in args:
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

	def background(self, args, mode):
		"""background processes (&), after launching the process(es)"""
		"""cmdloop() is called so user can return to the command line prompt"""
		if not mode:
			p = Popen(args.split())
		else:
			"""checks if the users input contains a redirection token"""
			"""wait for the process to end before returning to command line prompt"""
			mode = self.io_parse(args)
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
				try:
					eval(io[mode][1]+'(args[:mode_index], file)')
				except:
					print("myshell: command not found: ", *args)

	def emptyline(self):
		return 
		
	def default(self, args):
		mode = self.io_parse(args)
		if '&' in args:
			"""if the user input contains '&' (amperstand), program is launched"""
			"""as a background process and return to MyShell command line prompt"""
			self.background(args, mode)
		else:
			"""checks if the users input contains a redirection token"""
			"""wait for the process to end before returning to command line prompt"""
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
					print(args[:mode_index])
					p = eval(io[mode][1]+'(args[:mode_index], file)')
					p.wait()
			
			else:
				"""the process will execute and run"""
				files = args.split()
				try:
					p = Popen(args.split())
					p.wait()
				except: 
					print("myshell: command  not found: "+args)

	
if __name__ == '__main__':
	prompt = MyShell()
	if len(sys.argv) > 1:
		prompt.batchfile()
	prompt.theprompt()
	print('Starting MyShell...')
	prompt.cmdloop()
