
from cmd import Cmd
from subprocess import Popen, PIPE, STDOUT
import os, sys, subprocess, shlex

class MyRedirection():
	@staticmethod
	def overwrite_file(args, file):
		""" > stdout file (output redirection)"""
		"""'w' mode, write mode"""
		with open(file, "w") as f:
			for i in range(1,len(args)):
				p = Popen([args[0], args[i]],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
				grep_stdout = p.communicate()[0]
				f.write(grep_stdout.decode())
			f.close()
		return p

	def append_file(args, file): 
		""">> redirection token, appends to the output file if file exists in the current directory,"""
		"""otherwise creates output file if file does not exist in the current directory."""
		"""'a' mode, append mode"""
		with open(file,"a") as f:
			for i in range(1,len(args)):
				p = Popen([args[0], args[i]],stdout=PIPE, stdin=PIPE, stderr=STDOUT)
				grep_stdout = p.communicate()[0]
				f.write(grep_stdout.decode())
		f.close()
		return p

	def stdin_file(args, file):
		""" < stdin file (input redirection)"""
		p = Popen([args[0], args[1]], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
		grep_stdout = p.communicate(input=Popen(['cat', file], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0])[0]
		print(grep_stdout.decode())
		if len(args) - 1 > 1:
			current = args[0:1] + args[2:]
			MyShell.default(" ".join(current))

		return p


	def stdin_stdout(args):
		"""> stdin file and < stdout file, reading input from a (< redirectioninput)"""
		"""file that is given, then outputing the file to the (> redirection) file"""
		args = shlex.split(args)
		program = args[0]

		index_out = args.index(">")+1
		index_in = args.index("<")+1
		out = args[index_out]
		in_ = args[index_in]
		"""'w' mode, write mode"""
		with open(out, 'w') as f:
			for i in range(1,min(index_out-1, index_in-1)):
				p = Popen([program, args[i]], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
				grep_stdout = p.communicate(input=Popen(['cat',in_], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0])[0]
				f.write(grep_stdout.decode())
		f.close()
		return p
