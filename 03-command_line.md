# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Don't! rm -rf / ; I'll delete everything

> > hostname ; gives you the name of the computer you're using

> > pushd DIR ; adds the specified directory to a stack and moves to that directory

> > popd ; goes to the directory on top of the stack 

> > touch FILENAME ; creates a new empty file with the specified name

> > less FILENAME ; display a paged version of the contents of a file (q to exit)

> > cat FILENAME ; display entire file's contents as terminal output

> > man COMMAND ; brings up the manual page for any command, if i happen to forget what they do or how to use them

> > grep REGEX FILENAME ; finds lines in FILENAME that match the REGEX pattern

> > COMMAND1 | COMMAND2 ; the pipe takes the output of COMMAND1 and uses it as input for COMMAND2

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls: list contents of the working directory

> > ls -a: flag to add "." and ".." to list of directories within working directory

> > ls -l: flag to list contents in a long format with attributes for each item. Including: access permissions, filesize and last modified date and time

> > ls -lh: converts sizes to a more human-readable format by giving the units (kilobyte, megabyte, gigabyte, etc). 

> > ls -lah: combination of the three preceeding commands. Lists the long form of the directory's contents with human readable sizes and includes "." and ".."

> > ls -t: flag to sort contents by last modified date (most recently modified files first)

> > ls -Glp: -G colorizes the output, -l provides the long form output, and -p appends a "/" to a filename if it is a directory

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -d: lists only directories

> > ls -g: the long format, but excluding the owner name

> > ls -R: displays subdirectories as well

> > ls -m: displays files as a comma separated list (could be useful to append to a csv file?)

> > ls -1: displays each entry on its own line

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes standard input as a list of arguments to a command

> > example: find /path -type f -print | xargs rm

> > This command takes the result of find (which is printing out all of the files within /path) and pipes it into xargs. Xargs takes the list of filenames and adds each as an argument to rm. Effectively this will remove every file within /path. This could also possibly work with the command "rm `find /path -type f`"; however, it may fail depending on the number of files found and the max command line length of the system.

 

