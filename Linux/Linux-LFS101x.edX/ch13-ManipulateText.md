Chapter 13 : Manipulating Text
==============================

# Introduction/ Learning Objectives
[video][vid0]

## Learning Objectives
By the end of this chapter, you should be able to:

+ Display and append to file contents using `cat` and `echo`. 
+ Edit and print file contents using `sed` and `awk`.
+ Search for patterns using `grep`.
+ Use multiple other utilities for file and text manipulation.


# Section 1: cat and echo
## Command Line Tools
Irrespective of the role you play with Linux (system administrator, developer, or user), you often need to browse through and parse text files, and/or extract data from them. These are __file manipulation__ operations. Thus, it is essential for the Linux user to become adept at performing certain operations on files.

Most of the time, such file manipulation is done at the __command line__, which allows users to perform tasks more efficiently than while using a GUI. Furthermore, the command line is more suitable for automating often executed tasks.

Indeed, experienced system administrators write customized scripts to accomplish such repetitive tasks, standardized for each particular environment. We will discuss such scripting later in much detail.

In this section, we will concentrate on command line file and text manipulation-related utilities.

![image][img1]

## cat
__cat__ is short for __concatenate__ and is one of the most frequently used Linux command line utilities. It is often used to read and print files, as well as for simply viewing file contents. To view a file, use the following command: 
```bash
$ cat <filename>
```
For example, `cat readme.txt` will display the contents of `readme.txt` on the terminal. Often, the main purpose of `cat`, however, is to combine (concatenate) multiple files together. You can perform the actions listed in the following table using cat:

| `Command` | Usage |
|-----------|-------|
| `cat file1 file2` | Concatenate multiple files and display the output; i.e., the entire content of the first file is followed by that of the second file. |
| `cat file1 file2 > newfile` | Combine multiple files and save the output into a new file. |
| `cat file >> existingfile` | Append a file to the end of an existing file. |
| `cat > file` | Any subsequent lines typed will go into the file, until `CTRL-D` is typed. |
| `cat >> file` | Any subsequent lines are appended to the file, until `CTRL-D` is typed. |

The __tac__ command (`cat` spelled backwards) prints the lines of a file in reverse order. (Each line remains the same, but the order of lines is inverted.) The syntax of tac is exactly the same as for cat, as in:
```bash
$ tac file
$ tac file1 file2 > newfile
```
## Using cat Interactively
`cat` can be used to read from standard input (such as the terminal window) if no files are specified. You can use the `>` operator to create and add lines into a new file, and the `>>` operator to append lines (or files) to an existing file.

To create a new file, at the command prompt type `cat > <filename>` and press the Enter key.

This command creates a new file and waits for the user to edit/enter the text. After you finish typing the required text, press `CTRL-D` at the beginning of the next line to save and exit the editing.

Another way to create a file at the terminal is `cat > <filename> << EOF`. A new file is created and you can type the required input. To exit, enter `EOF` at the beginning of a line.

Note that `EOF` is case sensitive. (One can also use another word, such as `STOP`.)

## Using cat
Click below to view a demonstration on how to use cat.

[video][vid1]

## Try-It-Yourself : Using cat
To practice, click the link provided below.

[Using cat][cat]

## echo
__echo__ simply displays (echoes) text. It is used simply, as in:
```
$ echo string
```
__echo__ can be used to display a string on standard output (i.e., the terminal) or to place in a new file (using the `>` operator) or append to an already existing file (using the `>>` operator).

The `–e` option, along with the following switches, is used to enable special character sequences, such as the __newline__ character or __horizontal tab__.

+ `\n`  represents newline
+ `\t`  represents horizontal tab

`echo` is particularly useful for viewing the values of environment variables (built-in shell variables). For example, `echo $USERNAME` will print the name of the user who has logged into the current terminal.

The following table lists echo commands and their usage:

