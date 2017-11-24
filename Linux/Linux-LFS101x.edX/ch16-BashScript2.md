Chapter 16: Bash Shell Scripting II
===================================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Manipulate strings to perform actions such as comparison and sorting.
+ Use Boolean expressions when working with multiple data types, including strings or numbers, as well as files.
+ Use case statements to handle command line options.
+ Use looping constructs to execute one or more lines of code repetitively.
+ Debug scripts using `set -x` and `set +x`.
+ Create temporary files and directories.
+ Create and use random numbers.


# Section 1: String Manipulation
## String Manipulation
Let’s go deeper and find out how to work with strings in scripts.

A __string variable__ contains a sequence of text characters. It can include letters, numbers, symbols and punctuation marks. Some examples: `abcde, 123, abcde 123, abcde-123, &acbde=%123`

String operators include those that do comparison, sorting, and finding the length. The following table demonstrates the use of some basic string operators:

| Operator |  Meaning |
|----------|----------|
| `[[ string1 > string2 ]]` |  Compares the sorting order of string1 and string2. |
| `[[ string1 == string2 ]]` |  Compares the characters in string1 with the characters in string2. |
| `myLen1=${#string1}` |  Saves the length of string1 in the variable myLen1. |

In the first example, we compare the first string with the second string and display an appropriate message using the if statement.

In the second example, we pass in a file name and see if that file exists in the current directory or not.

![image][img1]

## Parts of a String
At times, you may not need to compare or use an entire string. To extract the first n characters of a string we can specify: `${string:0:n}`. Here, 0 is the offset in the string (i.e., which character to begin from) where the extraction needs to start and n is the number of characters to be extracted.

To extract all characters in a string after a dot (`.`), use the following expression: `${string#*.}`

[image][img2]

## Testing for Strings
Please note that this is an illustrated video that shows the steps, there is no audio.

[video][vid1]

__Objective__: To display the status of ping operation
```bash
#!/bin/bash

echo "Enter IP address"
read ip
echo 

if [ ! -z $ip ]; then
    ping -c 3 $ip
    if [ $? -eq 0 ]; then
        echo
        echo "Machine is giving ping response"
    else
        echo
        echo "Machine is not giving ping response"
    fi
else
    echo
    echo "IP address is empty"
fi
```

## String Operations
Please note that this is an illustrated video that shows the steps, there is no audio.

[video][vid2]

__Objective__: To accept the string/data passed from keyboard, manipulate them and display on the terminal
```bash
#!/bin/bash

echo -n "Enter the first string: ";  read str1
echo -n "Enter the second string: "; read str2

echo $str1; echo $str2

myLen1=${#str1}
myLen2=${#str2}

echo Length of the first string is: $myLen1
echo Length of the first string is: $myLen2
```

