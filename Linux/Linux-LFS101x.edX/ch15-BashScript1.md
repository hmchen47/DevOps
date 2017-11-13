Chapter 15 : Bash Shell Scripting I
=================================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Explain the features and capabilities of __bash shell scripting__.
+ Know the basic syntax of scripting statements.
+ Be familiar with various methods and constructs used.
+ Test for properties and existence of files and other objects.
+ Use conditional statements, such as __if-then-else__ blocks.
+ Perform arithmetic operations using scripting language.


# Section 1: Features and Capabilities
## Introduction to Scripting
Suppose you want to look up a filename, check if the associated file exists, and then respond accordingly, displaying a message confirming or not confirming the file's existence. If you only need to do it once, you can just type a sequence of commands at a terminal. However, if you need to do this multiple times, automation is the way to go. In order to automate sets of commands, you will need to learn how to write shell scripts, the most common of which are used with __bash__. The graphic illustrates several of the benefits of deploying scripts.

![image][img1]

Remember from our earlier discussion, a shell is a command line interpreter which provides the user interface for terminal windows. It can also be used to run scripts, even in non-interactive sessions without a terminal window, as if the commands were being directly typed in. For example, typing: `find . -name "*.c" -ls` at the command line accomplishes the same thing as executing a script file containing the lines:
```bash
#!/bin/bash
find . -name "*.c" -ls
```
The `#!/bin/bash` in the first line should be recognized by anyone who has developed any kind of script in UNIX environments. The first line of the script, that starts with `#!`, contains the full path of the command interpreter (in this case `/bin/bash`) that is to be used on the file. As we will see on the next screen, you have a few choices depending upon which scripting language you use.

## Command Shell Choices
The command interpreter is tasked with executing statements that follow it in the script. Commonly used interpreters include: `/usr/bin/perl, /bin/bash, /bin/csh, /usr/bin/python` and `/bin/sh`.

Typing a long sequence of commands at a terminal window can be complicated, time consuming, and error prone. By deploying shell scripts, using the command-line becomes an efficient and quick way to launch complex sequences of steps. The fact that shell scripts are saved in a file also makes it easy to use them to create new script variations and share standard procedures with several users.

Linux provides a wide choice of shells; exactly what is available on the system is listed in `/etc/shells`. Typical choices are:
```
/bin/sh
/bin/bash
/bin/tcsh
/bin/csh
/bin/ksh
```
Most Linux users use the default bash shell, but those with long UNIX backgrounds with other shells may want to override the default.

Click the link to download [UNIX Shell.pdf][shell] to read more about the UNIX Shell.

## bash Scripts
Let's write a simple __bash__ script that displays a one line message on the screen. Either type
```bash
$ cat > hello.sh
  #!/bin/bash
  echo "Hello Linux Foundation Student"
```
and press `ENTER` and `CTRL-D` to save the file, or just create `hello.sh` in your favorite text editor. Then, type `chmod +x hello.sh` to make the file executable by all users.

You can then run the script by  typing `./hello.sh` or by doing:
```
$ bash hello.sh
  Hello Linux Foundation Student
```
Note if you use the second form, you do not have to make the file executable.

# Interactive Example Using bash Scripts
Now, let's see how to create a more interactive example using a bash script. The user will be prompted to enter a value, which is then displayed on the screen. The value is stored in a temporary variable, name. We can reference the value of a shell variable by using a $ in front of the variable name, such as `$name`. To create this script, you need to create a file named `getname.sh` in your favorite editor with the following content: 
```bash
   #!/bin/bash
   # Interactive reading of a variable
   echo "ENTER YOUR NAME"
   read name
   # Display variable input
   echo The name given was :$name
```
Once again, make it executable by doing `chmod +x getname.sh`.

In the above example, when the user types `./getname.sh` and the script is executed, the user is prompted with the string  ENTER YOUR NAME. The user then needs to enter a value and press the Enter key. The value will then be printed out.

