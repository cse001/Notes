

# How CPU Works

## Registers

- 8 - 32 global variables of fixed size

### Special Registers: 

- **Global Variables**
  - `rax` , `rbx`
- **Program Counters**
  - Which instruction is going to be executed next
  - Essentially Instruction Pointer and Program Counter are the same.
  - **Usually** : `PC `  **Intel x86 Architecture**: `eip` or `ip`
- **Limitation** 
  - Since the number of registers and the size of a register is fixed, we can't directly use them for heavy computations.

### A little flavor of assembly:

```assembly
mov eax,0x5 #Moves the value of 5 to eax
add eax,0x3 #Adds 3 to the eax, thus eax is now 8
mov ebx,0x8 #8 stored in ebx
sub eax,ebx #The substraction results in 0
```

### Memory

Memory is accessed either with loads or stores at addresses as if it were a big array or through PUSH and POP operation as if it were a stack.

Load and Store instructions are called `mov` in x86 Assembler.

Intuitively, we can move values from register to memory and memory to register.

#### Memory Hierarchy 

**Registers** > **Cache** (L1) > **Cache** (L2) > **Memory**

### Stack

The memory at the bottom

Stack Pointer 

`sp` or `esp` or `rsp`

Whenever we push or pop, the value is stored in `eax` and `sp` changes.

Stack grows downwards, i.e. if we `PUSH `-> The `sp` decreases and when we `POP` -> `sp` decreases.

### Control Flow

Is done via GOTOs -- jumps, branches, or calls

`jmp` or `jne` or `je`or `bne` or `be`or `call`

#### Jump (`jmp`)

unconditional goto

More like 

```assembly
jmp 5
mov eip 5 # Both of them are essentially the same thing
```

When we encounter a jump we will always follow it.

#### Jump If equal (`je`)

Is computed by calculating the difference. If the difference is 0 , the `zeroflag` is set , otherwise it remains 0.

#### CALL 

This will push the instruction pointer of the next instruction to the stack and when the function we jumped to finishes ,it will execute the `RET` in instruction, and `RET` will pop the current value at the top of the stack into the instruction pointer and keep going where the `CALL` left.

### Source : 

1) [LiveOverFlow ](<https://www.youtube.com/watch?v=6jSKldt7Eqs&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=5>)

2) [Sock Puppet](https://sockpuppet.org/issue-79-file-0xb-foxport-hht-hacking.txt.html)

### Exercise :

[Microcorruption](<https://microcorruption.com/login>)

### Quote

> Understanding concept is way more valuable than mastering the technique.