| Command | Usage |
|---------|-------|
| `echo string > newfile` | The specified string is placed in a new file. |
| `echo string >> existingfile` | The specified string is appended to the end of an already existing file. |
| `echo $variable` | The contents of the specified environment variable are displayed. |`

## Try-It-Yourself : Using echo
To practice, click the link provided below.

[Using echo][echo]

## Knowledge Check
1. Which command is used to combine three files into a fourth file?

        A. cat file1 file2 file3 > file4 
        B. cp file1 file2 file3 > file4
        C. cat file1 > file2 > file3 > file4
        D. cat file1 > file2 > file3 | file4

        Ans: A
        Explanation
        The cat file1 file2 file3 > file4 command is used to combine three files into a fourth file.

2. Which command is used to display a line of text?

        Explanation
        The echo command is used to display a line of text.

# Section 2: Working with Large and Compressed Files
## Working with Large Files
System administrators need to work with configuration files, text files, documentation files, and log files. Some of these files may be large or become quite large as they accumulate data with time. These files will require both viewing and administrative updating. In this section, you will learn how to manage such large files.

For example, a banking system might maintain one simple large log file to record details of all of one day's ATM transactions. Due to a security attack or a malfunction, the administrator might be forced to check for some data by navigating within the file. In such cases, directly opening the file in an editor will cause issues, due to high memory utilization, as an editor will usually try to read the whole file into memory first. However, one can use `less` to view the contents of such a large file, scrolling up and down page by page, without the system having to place the entire file in memory before starting. This is much faster than using a text editor.

Viewing the file can be done by typing either of the two following commands:
```bash
$ less <filename>
$ cat <filename> | less
```
By default, manual (i.e., the man command) pages are sent through the `less` command.  (You may have encountered the older more utility which has the same basic function but fewer capabilities: i.e., less is `more`!)

![image][img2]

## head
__head__ reads the first few lines of each named file (10 by default) and displays it on standard output. You can give a different number of lines in an option.

For example, if you want to print the first 5 lines from `grub.cfg`, use the following command:
```bash
$ head –n 5 grub.cfg
```
(You can also just say `head -5 grub.cfg`.)

## tail
__tail__ prints the last few lines of each named file and displays it on standard output. By default, it displays the last 10 lines. You can give a different number of lines as an option. __tail__ is especially useful when you are troubleshooting any issue using log files, as you probably want to see the most recent lines of output.

For example, to display the last 15 lines of `atmtrans.txt`, use the following command:
```bash
$ tail -n 15 atmtrans.txt
```
(You can also just say `tail -15 atmtrans.txt`.) To continually monitor new output in a growing log file:
```
$ tail -f atmtrans.txt
```
This command will continuously display any new lines of output in `atmtrans.txt` as soon as they appear. Thus, it enables you to monitor any current activity that is being reported and recorded.

## Try-It-Yourself: Using head and tail
To practice, click the link provided below.

[Using head and tail][heil]

## Viewing Compressed Files
When working with compressed files, many standard commands cannot be used directly. For many commonly-used file and text manipulation programs, there is also a version especially designed to work directly with compressed files. These associated utilities have the letter __z__ prefixed to their name. For example, we have utility programs such as __zcat, zless, zdiff__, and __zgrep__.

Here is a table listing some __z__ family commands:

| Command | Description |
|---------|-------------|
| `$ zcat compressed-file.txt.gz` | To view a compressed file |
| `$ zless <filename>.gz` or `$ zmore <filename>.gz` | To page through a compressed file |
| `$ zgrep -i less test-file.txt.gz` | To search inside a compressed file |
| `$ zdiff filename1.txt.gz filename2.txt.gz` | To compare two compressed files |

Note that if you run `zless` on an uncompressed file, it will still work and ignore the decompression stage. There are also equivalent utility programs for other compression methods besides `gzip`; i.e, we have `bzcat` and `bzless` associated with `bzip2`, and `xzcat` and `xzless` associated with `xz`.

## Try-It-Yourself: Viewing Compressed Files
To practice, click the link provided below.

[Viewing Compressed Files][comp]

## Knowledge Check
Which of the following commands can be used to view the last 15 lines of a file?

    A. tail +15 some_file
    B. tail -15 some_file 
    C. tail -n15 some_file 
    D. tail=15 some_file

    Ans: B, C
    Explanation
    tail -15 or tail -n15 can be used to view the last 15 lines of a file.


# Section 3: sed and awk
## Introduction to sed and awk
It is very common to create and then repeatedly edit and/or extract contents from a file. Let’s learn how to use __sed__ and __awk__ to easily perform such operations.

Note that many Linux users and administrators will write scripts using more comprehensive language utilities, such as __Python__ and __perl__,rather than use __sed__ and __awk__ (and some other utilities we will discuss later.) Using such utilities is certainly fine in most circumstances; one should always feel free to use the tools one is experienced with. However, the utilities that are described here are much lighter; i.e., they use fewer system resources, and execute faster. There are situations (such as during booting the system) where a lot of time would be wasted using the more complicated tools, and the system may not even be able to run them. So, the simpler tools will always be needed.

## sed
__sed__ is a powerful text processing tool and is one of the oldest, earliest and most popular UNIX utilities. It is used to modify the contents of a file, usually placing the contents into a new file. Its name is an abbreviation for __stream editor__.

__sed__ can filter text, as well as perform substitutions in data streams, working like a churn-mill.

Data from an input source/file (or stream) is taken and moved to a working space. The entire list of operations/modifications is applied over the data in the working space and the final contents are moved to the standard output space (or stream).

![image][img3]

## sed Command Syntax
You can invoke sed using commands like those listed in the table below.

| Command | Usage |
|---------|-------|
| `sed -e command <filename>` | Specify editing commands at the command line, operate on file and put the output on standard out (e.g., the terminal) |
| `sed -f scriptfile <filename>` | Specify a scriptfile containing sed commands, operate on file and put output on standard out. |

## sed Basic Operations
Now that you know that you can perform multiple editing and filtering operations with `sed`, let’s explain some of them in more detail. The table explains some basic operations, where pattern is the current string and replace_string is the new string:

| Command | Usage |
|---------|-------|
| `sed s/pattern/replace_string/ file` | Substitute first string occurrence in a line |
| `sed s/pattern/replace_string/g file` | Substitute all string occurrences in a line |
| `sed 1,3s/pattern/replace_string/g file` | Substitute all string occurrences in a range of lines |
| `sed -i s/pattern/replace_string/g file` | Save changes for string substitution in the same file |

You must use the `-i` option with care, because the action is not reversible. It is always safer to use `sed` without the `–i` option and then replace the file yourself, as shown in the following example:
```bash
$ sed s/pattern/replace_string/g file1 > file2
```
The above command will replace all occurrences of `pattern` with `replace_string` in file1 and move the contents to `file2`. The contents of `file2` can be viewed with `cat file2`. If you approve you can then overwrite the original file with `mv file2 file1`.

Example: To convert 01/02/… to JAN/FEB/…
```bash
sed -e 's/01/JAN/' -e 's/02/FEB/' -e 's/03/MAR/' -e 's/04/APR/' -e 's/05/MAY/' \ 
    -e 's/06/JUN/' -e 's/07/JUL/' -e 's/08/AUG/' -e 's/09/SEP/' -e 's/10/OCT/' \
    -e 's/11/NOV/' -e 's/12/DEC/'
