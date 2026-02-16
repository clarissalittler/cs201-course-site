# Practice Problems for Modules 3 and 4

These practice problems cover the lessons that do not already have embedded LTI quizzes.

---

## Module 3, Lesson 1: The Build Process and Your First Assembly Program

**Q1 (Multiple Choice).** Which pair of commands assembles `hello.s` into an object file and then links it into an executable?

- A) `gcc -o hello hello.s` then `./hello`
- B) `as -o hello.o hello.s` then `ld -o hello hello.o`
- C) `ld -o hello.o hello.s` then `as -o hello hello.o`
- D) `as hello.s` then `ld hello.o`

**Answer:** B

---

**Q2 (Short Answer).** When you build a program with `as` and `ld` (no C library), the entry point label must be `_start`, not `main`. Why can't you use `main` as the entry point in this workflow?

**Answer:** `main` is called by the C runtime startup code (`_start` in `crt0`), which is only linked in when you use `gcc`. When linking directly with `ld`, the linker looks for `_start` as the default entry point. There is no C runtime to call `main`.

---

**Q3 (Multiple Choice).** Consider this complete program:

```asm
        .text
        .global _start
_start:
        mov $42, %rdi
        mov $60, %rax
        syscall
```

What does `echo $?` print after running this program?

- A) 60
- B) 0
- C) 42
- D) An error, because syscall is not a valid instruction

**Answer:** C

---

**Q4 (Short Answer).** In the `exit` syscall, the syscall number goes in `%rax` and the exit code goes in `%rdi`. What is the syscall number for `exit`, and what range of values can `echo $?` report?

**Answer:** The syscall number for `exit` is 60. `echo $?` reports the low 8 bits of the exit code, so values 0-255.

---

## Module 3, Lesson 2: Registers and the CPU Environment

**Q1 (Multiple Choice).** Which of the following correctly names the 32-bit, 16-bit, and 8-bit sub-registers of `%rcx`?

- A) `%ecx`, `%cx`, `%cl`
- B) `%rcx32`, `%rcx16`, `%rcx8`
- C) `%cx`, `%cl`, `%ch`
- D) `%lcx`, `%cx`, `%cl`

**Answer:** A

---

**Q2 (Multiple Choice).** In AT&T syntax, what does the instruction `movl %eax, %ebx` do?

- A) Moves the contents of `%ebx` into `%eax`
- B) Moves the contents of `%eax` into `%ebx`
- C) Exchanges the values of `%eax` and `%ebx`
- D) Moves the 64-bit value in `%rax` into `%rbx`

**Answer:** B

---

**Q3 (Short Answer).** What do the AT&T size suffixes `b`, `w`, `l`, and `q` stand for, and how many bytes does each specify?

**Answer:** `b` = byte (1 byte), `w` = word (2 bytes), `l` = long (4 bytes), `q` = quad (8 bytes).

---

**Q4 (Multiple Choice).** You want to see the disassembled machine code of an object file `prog.o`. Which command would you use?

- A) `as -d prog.o`
- B) `objdump -d prog.o`
- C) `ld --disassemble prog.o`
- D) `readelf -d prog.o`

**Answer:** B

---

## Module 3, Lesson 4: The Data Section and Labels

**Q1 (Multiple Choice).** Which section should you use for a string constant that your program reads but never modifies?

- A) `.text`
- B) `.data`
- C) `.rodata`
- D) `.bss`

**Answer:** C

---

**Q2 (Short Answer).** What is the difference between the `.data` section and the `.bss` section?

**Answer:** `.data` holds initialized global/static variables (the initial values are stored in the executable). `.bss` holds uninitialized (zero-initialized) variables and takes no space in the executable file on disk -- the OS zeroes the memory at load time.

---

**Q3 (Multiple Choice).** Given the following data declarations:

```asm
        .section .data
x:      .byte 0x41
y:      .long 100
z:      .quad 0
msg:    .asciz "Hi"
```

How many bytes does the label `msg` occupy in memory (including the null terminator)?