## Knowledge Check
0 points possible (ungraded)
Select the correct syntax to find the length of the string abc.

    A. $#[abc]
    B. ${abc#}
    C. $#{abc}
    D. ${#abc} 

    Ans: D
    Explanation
    The ${#abc} command is used to get the length of the string, abc.

## Lab 1: String Tests and Operations
Write a script which reads two strings as arguments and then:

+ Tests to see if the first string is of zero length, and if the other is of non-zero length, telling the user of both results.
+ Determines the length of each string, and reports on which one is longer or if they are of equal length.
+ Compares the strings to see if they are the same, and reports on the result.

Click [the link][lab1] to view a solution to the Lab exercise.


# Section 2: The Case Statement
The __case__ statement is used in scenarios where the actual value of a variable can lead to different execution paths. case statements are often used to handle command-line options.

Below are some of the advantages of using the case statement:

+ It is easier to read and write.
+ It is a good alternative to nested, multi-level if-then-else-fi code blocks.
+ It enables you to compare a variable against several values at once.
+ It reduces the complexity of a program.

[image][img3]

## Structure of the case Statement
Here is the basic structure of the case statement:
```bash
case expression in
   pattern1) execute commands;;
   pattern2) execute commands;;
   pattern3) execute commands;;
   pattern4) execute commands;;
   * )       execute some default commands or nothing ;;
esac
```
![image][img4]

## Example of Use of the case Construct
Here is an example of the use of a case construct. 

![image][img5]

## Knowledge Check
Which of the following statements are true about the case statement?

    A. It enables you to match several values against one variable. 
    B. It ensures that the condition is true for all cases.
    C. It is a good alternative to nested multilevel if-then-else-fi statements. correct
    D. It indicates that any one of the conditions needs to be true, to perform the specified action.

    Ans: A
    Explanation
    The case statement enables you to match several values against one variable and is a good alternative to nested multilevel if-then-else-fi statements.

## Lab 2: Using the case Statement
Write a script that takes as an argument a month in numerical form (i.e., between 1 and 12), and translates this to the month name and displays the result on standard out (the terminal).

If no argument is given, or a bad number is given, the script should report the error and exit.

Click [the link][lab2] to view a solution to the Lab exercise.

# Section 3: Looping Constructs
## Looping Constructs
By using looping constructs, you can execute one or more lines of code repetitively, usually on a selection of values of data such as individual files. Usually, you do this until a conditional test returns either true or false, as is required.

Three type of loops are often used in most programming languages:

+ `for`
+ `while`
+ `until`

All these loops are easily used for repeating a set of statements until the exit condition is true.

![image][img6]

## The 'for' Loop
The __for__ loop operates on each element of a list of items. The syntax for the __for__ loop is:
```bash
for variable-name in list
do
    execute one iteration for each item in the list until the list is finished
done
```
In this case, `variable-name` and `list` are substituted by you as appropriate (see examples). As with other looping constructs, the statements that are repeated should be enclosed by do and done.

The screenshots here show an example of the for loop to print the sum of numbers 1 to 10.

![image][img7]

## The 'for' Statement in Action (along with case)
Please note that this is an illustrated video that shows the steps, there is no audio.

[video][vid2]

__Objective__: To display the type of files, based on extension
```bash
#!/bin/bash

for filename in $(ls)
do
    # take extension available in a filename
    ext=${filename##*\.}
    case "$ext" in
        c)      echo "$filename : C source file"
        ;;
        o)      echo "$filename : Object file"
        ;;
        sh)     echo "$filename : Shell file"
        ;;
        txt)    echo "$filename : Text file"
        ;;
        *)      echo "$filename : Unknow file type/not processed"
        ;;
    esac
done
```

## The 'while' Loop
The __while__ loop repeats a set of statements as long as the control command returns __true__. The syntax is:
```bash
while condition is true
do
    Commands for execution
    ----
done
```
The set of commands that need to be repeated should be enclosed between `do` and `done`. You can use any command or operator as the condition.  Often, it is enclosed within square brackets (`[]`).

The screenshots here show an example of the while loop that calculates the factorial of a number. Do you know why the computation of 21! gives a bad result?

![image][img8]

## The while Statement
[video][vid3]

__Objective__: To display the contents of an existing file.
```bash
#!/bin/bash

echo -e "Enter absolute path of the file name you want to read"
read file
echo

exec < $file    # redirect strin to a file
if [ $? -ne 0 ]; then
    echo
    echo "$file not existed"
    exit 1
fi

while read line
do
    echo $line
done
```

## The 'until' loop
The __until__ loop repeats a set of statements as long as the control command is __false__. Thus, it is essentially the opposite of the while loop. The syntax is:
```bash
until condition is false
do
    Commands for execution
    ----
done
```
Similar to the while loop, the set of commands that need to be repeated should be enclosed between `do` and `done`. You can use any command or operator as the condition.

The screenshot here shows example of the until loop that once again computes factorials; it is only slightly different than the test case for the while loop.

![image][img9]

[Video][vid4]

__objective__: To display the contents of a variable until it meets a condition using 'd' loop
```bash
#!/bin/bash

number=0

until [ $number -ge 10 ]; do
    echo "Number = $number"
    number=$(($number + 1))
done
```

## Knowledge Check
1. Which of the following looping constructs produces an output different than the others?

        A. j=7 ; while [ $j -lt 10 ] ; do echo $j ; j=$(($j+1)) ; done
        B. j=7 ; until [ $j -eq 10 ] ; do echo $j ; j=$(($j+1)) ; done
        C. for j in 7 8 9 ; do echo $j ; done
        D. j=7 ; for ( j < 10 ) ; do echo $j ; j=$j+1 ; done 

        Ans: D
        Explanation
        The first three sets of statements will produce as output: 
        7
        8
        9
        while the last one produces a syntax error.

2. Which of the following is not a valid looping construct?

        A. while
        B. until
        C. after 
        D. for

        Ans: C
        Explanation
        There is no looping construct associated with after.


# Section 4: Script Debugging
## Introduction to Script Debugging
While working with scripts and commands, you may run into errors. These may be due to an error in the script, such as an incorrect syntax, or other ingredients, such as a missing file or insufficient permission to do an operation. These errors may be reported with a specific error code, but often just yield incorrect or confusing output. So, how do you go about identifying and fixing an error?

__Debugging__ helps you troubleshoot and resolve such errors, and is one of the most important tasks a system administrator performs.

Before fixing an error (or bug), it is vital to know its source.

You can run a bash script in debug mode either by doing `bash –x ./script_file`,  or bracketing parts of the script with `set -x` and `set +x`. The debug mode helps identify the error because:

+ It traces and prefixes each command with the `+` character.
+ It displays each command before executing it.
+ It can debug only selected parts of a script (if desired) with:
```bash
    set -x    # turns on debugging
    ...
    set +x    # turns off debugging
```
The screenshot shown here demonstrates a script which runs in debug mode if run with any argument on the command line.

![image][imga]

## Redirecting Errors to File and Screen
In UNIX/Linux, all programs that run are given three open file streams when they are started as listed in the table: 

| File stream | Description | File Descriptor |
|-------------|-------------|-----------------|
| `stdin` | Standard Input, by default the keyboard/terminal for programs run from the command line | 0 |
| `stdout` | Standard output, by default the screen for programs run from the command line | 1 |
| `stderr` | Standard error, where output error messages are shown or saved | 2 |

Using redirection, we can save the stdout and stderr output streams to one file or two separate files for later analysis after a program or command is executed.

On the left screen is a buggy shell script. On the right screen the buggy script is executed and the errors are redirected to the file "error.txt". Using "cat" to display the contents of "error.txt" shows the errors of executing the buggy shell script (presumably for further debugging).

![image][imgb]

## Knowledge Check
1. Select the command that appends the error output to a temporary log file.

        A. $ ./script 2>> /tmp/scriptlogfile
        B. $ ./script 2> /tmp/scriptlogfile
        C. $ ./script 2<< /tmp/scriptlogfile
        D. $ ./script 2/>> /tmp/scriptlogfile

        Ans: A
        Explanation
        The ./script 2>> /tmp/scriptlogfile command appends errors to a log file.

2. If we want to debug the 15th line of a script, we must provide the _______ command on 14th line and the ___________command on 16th line of the script.

        A. ./script 2> >, set +x
        B. set -x, set +x 
        C. ./script 2>>, set +x
        D. set +x, ./script 2>>

        Ans: B
        Explanation
        The set -x and set +x arguments are used in the debugging shell scripts.


# Section 5: Some Additional Useful Techniques
## Creating Temporary Files and Directories
Consider a situation where you want to retrieve 100 records from a file with 10,000 records. You will need a place to store the extracted information, perhaps in a __temporary__ file, while you do further processing on it.

Temporary files (and directories) are meant to store data for a short time. Usually, one arranges it so that these files disappear when the program using them terminates. While you can also use __touch__ to create a temporary file, this may make it easy for hackers to gain access to your data.

The best practice is to create random and unpredictable filenames for temporary storage. One way to do this is with the mktemp utility, as in the following examples.

The `XXXXXXXX` is replaced by the `mktemp` utility with random characters to ensure the name of the temporary file cannot be easily predicted and is only known within your program.

| Command | Usage |
|---------|-------|
| `TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)` | To create a temporary file |
| `TEMPDIR=$(mktemp -d /tmp/tempdir.XXXXXXXX)` | To create a temporary directory |

## Example of Creating a Temporary File and Directory
Sloppiness in creation of temporary files can lead to real damage, either by accident or if there is a malicious actor. For example, if someone were to create a symbolic link from a known temporary file used by root to the `/etc/passwd` file, like this:
```bash
$ ln -s /etc/passwd /tmp/tempfile
```
There could be a big problem if a script run by root has a line in like this:
```bash
echo $VAR > /tmp/tempfile
```
The `password` file will be overwritten by the `temporary` file contents.

To prevent such a situation, make sure you randomize your temporary file names by replacing the above line with the following lines:
```bash
TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)
echo $VAR > $TEMP
```
Note the screen capture shows similarly named temporary files from different days, but with randomly generated characters in them.

![image][imgc]

## Discarding Output with /dev/null
Certain commands like __find__ will produce voluminous amounts of output, which can overwhelm the console. To avoid this, we can redirect the large output to a special file (a device node) called `/dev/null`. This pseudofile is also called the __bit bucket__ or __black hole__.

All data written to it is discarded and write operations never return a failure condition. Using the proper redirection operators, it can make the output disappear from commands that would normally generate output to stdout and/or stderr:
```bash
$ ls -lR /tmp > /dev/null
```
In the above command, the entire standard output stream is ignored, but any errors will still appear on the console. However, if one does
```bash
$ ls -lR /tmp >& /dev/null
```
both stdout and stderr will be dumped into `/dev/null`.

## Random Numbers and Data
It is often useful to generate __random numbers__ and other random data when performing tasks such as:

+ Performing security-related tasks
+ Reinitializing storage devices
+ Erasing and/or obscuring existing data
+ Generating meaningless data to be used for tests.

Such random numbers can be generated by using the `$RANDOM`  environment variable, which is derived from the Linux kernel’s built-in random number generator, or by the __OpenSSL__ library function, which uses the FIPS140 algorithm to generate random numbers for encryption

To read more about FIPS140, see http://en.wikipedia.org/wiki/FIPS_140-2

The example shows you how to easily use the environmental variable method to generate random numbers.

[image][imgd]

## How the Kernel Generates Random Numbers
Some servers have hardware random number generators that take as input different types of noise signals, such as thermal noise and photoelectric effect. A __transducer__ converts this noise into an electric signal, which is again converted into a digital number by an __A-D converter__. This number is considered random. However, most common computers do not contain such specialized hardware and, instead, rely on events created during booting to create the raw data needed.

Regardless of which of these two sources is used, the system maintains a so-called __entropy pool__ of these digital numbers/random bits. Random numbers are created from this entropy pool.

The Linux kernel offers the `/dev/random` and `/dev/urandom` device nodes, which draw on the entropy pool to provide random numbers which are drawn from the estimated number of bits of noise in the entropy pool.

`/dev/random` is used where very high quality randomness is required, such as one-time pad or key generation, but it is relatively slow to provide vaules.  `/dev/urandom` is faster and suitable (good enough) for most cryptographic purposes.

Furthermore, when the __entropy pool__ is empty, `/dev/random` is blocked and does not generate any number until additional environmental noise (network traffic, mouse movement, etc.) is gathered, whereas `/dev/urandom` reuses the internal pool to produce more pseudo-random bits.

## Knowledge Check
1. Which command is used to create a temporary directory?

        A. mktemp –d 
        B. mktemp –dir
        C. mkstemp -d
        D. mktempdir

        Ans: 
        Explanation
        The mktemp -d command is used to create a temporary directory.

2. The /dev/null file is also known as the _________ or black hole.

        Explanation
        The /dev/null file is also known as the bit bucket or black hole.

3. Which of the following Linux device nodes provide random numbers?

        A. /dev/rnd
        B. /dev/urandom 
        C. /dev/urnd
        D. /dev/random 

        Ans: B, D
        Explanation
The /dev/urandom and /dev/random device nodes provide random numbers.

## Lab 3: Using Random Numbers
Write a script which:

1. Takes a word as an argument.
2. Appends a random number to it.
3. Displays the answer.

Click [the link][lab3] to view a solution to the Lab exercise.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ You can manipulate strings to perform actions such as comparison, sorting, and finding length.
+ You can use Boolean expressions when working with multiple data types, including strings or numbers, as well as files.
+ The output of a Boolean expression is either true or false.
+ Operators used in Boolean expressions include the __&& (AND), ||(OR)__, and __! (NOT)__ operators.
+ We looked at the advantages of using the case statement in scenarios where the value of a variable can lead to different execution paths.
+ Script debugging methods help troubleshoot and resolve errors.
+ The standard and error outputs from a script or shell commands can easily be redirected into the same file or separate files to aid in debugging and saving results
+ Linux allows you to create temporary files and directories, which store data for a short duration, both saving space and increasing security.
+ Linux provides several different ways of generating random numbers, which are widely used.


[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009800_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V007100_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V006300_DTH.mp4
[vid3]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009700_DTH.mp4
[vid4]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V001400_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a0d340de66c679694dcf6fee02a1c583/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/stringdemos.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/55bddf886d7e365fae4c1842a4f0e58d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/stringmanip.png
[img3]: https://courses.edx.org/assets/courseware/v1/64b3740b3b0299bc1ad21e3999baf3bd/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Chapter15_Screen17.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/afb49c3ebe75ff82910621adb09a22c6/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch15_screen18.jpg
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d8b4e5bc4dec2df7351c100a88cf194a/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/testcase.png
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5501cea8fcca399926635852bc90f847/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch15_screen23.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/038af602fa06b5f5cb01872bd46f2423/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/testfor.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8c4861a61a1dc05f846c70efcc38023f/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/testwhile.png
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/3d9d6fd37f62074ecfb72259fd7aff2d/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/testuntil.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c79e74ef2465111f5d42ab90f5354816/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/shdebug.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/114415865abf3ae538df097fccdb0a8c/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch15_screen32.jpg
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/433c4d5c1a0172fe4a8f3e2cabfcf2d9/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/tmpfilecentos.png
[imgd]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/bea7e92c667890b6a5ae69110ca423b0/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/randomubuntu.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-teststrings.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-case.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-testrandom.html