```
## Using sed
Click    below to view the demonstration on using sed.

[video][vid2]

## Try-It-Yourself : Using sed
To practice, click the link provided below.

[Using sed][sed]

## awk
__awk__ is used to extract and then print specific contents of a file and is often used to construct reports. It was created at Bell Labs in the 1970s and derived its name from the last names of its authors: __Alfred Aho, Peter Weinberger__, and __Brian Kernighan__.

__awk__ has the following features:

+ It is a powerful utility and interpreted programming language.
+ It is used to manipulate data files, retrieving, and processing text.
+ It works well with __fields__ (containing a single piece of data, essentially a column) and __records__ (a collection of fields, essentially a line in a file).

__awk__ is invoked as shown in the following:

| Command | Usage |
|---------|-------|
| `awk ‘command’ var=value file` | Specify a command directly at the command line |
| `awk -f scriptfile var=value file` | Specify a file that contains the script to be executed along with `f` |

As with `sed`, short `awk` commands can be specified directly at the command line, but a more complex script can be saved in a file that you can specify using the `-f` option.

![image][img4]

## awk Basic Operations
The table explains the basic tasks that can be performed using __awk__. The input file is read one line at a time, and, for each line, __awk__ matches the given pattern in the given order and performs the requested action. The `-F` option allows you to specify a particular __field separator__ character. For example, the `/etc/passwd` file uses "`:`" to separate the fields, so the `-F:` option is used with the `/etc/passwd` file.

The command/action in __awk__ needs to be surrounded with apostrophes (or single-quote (`'`)). __awk__ can be used as follows:

