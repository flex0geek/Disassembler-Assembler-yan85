# Simple Disassembler & Assembler for Yan85

This is a simple disassembler/assembler for yan85 that could be used in pwn.college challenges, the scripts are not perfect.

Yan85 has 3 bytes `op, arg1, arg2`

### Registers
------

| Register        | Descriptio |
| ------------- |:-------------:|
| a | General purpose register |
| b | General purpose register      |
| c | General purpose register      |
| d | General purpose register      |
| s | Stack Pointer      |
| i | Instruction pointer      |
| f | Flags register      |


### Instructions
------
| Register        | Descriptio |  Example |
| ------------- |:-------------:|:-------------:|
| imm | Moves a byte to a register | imm a 0x41|
| add | Adds two registers      | add a b|
| stk | Stack instruction deals with push and pop      | stk a 0 (pop)|
| stm | Set a memory value in a register     | stm *c a|
| ldm | Load value of memory into a register      | ldm c *a|
| cmp | Compares two registers      | cmp a b|
| jmp | Jump instruction      | jmp 0x10 a|
| sys | Execute syscalls      | sys 0x10 a|

- stk
  - to push `arg1=0`      `arg2=reg`
  - to pop  `arg2=reg`    `arg2=0`


### Syscalls
------

| Register        | Descriptio |
| ------------- |:-------------:|
| open | open syscall |
| read code | Write into memory space      |
| read memory |   will pass the offset of what part in memory to write to    |
| write | write bytes from the buffer pointed to by buf to the file associated with the open file descriptor, fildes |
| sleep | Delay for seconds       |
| exit | terminate the function currently running      |

---
For more details you can read this [Manual](https://drive.google.com/file/d/130mxJwJnfohfW0NYKD9z5xxu5LloPEZU/view)
