import sys, os

def usage():
    print(sys.argv[0] + " <file>")
OP_ORDER = [0,1,2]

operations = {
    "imm":0x10,
    "add":0x1,
    "stk":0x2,
    "stm":0x8,
    "ldm":0x4,
    "cmp":0x80,
    "jmp":0x40,
    "sys":0x20}
registers = {
    "a":0x10,
    "b":0x20,
    "c":0x1,
    "d":0x2,
    "s":0x4,
    "i":0x8,
    "f":0x40
    }
syscalls = {
    "open":0x10,
    "read_code":0x20,
    "read_mem":0x1,
    "write":0x4,
    "sleep":0x8,
    "exit":0x2
    }
jmp_ops = {
    "L":0x10,
    "G":0x01,
    "E":0x08,
    "N":0x04,
    "Z":0x02
}
try:
    opcode = open(sys.argv[1], "rb").read()
except IndexError:
    usage()
    exit()

def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))

def regs(val):
    for k, v in registers.items():
        if v == val:
            return k
        
def imm(arg1, arg):
    op = 'imm'
    val = arg
    arg1 = regs(arg1)
    return op, arg1, hex(val)

def add(arg1, arg2):
    op = 'add'
    arg1 = regs(arg1)
    arg2 = regs(arg2)
    return op, arg1, arg2

def stk(arg1, arg2):
    op = 'stk'
    for k, v in registers.items():
        if arg2 != 0: # stk 0 A -> push a
            if arg2 == v:
                arg2 = k
                pp = 'push'
                return op, arg1, arg2
        else: # stk A 0 -> pop a
            if arg1 == v:
                arg1 = k
                pp = 'pop'
                return op, arg1, arg2

def stm(arg1, arg2):
    op = 'stm'
    arg1 = regs(arg1)
    arg2 = regs(arg2)
    return op, arg1, arg2

def ldm(arg1, arg2):
    op = 'ldm'
    arg1 = regs(arg1)
    arg2 = regs(arg2)
    return op, arg1, arg2

def cmp(arg1, arg2):
    op = 'cmp'
    arg1 = regs(arg1)
    arg2 = regs(arg2)
    return op, arg1, arg2

def jmp(arg1, arg2):
    for k, v in jmp_ops.items():
        if v == arg1:
            arg1 = k

    op = 'jmp'
    arg2 = regs(arg2)
    return op, arg1, arg2
        
def syscall(arg1, arg2):
    for k, v in syscalls.items():
        if v == arg1:
            arg1 = hex(v)

    op = 'sys'
    arg2 = regs(arg2)
    return op, arg1, arg2


def disass(opcode):
    if len(opcode) % 3 != 0 :
        print("Opcode is not correct, maybe there is a wrong bytes")
        exit()
    else:
        op, arg1, arg2 = opcode
        for k, v in operations.items():
            if op == v: # then we know the operation
                if k == 'imm':
                    op, reg, val = imm(arg1, arg2)
                    return op, reg, val
                elif k == 'add':
                    op, reg, val = add(arg1, arg2)
                    return op, reg, val
                
                elif k == 'stk':
                    op, reg, val = stk(arg1, arg2)
                    return op, reg, val
                
                elif k == 'stm':
                    op, reg, val = stm(arg1, arg2)
                    return op, reg, val
                
                elif k == 'ldm':
                    op, reg, val = ldm(arg1, arg2)
                    return op, reg, val
                
                elif k == 'cmp':
                    op, reg, val = cmp(arg1, arg2)
                    return op, reg, val
                
                elif k == 'jmp':
                    op, reg, val = jmp(arg1, arg2)
                    return op, reg, val
                
                elif k == 'sys':
                    op, reg, val = syscall(arg1, arg2)
                    return op, reg, val

def main():
    instructions = chunkstring(opcode, 3)
    print("[+] Length of Instructions: "+str(len(instructions)))
    for i in range(len(instructions)):
        op, arg1, arg2 = disass(instructions[i])

        if op == 'stk':
            if arg1 == 0:
                print(op.upper(), arg1, arg2, '\t\t\t# push') # STK 0 A --> Push A
            elif arg2 == 0:
                print(op.upper(), arg1, arg2, '\t\t\t# pop')  # STK A 0 --> Pop  A

        elif op == "stm":
            print(op.upper(), "*"+arg1, arg2)

        elif op == "ldm":
            print(op.upper(), arg1, "*"+arg2)

        else:
            print(op.upper(), arg1, arg2)

main()