| Command | Usage |
|---------|-------|
| `awk '{ print $0 }' /etc/passwd` | Print entire file |
| `awk -F: '{ print $1 }' /etc/passwd` | Print first field (column) of every line, separated by a space |
| `awk -F: '{ print $1 $7 }' /etc/passwd` | Print first and seventh field of every line |

## Try-It-Yourself : Using awk
To practice, click the link provided below.

[Using awk][awk]

## Knowledge Check
1. Which of the following commands will replace all instances of the word "dog" with "pig" in the file named some_file and send the output to stdout?

        A. sed -e s/dog/pig/g some_file 
        B. sed -e s/dog/pig/ some_file
        C. sed -e s:dog:pig:g some_file 
        D. cat some_file | sed -e s/dog/pig/g 

        Ans: A, C, D
        Explanation
        The g flag is needed to tell sed to replace all instances of the word "dog" with "pig". Either / or : can be used as a delimiter between fields in the command.

2. Consider a data file /usr/data/employee that contains the information of 300 employees, in the following format:
(emp-name:age:date-of-birth)
Select the correct syntax of the awk command that prints the name and date-of-birth.

        A. $ awk -F: '{ print $1 ; $3 }' /usr/data/employee
        B. $ awk -F: '{ print $1 & $3 }' /usr/data/employee
        C. $ awk -F: '{ print $1 $3 }' /usr/data/employee 
        D. $ awk -F: '{ print $1 - $3 }' /usr/data/employee

        Ans: C
        Explanation
        $ awk -F: '{ print $1 $3 }' /usr/data/employee is used to select the employee name and date-of-birth.

## Lab 1: Using sed
Search for all instances of the user command interpreter (shell) equal to `/sbin/nologin` in `/etc/passwd` and replace them with `/bin/bash`.

Click [the link][lab1] to view a solution to the Lab exercise.

> Solution: 
> To get output on standard out (terminal screen):
> 
> student:/tmp> sed s/'\/sbin\/nologin'/'\/bin\/bash'/g /etc/passwd
> 
> or to direct to a file:
> 
> student:/tmp> sed s/'\/sbin\/nologin'/'\/bin\/bash'/g /etc/passwd > passwd_new
> 
> Note this is kind of painful and obscure because we are trying to use 
> the forward slash > ( / ) as both a string and a delimiter between 
> fields. One can do instead:
> 
> student:/tmp> sed s:'/sbin/nologin':'/bin/bash':g /etc/passwd
> 
> where we have used the colon ( : ) as the delimiter instead. (You are 
> free to choose  your delimiting character!) In fact when doing this 
> we do not even need the single quotes:
>
> student:/tmp> sed s:/sbin/nologin:/bin/bash:g /etc/passwd works
>

# Section 4: File Manipulation Utilities
## File Manipulation Utilities
In managing your files, you may need to perform many tasks, such as sorting data and copying data from one location to another. Linux provides several file manipulation utilities that you can use while working with text files. In this section, you will learn about the following file manipulation programs:

+ `sort`
+ `uniq`
+ `paste`
+ `join`
+ `split`

You will also learn about __regular expressions__ and __search patterns__.


## sort
__sort__ is used to rearrange the lines of a text file either in ascending or descending order, according to a sort key. You can also sort by particular fields of a file. The default sort key is the order of the ASCII characters (i.e., essentially alphabetically).

sort can be used as follows:

