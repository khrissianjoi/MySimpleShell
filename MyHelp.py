"""Help Class"""


"""Help dictionary"""
"""Key : string is the command name"""
"""Value : tuple containing two strings. First (index 0) contains the normal output to the terminal, containing colours etc""" 
"""second (index 1) contains the output for redirection to a file"""

help_dic = {
	'cd' : ('print(RED + "CD <directory>" + RED + WHITE + " - cd command changes the current default directory to <directory>. If the <directory> argument is not present, report the current directory. If the directory does not exist an appropriate error should be reported." + WHITE)', 'CD - Accepts argument (eg. cd <directory>). Changes the current directory to supplied directory argument/<directory> by the user.'),
	'echo' : ('print(RED+ "ECHO <comment>" +RED + WHITE +" - echo command displays <comment> on the display followed by a new line"+WHITE)','ECHO - Accepts arguments (eg. echo <comment>). Displays the <comment> supplied by the user.'),
	'environ' : ('print(RED+"ENVIRON"+ RED + WHITE + " - environ command list all the environment strings" + WHITE)','ENVIRON - lists the environment strings'),
	'clr' : ('print(RED + "CLR" + RED + WHITE + " - clears the shell" + WHITE)', 'CLR - Clears the shell screen'),
	'quit': ('print(RED + "QUIT" + RED + WHITE + " - quit command raises the SystemExist and stops the execution of this script." + WHITE)','QUIT - Quits the shell'),
	'pause' : ('print(RED + "PAUSE" + RED + WHITE + " - Pause command suspends the operation of the shell until ENTER is pressed by the user." + WHITE)', 'PAUSE -  Pause the operation of the shell, until ENTER is entered by the user.'),
	'dir' : ('print(RED + "DIR <directory>" + RED + WHITE + " - dir command lists the contents of directory <directory>.")',  'DIR - Lists the contents of the current directory'),
	'help' : ('print(RED + "HELP" +RED + WHITE + " - Accepts arugment (eg. help <command> / help(<command>)). If argument is supplied the description of that command is displayed. Otherwise, it lists all the commands, one by one (by pressing Enter). + WHITE")','HELP - Accepts arugment (eg. help <command> / help(<command>)). If argument is supplied the description of that command is displayed. Otherwise, it lists all the commands, one by one (by pressing Enter).')
}

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