- A) 2
- B) 3
- C) 4
- D) 8

**Answer:** B

---

**Q4 (Short Answer).** Explain what `lea msg(%rip), %rsi` does and why `%rip`-relative addressing is used instead of `mov $msg, %rsi`.

**Answer:** `lea msg(%rip), %rsi` computes the address of `msg` relative to the current instruction pointer and stores that address in `%rsi`. RIP-relative addressing is used because it produces position-independent code (PIC) -- the code works correctly regardless of where it is loaded in memory, which is required by modern loaders and ASLR.

---

## Module 3, Lesson 6: Logical and Shift Operations

**Q1 (Multiple Choice).** What value is in `%rax` after these two instructions?

```asm
        mov $0xABCD, %rax
        and $0xFF, %rax
```

- A) `0xABCD`
- B) `0xAB`
- C) `0xCD`
- D) `0x00`

**Answer:** C

---

**Q2 (Short Answer).** The shift amount for `shl`, `shr`, and `sar` can be an immediate value or a register. If you want to use a register, which specific register must you use, and why can't you use any other?

**Answer:** You must use `%cl` (the low byte of `%rcx`). This is a hardware restriction of the x86 architecture -- the shift instructions are hard-wired to read the shift count only from `%cl` or from an immediate operand. No other register is accepted.

---

**Q3 (Multiple Choice).** What is the difference between `shr $2, %eax` and `sar $2, %eax` when `%eax` contains `0xFFFFFFE0` (-32 in two's complement)?

- A) Both produce the same result
- B) `shr` fills with zeros on the left (result: `0x3FFFFFF8`); `sar` fills with copies of the sign bit (result: `0xFFFFFFF8`)
- C) `shr` fills with ones; `sar` fills with zeros
- D) `shr` is invalid on negative values

**Answer:** B

---

**Q4 (Short Answer).** Trace the XOR swap below. What are the values of `%rax` and `%rbx` after all three `xor` instructions?

```asm
        mov $10, %rax
        mov $25, %rbx
        xor %rbx, %rax
        xor %rax, %rbx
        xor %rbx, %rax
```

**Answer:** After the three XOR instructions, `%rax` = 25 and `%rbx` = 10. The values have been swapped. Step by step: (1) `%rax` = 10 ^ 25 = 19; (2) `%rbx` = 19 ^ 25 = 10; (3) `%rax` = 19 ^ 10 = 25.

---

## Module 3, Lesson 7: The Stack, Push, and Pop

**Q1 (Multiple Choice).** On x86-64, the stack grows toward __________ memory addresses. Executing `pushq %rax` causes `%rsp` to __________.

- A) higher; increase by 8
- B) lower; decrease by 8
- C) higher; decrease by 8
- D) lower; increase by 8

**Answer:** B

---

**Q2 (Short Answer).** Write the two-instruction sequence that `pushq %rax` is equivalent to.

**Answer:**
```asm
subq $8, %rsp
movq %rax, (%rsp)
```

---

**Q3 (Multiple Choice).** Suppose `%rsp` is `0x7FFF00` at the start of this sequence. What is `%rsp` after?

```asm
        pushq %rax
        pushq %rbx
        popq %rcx
```

- A) `0x7FFEF0`
- B) `0x7FFEF8`
- C) `0x7FFF00`
- D) `0x7FFF08`

**Answer:** B -- First push: `0x7FFF00 - 8 = 0x7FFEF8`. Second push: `0x7FFEF8 - 8 = 0x7FFEF0`. Pop: `0x7FFEF0 + 8 = 0x7FFEF8`.

---

**Q4 (Short Answer).** Instead of using `push`/`pop`, a programmer allocates space for four 8-byte local variables with `sub $32, %rsp`. How do they access the third local variable (bytes 16-23), and how do they deallocate the space when done?

**Answer:** The third local variable is accessed at `16(%rsp)` (e.g., `movq $0, 16(%rsp)`). The space is deallocated with `add $32, %rsp`, which restores `%rsp` to its original value.

---