| Syntax | Usage |
|--------|-------|
| `sort <filename>` | Sort the lines in the specified file, according to the characters at the beginning of each line. |
| `cat file1 file2 | sort` | Combine the two files, then sort the lines and display the output on the terminal |
| `sort -r <filename>` | Sort the lines in reverse order |
| `sort -k 3 <filename>` | Sort the lines by the 3rd field on each line instead of the beginning |

When used with the `-u` option, sort checks for unique values after sorting the records (lines). It is equivalent to running `uniq` (which we shall discuss) on the output of sort.

## uniq
__uniq__ is used to remove duplicate lines in a text file and is useful for simplifying the text display.

__uniq__ requires that the duplicate entries must be consecutive. Thus, one often runs __sort__ first and then pipes the output into __uniq__; if sort is passed with the `-u` option, it can do all this in one step.

To remove duplicate entries from multiple files at once, use the following command: 
```bash
sort file1 file2 | uniq > file3
```
OR
```bash
sort -u file1 file2 > file3
```
To count the number of duplicate entries, use the following command: 
```bash
uniq -c filename
```
## Try-It-Yourself: Using sort and uniq
To practice, click the link provided below.

[Using sort and uniq][srun]

## paste
![image][img5]

Suppose you have a file that contains the full name of all employees and another file that lists their phone numbers and Employee IDs. You want to create a new file that contains all the data listed in three columns: name, employee ID, and phone number. How can you do this effectively without investing too much time?

__paste__ can be used to create a single file containing all three columns. The different columns are identified based on delimiters (spacing used to separate two fields). For example, delimiters can be a blank space, a tab, or an Enter. In the image provided, a single space is used as the delimiter in all files.

__paste__ accepts the following options:

+ `-d` delimiters, which specify a list of delimiters to be used instead of tabs for separating consecutive values on a single line. Each delimiter is used in turn; when the list has been exhausted, paste begins again at the first delimiter.
+ `-s`, which causes paste to append the data in series rather than in parallel; that is, in a horizontal rather than vertical fashion.

__paste__ can be used to combine fields (such as name or phone number) from different files, as well as combine lines from multiple files. For example, line one from file1 can be combined with line one of file2, line two from file1 can be combined with line two of file2, and so on.

To paste contents from two files one can do:
```
$ paste file1 file2
```
The syntax to use a different delimiter is as follows:
```
$ paste -d, file1 file2
```
Common delimiters are 'space', 'tab', '|', 'comma', etc.

## join
![image][img6]

Suppose you have two files with some similar columns. You have saved employees’ phone numbers in two files, one with their first name and the other with their last name. You want to combine the files without repeating the data of common columns. How do you achieve this?

The above task can be achieved using __join__, which is essentially an enhanced version of __paste__. It first checks whether the files share common fields, such as names or phone numbers, and then __joins__ the lines in two files based on a common field.

To combine two files on a common field, at the command prompt type `join file1 file2` and press the Enter key.

For example, the common field (i.e., it contains the same values) among the phonebook and  cities  files is the phone number, and the result of joining these two files is shown in the screen capture.

![image][img7]

## split
__split__ is used to break up (or split) a file into equal-sized segments for easier viewing and manipulation, and is generally used only on relatively large files. By default, __split__ breaks up a file into 1,000-line segments. The original file remains unchanged, and a set of new files with the same name plus an added prefix is created. By default, the `x` prefix is added. To split a file into segments, use the command split infile.

To __split__ a file into segments using a different prefix, use the command `split infile <Prefix>`.

![image][img8]

We will apply __split__ to an American-English dictionary file of over 99,000 lines:
```
$ wc -l american-english
99171 american-english
```
where we have used `wc`  (word count, soon to be discussed) to report on the number of lines in the file. Then, typing:
```
$ split american-english dictionary
```
will split the American-English file into 100 equal-sized segments named 'dictionary??. (The last one will of course be somewhat smaller.)

![image][img9]

## Regular Expressions and Search Patterns
__Regular expressions__ are text strings used for matching a specific __pattern__, or to search for a specific location, such as the start or end of a line or a word. Regular expressions can contain both normal characters or so-called __meta-characters__, such as `*` and `$`.

