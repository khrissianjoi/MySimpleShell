"""Help Class"""


"""Help dictionary"""
"""Key : string is the command name"""
"""Value : tuple containing two strings. First (index 0) contains the normal output to the terminal, containing colours etc""" 
"""second (index 1) contains the output for redirection to a file"""

help_dic = {
	'cd' : ('print(RED + "cd [DIR]" + RED + WHITE + " -Changes the current directory to [DIR]. If [DIR] is not provided, the current path is displayed." + WHITE)', 'cd [DIR] - Accepts argument (eg. cd <directory>). Changes the current directory to supplied directory argument/<directory> by the user.'),
	'echo' : ('print(RED+ "echo [STRING]" +RED + WHITE +" - Displays the [STRING] on the terminal screen."+WHITE)','echo [STRING]- Displays the [STRING] on the terminal screen.'),
	'environ' : ('print(RED+"ENVIRON"+ RED + WHITE + " - Lists the environment strings" + WHITE)','ENVIRON - Lists the environment strings'),
	'clr' : ('print(RED + "clr" + RED + WHITE + " - Clears the screen" + WHITE)', 'clr - Clears the screen'),
	'quit': ('print(RED + "QUIT" + RED + WHITE + " - Quits the shell." + WHITE)','quit - Quits the shell..'),
	'pause' : ('print(RED + "PAUSE" + RED + WHITE + " - Pause the operation of the shell, until ENTER (interrupt signal) is entered by the user." + WHITE)', 'pause - Pause the operation of the shell, until ENTER (interrupt signal) is entered by the user.'),
	'dir' : ('print(RED + "dir [FILE]" + RED + WHITE + " - Lists the contents of the [FILE] directory, if [FILE] not given, the contents of the current directory is listed")',  'dir [FILE] - Lists the contents of the [FILE] directory, if [FILE] not given, the contents of the current directory is listed')
}
WHITE = '\033[37;0m'
RED = '\033[31;1m'
CYAN = '\033[36;1m'
BOLD = '\033[37;1m'
class MyHelp():
	"""Help command, called by MyShell class when user calls help <command> or help(<command>), the class then uses the"""
	"""help_dic dictionary for an output for the appropriate help command description needed""" 
	"""index 0 of the value tuple is used"""
	@staticmethod
	def help_cd():
		command = help_dic['cd'][0]
		eval(command)

	def help_echo():
		command = help_dic['echo'][0]
		eval(command)

	def help_environ():
		command = help_dic['environ'][0]
		eval(command)

	def help_clr():
		command = help_dic['clr'][0]
		eval(command)

	def help_quit():
		command = help_dic['quit'][0]
		eval(command)

	def help_pause():
		command =help_dic['pause'][0]
		eval(command)
		
	def help_dir():
		command = help_dic['dir'][0]
		eval(command)

	def help_help():
		command = help_dic['help'][0]
		eval(command)