## Module 3, Lesson 8: Putting It All Together

**Q1 (Multiple Choice).** What is the purpose of the `.extern` directive?

- A) It makes a label visible to other files
- B) It declares that a label is defined in another file and will be resolved at link time
- C) It exports a function to the C standard library
- D) It marks a section as executable

**Answer:** B

---

**Q2 (Short Answer).** In a `_start` program (not using the C runtime), the stack is initially 8 bytes off from 16-byte alignment. Why does the echo program below begin with `push %rbp` before calling `readInt`?

```asm
_start:
        push %rbp
        call readInt
        mov %rax, %rdi
        call writeInt
        pop %rbp
        mov $60, %rax
        xor %rdi, %rdi
        syscall
```

**Answer:** The System V ABI requires `%rsp` to be 16-byte aligned at the point of a `call` instruction. Since the OS sets up `%rsp` at an address that is 8 bytes off from a 16-byte boundary in a `_start` program, the `push %rbp` subtracts 8 from `%rsp`, bringing it into alignment before the `call`.

---

**Q3 (Multiple Choice).** To build a program from three source files (`main.s`, `readInt.s`, `writeInt.s`), which sequence is correct?

- A) `as -o program main.s readInt.s writeInt.s`
- B) `as -o main.o main.s && as -o readInt.o readInt.s && as -o writeInt.o writeInt.s && ld -o program main.o readInt.o writeInt.o`
- C) `ld -o program main.s readInt.s writeInt.s`
- D) `gcc -nostdlib -o program main.s readInt.s writeInt.s` (this works but `as`/`ld` does not)

**Answer:** B

---

**Q4 (Short Answer).** In the complete program from the lesson, the `readInt` helper returns a value in `%rax`, and `writeInt` expects its argument in `%rdi`. After calling `readInt`, the program saves the result with `push %rax` before making a syscall. Why is this save necessary?

**Answer:** The `write` syscall (and other function calls) will overwrite `%rax` with the syscall return value. If the first number were left in `%rax` without saving it, it would be destroyed by the subsequent syscall or function call. Pushing it onto the stack preserves it so it can be restored later with `pop`.

---

## Module 4, Lesson 1: Condition Codes, Comparisons, and Jumps

**Q1 (Multiple Choice).** Which instruction sets the condition code flags but does NOT store its result in any register?

- A) `sub %rbx, %rax`
- B) `lea (%rax,%rbx), %rcx`
- C) `cmp %rbx, %rax`
- D) `add $1, %rax`

**Answer:** C -- `cmp` computes the subtraction and sets flags but discards the result. (`sub` also sets flags but stores the result. `lea` does NOT set flags at all.)

---

**Q2 (Short Answer).** After `cmp %rbx, %rax`, the flags reflect the result of `%rax - %rbx`. If `%rax` = 5 and `%rbx` = 10, which flags are set? Would a `jl` (jump if less, signed) be taken?

**Answer:** `%rax - %rbx` = 5 - 10 = -5. The result is negative and non-zero, so SF = 1 and ZF = 0. There is no signed overflow, so OF = 0. Since `jl` checks `SF ^ OF`, and `1 ^ 0 = 1`, the jump IS taken.

---

**Q3 (Multiple Choice).** Which pair of jump instructions would you use for an **unsigned** comparison?

- A) `jg` / `jl`
- B) `ja` / `jb`
- C) `js` / `jns`
- D) `je` / `jne`

**Answer:** B -- `ja` (jump if above) and `jb` (jump if below) use CF and ZF, which are the unsigned comparison flags.

---

**Q4 (Multiple Choice).** What does the `sete %al` instruction do?

- A) Sets `%al` to 1 if the carry flag is set, 0 otherwise
- B) Sets `%al` to 1 if the zero flag is set (i.e., the previous comparison was equal), 0 otherwise
- C) Sets `%rax` to 0
- D) Sets the equal flag in the condition codes

**Answer:** B

---

## Module 4, Lesson 2: If Statements in Assembly