Many text editors and utilities such as __vi, sed, awk, find__ and __grep__ work extensively with regular expressions. Some of the popular computer languages that use regular expressions include __Perl, Python__ and __Ruby__. It can get rather complicated and there are whole books written about regular expressions; thus, we will do no more than skim the surface here.

These regular expressions are different from the wildcards (or "meta-characters") used in filename matching in command shells such as __bash__ (which were covered in the earlier Chapter on Command Line Operations). The table lists search patterns and their usage.

| Search Patterns | Usage |
|-----------------|-------|
| `.(dot)` | Match any single character |
| `a|z` | Match `a` or `z` |
| `$` | Match end of string |
| `*` | Match preceding item 0 or more times |

For example, consider the following sentence:

> the quick brown fox jumped over the lazy dog

Some of the patterns that can be applied to this sentence are as follows:

| Command | Usage |
|---------|-------|
| `a..` | matches `azy` |
| `b.|j.` | matches both `br` and `ju` |
| `..$` | matches `og` |
| `l.*` | matches `lazy dog` |
| `l.*y` | matches `lazy` |
| `the.*` | matches the whole sentence |

## Knowledge Check
1. Identify the command option that should be present in the paste command to combine two files with a specified delimiter.

        A. -d 
        B. -n
        C. -t
        D. -r

        Ans: A
        Explanation
        -d is the command option that should be present in the paste command to combine two files with a specified delimiter.

2. Which command will combine two files that share a common field?

        A. merge
        B. paste
        C. join 
        D. cat

        Ans: C
        Explanation
        The join command will combine two files that share a common field.

3. In search patterns, what is the syntax to match the end of the string?

        A. .
        B. ^
        C. $ 
        D. *

        Ans: C
        Explanation
        In search patterns, the $ character matches the end of the string.

## Lab 2: Parsing Files with awk (and sort and uniq)
Generate a column containing a unique list of all the shells used for users in `/etc/passwd`.

You may need to consult the manual page for `/etc/passwd` as in:
```
student:/tmp> man 5 passwd
```
Which field in `/etc/passwd` holds the account’s default shell (user command interpreter) ?

How do you make a list of unique entries (with no repeats.)

Click [the link][lab2] to view a solution to the Lab exercise.


# Section 5: grep and strings
## grep
__grep__ (Global Regular Expression Print) is extensively used as a primary text searching tool. It scans files for specified patterns and can be used with regular expressions, as well as simple strings, as shown in the table:

| Command | Usage |
|---------|-------|
| `grep [pattern] <filename>` | Search for a pattern in a file and print all matching lines |
| `grep -v [pattern] <filename>` | Print all lines that do not match the pattern |
| `grep [0-9] <filename>` | Print the lines that contain the numbers 0 through 9 |
| `grep -C 3 [pattern] <filename>` | Print context of lines (specified number of lines above and below the pattern) for matching the pattern. Here, the number of lines is specified as 3. |

## strings
__strings__ is used to extract all printable character strings found in the file or files given as arguments. It is useful in locating human-readable content embedded in binary files; for text files one can just use grep.

For example, to search for the string my_string in a spreadsheet:
```
$ strings book1.xls | grep my_string
```
The screenshot shows a  search of a number of programs to see which ones have GPL licenses of various versions.

![image][imga]

## Knowledge Check
1. Which commands can be used to print the lines that contain the numbers 0–5 in a file?

        A. grep [0,1,2,3,4,5] filename 
        B. grep [0-5] filename 
        C. grep [-e0 -e1 -e2 -e3 -e4 -e5] filename
        D. grep {0-5} filename

        Ans: A, B
        Explanation
        The grep [0-5] filename and grep [0,1,2,3,4,5] filename commands can be used to print the lines that contain the numbers 0–5 in a file.

2. Which of the following grep commands can be used to print out all of the lines that do not match the specified pattern?

        A. grep -C 3 [pattern] <filename>
        B. grep -v [pattern] <filename>correct
        C. grep [pattern] <filename>
        D. grep -w [pattern] <filename>

        Ans: B
        Explanation
        The command grep -v [pattern] <filename> can be used to print out all of the lines that do not match the specified pattern.

