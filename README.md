# passGen
Python script to generagte probablies passwords depends on given words.

# Installation
```bash
git clone https://github.com/mustaphazdali/passGen.git
cd passGen
chmod +x passGen.py
./passGen.py
```

> you may need to install some libraries 

# Usage
``` bash
┌──(mustaphazdali㉿kali)-[/opt]
└─$ ./passgen
usage: passgen [-h] [-l LENGTH] -r REPEAT -w WORDS [-o OUTPUT] [-v] [-q]
passgen: error: the following arguments are required: -r/--repeat, -w/--words
```

> To get more informations

```
┌──(muss㉿muss)-[/opt]
└─$ ./passgen -h
usage: passgen [-h] [-l LENGTH] -r REPEAT -w WORDS [-o OUTPUT] [-v] [-q]

This script generate password from given probs

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        lenght of password
  -r REPEAT, --repeat REPEAT
                        repeated words from 1 to N
  -w WORDS, --words WORDS
                        words space separated "foo bar \s test". the \s for space
  -o OUTPUT, --output OUTPUT
                        output path file name
  -v, --verbose         print the password to stdout
  -q, --quit            print only psswords
```
  
# Test
## With some information
![img][ex01]

## Add -v to show generated password
![img][ex02]

## To print only password you can add -q and -v
![img][ex04]

## Preview
![img][ex03]

  
[ex01]: imgs/ex01.png
[ex02]: imgs/ex02.png
[ex03]: imgs/ex03.gif
[ex04]: imgs/ex04.png
