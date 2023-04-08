# Simple Disassembler & Assembler for Yan85

This is a simple disassemlber / assember for yan85 could be used in pwn.college challenges, the scripts are not perfect.

Yan85 have 3 bytes `op, arg1, arg2`

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
| stm | Mobes a byte value from src register to memory location     | stm *c a|
| ldm | Moves a byte value from the memory location to register      | ldm c *a|
| cmp | Compares two registers      | cmp a b|
| jmp | Jmp instruction      | jmp L a|
| sys | call syscalls      | sys 0x10 a|

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