3. Which command is used to print strings of printable characters found in files?

        Explanation
        The strings command is used to print strings of printable characters found in files.

## Lab 3: Using grep
In the following we give some examples of things you can do with the grep command; your task is to experiment with these examples and extend them.

1. Search for your username in file /etc/passwd .
2. Find all entries in /etc/services that include the string ftp.
    + Restrict to those that use the tcp protocol.
    + Now restrict to those that do not use the tcp protocol, while printing out the line number
    + Get all strings that start with ts or end with st.

Click [the link][lab3] to view a solution to the Lab exercise.


# Section 6: Miscellaneous Text Utilities
In this section, you will learn about some additional text utilities that you can use for performing various actions on your Linux files, such as changing the case of letters or determining the count of words, lines, and characters in a file.

## tr
The __tr__ utility is used to __translate__ specified characters into other characters or to delete them. The general syntax is as follows:
```
$ tr [options] set1 [set2]
```
The items in the square brackets are optional. __tr__ requires at least one argument and accepts a maximum of two. The first, designated `set1` in the example, lists the characters in the text to be replaced or removed. The second, `set2`, lists the characters that are to be substituted for the characters listed in the first argument. Sometimes these sets need to be surrounded by apostrophes (or single-quotes (`'`)) in order to have the shell ignore that they mean something special to the shell. It is usually safe (and may be required) to use the single-quotes around each of the sets as you will see in the examples below.

For example, suppose you have a file named `city` containing several lines of text in mixed case. To translate all lower case characters to upper case, at the command prompt type `cat city | tr a-z A-Z` and press the Enter key.

| Command | Usage |
|---------|-------|
| `$ tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ` | Convert lower case to upper case |
| `$ tr '{}' '()' < inputfile > outputfile` | Translate braces into parenthesis |
| `$ echo "This is for testing" | tr [:space:] '\t'` | Translate white-space to tabs |
| `$ echo "This   is   for    testing" | tr -s [:space:]` |Squeeze repetition of characters using `-s` |
| `$ echo "the geek stuff" | tr -d 't'` | Delete specified characters using `-d` option |
| `$ echo "my username is 432234" | tr -cd [:digit:]` | Complement the sets using `-c` option |
| `$ tr -cd [:print:] < file.txt` | Remove all non-printable character from a file |
| `$ tr -s '\n' ' ' < file.txt` | Join all the lines in a file into a single line |

![image][imgb]

## Try-It-Yourself : Using tr
To practice, click the link provided below.

[Using tr][tr]

## tee
__tee__ takes the output from any command, and, while sending it to standard output, it also saves it to a file. In other words, it "tees" the output stream from the command: one stream is displayed on the standard output and the other is saved to a file.

For example, to list the contents of a directory on the screen and save the output to a file, at the command prompt type `ls -l | tee newfile` and press the Enter key.

Typing `cat newfile` will then display the output of `ls –l`.

![image][imgc]

## wc
__wc (word count)__ counts the number of lines, words, and characters in a file or list of files. Options are given in the table below.

By default, all three of these options are active.

For example, to print only the number of lines contained in a file, type `wc -l filename` and press the Enter key.

| Option | Description |
|--------|-------------|
| `–l` | Displays the number of lines. |
| `-c` | Displays the number of bytes. |
| `-w` | Displays the number of words. |

## Try-It-Yourself: Using wc
To practice, click the link provided below.

[Using wc][wc]

## cut
__cut__ is used for manipulating column-based files and is designed to extract specific columns. The default column separator is the tab character. A different delimiter can be given as a command option.

For example, to display the third column delimited by a blank space, at the command prompt type `ls -l | cut -d" " -f3` and press the Enter key.


## Knowledge Check
Which command is used to extract columns from a file to work on them later?

    A. tr
    B. tee
    C. wc
    D. cut 

    Ans: D
    Explanation
    The cut command is used to extract columns from a file to work on them later.

