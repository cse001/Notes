# Reversing and cracking the first program

This piece of notes talk about the key commands that are used while cracking an application.

```perl
(gdb) disassemble main 
# This shows all the assembly instructions from the main function
```

By default the output is in the AT&T syntax

To set it up more appropriately, use the command 

​	`set disassembly-flavor intel`

- First get a high level view of it. 

- Doesn't make sense to read all the instructions one by one.

- The main function will call a lot of functions, so at the higher level, all we need is ***mental picture of the rough control flow***

#### Adding Break Points

`break *main`

#### Running the program until the break point

`run`

#### View the values stored in different registers

`info registers`

​	RIP - Instruction Pointer , points to the first address in main

#### Execute one instruction , step - by - step

`si` - Step one instruction

`ni`- Next instruction

**Note** : Use `ni` instead of `si` because `si` steps into the functions and `ni` doesn't.

#### Modifying the values of registers

`set $eax = 0` 

To change the value of the register `eax`

#### Making Control Flow Graphs

Making the control graph is very important.

There are applications that do that for us.

- Hopper App
- IDA Pro
- Radare 2

#### Suggested Practice 

[Crack Me Challenges](http://crackme.de)

Since the crackme.des in not working anymore: 

Here are a few alternatives : 

1) [Github Repository](https://github.com/crackmes/crackmes)

2) [Root Me](https://www.root-me.org/en/Challenges/Cracking/ )

If you have any other sources, do add to this list and create a pull request

### Source

[Live Overflow](<https://www.youtube.com/watch?v=VroEiMOJPm8&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=6>)



> It is impossible to make an program uncrackable