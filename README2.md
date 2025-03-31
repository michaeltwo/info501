# Program Assignment 2

This is to attack vulernable program called vuln_program

## Prerequisites

unzip the files into one folder, and compile the vuln_program

```bash
unzip PA2_wzheng.zip &&  gcc -fno-stack-protector -z execstack -fno-pie -no-pie -m32 -O0 -g vuln_program.c -o vuln_program

```

## Usage

```python
Part 1. bypass attack

# Start a shell, run below command to get the target address
$nm vuln_program |grep -i "target"

# Run below command, and paste the address from last step
$ python3 attack.py <address>

# Exploit
$./vuln_program < attack_string

Part 2. shell attack

#Run below command to generate a shell string
$ python3 attack.py shellcode

#Exploit
$setarch ‘uname-m‘-R ./vuln_program < shell_string
```

## Statements

Part one will generate a attack_string in the same folder, whicle part 2 will generate a shell_string in the same folder.  
Please make sure to update tests as appropriate.

## Optional

If there is something wrong, can perform gdb to explore it by using below useful command 

1.gdb ./vuln_program  
2.run < attack_string  
3.info reg  
4.x/40x $esp  
5.x/40xw $esp  
6.info frame  
7.break b
8.continue  