**Q1 (Multiple Choice).** A compiler typically translates `if (a == 0) { body }` into assembly using an **inverted** condition. Which pattern does this produce?

- A) `cmp $0, %eax` / `je body_label`
- B) `cmp $0, %eax` / `jne skip_body` / `<body>` / `skip_body:`
- C) `test %eax, %eax` / `je skip_body` / `<body>` / `skip_body:`
- D) `cmp $0, %eax` / `jg body_label`

**Answer:** B -- The compiler inverts the condition: instead of "jump to body if equal," it writes "jump past body if NOT equal."

---

**Q2 (Short Answer).** What does `testl %esi, %esi` compute, and why is it used instead of `cmpl $0, %esi`?

**Answer:** `testl %esi, %esi` computes `%esi & %esi` and sets the flags (discarding the result). The AND of a register with itself equals the register's value, so ZF is set if and only if the register is zero. It is preferred over `cmpl $0, %esi` because it encodes in fewer bytes (no immediate operand needed).

---

**Q3 (Multiple Choice).** What does `cmovgl %edi, %eax` do?

- A) Always moves `%edi` into `%eax`
- B) Moves `%edi` into `%eax` only if the previous comparison indicated "greater than" (signed)
- C) Moves `%eax` into `%edi` if greater
- D) Compares `%edi` and `%eax` and moves the greater value into `%eax`

**Answer:** B

---

**Q4 (Short Answer).** Trace this code. What exit code does the program produce?

```asm
_start:
        mov $-5, %rax
        cmp $0, %rax
        jg positive
        je is_zero
negative:
        mov $1, %rdi
        jmp done
is_zero:
        mov $2, %rdi
        jmp done
positive:
        mov $3, %rdi
done:
        mov $60, %rax
        syscall
```

**Answer:** The exit code is 1. `%rax` is -5, so `cmp $0, %rax` computes -5 - 0 = -5. This is not greater than 0 (`jg` not taken) and not equal to 0 (`je` not taken), so execution falls through to `negative:`, setting `%rdi` to 1.

---

## Module 4, Lesson 4: Switch Statements

**Q1 (Multiple Choice).** When gcc compiles a dense switch statement, it stores the jump table in which section?

- A) `.text`
- B) `.data`
- C) `.rodata`
- D) `.bss`

**Answer:** C -- The jump table is read-only data (an array of constant code addresses).

---

**Q2 (Short Answer).** In a switch jump table implementation, the range check uses `cmpl $N, %eax` followed by `ja default`. Why is `ja` (unsigned above) used instead of `jg` (signed greater)?

**Answer:** Using `ja` (unsigned comparison) handles negative input values automatically. When a negative value is treated as an unsigned integer, it becomes a very large positive number, which is above the valid range N, so it correctly falls through to the default case. With `jg`, negative values would not be "greater than" N and could bypass the range check.

---

**Q3 (Multiple Choice).** What does the instruction `jmp *(%rdx,%rax,8)` do?

- A) Jumps to the address stored in `%rdx` plus `%rax`
- B) Reads a 64-bit address from memory at `%rdx + %rax * 8`, then jumps to that address
- C) Jumps to label `%rdx` unconditionally
- D) Compares `%rdx` and `%rax` and jumps if they differ by less than 8

**Answer:** B

---

**Q4 (Short Answer).** Consider a switch statement with cases 0, 1, 2, 3, and 5 (no case 4), plus a default. The jump table has 6 entries (indices 0-5). What does the jump table entry at index 4 contain?

**Answer:** The entry at index 4 contains the address of the default case code. Since there is no `case 4` in the switch, the jump table fills that gap with a pointer to the default handler so that input value 4 still goes to the correct destination.

---

## Module 4, Lesson 6: Local Variables and the Stack Frame

**Q1 (Multiple Choice).** What is the standard function prologue for a function that needs 24 bytes of local variable space?