Additional note: The __hash-tag/pound-sign/number-sign (#)__ is used to start comments in the script and can be placed anywhere in the line (the rest of the line is considered a comment).

## Return Values
All shell scripts generate a return value upon finishing execution, the value can be set with the exit statement. Return values permit a process to monitor the __exit__ state of another process, often in a parent-child relationship. This helps to determine how this process terminated and take any appropriate steps necessary, contingent on success or failure.

![image][img2]

As a script executes, one can check for a specific value or condition and return success or failure as the result. By convention, success is returned as 0, and failure is returned as a non-zero value. An easy way to demonstrate success and failure completion is to execute ls on a file that exists and one that does not, the return value is stored in the environment variable represented by `$?`:
```bash
$ ls /etc/logrotate.conf
/etc/logrotate.conf

$ echo $?
0
```
In this example, the system is able to locate the file `/etc/logrotate.conf` and `ls` returns a value of 0 to indicate success. Applications often translate these return values into meaningful messages easily understood by the user.

## Knowledge Check
1. hich command is used to make some_script.sh executable?

        A. chmod a some_script.sh
        B. chmod +x some_script.sh 
        C. ./some_script.sh some_command
        D. cat ./somescript.sh

        Ans: B
        Explanation
        The command chmod +x some_script.sh is used to make the script executable.

2. Which of the following commands is used to manually pass a text file, script.sh, to the shell interpreter?

        A. bash script.sh 
        B. script.sh bash
        C. ./script.sh 
        D. .sh ./script

        Ans: A 
        Explanation
        The bash script.sh command is used to manually pass a text file, script.sh, to the shell interpreter.

## Lab 1: Exit Status Codes
Write a script which:

+ Does `ls` for a non-existent file, and then displays the resulting exit status.
+ Creates a file and does `ls` for it, and then once again displays the resulting exit status.

Click [the link][lab1] below to view a solution to the Lab exercise.


# Section 2: Syntax
## Basic Syntax and Special Characters
Scripts require you to follow a standard language syntax. Rules delineate how to define variables and how to construct and format allowed statements, etc. The table lists some special character usages within __bash__ scripts:

| Character | Description |
|------------|-------------|
| `#` | Used to add a comment, except when used as `\#`, or as `#!` when starting a script |
| `\` | Used at the end of a line to indicate continuation on to the next line |
| `;` | Used to interpret what follows as a new command to be executed next |
| `$` | Indicates what follows is an environment variable |
| `>` | Redirect output |
| `>>` | Append output |
| `<` | Redirect input |
| `|` | Used to pipe the result into the next command |

There are other special characters and character combinations and constructs that scripts understand, such as `(..)`, `{..}`, `[..]`, `&&`, `||`, `'`, `"`, `$((...))`, some of which we will discuss later.

## Splitting Long Commands Over Multiple Lines
Sometimes, commands are too long to either easily type on one line, or to grasp and understand (even though there is no real practical limit to the length of a command line.)

In this case, the __concatenation operator (\)__, the backslash character, is used to continue long commands over several lines.

For example, suppose you want to copy the file `/var/ftp/pub/userdata/custdata/read` from `server1.linux.com`, to the `/opt/oradba/master/abc` directory on `server3.linux.co.in`.  To perform this action, you can write the command using the \ operator, as in:
```bash
scp abc@server1.linux.com:/var/ftp/pub/userdata/custdata/read \
abc@server3.linux.co.in:/opt/oradba/master/abc/
```
The command is divided into multiple lines to make it look readable and easier to understand. The `\` operator at the end of each line causes the shell to combine (concatenate) multiple lines and executes them as one single command.

![image][img3]

## Putting Multiple Commands on a Single Line
Users sometimes need to combine several commands and statements and even conditionally execute them based on the behavior of operators used in between them. This method is called chaining of commands.

There are several different ways to do this, depending on what you want to do. The __; (semicolon)__ character is used to separate these commands and execute them sequentially, as if they had been typed on separate lines. Each ensuing command is executed whether or not the preceding ones succeed.

Thus, the three commands in the following example will all execute, even if the ones preceding them fail:
```bash
$ make ; make install ; make clean
```
However, you may want to abort subsequent commands when an earlier one fails. You can do this using the __&& (and)__ operator as in:
```bash
$ make && make install && make clean
```
If the first command fails, the second one will never be executed. A final refinement is to use the __|| (or)__ operator, as in:
```bash
$ cat file1 || cat file2 || cat file3
```
In this case, you proceed until something succeeds and then you stop executing any further steps.

## Output Redirection
Most operating systems accept input from the keyboard and display the output on the terminal. However, in shell scripting you can send the output to a file. The process of diverting the output to a file is called __output redirection__.

The `>` character is used to write output to a file. For example, the following command sends the output of free to  `/tmp/free.out`:
```bash
$ free > /tmp/free.out
```
To check the contents of `/tmp/free.out`, at the command prompt type  `cat /tmp/free.out`.

Two > characters `(>>`) will append output to a file if it exists, and act just like > if the file does not already exist.

## Input Redirection
Just as the output can be redirected to a file, the input of a command can be read from a file. The process of reading input from a file is called __input redirection__ and uses the `<` character.

The following three commands are entirely equivalent and involve input redirection, direction action on a file, and piping into a second process:
```bash
wc < /etc/passwd
49  105 2678

wc /etc/passwd
49  105 2678

cat /etc/passwd | wc>
49  105 2678
```

## Built-In Shell Commands
Shell scripts execute sequences of commands and other types of statements. These commands can be:

+ Compiled applications
+ Built-in __bash__ commands
+ Shell scripts or scripts from other interpreted languages, such as __perl__ and __Python__.

Compiled applications are binary executable files, generally residing on the filesystem in well-known directories such as `/usr/bin`. Shell scripts always have access to applications such as __rm, ls, df, vi__, and __gzip__, which are programs compiled from lower level programming languages such as __C__.

In addition, bash has many built-in commands, which can only be used to display the output within a terminal shell or shell script. Sometimes, these commands have the same name as executable programs on the system, such as echo which can lead to subtle problems. bash built-in commands include and __cd, pwd, echo, read, logout, printf, let__, and __ulimit__.  Thus, slightly different behavior can be expected from the built-in version of a command such as `echo` as compared to `/bin/echo`.

A complete list of bash built-in commands can be found in the __bash__ man page, or by simply typing __help__.

![image][img4]

## Script Parameters
Users often need to pass parameter values to a script, such as a filename, date, etc. Scripts will take different paths or arrive at different values according to the parameters (command arguments) that are passed to them. These values can be text or numbers as in:
```bash
$ ./script.sh /tmp
$ ./script.sh 100 200
```
Within a script, the parameter or an argument is represented with a `$` and a number or special character. The table lists some of these parameters.

| Parameter | Meaning |
|-----------|---------|
| `$0` | Script name |
| `$1` | First parameter |
| `$2, $3, etc.` | Second, third parameter, etc. |
| `$*` | All parameters |
| `$#` | Number of arguments |

![image][img5]

If you type in the script shown in the figure, make the script executable with `chmod +x param.sh`. Then run the script giving it several arguments, as shown. The script is processed as follows:

+ $0 prints the script name: param.sh
+ $1 prints the first parameter: one
+ $2 prints the second parameter: two
+ $3 prints the third parameter: three
+ $* prints all parameters: one two three four five

The final statement becomes: All done with param.sh

Please note that this is an illustrated video that shows the steps, there is no audio.

[video][vid1]

## Command Substitution
At times, you may need to substitute the result of a command as a portion of another command. It can be done in two ways:

+ By enclosing the inner command with backticks (`)
+ By enclosing the inner command in `$( )`

No matter the method, the innermost command will be executed in a newly launched shell environment, and the standard output of the shell will be inserted where the command substitution was done.

Virtually any command can be executed this way. Both of these methods enable command substitution; however, the `$( )` method allows command nesting. New scripts should always use of this more modern method. For example:
```bash
$ ls /lib/modules/$(uname -r)/
```
In the above example, the output of the command "`uname –r`" becomes the argument for the ls command.

## Environment Variables
Most scripts use variables containing a value, which can be used anywhere in the script. These variables can either be user or system-defined. Many applications use such environment variables (covered in the "User Environment" chapter) for supplying inputs, validation, and controlling behavior.

Some examples of standard environment variables are __HOME, PATH__, and __HOST__. When referenced, environment variables must be prefixed with the `$` symbol, as in `$HOME`. You can view and set the value of environment variables. For example, the following command displays the value stored in the `PATH` variable:
```bash
$ echo $PATH
```
However, no prefix is required when setting or modifying the variable value. For example, the following command sets the value of the MYCOLOR variable to blue:
```bash
$ MYCOLOR=blue
```
You can get a list of environment variables with the env, set, or printenv commands.

## Exporting Environment Variables
By default, the variables created within a script are available only to the subsequent steps of that script. Any child processes (sub-shells) do not have automatic access to the values of these variables. To make them available to child processes, they must be promoted to environment variables using the __export__ statement, as in:
```bash
export VAR=value
```
or
```bash
VAR=value ; export VAR
```
While child processes are allowed to modify the value of exported variables, the parent will not see any changes; exported variables are not shared, they are only copied and inherited.

Typing `export` with no arguments will give a list of all currently exported environment variables.

## Functions
A __function__ is a code block that implements a set of operations. Functions are useful for executing procedures multiple times perhaps with varying input variables. Functions are also often called __subroutines__. Using functions in scripts requires two steps:

1. Declaring a function
2. Calling a function.

The function declaration requires a name which is used to invoke it. The proper syntax is:
```bash
    function_name () {
       command...
    }
```
For example, the following function is named display:
```bash
    display () {
       echo "This is a sample function"
    }
```
The function can be as long as desired and have many statements. Once defined, the function can be called later as many times as necessary. In the full example shown in the figure, we are also showing an often-used refinement: how to pass an argument to the function. The first argument can be referred to as `$1`, the second as `$2`, etc.

![image][img6]

## Knowledge Check
1. Which character is used to represent the continuation of a command over several lines?

        A. /
        B. |
        C. \
        D. -

        Ans: C
        Explanation
        The \ character is used to logically join the next line.

2. What are the different types of commands that can be used in a bash shell script?

        A. Compiled applications
        B. Built-in bash commands
        C. Other scripts
        D. All of the above 

        Ans: D
        Explanation
        Compiled applications, built-in bash commands, and other scripts are the types of commands that can be used in a bash shell script.

3. If you want to substitute the result of an expression (say echo /tmp) to be the argument for cd, how will you represent them (select all that apply)?

        A. cd `echo /tmp` 
        B. cd (echo /tmp)
        C. cd echo /tmp
        D. cd $(echo /tmp) 

        Ans: A, D
        Explanation
        To substitute the result of an expression (e.g. echo /tmp) to be the argument for cd, use either cd `echo /tmp` or cd $(echo /tmp).

4. Which of the following supplies the correct syntax to declare the function named showpath?

        A.  showpath [
                echo $PATH
            ]
        B.  showpath {echo $PATH}
        C.  showpath () {
                echo $PATH
            } 
        D.  showpath (echo PATH)

        Ans: C
        Explanation
            showpath () {
                echo $PATH
            }
        is the correct syntax to declare showpath.

5. Which of the following parameters contains the name of the script being executed?

        A. $n
        B. var
        C. $0 
        D. $*

        Ans: C
        Explanation
        In a Bash Shell script, the command echo $0 will display the script name.

6. What commands are used to write the output of the free command to /tmp/free.out?

        A. free >> /tmp/free.out 
        B. free < /tmp/free.out
        C. free > /tmp/free.out 
        D. free <> /tmp/free.out

        Ans: A, C
        Explanation
        The free > /tmp/free.out and free >> /tmp/free.out commands are used to write the output of the free command to /tmp/free.out.

## Lab 2: Working with Files and Directories in a Script
Write a script which:

1. Prompts the user for a directory name and then creates it with mkdir.
2. Changes to the new directory and prints out where it is using pwd.
3. Using touch, creates several empty files and runs ls on them to verify they are 4. empty.
4. Puts some content in them using echo and redirection.
5. Displays their content using cat.
6. Says goodbye to the user and cleans up after itself.

Click [the link][lab2] to view a solution to the Lab exercise.

## Lab 3: Passing Arguments
Write a script that takes exactly one argument, and prints it back out to standard output. Make sure the script generates a usage message if it is run without giving an argument.

Click [the link][lab3] to view a solution to the Lab exercise.

## Lab 4: Environment Variables
Write a script which:

1. Asks the user for a number, which should be "1" or "2". Any other input should lead to an error report.
2. Sets an environmental variable to be "Yes" if it is "1", and "No" if it is "0".
3. Exports the environmental variable and displays it.

Click [the link][lab4] to view a solution to the Lab exercise.

## Lab 5: Working with Functions
Write a script which:

1. Asks the user for a number ( 1 , 2 or 3).
2. Calls a function with that number in its name. The function should display a message with its name included.

Click [the link][lab5] to view a solution to the Lab exercise.


# Section 3: Constructs
## The if Statement
Conditional decision making, using an __if__ statement, is a basic construct that any useful programming or scripting language must have.

When an if statement is used, the ensuing actions depend on the evaluation of specified conditions, such as:

+ Numerical or string comparisons
+ Return value of a command (0 for success)
+ File existence or permissions.

In compact form, the syntax of an if statement is:
```bash
if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi
```
A more general definition is:
```bash
if condition
then
       statements
else
       statements
fi
```
![image][img7]

__Objective__: To accept a filename from command prompt and display its existence
```bash
#!/bin/bash

file=$1

if [ -f $file ]
then
    echo "The $file exists"
else
    echo "The $file does not exist"
fi
```

[video][vid2]

The following __if__ statement checks for the `/etc/passwd` file, and if the file is found, it displays the message "`/etc/passwd exists.`":
```bash
if [ -f /etc/passwd ]
then
    echo "/etc/passwd exists."
fi
```
Notice the use of the __square brackets (`[]`)__ to delineate the test condition. There are many other kinds of tests you can perform, such as checking whether two numbers are equal to, greater than, or less than each other and make a decision accordingly; we will discuss these other tests.

In modern scripts, you may see doubled brackets as in `[[ -f /etc/passwd ]]`. This is not an error. It is never wrong to do so and it avoids some subtle problems, such as referring to an empty environment variable without surrounding it in double quotes; we will not talk about this here.

## Nested if Statements
__Objective__: To accept 2 numbers, 1 operator and display the calculate value based on the operator

```bash
#!/bin/bash
echo "Enter the first number"
read inp1

echo "Enter the second number"
read inp2

echo 
echo "1. Addition"
echo "2. Substraction"
echo "3. Multiplication"
echo -n "Please choose a word [1, 2, or 3]? "
read oper
echo " "

if [ $oper -eq 1 ]
then
    echo "Addition result " $(($inp1 + $inp2))
else
    if [ $oper -eq 2 ]
    then
        echo "Substraction result " $(($inp1 - $inp2))
    else
        if [ $oper -eq 3 ]
        then
            echo "Multiplication result " $(($inp1 * $inp2))
        fi
    fi
fi
```

[video][vid3]

## The elif Statement
__Objective__: To accept a number and display whether it is equal to or greater or less than 100

```bash
#!/bin/bash

echo -n "Enter a number: "
read count

if [ $count -eq 100 ]
then
    echo "Count is 100."
elif [ $count -gt 100 ]
    echo "Count is greater than 100."
else
    echo "Counter is less than 100."
fi
```

## Testing for Files
You can  use the if statement to test for __file attributes__, such as:

+ File or directory existence
+ Read or write permission
+ Executable permission.

For example, in the following example:
```bash
if [ -f /etc/passwd ] ; then
    ACTION
fi
```
the if statement checks if the file `/etc/passwd` is a regular file.
Note the very common practice of putting “`; then`” on the same line as the if statement.

bash provides a set of file conditionals, that can used with the if statement, including:

| Condition |  Meaning |
|-----------|----------|
| `-e file` |  Checks if the file exists. |
| `-d file` |  Checks if the file is a directory. |
| `-f file` |  Checks if the file is a regular file (i.e., not a symbolic link, device node, directory, etc.) |
| `-s file` |  Checks if the file is of non-zero size. |
| `-g file` |  Checks if the file has sgid set. |
| `-u file` |  Checks if the file has suid set. |
| `-r file` |  Checks if the file is readable. |
| `-w file` |  Checks if the file is writable. |
| `-x file` |  Checks if the file is executable. |

You can view the full list of file conditions using the command `man 1 test`.

## Boolean Expressions
__Boolean expressions__ evaluate to either __TRUE__ or __FALSE__, and results are obtained using the various Boolean operators listed in the table.

| Operator |  Operation |  Meaning |
|----------|------------|----------|
| `&&` |  AND |  The action will be performed only if both the conditions evaluate to true. |
| `||` |  OR |  The action will be performed if any one of the conditions evaluate to true. |
| `!` |  NOT |  The action will be performed only if the condition evaluates to false.  |

Note that if you have multiple conditions strung together with the `&&` operator, processing stops as soon as a condition evaluates to false. For example, if you have `A && B && C` and A is true but B is false, C will never be executed.

Likewise, if you are using the `||` operator, processing stops as soon as anything is true. For example, if you have `A || B || C` and A is false and B is true, you will also never execute C.

## Tests in Boolean Expressions
Boolean expressions return either __TRUE__ or __FALSE__. We can use such expressions when working with multiple data types, including strings or numbers, as well as with files. For example, to check if a file exists, use the following conditional test:
```bash
[ -e <filename> ]
```
Similarly, to check if the value of number1 is greater than the value of `number2`, use the following conditional test:
```bash
[ $number1 -gt $number2 ]
```
The operator `-gt` returns __TRUE__ if `number1` is greater than `number2`.

## String Tests
You can use the if statement to compare __strings__ using the operator `==` (two equal signs). The syntax is as follows:
```bash
if [ string1 == string2 ] ; then
   ACTION
fi
```
Note that using one `=` sign will also work, but some consider it deprecated usage. Let’s now consider an example of testing strings.

In the example illustrated here, the if statement is used to compare the input provided by the user and accordingly display the result.

![image][img8]

## Numerical Tests
You can use specially defined operators with the if statement to compare __numbers__. The various operators that are available are listed in the table:

| Operator |  Meaning |
|----------|----------|
| `-eq` |  Equal to |
| `-ne` |  Not equal to |
| `-gt` |  Greater than |
| `-lt` |  Less than |
| `-ge` |  Greater than or equal to |
| `-le` |  Less than or equal to |

The syntax for comparing numbers is as follows:
```bash
exp1 -op exp2
```

Let us now consider an example of comparing numbers using the various operators:

![image][img9]

__Objective__: To display whether numbers are zeros or equal or greater or smaller 
```bash
#!/bin/bash

echo "Please enter the first number "
read first
echo "Please enter teh second number "
read second
echo

if [ $first -eq 0 ] && [ $second -eq 0 ]
then
    echo "Num1 and Num2 are zero."
elif [ $first -eq $second ]
then
    echo "Both values ($first) are equal"
elif [ $first -gt $second ]
then
    echo "$first is greather than $second"
else
    echo "$first is less than $second"
fi
```

[video][vid4]

## Arithmetic Expressions
__Arithmetic expressions__ can be evaluated in the following three ways (spaces are important!):

+ Using the `expr` utility: expr is a standard but somewhat deprecated program. The syntax is as follows:
```bash
    expr 8 + 8
    echo $(expr 8 + 8)
```
+ Using the `$((...))` syntax: This is the built-in shell format. The syntax is as follows: (better usgae in modern age)
```bash
    echo $((x+1))
```
+ Using the built-in shell command `let`. The syntax is as follows:
```bash
    let x=( 1 + 2 ); echo $x
```
In modern shell scripts, the use of `expr` is better replaced with `var=$((...))`.

## Knowledge Check
1. Which are possible correct commands to add two numbers?

        A. expr 2 + 3 
        B. echo expr 2 + 3
        C. let x=( 1 + 2 ); echo $x 
        D. echo (expr(2 + 3))

        Ans: A, C
        expr 2 + 3 and let x=( 1 + 2 ); echo $x are possible correct commands to add two numbers.

2. Which of the following statements can be used to compare two strings?

        A. if [ $STR1 == $STR2 ] ; then echo match found ; fi 
        B. if [ $STR1 -eq $STR2 ] ; then echo match found ; fi
        C. if [[ $STR1 = $STR2 ]] ; then echo match found ; fi 
        D. All of the above

        Ans: 1, C
        Explanation
        The syntax for string matching in bash will accept either one or two equal signs. Conditional tests will also accept either single or double square brackets around the test.

3. Which of the following are correct conditional options that can be used to test for file attributes?

        A. -e 
        B. -z
        C. -d 
        D. -r 

        Ans: A, C, D
        –e, -d, and –r are file conditional options that can be used to test for file attributes.

4. The NOT operator is represented as _.

        Explanation
        The NOT operator is represented as ! .

5. In an if statement, the ____ operator is used with a name as argument to check if it exists and is a directory.

        A. -e
        B. -d 
        C. -f
        D. -s

        Explanation
        We must use the -d operator along with a directory name to check for its existence.

## Lab 6: Arithmetic and Functions
Write a script that will act as a simple calculator for add, subtract, multiply and divide.

+ Each operation should have its own function.
+ Any of the three methods for bash arithmetic, ( $((..)) , let , or expr ) may be used.
 + The user should give 3 arguments when executing the script:
    - The first should be one of the letters a, s, m, or d to specify which math operation.
    - The second and third arguments should be the numbers that are being operated on.

 The script should detect for bad or missing input values and display the results when done.

Click [the link][lab6] to view a solution to the Lab exercise.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ Scripts are a sequence of statements and commands stored in a file that can be executed by a shell. The most commonly used shell in Linux is bash.
+ Command substitution allows you to substitute the result of a command as a portion of another command.
+ Functions or routines are a group of commands that are used for execution.
+ Environmental variables are quantities either pre-assigned by the shell or defined and modified by the user.
+ To make environment variables visible to child processes, they need to be exported.
+ Scripts can behave differently based on the parameters (values) passed to them.
+ The process of writing the output to a file is called output redirection.
+ The process of reading input from a file is called input redirection.
+ The if statement is used to select an action based on a condition.
+ Arithmetic expressions consist of numbers and arithmetic operators, such as `+`, `-`, and `*`.




[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009100_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002300_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009400_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003700_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V008000_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/86597edd8ece86b852333387ed386d8b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch14_screen03.jpg
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4d9ca0cc7e62c429a040b0592dfe56dc/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch14_screen10.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/6a8aafbe31545a076aeecc9b89ed70ce/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Chapter14_Screen12.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/552b91648741f8ce6769d7859aec989f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_chapter14_screen_15.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a7d08ff7b0604bb8bd5d324cc162d17f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/scriptparams.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f504c2c7131128204c2482cfc4eb4926/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/bashfunubuntu.png
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c223a7b1887b6786aaf1d0948e330eae/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Chapter14_Screen29.jpg
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/cfe88d1d2fd45ad3e5330dfe36d1b388/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/ifstringubuntu.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ec0a1d119f27a66c769d359c79c2903c/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/mathtestubuntu.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-testls.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-testfile.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-basharg.html
[lab4]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-testenv.html
[lab5]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-testfun.html
[lab6]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-testmath.html

[shell]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5aea6c90c567d92ae40a4763861a3a44/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/Chap14_UNIXShell.pdf

