# Simple Tools 

#### The File Command

```bash
--> file license_1
license_1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=72922f8327afa289f1680c03499675863479489c, not stripped

```

#### Hexdump

```bash
-> hexdump -C license_1
00000000  7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  02 00 3e 00 01 00 00 00  d0 04 40 00 00 00 00 00  |..>.......@.....|
00000020  40 00 00 00 00 00 00 00  a8 11 00 00 00 00 00 00  |@...............|
00000030  00 00 00 00 40 00 38 00  09 00 40 00 1e 00 1b 00  |....@.8...@.....|
00000040  06 00 00 00 05 00 00 00  40 00 00 00 00 00 00 00  |........@.......|
00000050  40 00 40 00 00 00 00 00  40 00 40 00 00 00 00 00  |@.@.....@.@.....|
00000060  f8 01 00 00 00 00 00 00  f8 01 00 00 00 00 00 00  |................|
00000070  08 00 00 00 00 00 00 00  03 00 00 00 04 00 00 00  |................|
00000080  38 02 00 00 00 00 00 00  38 02 40 00 00 00 00 00  |8.......8.@.....|
00000090  38 02 40 00 00 00 00 00  1c 00 00 00 00 00 00 00  |8.@.............|
000000a0  1c 00 00 00 00 00 00 00  01 00 00 00 00 00 00 00  |................|
000000b0  01 00 00 00 05 00 00 00  00 00 00 00 00 00 00 00  |................|
000000c0  00 00 40 00 00 00 00 00  00 00 40 00 00 00 00 00  |..@.......@.....|
000000d0  3c 08 00 00 00 00 00 00  3c 08 00 00 00 00 00 00  |<.......<.......|
000000e0  00 00 20 00 00 00 00 00  01 00 00 00 06 00 00 00  |.. .............|
000000f0  10 0e 00 00 00 00 00 00  10 0e 60 00 00 00 00 00  |..........`.....|
00000100  10 0e 60 00 00 00 00 00  40 02 00 00 00 00 00 00  |..`.....@.......|
00000110  48 02 00 00 00 00 00 00  00 00 20 00 00 00 00 00  |H......... .....|
00000120  02 00 00 00 06 00 00 00  28 0e 00 00 00 00 00 00  |........(.......|
00000130  28 0e 60 00 00 00 00 00  28 0e 60 00 00 00 00 00  |(.`.....(.`.....|
00000140  d0 01 00 00 00 00 00 00  d0 01 00 00 00 00 00 00  |................|
00000150  08 00 00 00 00 00 00 00  04 00 00 00 04 00 00 00  |................|
...
(A few more lines :P )

```

#### Strings

The strings command outputs all the readable strings.

```bash
-> strings license_1
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
printf
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.2.5
UH-P
UH-P
[]A\A]A^A_
Checking License: %s
AAAA-Z10N-42-OK
Access Granted!
WRONG!
Usage: <key>
(Plus some more)
```

#### Object Dump

```bash
-> objdump -d license_1

license_1:     file format elf64-x86-64

Disassembly of section .init:

0000000000400450 <_init>:
  400450:	48 83 ec 08          	sub    $0x8,%rsp
  400454:	48 8b 05 9d 0b 20 00 	mov    0x200b9d(%rip),%rax        # 600ff8 <__gmon_start__>
  40045b:	48 85 c0             	test   %rax,%rax
  40045e:	74 05                	je     400465 <_init+0x15>
  400460:	e8 5b 00 00 00       	callq  4004c0 <__gmon_start__@plt>
  400465:	48 83 c4 08          	add    $0x8,%rsp
  400469:	c3                   	retq   

Disassembly of section .plt:

0000000000400470 <.plt>:
  400470:	ff 35 92 0b 20 00    	pushq  0x200b92(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400476:	ff 25 94 0b 20 00    	jmpq   *0x200b94(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40047c:	0f 1f 40 00          	nopl   0x0(%rax)
(A lot of more lines)
```

```bash
-> objdump -c lincense_1


```

Interesting Features

- elf format
- architecture
- the stack is executable or not
- sections
  - We can see here where certain data will later end up in memory
  - Interesting section is the text section
  - and the ro section - this is the read only section

### Strace

It can trace system calls and signals

### Ltrace

It traces the library functions.

### Source

[Live Overflow](<https://www.youtube.com/watch?v=3NTXFUxcKPc&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=7>)

### Quotes

> No tools is better than the other, all tools have different features and representations of the information

> Some say that radare is the best, but no one masters radare