## Lab 4: Using tee
The tee utility is very useful for saving a copy of your output while you are watching it being generated.

Execute a command such as doing a directory listing of the /etc directory:
```
student:/tmp> ls -l /etc
```
while both saving the output in a file and displaying it at your terminal.

Click [the link][lab4] to view a solution to the Lab exercise.

## Lab 5: Using wc
Using wc (word count), find out how many lines, words, and characters there are in all the files in /var/log that have the .log extension.

Click [the link][lab5] to view a solution to the Lab exercise.


# Summary
You have completed this chapter. Let’s summarize the key concepts covered:

+ The command line often allows the users to perform tasks more efficiently than the GUI.
+ __cat__, short for concatenate, is used to read, print, and combine files.
+ __echo__ displays a line of text either on standard output or to place in a file.
+ __sed__ is a popular stream editor often used to filter and perform substitutions on files and text data streams.
+ __awk__ is an interpreted programming language, typically used as a data extraction and reporting tool.
+ __sort__ is used to sort text files and output streams in either ascending or descending order.
+ __uniq__ eliminates duplicate entries in a text file.
+ __paste__ combines fields from different files. It can also extract and combine lines from multiple sources.
+ __join__ combines lines from two files based on a common field. It works only if files share a common field.
+ __split__ breaks up a large file into equal-sized segments.
+ Regular expressions are text strings used for pattern matching. The pattern can be used to search for a specific location,such as the start or end of a line or a word.
+ __grep__ searches text files and data streams for patterns and can be used with regular expressions.
+ __tr__ translates characters, copies standard input to standard output, and handles special characters.
+ __tee__ saves a copy of standard output to a file while still displaying at the terminal.
+ __wc (word count)__ displays the number of lines, words, and characters in a file or group of files.
+ __cut__ extracts columns from a file.
+ __less__ views files a page at a time and allows scrolling in both directions.
+ __head__ displays the first few lines of a file or data stream on standard output. By default, it displays 10 lines.
+ __tail__ displays the last few lines of a file or data stream on standard output. By default, it displays 10 lines.
+ __strings__ extracts printable character strings from binary files.
+ The __z__ command family is used to read and work with compressed files.



[vid0]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V002500_DTH.mp4
[vid1]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V003800_DTH.mp4
[vid2]: https://d2f1egay8yehza.cloudfront.net/LINLFS10/LINLFS102014-V009000_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/bb5d324b58755524591ddba0757cdd98/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/debcmdline.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/18d15afaca72d0bd1ec205e4afc4d2bb/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_Ch12_Screen50.jpg
[img3]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/64bebc2555b3777d251a871e72e873d7/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch12_screen_13.jpg
[img4]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0969d1beca3f2106cc15d5fb77f74fc0/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/awkmint.png
[img5]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0c746d1cc41ea999719d5cdad330d97b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch12_screen27.jpg
[img6]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/da3d180e87ba8b70a3312fca74ecf815/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch12_screen30.jpg
[img7]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4ca7406b9c16747faf118ba6336e0cc5/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/join.png
[img8]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b842783bcec2180547358c235590e3f6/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/LFS01_ch012_screen31.jpg
[img9]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/cccb1abafbbcd04bad08b735f151cbb0/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/splitubuntu.png
[imga]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/5670ec4dbedb86c54df7f79000248207/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/strings.png
[imgb]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8d86fe669e95004b6b55386e5f15957b/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/trfedora.png
[imgc]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/bcd999b4dee2c8d4649d5e0355d1abe2/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/teerhel7.png

[lab1]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-sed.html
[lab2]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-awk.html
[lab3]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-grep.html
[lab4]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-tee.html
[lab5]: https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2017+type@asset+block/labsol-wc.html

[cat]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingcat/index.html
[echo]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingecho/index.html
[heil]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingheadtail/index.html
[compt]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usinggzip/index.html
[sed]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingsed/index.html
[awk]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingawk/index.html
[srun]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingsort/index.html
[tr]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingtr/index.html
[wc]: http://linuxfoundation.s3-website-us-east-1.amazonaws.com/TIY/usingwc/index.html