- A) `sub $24, %rsp`
- B) `push %rbp` / `mov %rsp, %rbp` / `sub $24, %rsp`
- C) `push %rbp` / `sub $24, %rsp` / `mov %rsp, %rbp`
- D) `mov %rbp, %rsp` / `push %rbp` / `sub $24, %rsp`

**Answer:** B

---

**Q2 (Short Answer).** The `leave` instruction is a shorthand. Write the two instructions it is equivalent to.

**Answer:**
```asm
movq %rbp, %rsp
popq %rbp
```
It first restores `%rsp` from `%rbp` (deallocating locals), then pops the saved base pointer.

---

**Q3 (Multiple Choice).** In a function that uses `%rbp` as a frame pointer, local variables are accessed at negative offsets from `%rbp`. If a function has two 8-byte local variables, where are they located?

- A) `8(%rbp)` and `16(%rbp)`
- B) `-8(%rbp)` and `-16(%rbp)`
- C) `(%rsp)` and `8(%rsp)`
- D) `-4(%rbp)` and `-8(%rbp)`

**Answer:** B

---

**Q4 (Short Answer).** The System V ABI requires `%rsp` to be 16-byte aligned at the point of a `call` instruction. Suppose a function's prologue is `push %rbp` / `mov %rsp, %rbp` / `sub $24, %rsp`. Is the stack correctly aligned for a subsequent `call`? Explain.

**Answer:** At function entry, `%rsp` is 8 bytes off from 16-byte alignment (because the caller's `call` pushed an 8-byte return address). The `push %rbp` subtracts another 8, making `%rsp` 16-byte aligned. Then `sub $24, %rsp` subtracts 24, which is not a multiple of 16, so `%rsp` is now 8 bytes off alignment. The stack is NOT correctly aligned for a `call`. The subtraction should be `$32` (or any multiple of 16) to maintain alignment.

---

## Module 4, Lesson 8: Buffer Overflows and Security

**Q1 (Multiple Choice).** Why is `gets()` considered dangerous and removed from the C standard as of C11?

- A) It is slower than `fgets()`
- B) It reads input until a newline with no maximum length, allowing buffer overflows
- C) It does not handle Unicode characters
- D) It leaks memory on every call

**Answer:** B

---

**Q2 (Short Answer).** Name the three defense mechanisms against buffer overflow attacks discussed in the lesson, and briefly describe what each does.

**Answer:** (1) **ASLR** (Address Space Layout Randomization) -- randomizes the starting address of the stack (and other memory regions) each time a program runs, making it hard for attackers to predict where injected code will be. (2) **Stack canaries** -- the compiler places a random value between the buffer and the return address; before returning, it checks whether this value was modified and aborts if so. (3) **NX bit / DEP** (Non-Executable stack) -- marks the stack as non-executable at the hardware level, so even if an attacker controls the return address, the CPU refuses to execute code from the stack.

---

**Q3 (Multiple Choice).** In gcc-generated code with stack protection, the canary value is loaded from `%fs:0x28`. What happens at function exit if the canary has been overwritten?

- A) The function returns normally but with corrupted data
- B) The program jumps to `__stack_chk_fail`, which prints an error and aborts
- C) The OS sends a SIGSEGV signal
- D) The canary is silently restored

**Answer:** B

---

**Q4 (Short Answer).** An attacker fills a buffer with a long NOP sled followed by shellcode. What is a NOP sled, and which defense mechanism is it designed to defeat?

**Answer:** A NOP sled is a long sequence of `nop` instructions placed before the actual malicious payload. If execution lands anywhere within the sled, it "slides" forward through the `nop` instructions until it reaches the shellcode. This is designed to defeat **ASLR** -- since ASLR randomizes addresses, the attacker doesn't know exactly where the buffer starts, but a large NOP sled increases the chance that a guessed return address will land somewhere in the sled.

---

## Module 4, Lesson 9: Floating Point in Assembly

**Q1 (Multiple Choice).** Which registers are used for floating point operations on x86-64?

- A) `%rax` through `%r15`
- B) `%st(0)` through `%st(7)` (x87 stack)
- C) `%xmm0` through `%xmm15` (SSE registers)
- D) `%fp0` through `%fp15`

