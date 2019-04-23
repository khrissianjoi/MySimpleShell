## NAME

  MyShell

## SYNOPSIS

  python3 MyShell.py [FILE]

## DESCRIPTION

  MyShell is a simple command line shell written in Python3 enforced on Linux.

## COMMANDS

### cd -
cd _[DIR]_

Changes the current directory to _[DIR]_. If _[DIR]_ is not provided, the current
path is displayed.

### clr -

Clears the terminal screen.

### dir - 
dir _[FILE]_

Lists the contents of the _[FILE]_ directory, if _[FILE]_ not given, the contents 
of the current directory is listed. 

### environ -

lists the environment strings.

### echo -
echo _[STRING]_
Displays the _[STRING]_ on the terminal screen.


### pause - 
Pause the operation of the shell, until 'ENTER' (interrupt signal) is entered 
by the user.

### quit -
Quits the shell.

## BACKGROUND PROCESS

  If you wish to be able to run a program and return to the command line prompt
  and be able to do more programs after launching that program. The addition of
  '&' (amperstand) at the end of each command line (eg. programname arg1 &)
  allows background execution of programs. MyShell allows you to do something 
  else after running a program that may take awhile.

## INPUT/OUTPUT REDIRECTION

### > _file_
The greater-than sign followed by a file allows the output of the command be 
written in to the supplied file.If the file supplied is non-existant it will 
create it and write its output, otherwise it will OVERWITE the contents of your
supplied file with the output of the command. Output redirection redirects the 
standard output to the terminal, into the specified file.


### >> _file_
The double-greater-than sign followed by a file is similar to the single
greater-than sign (> file). It APPENDS the output of the command to the supplied
file.


### < _file_
The less-than sign followed by a file allows the input of a command to be
redirected from a file. Input redirection redirects the standard input (supplied 
by you in the terminal) to the specified file.

