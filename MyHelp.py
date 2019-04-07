help_dic = {
	'cd' : 'print(RED + "CD <directory>" + RED + WHITE + " - cd command changes the current default directory to <directory>. If the <directory> argument is not present, report the current directory. If the directory does not exist an appropriate error should be reported." + WHITE)',
	'echo' : 'print(RED+ "ECHO <comment>" +RED + WHITE +" - echo command displays <comment> on the display followed by a new line"+WHITE)',
	'environ' : 'print(RED+"ENVIRON"+ RED + WHITE + " - environ command list all the environment strings" + WHITE)',
	'clr' : 'print(RED + "CLR" + RED + WHITE + " - clears the shell" + WHITE)',
	'quit': 'print(RED + "QUIT" + RED + WHITE + " - quit command raises the SystemExist and stops the execution of this script." + WHITE)',
	'pause' : 'print(RED + "PAUSE" + RED + WHITE + " - pause command suspends the operation of the shell until Enter is pressed by the user." + WHITE)',
	'dir' : 'print(RED + "DIR <directory>" + RED + WHITE + " - dir command lists the contents of directory <directory>." + WHITE)'
}

WHITE = '\033[37;0m'
RED = '\033[31;1m'
CYAN = '\033[36;1m'
BOLD = '\033[37;1m'

class MyShellHelp():
	@staticmethod
	def help_cd():
		eval(help_dic['cd'])

	def help_echo():
		eval(help_dic['echo'])

	def help_environ():
		eval(help_dic['environ'])

	def help_clr():
		eval(help_dic['clr'])

	def help_quit():
		eval(help_dic['quit'])

	def help_pause():
		eval(help_dic['pause'])
		
	def help_dir():
		eval(help_dic['dir'])
