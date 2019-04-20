## NAME
MyShell

## SYNOPSIS

python3 MyShell.py [file]

## DESCRIPTION

MyShell is a simple command line shell written in Python3 enforced on Linux

## COMMANDS

### cd - 
Accepts argument (eg. cd _< directory >_). Changes the current directory to supplied directory argument/<directory> by the user.

### clr -
Clears the shell screen

### dir - 
Lists the contents of the current directory

### environ -
lists the environment strings

### echo -
Accepts arguments (eg. echo <comment>). Displays the <comment> supplied by the user.

### help - 
Accepts arugment (eg. help <command> / help(<command>). If argument is supplied the description of that command is displayed. Otherwise, it lists all the commands, one by one (by pressing Enter). 

### pause - 
Pause the operation of the shell, until 'ENTER' is entered by the user.

### quit -
Quits the shell

## BACKGROUND PROCESS

If you wish to be able to run a program and return to the command line prompt and be able to do more programs after launching that program. The addition of '&' (amperstand) at the end of each command line (eg. programname arg1 &) allows background execution of programs. MyShell allows you to do something else after running a program that may take awhile.

## Input/Output redirection
### > _file_
The greater-than sign followed by a file allows the output of the command be written in to the supplied file. If the file supplied is non-existant, it will create the file and write its output to the file, otherwise it will overwrite the contents of your supplied file with the output of the command. Output redirection redirects the standard output to the terminal, into the specified file.

### >> _file_
The double-greater-than sign followed by a file is similar to the single greater-than sign (> file). It appends the output of the command to the supplied file.

### < _file_
The less-than sign followed by a file allows the input of a command to be redirected from a file. Input redirection redirects the standard input (supplied by you in the terminal) to the specified file.

The command line <b>programname arg1 arg2 < inputfile > outputfile</b> is valid.