**Answer:** C

---

**Q2 (Short Answer).** Consider the C function `void f(float a, int b, float c)`. In which registers do the three arguments arrive, according to the System V calling convention?

**Answer:** `a` is in `%xmm0`, `b` is in `%edi`, and `c` is in `%xmm1`. Floating point and integer arguments are numbered independently -- `a` and `c` are the first and second FP arguments (so `%xmm0` and `%xmm1`), while `b` is the first integer argument (so `%edi`).

---

**Q3 (Multiple Choice).** What does `xorpd %xmm0, %xmm0` do?

- A) Computes the XOR of two doubles and stores the result in memory
- B) Sets `%xmm0` to 0.0
- C) Flips all bits in `%xmm0`
- D) Tests whether `%xmm0` is zero and sets condition flags

**Answer:** B -- XOR of any value with itself produces all zeros. This is the standard idiom for zeroing a floating point register, since you cannot write `mov $0, %xmm0`.

---

**Q4 (Short Answer).** Trace this code. What value ends up in `%rdi`?

```asm
        .section .data
val_a:  .double 3.5
val_b:  .double 12.0

        .text
        .global _start
_start:
        movsd val_a(%rip), %xmm0
        movsd val_b(%rip), %xmm1
        mulsd %xmm1, %xmm0
        cvttsd2si %xmm0, %rdi
        mov $60, %rax
        syscall
```

**Answer:** `%rdi` = 42. The program loads 3.5 into `%xmm0` and 12.0 into `%xmm1`, multiplies them (`3.5 * 12.0 = 42.0`), then converts the double 42.0 to the integer 42 with `cvttsd2si` (truncation toward zero).

---

## Module 3, Lesson 9: Debugging with GDB

**Q1 (Multiple Choice).** You have assembled a program with `as -o prog.o prog.s` and linked it with `ld -o prog prog.o`. When you load it in GDB, you see raw addresses instead of label names. What did you forget?

- A) You forgot to use `ld -g`
- B) You forgot to add the `-g` flag when assembling: `as -g -o prog.o prog.s`
- C) You forgot to run `strip prog` before loading it
- D) GDB never shows label names for assembly programs

**Answer:** B -- The `-g` flag on the assembler includes debug symbols (label names, line numbers) in the object file. Without it, GDB only has raw addresses to work with.

---

**Q2 (Short Answer).** Explain the difference between `stepi` and `nexti` in GDB. When would you use each one?

**Answer:** `stepi` (step instruction) executes one machine instruction and, if that instruction is a `call`, steps *into* the called function. `nexti` (next instruction) also executes one machine instruction, but if it is a `call`, it executes the entire called function and stops after it returns. Use `stepi` when you want to debug inside a function call; use `nexti` when you trust the function and want to skip over it.

---

**Q3 (Multiple Choice).** You are stopped at a breakpoint and want to see the 4 quad-words (8 bytes each) at the top of the stack. Which GDB command would you use?

- A) `print $rsp`
- B) `x/4xg $rsp`
- C) `info stack 4`
- D) `x/4xb $rsp`

**Answer:** B -- `x/4xg $rsp` examines 4 units (`4`), in hex format (`x`), each 8 bytes (`g` for "giant"). Option D would show 4 individual bytes, not 4 quad-words.

---

**Q4 (Short Answer).** You are debugging a program and suspect that `%rax` is being corrupted somewhere. Describe a GDB feature that would let you automatically pause the program whenever `%rax` changes, without manually stepping through every instruction.

**Answer:** Use a **watchpoint**: `watch $rax`. GDB will automatically pause execution whenever the value of `%rax` changes, and will show you the old and new values along with the instruction that caused the change.

---

## Module 4, Lesson 10: Static and Dynamic Linking

**Q1 (Multiple Choice).** You see this error when linking:

```
ld: main.o: in function `_start':
main.s:(.text+0x5): undefined reference to `readInt'
```

What is the most likely cause?

- A) `readInt` is defined in `main.s` but not marked `.global`
- B) The object file containing `readInt` was not included on the `ld` command line
- C) `readInt` is a weak symbol and was overridden
- D) The linker does not support external references

**Answer:** B -- The linker could not find any definition of `readInt` in the object files it was given. You need to include the object file that defines `readInt` (e.g., `ld -o program main.o readInt.o`).

---

**Q2 (Short Answer).** In the linker's symbol resolution rules, what is the difference between a "strong" symbol and a "weak" symbol? Give an example of each in C.

**Answer:** A **strong symbol** is a function or an initialized global variable (e.g., `int x = 5;` or `void foo() { ... }`). A **weak symbol** is an uninitialized global variable (e.g., `int x;` without an initializer). If the linker finds one strong and one weak symbol with the same name, the strong symbol wins. Two strong symbols with the same name cause a "multiple definition" error.

---

**Q3 (Multiple Choice).** A statically linked "Hello, World" program is ~900 KB, while the dynamically linked version is ~16 KB. Why is the static version so much larger?

- A) The static version includes debug symbols; the dynamic version does not
- B) The static version includes a copy of the entire C library in the executable
- C) The dynamic version is compressed
- D) The static version includes the Linux kernel

**Answer:** B -- Static linking copies all needed library code (from libc.a) into the executable. Dynamic linking just records that the program needs `libc.so.6`, which is loaded from a shared file at runtime.

---

**Q4 (Short Answer).** Briefly explain the role of the PLT and GOT in dynamic linking. Why is the first call to a dynamically linked function slower than subsequent calls?

**Answer:** The **PLT** (Procedure Linkage Table) contains small code stubs, one per external function. The **GOT** (Global Offset Table) stores the actual runtime addresses of those functions. On the first call, the PLT stub invokes the dynamic linker to look up the function's real address in the shared library and write it into the GOT. On subsequent calls, the PLT stub reads the address directly from the GOT without involving the dynamic linker, so it is much faster.

---

## Module 8, Lesson 6: Garbage Collection

**Q1 (Multiple Choice).** Object A points to object B, and object B points back to object A. No other references to A or B exist. Which garbage collection technique will fail to reclaim this memory?

- A) Mark-and-sweep
- B) Reference counting (without a cycle detector)
- C) Generational GC
- D) Copying collector

**Answer:** B -- With reference counting alone, both A and B have a reference count of 1 (from each other), so neither will ever reach 0. Mark-and-sweep, generational GC, and copying collectors are all tracing collectors that detect unreachable cycles.

---

**Q2 (Short Answer).** Explain the two phases of mark-and-sweep garbage collection. What are the "roots" that the mark phase starts from?

**Answer:** In the **mark phase**, the collector starts from the roots (local variables on the stack, global/static variables, and CPU registers) and follows all pointers, marking each reachable object. In the **sweep phase**, the collector walks through the entire heap and frees any object that was not marked. The roots are the starting points because they represent every memory location the program can directly access without following a pointer from another heap object.

---

**Q3 (Multiple Choice).** Why can't C use a moving/compacting garbage collector?

- A) C programs are too slow for garbage collection
- B) C does not have a heap
- C) C allows raw pointer arithmetic, so the runtime cannot find and update all pointers to a moved object
- D) Moving objects would change their hash codes

**Answer:** C -- In C, pointers are raw memory addresses and can be stored as integers, computed via arithmetic, or hidden in ways the runtime cannot track. Moving an object would invalidate every pointer to it, and the runtime has no reliable way to find them all.

---

**Q4 (Short Answer).** The generational hypothesis states that "most objects die young." How does a generational garbage collector exploit this observation to improve performance?

**Answer:** A generational collector divides the heap into a young generation (nursery) and one or more old generations. It collects the young generation frequently, which is fast because most young objects are already dead (few survivors to copy/mark). Objects that survive several young collections are promoted to the old generation, which is collected rarely. This avoids the cost of repeatedly scanning long-lived objects, dramatically reducing the average collection time.
