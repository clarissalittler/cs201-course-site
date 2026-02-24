# Practice Problems and Module Quizzes

Practice problems for each lesson and a quiz for each module.

---

## Module 1, Lesson 1: C Language Basics

**Q1 (Multiple Choice).** In C, which function is used for dynamic memory allocation instead of the C++ `new` operator?

- A) `alloc()`
- B) `calloc()`
- C) `malloc()`
- D) `create()`

**Answer:** C

---

**Q2 (Short Answer).** What format specifier is used in `printf` to print a signed integer in decimal?

**Answer:** %d

---

**Q3 (Multiple Choice).** How do you pass a primitive variable by reference in C?

- A) Use the `&` symbol in the parameter declaration, just like C++
- B) Pass the address of the variable using `&` and use a pointer parameter
- C) Use the `ref` keyword before the parameter
- D) C does not support any form of pass by reference

**Answer:** B

---

**Q4 (Short Answer).** What compiler command is used to compile C source code on Linux?

**Answer:** gcc

---

## Module 1, Lesson 2: Hexadecimal Numbers

**Q1 (Multiple Choice).** How many binary digits does each hexadecimal digit represent?

- A) 2
- B) 3
- C) 4
- D) 8

**Answer:** C

---

**Q2 (Short Answer).** What is the hexadecimal number 0x1A in decimal?

**Answer:** 26

---

**Q3 (Multiple Choice).** What is the binary representation of the hexadecimal digit `F`?

- A) 1110
- B) 1010
- C) 1101
- D) 1111

**Answer:** D

---

**Q4 (Short Answer).** In C, what prefix is used before a literal number to indicate it is hexadecimal?

**Answer:** 0x

---

## Module 1, Lesson 3: Numeric Representation

**Q1 (Multiple Choice).** What is the smallest addressable unit of memory?

- A) 1 bit
- B) 1 nibble (4 bits)
- C) 1 byte (8 bits)
- D) 1 word

**Answer:** C

---

**Q2 (Short Answer).** On a 64-bit architecture, how many bytes does an `int` occupy?

**Answer:** 4 bytes

---

**Q3 (Multiple Choice).** What does the word size of a computer system represent?

- A) The size of an int data type
- B) The size of a pointer (number of bits for an address)
- C) The maximum size of a single file
- D) The clock speed of the processor

**Answer:** B

---

**Q4 (Short Answer).** On a 64-bit architecture, how many bytes does a `char*` (pointer) occupy?

**Answer:** 8 bytes

---

## Module 1, Lesson 4: Byte Ordering

**Q1 (Multiple Choice).** If the hex value `0x12345678` is stored at address 200 on a little-endian machine, which byte is stored at address 200?

- A) 0x12
- B) 0x34
- C) 0x56
- D) 0x78

**Answer:** D

---

**Q2 (Short Answer).** What byte ordering stores the most significant byte at the lowest address?

**Answer:** big-endian

---

**Q3 (Multiple Choice).** Which of the following is true about most modern consumer computers (Intel architecture)?

- A) They use big-endian byte ordering
- B) They use little-endian byte ordering
- C) They use mixed-endian byte ordering
- D) Byte ordering varies depending on the data type

**Answer:** B

---

**Q4 (Short Answer).** How many consecutive bytes are needed to store one `int` value in memory?

**Answer:** 4

---

## Module 1, Lesson 5: Pointwise Bit Operations

**Q1 (Multiple Choice).** What is the result of the bitwise operation `1010 & 1100`?

- A) 1110
- B) 1000
- C) 0110
- D) 1010

**Answer:** B

---

**Q2 (Short Answer).** What is the result of `1010 ^ 1001` (bitwise XOR)?

**Answer:** 0011

---

**Q3 (Multiple Choice).** When performing a right shift on a signed integer, what type of shift is used?

- A) Logical shift (fills with zeros)
- B) Arithmetic shift (fills with the sign bit)
- C) Circular shift (wraps bits around)
- D) Random shift (undefined behavior)

**Answer:** B

---

**Q4 (Short Answer).** What is the result of the bitwise complement `~1011` (assuming 4-bit values)?

**Answer:** 0100

---

## Module 1, Lesson 6: Bit Flags and Masking

**Q1 (Multiple Choice).** Given `#define SPEED_HIGH 8`, which operation turns on the high speed bit in `bit_flag`?

- A) `bit_flag = bit_flag & SPEED_HIGH;`
- B) `bit_flag = bit_flag | SPEED_HIGH;`
- C) `bit_flag = bit_flag ^ SPEED_HIGH;`
- D) `bit_flag = bit_flag ~ SPEED_HIGH;`

**Answer:** B

---

**Q2 (Short Answer).** To create a mask for the 5th bit position (counting from position 1 on the right), what expression would you use?

**Answer:** 1 << 4

---

**Q3 (Multiple Choice).** Which operation correctly turns OFF the `MOTOR_ON` bit in `bit_flag`?

- A) `bit_flag = bit_flag | MOTOR_ON;`
- B) `bit_flag = bit_flag & MOTOR_ON;`
- C) `bit_flag = bit_flag & ~MOTOR_ON;`
- D) `bit_flag = bit_flag ^ ~MOTOR_ON;`

**Answer:** C

---

**Q4 (Short Answer).** What is the result of `00010101 & 00000100` in binary?

**Answer:** 00000100

---

## Module 1, Lesson 7: Integer Data Types

**Q1 (Multiple Choice).** What is the maximum value of an `unsigned char`?

- A) 127
- B) 128
- C) 255
- D) 256

**Answer:** C

---

**Q2 (Short Answer).** What is the minimum value of a `signed char`?

**Answer:** -128

---

**Q3 (Multiple Choice).** Why is the magnitude of the minimum signed value one greater than the magnitude of the maximum signed value?

- A) Because one bit is reserved for the sign
- B) Because zero takes up one of the positive values, and negative zero is reassigned to represent one extra negative number
- C) Because of a hardware design flaw
- D) Because unsigned values are always one larger

**Answer:** B

---

**Q4 (Short Answer).** What is the maximum value of an `unsigned short`?

**Answer:** 65535

---

## Module 1, Lesson 8: Unsigned Integer Encoding

**Q1 (Multiple Choice).** For an unsigned integer type of width `w` bits, what is the formula for the maximum value (UMAX)?

- A) 2^w
- B) 2^w - 1
- C) 2^(w-1) - 1
- D) 2^(w-1)

**Answer:** B

---

**Q2 (Short Answer).** What is UMAX for an 8-bit unsigned integer?

**Answer:** 255

---

**Q3 (Multiple Choice).** How do you indicate in C that a literal integer value should be treated as unsigned?

- A) Prefix with `u`
- B) Suffix with `u` or `U`
- C) Wrap in `unsigned()`
- D) Prefix with `0u`

**Answer:** B

---

**Q4 (Short Answer).** What is the minimum value (UMIN) for any unsigned integer type?

**Answer:** 0

---

## Module 1, Lesson 9: Signed Integer Encoding

**Q1 (Multiple Choice).** In two's complement representation with 4 bits, what decimal value does the bit pattern `1111` represent?

- A) 15
- B) -0
- C) -1
- D) -7

**Answer:** C

---

**Q2 (Short Answer).** What is the two's complement bit pattern for -6 in 4 bits?

**Answer:** 1010

---

**Q3 (Multiple Choice).** To convert a positive number to its negative two's complement representation, what steps do you follow?

- A) Set the leftmost bit to 1
- B) Flip all bits (complement) and then add 1
- C) Subtract the number from 2^w
- D) Both B and C are correct methods

**Answer:** D

---

**Q4 (Short Answer).** For a signed integer of width `w` bits, what is the formula for the minimum value (TMIN)?

**Answer:** -2^(w-1)

---

## Module 1, Lesson 10: Type Casting

**Q1 (Multiple Choice).** When casting a negative signed integer to an unsigned integer of the same size, what happens?

- A) The value becomes 0
- B) The compiler produces an error
- C) The bit pattern is preserved but reinterpreted, resulting in a large positive number
- D) The magnitude is preserved and the sign is dropped

**Answer:** C

---

**Q2 (Short Answer).** When expanding a signed integer from a smaller type to a larger type, what technique is used to fill the new left bits?

**Answer:** sign extension

---

**Q3 (Multiple Choice).** When converting from a larger integer type to a smaller integer type, what happens to the leftmost bits?

- A) They are sign-extended
- B) They are zero-extended
- C) They are truncated (discarded)
- D) They cause a compiler error

**Answer:** C

---

**Q4 (Short Answer).** When expanding an unsigned integer from a smaller type to a larger type, what technique is used to fill the new left bits?

**Answer:** zero extension

---

## Module 1, Lesson 11: Integer Arithmetic

**Q1 (Multiple Choice).** How can you detect unsigned addition overflow?

- A) Check if the result equals zero
- B) Check if the sum is smaller than either operand
- C) Check if the sum is negative
- D) Check if the sum is larger than UMAX

**Answer:** B

---

**Q2 (Short Answer).** What is the expression `num << 3` equivalent to in terms of arithmetic?

**Answer:** num * 8

---

**Q3 (Multiple Choice).** For signed integer addition, under what condition can overflow occur?

- A) When one operand is positive and the other is negative
- B) When both operands are zero
- C) Only when both operands have the same sign (both positive or both negative)
- D) Overflow can never occur in signed addition

**Answer:** C

---

**Q4 (Short Answer).** How many extra bits are needed to hold the product of two w-bit integers without overflow?

**Answer:** w

---

## Module 1 Quiz

**Q1 (Multiple Choice).** On a little-endian 64-bit machine, the 4-byte integer `0xAABBCCDD` is stored starting at address 0x100. What byte value is at address 0x102?

- A) 0xAA
- B) 0xBB
- C) 0xCC
- D) 0xDD

**Answer:** B

---

**Q2 (Short Answer).** What is the hexadecimal representation of the binary number `11011110 10101101`?

**Answer:** 0xDEAD

---

**Q3 (Multiple Choice).** A signed `char` variable holds the bit pattern `10000000`. What decimal value does this represent in two's complement?

- A) 128
- B) -128
- C) -0
- D) -127

**Answer:** B

---

**Q4 (Multiple Choice).** In C, what happens when you cast the `signed char` value `-1` (bit pattern `11111111`) to an `unsigned char`?

- A) The result is 0
- B) The result is 1
- C) The result is 127
- D) The result is 255

**Answer:** D

---

**Q5 (Short Answer).** What is the result of `0xA3 & 0x0F`?

**Answer:** 0x03

---

**Q6 (Multiple Choice).** If you perform `unsigned char x = 200; signed char y = (signed char) x;`, what is the value of `y`?

- A) 200
- B) -56
- C) -200
- D) 56

**Answer:** B

---

**Q7 (Short Answer).** In C, which library must be included to use `malloc()` and `free()`?

**Answer:** stdlib.h

---

**Q8 (Multiple Choice).** What does the expression `1 << 4` evaluate to in decimal?

- A) 4
- B) 8
- C) 16
- D) 32

**Answer:** C

---

**Q9 (Multiple Choice).** You have two unsigned 8-bit values: `x = 250` and `y = 10`. What is the result of `x + y` stored in an `unsigned char`?

- A) 260
- B) 4
- C) 0
- D) 255

**Answer:** B

---

**Q10 (Short Answer).** What is the two's complement representation of `-3` in 8-bit binary?

**Answer:** 11111101

---

**Q11 (Multiple Choice).** When a signed `short` (16-bit) value of `-5` is expanded to a signed `int` (32-bit), what fills the new upper 16 bits?

- A) All zeros
- B) All ones
- C) Alternating ones and zeros
- D) Undefined/random bits

**Answer:** B

---

**Q12 (Multiple Choice).** Which of the following C features does NOT exist in C but does exist in C++?

- A) Structs
- B) Pointers
- C) Reference parameters using `&` in the function signature
- D) The `printf` function

**Answer:** C

---

**Q13 (Short Answer).** What is `num >> 2` equivalent to arithmetically (assuming `num` is a positive integer)?

**Answer:** num / 4

---

**Q14 (Multiple Choice).** An 8-bit unsigned number has a maximum value of 255. If this same 8-bit field is interpreted as a signed two's complement value, what is its maximum positive value?

- A) 255
- B) 128
- C) 127
- D) 64

**Answer:** C

---

**Q15 (Multiple Choice).** Given `bit_flag = 0b00010101`, which settings are ON using the motor control scheme from the lesson (bit 1 = motor on, bit 2 = slow, bit 3 = medium, bit 4 = fast, bit 5 = reverse)?

- A) Motor on, slow speed, fast speed
- B) Motor on, medium speed, reverse
- C) Motor on, fast speed, reverse
- D) Slow speed, medium speed, reverse

**Answer:** B

---

## Module 2, Lesson 1: Fractional Binary Numbers

**Q1 (Multiple Choice).** What is the decimal value of the fractional binary number 1011.101?

- A) 10.625
- B) 11.625
- C) 11.5
- D) 10.75

**Answer:** B

---

**Q2 (Short Answer).** What is the fractional binary number 1011.101 expressed in binary scientific notation?

**Answer:** 1.011101 x 2^3

---

**Q3 (Multiple Choice).** In C/C++, a `float` type is how many bits wide?

- A) 16
- B) 32
- C) 64
- D) 128

**Answer:** B

---

**Q4 (Short Answer).** Convert the binary scientific notation 1.0011 x 2^13 to a decimal number.

**Answer:** 9728

---

## Module 2, Lesson 2: IEEE 754 Floating Point Encoding Scheme

**Q1 (Multiple Choice).** In IEEE 754 single-precision, the exponent field uses biased encoding. What is the bias value?

- A) 63
- B) 126
- C) 127
- D) 255

**Answer:** C

---

**Q2 (Short Answer).** In IEEE 754 single-precision, what are the three field widths in order (sign, exponent, fraction)?

**Answer:** 1, 8, 23

---

**Q3 (Multiple Choice).** A floating point number has an exponent field that is all zeros. What category does this number fall into?

- A) Normalized
- B) Denormalized
- C) Special case (infinity or NaN)
- D) Undefined

**Answer:** B

---

**Q4 (Short Answer).** In IEEE 754 single-precision, what does a bit pattern with the exponent field all ones and the fraction field all zeros represent?

**Answer:** infinity

---

## Module 2, Lesson 3: Floating Point Examples

**Q1 (Multiple Choice).** Given the single-precision bit pattern `1 10000001 10100000000000000000000`, what is the sign bit and the decimal value of the exponent field?

- A) Positive, exponent field = 129
- B) Negative, exponent field = 127
- C) Negative, exponent field = 129
- D) Positive, exponent field = 131

**Answer:** C

---

**Q2 (Short Answer).** What is the IEEE 754 single-precision bit pattern for the decimal value -6.5? Write your answer with spaces between the three fields (sign, exponent, fraction).

**Answer:** 1 10000001 10100000000000000000000

---

**Q3 (Multiple Choice).** When decoding a denormalized IEEE 754 single-precision number, what is the exponent E?

- A) E = 0
- B) E = -127
- C) E = -126
- D) E = -128

**Answer:** C

---

**Q4 (Short Answer).** What is the smallest positive value representable in IEEE 754 single-precision, expressed as a power of 2?

**Answer:** 2^-149

---

## Module 2, Lesson 4: Floating Point Rounding

**Q1 (Multiple Choice).** Which rounding mode is the default in IEEE 754?

- A) Toward +infinity
- B) Toward -infinity
- C) Toward zero
- D) Round-to-even

**Answer:** D

---

**Q2 (Short Answer).** In a system with 3 fraction bits, using round-to-even, what does the value 1.00110 round to?

**Answer:** 1.010

---

**Q3 (Multiple Choice).** What are the three extra precision bits the floating-point hardware uses internally to determine rounding direction?

- A) Sign, exponent, and fraction bits
- B) Guard, round, and sticky bits
- C) Carry, overflow, and underflow bits
- D) Most significant, middle, and least significant bits

**Answer:** B

---

**Q4 (Short Answer).** In the GRS (guard, round, sticky) system under round-to-even, what rounding action is taken when GRS = 100?

**Answer:** round to even

---

## Module 2, Lesson 5: Floating Point Operations

**Q1 (Multiple Choice).** Given the following two C expressions, what are their results?
```
(3.14 + 1e10) - 1e10
3.14 + (1e10 - 1e10)
```

- A) Both produce 3.14
- B) The first produces 3.14, the second produces 0.0
- C) The first produces 0.0, the second produces 3.14
- D) Both produce 0.0

**Answer:** C

---

**Q2 (Short Answer).** When casting a float or double to an int in C, what rounding mode is used?

**Answer:** toward zero

---

**Q3 (Multiple Choice).** Why is it unreliable to compare two floating point numbers using `==` in C?

- A) The `==` operator is not defined for floating point types
- B) Rounding errors mean two computations that should be mathematically equal often produce slightly different values
- C) Floating point comparisons always return false
- D) The compiler optimizes away all floating point comparisons

**Answer:** B

---

**Q4 (Short Answer).** In single-precision floating point, what value does `(1e20 * 1e20) * 1e-20` evaluate to?

**Answer:** +inf

---

## Module 2, Lesson 6: The Posit Number System

**Q1 (Multiple Choice).** In the posit number system, how is a negative value encoded?

- A) By setting the sign bit to 1, same as IEEE 754
- B) By storing the two's complement of the positive encoding
- C) By using biased notation for the sign
- D) By inverting all fraction bits

**Answer:** B

---

**Q2 (Short Answer).** In a Posit<n, es> with es = 2, what is the useed value?

**Answer:** 16

---

**Q3 (Multiple Choice).** In the posit number system, how many special (non-numeric) bit patterns exist?

- A) 1 (only zero)
- B) 2 (zero and NaR)
- C) 3 (zero, NaR, and infinity)
- D) Over 16 million (same as IEEE 754 NaN patterns)

**Answer:** B

---

**Q4 (Short Answer).** In a posit, if the regime field is "1110", what is the regime value?

**Answer:** 2

---

## Module 2 Quiz

**Q1 (Multiple Choice).** What is the decimal value of the fractional binary number 110.11?

- A) 6.5
- B) 6.75
- C) 7.5
- D) 7.75

**Answer:** B

---

**Q2 (Multiple Choice).** In IEEE 754 double-precision, how many bits are used for the exponent field, and what is the bias?

- A) 8 bits, bias = 127
- B) 11 bits, bias = 1023
- C) 11 bits, bias = 1022
- D) 15 bits, bias = 16383

**Answer:** B

---

**Q3 (Short Answer).** In IEEE 754 single-precision, a normalized number has an exponent of -12. What decimal value is stored in the exponent field?

**Answer:** 115

---

**Q4 (Multiple Choice).** What distinguishes a quiet NaN from a signaling NaN in IEEE 754 (on Intel architecture)?

- A) The sign bit is different
- B) The leftmost fraction bit is 1 for quiet NaN and 0 for signaling NaN
- C) The exponent field is different
- D) Quiet NaN has all fraction bits set to 1

**Answer:** B

---

**Q5 (Short Answer).** The decimal value 0.1 cannot be represented exactly in binary floating point. What repeating binary pattern does it produce after the leading "0.0"?

**Answer:** 0011

---

**Q6 (Multiple Choice).** In a system with 3 fraction bits using round-to-even, the value 1.01010 (exactly at the midpoint between 1.010 and 1.011) rounds to which value?

- A) 1.011 (round up)
- B) 1.010 (round down)
- C) 1.100 (round up with carry)
- D) It depends on the sign of the number

**Answer:** B

---

**Q7 (Multiple Choice).** Which of the following is a correct strategy to reduce accumulated rounding error when summing a large array of small floating point numbers?

- A) Cast all values to integers first
- B) Sum from largest to smallest magnitude
- C) Sum from smallest to largest magnitude
- D) Use integer arithmetic throughout

**Answer:** C

---

**Q8 (Short Answer).** When casting the C expression `(int)3.9f`, what integer value is produced?

**Answer:** 3

---

**Q9 (Multiple Choice).** What is the key innovation of the posit number system compared to IEEE 754?

- A) A larger sign field
- B) A variable-length regime field that provides tapered precision
- C) A fixed exponent field with higher bias
- D) Support for complex numbers

**Answer:** B

---

**Q10 (Short Answer).** Decode the Posit<8, 2> bit pattern 0 110 01 10. What decimal value does it represent?

**Answer:** 48

---

**Q11 (Multiple Choice).** Why does IEEE 754 define denormalized numbers (exponent field all zeros)?

- A) To represent infinity
- B) To allow gradual underflow instead of an abrupt cutoff to zero
- C) To encode NaN values
- D) To increase the precision of large numbers

**Answer:** B

---

**Q12 (Multiple Choice).** Which of the following is a limitation of the posit number system that prevents it from replacing IEEE 754 today?

- A) Posits cannot represent negative numbers
- B) Posits have lower dynamic range than IEEE 754
- C) Posit hardware support is still in the research/prototype stage, and IEEE 754 is universally supported
- D) Posits require twice as many bits as IEEE 754 for the same precision

**Answer:** C

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

## Module 3, Lesson 2: Writing Makefiles

**Q1 (Multiple Choice).** In a Makefile rule, what character must be used to indent recipe lines?

- A) Two spaces
- B) Four spaces
- C) A literal tab character
- D) Either tabs or spaces

**Answer:** C

---

**Q2 (Short Answer).** In a Makefile, what automatic variable represents the target of the current rule?

**Answer:** $@

---

**Q3 (Multiple Choice).** Given the following Makefile rule, what does `$^` expand to?

```
program: main.o readInt.o writeInt.o
	$(LD) -o $@ $^
```

- A) program
- B) main.o
- C) main.o readInt.o writeInt.o
- D) $(LD)

**Answer:** C

---

**Q4 (Short Answer).** What is the purpose of declaring `.PHONY: clean` in a Makefile?

**Answer:** Tells Make clean is not a file

---

## Module 3, Lesson 3: Registers and the CPU Environment

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

## Module 3, Lesson 4: Moving Data

**Q1 (Multiple Choice).** Which of the following `mov` instructions is INVALID in x86-64 assembly?

- A) `movq %rax, %rcx`
- B) `movq $42, %rax`
- C) `movq (%rax), (%rdx)`
- D) `movq (%rax), %rcx`

**Answer:** C

---

**Q2 (Short Answer).** Given that `%rbp` holds the value 10 and `%r10` holds the value 2, what address does the memory operand `200(%rbp, %r10, 4)` compute?

**Answer:** 218

---

**Q3 (Multiple Choice).** What does the `lea` instruction do, compared to `mov`?

- A) `lea` loads the value at a computed memory address; `mov` loads the address itself
- B) `lea` loads the computed address itself into a register; `mov` loads the value at that address
- C) `lea` and `mov` are identical in function
- D) `lea` can only be used with immediate values

**Answer:** B

---

**Q4 (Short Answer).** What instruction is commonly used as an idiom to set a register to zero?

**Answer:** xor %reg, %reg

---

## Module 3, Lesson 5: The Data Section and Labels

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

## Module 3, Lesson 6: Arithmetic Operations

**Q1 (Short Answer).** What instruction must be executed immediately before `idiv` to sign-extend `%rax` into `%rdx:%rax` for 64-bit division?

**Answer:** cqto

---

**Q2 (Multiple Choice).** After executing the following instructions, what value is in `%rax`?

```asm
mov $100, %rax
cqto
mov $7, %rcx
idiv %rcx
```

- A) 2
- B) 7
- C) 14
- D) 100

**Answer:** C

---

**Q3 (Short Answer).** After the `idiv` instruction in Q2 above, what value is in `%rdx`?

**Answer:** 2

---

**Q4 (Multiple Choice).** The compiler generates `leaq (%rdx, %rdx, 4), %rdx`. What arithmetic operation does this perform on the value in `%rdx`?

- A) Multiplies %rdx by 4
- B) Multiplies %rdx by 5
- C) Adds 4 to %rdx
- D) Multiplies %rdx by 8

**Answer:** B

---

## Module 3, Lesson 7: Logical and Shift Operations

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

**Answer:** After the three XOR instructions, `%rax` = 25 and `%rbx` = 10. The values have been swapped.

---

## Module 3, Lesson 8: The Stack, Push, and Pop

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

**Answer:** B

---

**Q4 (Short Answer).** Instead of using `push`/`pop`, a programmer allocates space for four 8-byte local variables with `sub $32, %rsp`. How do they access the third local variable (bytes 16-23), and how do they deallocate the space when done?

**Answer:** The third local variable is accessed at `16(%rsp)` (e.g., `movq $0, 16(%rsp)`). The space is deallocated with `add $32, %rsp`, which restores `%rsp` to its original value.

---

## Module 3, Lesson 9: Putting It All Together

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

**Answer:** The System V ABI requires `%rsp` to be 16-byte aligned at the point of a `call` instruction. The `push %rbp` adjusts the stack alignment before the `call`.

---

**Q3 (Multiple Choice).** To build a program from three source files (`main.s`, `readInt.s`, `writeInt.s`), which sequence is correct?

- A) `as -o program main.s readInt.s writeInt.s`
- B) `as -o main.o main.s && as -o readInt.o readInt.s && as -o writeInt.o writeInt.s && ld -o program main.o readInt.o writeInt.o`
- C) `ld -o program main.s readInt.s writeInt.s`
- D) `gcc -nostdlib -o program main.s readInt.s writeInt.s` (this works but `as`/`ld` does not)

**Answer:** B

---

**Q4 (Short Answer).** In the complete program from the lesson, the `readInt` helper returns a value in `%rax`, and `writeInt` expects its argument in `%rdi`. After calling `readInt`, the program saves the result with `push %rax` before making a syscall. Why is this save necessary?

**Answer:** The `write` syscall (and other function calls) will overwrite `%rax` with the syscall return value. Pushing it onto the stack preserves it so it can be restored later with `pop`.

---

## Module 3, Lesson 10: Debugging with GDB

**Q1 (Multiple Choice).** You have assembled a program with `as -o prog.o prog.s` and linked it with `ld -o prog prog.o`. When you load it in GDB, you see raw addresses instead of label names. What did you forget?

- A) You forgot to use `ld -g`
- B) You forgot to add the `-g` flag when assembling: `as -g -o prog.o prog.s`
- C) You forgot to run `strip prog` before loading it
- D) GDB never shows label names for assembly programs

**Answer:** B

---

**Q2 (Short Answer).** Explain the difference between `stepi` and `nexti` in GDB. When would you use each one?

**Answer:** `stepi` steps into function calls; `nexti` steps over them (executes the entire called function and stops after it returns). Use `stepi` to debug inside a function; use `nexti` to skip over it.

---

**Q3 (Multiple Choice).** You are stopped at a breakpoint and want to see the 4 quad-words (8 bytes each) at the top of the stack. Which GDB command would you use?

- A) `print $rsp`
- B) `x/4xg $rsp`
- C) `info stack 4`
- D) `x/4xb $rsp`

**Answer:** B

---

**Q4 (Short Answer).** You are debugging a program and suspect that `%rax` is being corrupted somewhere. Describe a GDB feature that would let you automatically pause the program whenever `%rax` changes.

**Answer:** Use a watchpoint: `watch $rax`. GDB will automatically pause execution whenever the value of `%rax` changes.

---

## Module 3 Quiz

**Q1 (Multiple Choice).** What are the four stages of the build process for a C program, in order?

- A) Compiling, Assembling, Linking, Loading
- B) Preprocessing, Compiling, Assembling, Linking
- C) Parsing, Compiling, Optimizing, Linking
- D) Preprocessing, Parsing, Assembling, Loading

**Answer:** B

---

**Q2 (Short Answer).** What flag do you pass to `gcc` to produce an assembly (.s) file and stop before assembling?

**Answer:** -S

---

**Q3 (Multiple Choice).** In a Makefile, what does the pattern rule `%.o: %.s` mean?

- A) All .o files depend on all .s files
- B) Any .o file depends on the .s file with the same stem
- C) Only files named %.o and %.s are built
- D) The .s files should be deleted after creating .o files

**Answer:** B

---

**Q4 (Short Answer).** How many general-purpose 64-bit registers does the x86-64 architecture have?

**Answer:** 16

---

**Q5 (Multiple Choice).** In AT&T syntax, what does `movq $5, %rax` do?

- A) Moves the value in memory address 5 into %rax
- B) Moves the contents of %rax into memory address 5
- C) Moves the immediate value 5 into register %rax
- D) Moves the contents of %rax into register $5

**Answer:** C

---

**Q6 (Short Answer).** What size suffix on an instruction indicates an 8-byte (64-bit) operation?

**Answer:** q

---

**Q7 (Multiple Choice).** What is the full form of a memory address in AT&T syntax, and what does it compute?

- A) `displacement(base, index, scale)` computes `displacement + base + index * scale`
- B) `scale(base, index, displacement)` computes `base + index + scale * displacement`
- C) `base(displacement, index, scale)` computes `base + displacement + index`
- D) `displacement[base + index * scale]` computes `displacement + base + index * scale`

**Answer:** A

---

**Q8 (Short Answer).** Which section directive places data in a read-only data section?

**Answer:** .section .rodata

---

**Q9 (Multiple Choice).** What does `shl $3, %rax` do?

- A) Divides %rax by 3
- B) Multiplies %rax by 3
- C) Multiplies %rax by 8
- D) Divides %rax by 8

**Answer:** C

---

**Q10 (Short Answer).** What instruction is used for arithmetic (signed) right shift in x86-64?

**Answer:** sar

---

**Q11 (Multiple Choice).** What happens to `%rsp` when `pushq %rax` is executed?

- A) %rsp increases by 8, then %rax is written to (%rsp)
- B) %rax is written to (%rsp), then %rsp decreases by 8
- C) %rsp decreases by 8, then %rax is written to (%rsp)
- D) %rsp does not change; %rax is written to the next available stack slot

**Answer:** C

---

**Q12 (Multiple Choice).** In the complete program from Lesson 9, why is `push %rbp` executed at the start of `_start` before calling `readInt` or `writeInt`?

- A) To save the value of %rbp for later use
- B) To align the stack to a 16-byte boundary before the call instruction
- C) To create space for local variables
- D) To pass %rbp as an argument to the function

**Answer:** B

---

**Q13 (Short Answer).** In GDB, what command executes one machine instruction while stepping over (not into) function calls?

**Answer:** nexti

---

**Q14 (Multiple Choice).** Which assembler flag must you include when building your program so that GDB can display label names and source line numbers?

- A) -O
- B) -g
- C) -S
- D) -d

**Answer:** B

---

## Module 4, Lesson 1: Condition Codes, Comparisons, and Jumps

**Q1 (Multiple Choice).** Which instruction sets the condition code flags but does NOT store its result in any register?

- A) `sub %rbx, %rax`
- B) `lea (%rax,%rbx), %rcx`
- C) `cmp %rbx, %rax`
- D) `add $1, %rax`

**Answer:** C

---

**Q2 (Short Answer).** After `cmp %rbx, %rax`, the flags reflect the result of `%rax - %rbx`. If `%rax` = 5 and `%rbx` = 10, which flags are set? Would a `jl` (jump if less, signed) be taken?

**Answer:** SF = 1, ZF = 0, OF = 0. Since `jl` checks SF ^ OF, and 1 ^ 0 = 1, the jump IS taken.

---

**Q3 (Multiple Choice).** Which pair of jump instructions would you use for an **unsigned** comparison?

- A) `jg` / `jl`
- B) `ja` / `jb`
- C) `js` / `jns`
- D) `je` / `jne`

**Answer:** B

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

**Answer:** B

---

**Q2 (Short Answer).** What does `testl %esi, %esi` compute, and why is it used instead of `cmpl $0, %esi`?

**Answer:** `testl %esi, %esi` computes `%esi & %esi` and sets flags. It is preferred over `cmpl $0, %esi` because it encodes in fewer bytes (no immediate operand needed).

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

**Answer:** 1

---

## Module 4, Lesson 3: Loops

**Q1 (Multiple Choice).** In the "do-while" loop pattern in assembly, where is the condition check placed relative to the loop body?

- A) Before the loop body, at the top of the loop
- B) After the loop body, at the bottom of the loop
- C) Both before and after the loop body
- D) There is no condition check; the loop runs forever

**Answer:** B

---

**Q2 (Short Answer).** In the "jump-to-middle" while loop pattern, what instruction is used at the beginning to skip directly to the condition test before the first iteration?

**Answer:** jmp

---

**Q3 (Multiple Choice).** Consider this assembly loop:

```asm
        mov $5, %rcx
loop:
        dec %rcx
        jnz loop
```

How many times does the `dec` instruction execute?

- A) 4
- B) 5
- C) 6
- D) Infinite loop

**Answer:** B

---

**Q4 (Short Answer).** In assembly, a C `for` loop is structurally equivalent to which other type of C loop?

**Answer:** while

---

## Module 4, Lesson 4: Switch Statements

**Q1 (Multiple Choice).** When gcc compiles a dense switch statement, it stores the jump table in which section?

- A) `.text`
- B) `.data`
- C) `.rodata`
- D) `.bss`

**Answer:** C

---

**Q2 (Short Answer).** In a switch jump table implementation, the range check uses `cmpl $N, %eax` followed by `ja default`. Why is `ja` (unsigned above) used instead of `jg` (signed greater)?

**Answer:** Using `ja` (unsigned comparison) handles negative input values automatically. When a negative value is treated as unsigned, it becomes a very large positive number, which is above the valid range N, so it correctly falls through to the default case.

---

**Q3 (Multiple Choice).** What does the instruction `jmp *(%rdx,%rax,8)` do?

- A) Jumps to the address stored in `%rdx` plus `%rax`
- B) Reads a 64-bit address from memory at `%rdx + %rax * 8`, then jumps to that address
- C) Jumps to label `%rdx` unconditionally
- D) Compares `%rdx` and `%rax` and jumps if they differ by less than 8

**Answer:** B

---

**Q4 (Short Answer).** Consider a switch statement with cases 0, 1, 2, 3, and 5 (no case 4), plus a default. The jump table has 6 entries (indices 0-5). What does the jump table entry at index 4 contain?

**Answer:** The address of the default case code.

---

## Module 4, Lesson 5: Writing Functions

**Q1 (Multiple Choice).** In the System V AMD64 calling convention used on Linux, which register holds the first integer argument to a function?

- A) %rax
- B) %rsi
- C) %rdi
- D) %rcx

**Answer:** C

---

**Q2 (Short Answer).** In the System V AMD64 ABI, which register holds the return value of a function?

**Answer:** %rax

---

**Q3 (Multiple Choice).** Which of the following registers is callee-saved (i.e., must be preserved by the called function)?

- A) %rax
- B) %rcx
- C) %rbx
- D) %rdi

**Answer:** C

---

**Q4 (Multiple Choice).** What does the `call` instruction do?

- A) Jumps to a label without saving any state
- B) Pushes the return address onto the stack and then jumps to the target label
- C) Pops the return address from the stack and jumps to it
- D) Saves all registers to the stack and jumps to the target label

**Answer:** B

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

---

**Q3 (Multiple Choice).** In a function that uses `%rbp` as a frame pointer, local variables are accessed at negative offsets from `%rbp`. If a function has two 8-byte local variables, where are they located?

- A) `8(%rbp)` and `16(%rbp)`
- B) `-8(%rbp)` and `-16(%rbp)`
- C) `(%rsp)` and `8(%rsp)`
- D) `-4(%rbp)` and `-8(%rbp)`

**Answer:** B

---

**Q4 (Short Answer).** The System V ABI requires `%rsp` to be 16-byte aligned at the point of a `call` instruction. Suppose a function's prologue is `push %rbp` / `mov %rsp, %rbp` / `sub $24, %rsp`. Is the stack correctly aligned for a subsequent `call`? Explain.

**Answer:** No. The `sub $24` leaves the stack 8 bytes off alignment. The subtraction should be $32 (or any multiple of 16) to maintain alignment.

---

## Module 4, Lesson 7: Arrays, Structs, and Data Alignment

**Q1 (Multiple Choice).** Given an array of `.quad` (8-byte) elements with base address in `%r8` and index in `%rcx`, which addressing mode accesses element `arr[i]`?

- A) `(%r8,%rcx)`
- B) `(%r8,%rcx,4)`
- C) `(%r8,%rcx,8)`
- D) `8(%r8,%rcx)`

**Answer:** C

---

**Q2 (Short Answer).** Consider the following struct. What is the total size in bytes after the compiler adds alignment padding?

```c
struct example {
    char  a;   // 1 byte
    int   b;   // 4 bytes
    char  c;   // 1 byte
    long  d;   // 8 bytes
};
```

**Answer:** 24 bytes

---

**Q3 (Multiple Choice).** What is the key difference between a `struct` and a `union` in terms of memory layout?

- A) A struct stores all fields at the same offset; a union stores them at different offsets
- B) A struct stores fields at sequential offsets; a union stores all fields at offset 0
- C) A struct requires alignment; a union does not
- D) A struct is always larger than a union

**Answer:** B

---

**Q4 (Short Answer).** If the struct from Q2 is reordered with fields from largest to smallest (long, int, char, char), what is the total size in bytes?

**Answer:** 16 bytes

---

## Module 4, Lesson 8: Buffer Overflows and Security

**Q1 (Multiple Choice).** Why is `gets()` considered dangerous and removed from the C standard as of C11?

- A) It is slower than `fgets()`
- B) It reads input until a newline with no maximum length, allowing buffer overflows
- C) It does not handle Unicode characters
- D) It leaks memory on every call

**Answer:** B

---

**Q2 (Short Answer).** Name the three defense mechanisms against buffer overflow attacks discussed in the lesson.

**Answer:** ASLR, stack canaries, NX bit / DEP

---

**Q3 (Multiple Choice).** In gcc-generated code with stack protection, the canary value is loaded from `%fs:0x28`. What happens at function exit if the canary has been overwritten?

- A) The function returns normally but with corrupted data
- B) The program jumps to `__stack_chk_fail`, which prints an error and aborts
- C) The OS sends a SIGSEGV signal
- D) The canary is silently restored

**Answer:** B

---

**Q4 (Short Answer).** An attacker fills a buffer with a long NOP sled followed by shellcode. What is a NOP sled, and which defense mechanism is it designed to defeat?

**Answer:** A NOP sled is a long sequence of `nop` instructions placed before malicious payload. It is designed to defeat ASLR by increasing the chance that a guessed return address lands somewhere in the sled.

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

**Answer:** a in %xmm0, b in %edi, c in %xmm1

---

**Q3 (Multiple Choice).** What does `xorpd %xmm0, %xmm0` do?

- A) Computes the XOR of two doubles and stores the result in memory
- B) Sets `%xmm0` to 0.0
- C) Flips all bits in `%xmm0`
- D) Tests whether `%xmm0` is zero and sets condition flags

**Answer:** B

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

**Answer:** 42

---

## Module 4 Quiz

**Q1 (Short Answer).** Which condition code flag is set when the result of an arithmetic operation is zero?

**Answer:** ZF

---

**Q2 (Multiple Choice).** After executing `cmp %rbx, %rax`, the condition flags reflect which computation?

- A) %rbx - %rax
- B) %rax - %rbx
- C) %rax + %rbx
- D) %rbx AND %rax

**Answer:** B

---

**Q3 (Multiple Choice).** What advantage does `cmov` (conditional move) have over a compare-and-jump sequence for simple two-way choices?

- A) `cmov` uses fewer registers
- B) `cmov` avoids branch misprediction penalties
- C) `cmov` can operate on memory-to-memory values
- D) `cmov` sets the condition code flags

**Answer:** B

---

**Q4 (Short Answer).** In the "jump-to-middle" pattern for a while loop, what kind of jump instruction begins the pattern (before the loop body)?

**Answer:** jmp

---

**Q5 (Multiple Choice).** In the do-while loop pattern below, how many times does the loop body execute if `%rcx` starts at 1?

```asm
        mov $0, %rax
        mov $1, %rcx
loop:
        add %rcx, %rax
        inc %rcx
        cmp $11, %rcx
        jl loop
```

- A) 9
- B) 10
- C) 11
- D) 12

**Answer:** B

---

**Q6 (Multiple Choice).** A switch statement with many consecutive case values is typically compiled using what data structure?

- A) A linked list of case addresses
- B) A hash table
- C) A jump table (array of code addresses)
- D) A binary search tree

**Answer:** C

---

**Q7 (Short Answer).** In the System V AMD64 ABI, which register holds the second argument to a function?

**Answer:** %rsi

---

**Q8 (Multiple Choice).** Which of the following is NOT a callee-saved register in the System V AMD64 calling convention?

- A) %rbx
- B) %r12
- C) %r10
- D) %rbp

**Answer:** C

---

**Q9 (Short Answer).** What single instruction is equivalent to `mov %rbp, %rsp` followed by `pop %rbp` in a function epilogue?

**Answer:** leave

---

**Q10 (Multiple Choice).** In a function's stack frame, local variables are accessed using negative offsets from which register?

- A) %rsp
- B) %rax
- C) %rbp
- D) %rdi

**Answer:** C

---

**Q11 (Multiple Choice).** In a struct, why does the compiler insert padding bytes between fields?

- A) To make the struct easier to read in a debugger
- B) To ensure each field is aligned to a memory address that is a multiple of its size
- C) To prevent buffer overflow attacks
- D) To make the struct exactly 64 bytes

**Answer:** B

---

**Q12 (Short Answer).** What is the name of the defense mechanism where the compiler inserts a random value between a buffer and the return address on the stack?

**Answer:** stack canary

---

**Q13 (Multiple Choice).** In x86-64 floating point, which register holds the first floating-point argument to a function?

- A) %rdi
- B) %xmm0
- C) %mm0
- D) %rax

**Answer:** B

---

**Q14 (Multiple Choice).** What does ASLR (Address Space Layout Randomization) do to defend against buffer overflow attacks?

- A) Encrypts the contents of the stack
- B) Marks the stack as non-executable
- C) Randomizes the starting address of the stack (and other memory regions) each time a program runs
- D) Inserts canary values between stack variables

**Answer:** C

---

**Q15 (Short Answer).** What instruction is used to move a double-precision floating-point value between an XMM register and memory?

**Answer:** movsd

---

## Module 5, Lesson 1: Flow Control

**Q1 (Multiple Choice).** What is the term for moving from one instruction to another during program execution?

- A) Flow of control
- B) Control transfer
- C) Exceptional control flow
- D) Context switch

**Answer:** B

---

**Q2 (Multiple Choice).** Which of the following is an example of an event that would cause exceptional control flow (ECF)?

- A) An if-else branch in the program's source code
- B) A for-loop iterating over an array
- C) A hardware timer going off at a regular interval
- D) A function call within the same program

**Answer:** C

---

**Q3 (Short Answer).** What is the name for an abrupt change to the normal flow of control caused by an outside event?

**Answer:** exceptional control flow

---

**Q4 (Multiple Choice).** Which of the following is NOT described as a reason for exceptional control flow?

- A) A hardware timer goes off at regular intervals
- B) A program requests data from a disk
- C) A parent process is notified that a child has terminated
- D) A program executes a jump instruction to a new address

**Answer:** D

---

## Module 5, Lesson 2: Exceptions

**Q1 (Multiple Choice).** When an exception occurs, where does the hardware look up the address of the appropriate exception handler?

- A) The program's stack
- B) The exception table
- C) The symbol table
- D) The page table

**Answer:** B

---

**Q2 (Short Answer).** What is the data structure, indexed by exception number, that stores the starting addresses of exception handlers?

**Answer:** exception table

---

**Q3 (Multiple Choice).** After an exception handler finishes executing, which of the following is NOT a possible outcome?

- A) Return control to the instruction that caused the exception
- B) Return control to the next instruction after the one that caused the exception
- C) Abort (terminate) the program
- D) Restart the entire program from the beginning

**Answer:** D

---

**Q4 (Multiple Choice).** Exception numbers can be assigned by which of the following?

- A) Only the hardware
- B) Only the operating system
- C) Either the hardware or the operating system
- D) Only the application programmer

**Answer:** C

---

## Module 5, Lesson 3: Classes of Exceptions

**Q1 (Multiple Choice).** Which class of exception occurs asynchronously as a result of signals from I/O devices external to the processor?

- A) Traps
- B) Faults
- C) Aborts
- D) Interrupts

**Answer:** D

---

**Q2 (Short Answer).** What class of exception is a system call (such as the `syscall` instruction) an example of?

**Answer:** trap

---

**Q3 (Multiple Choice).** A fault handler that successfully corrects an error condition will do which of the following?

- A) Return control to the next instruction after the faulting instruction
- B) Return control to the same (faulting) instruction so it can re-execute
- C) Always abort the program
- D) Restart the entire program

**Answer:** B

---

**Q4 (Multiple Choice).** Which of the following best describes an abort?

- A) An intentional, synchronous exception used for system calls
- B) An asynchronous exception from an I/O device
- C) A synchronous, unrecoverable error that terminates the program
- D) A recoverable error that re-executes the faulting instruction

**Answer:** C

---

## Module 5, Lesson 4: Exceptions in Linux/x86-64 Systems

**Q1 (Short Answer).** How many total possible exception types exist in modern Linux/x86-64 systems?

**Answer:** 256

---

**Q2 (Multiple Choice).** In Linux/x86-64 systems, exception numbers 0-31 are defined by:

- A) The Linux operating system
- B) The application programmer
- C) The Intel x86-64 hardware architecture
- D) The C standard library

**Answer:** C

---

**Q3 (Multiple Choice).** What happens in Linux when a floating-point divide by zero is performed?

- A) A divide error exception (exception 0) is raised
- B) The result is set to infinity (inf)
- C) A segmentation fault occurs
- D) A machine check exception is raised

**Answer:** B

---

**Q4 (Short Answer).** What is the exception number for a General Protection Fault (segmentation fault) on Linux/x86-64?

**Answer:** 13

---

## Module 5, Lesson 5: Processes

**Q1 (Multiple Choice).** Which of the following is NOT part of a process's context?

- A) The program counter
- B) The contents of general-purpose registers
- C) The source code of the program on disk
- D) The set of open file descriptors

**Answer:** C

---

**Q2 (Short Answer).** What is the term for when a running process is suspended temporarily to allow another process to use the CPU?

**Answer:** preempted

---

**Q3 (Multiple Choice).** In the context of processes, what does the term "virtual memory" refer to?

- A) Memory stored on the GPU
- B) A technique that maps each process's addresses to actual physical addresses, giving the illusion of private memory
- C) Extra RAM installed in the system
- D) Memory reserved exclusively for the operating system kernel

**Answer:** B

---

**Q4 (Multiple Choice).** What determines whether a process has full access to all instructions and memory, or restricted access?

- A) The process ID
- B) The program counter value
- C) The mode bit in a control register
- D) The virtual memory page table

**Answer:** C

---

## Module 5, Lesson 6: Process Control

**Q1 (Short Answer).** What function does a process call to obtain its own process ID?

**Answer:** getpid()

---

**Q2 (Multiple Choice).** A child process that has terminated but has not yet been reaped by its parent is called a:

- A) Daemon process
- B) Orphan process
- C) Zombie process
- D) Stopped process

**Answer:** C

---

**Q3 (Multiple Choice).** What does the `fork()` function return in the child process?

- A) The child's own PID
- B) The parent's PID
- C) 0
- D) -1

**Answer:** C

---

**Q4 (Multiple Choice).** What happens when `execve()` is called successfully within a process?

- A) It creates a new child process running the specified program
- B) The current process is replaced by the new program and does not return
- C) It returns 0 to indicate success
- D) It forks the process and runs the new program in the child

**Answer:** B

---

## Module 5, Lesson 7: Examples of Using Fork

**Q1 (Multiple Choice).** In the fork1.c example, if `cpid1 = fork()` is called and is successful, what value does `cpid1` hold in the parent process?

- A) 0
- B) -1
- C) The parent's own PID
- D) The child's PID

**Answer:** D

---

**Q2 (Short Answer).** After a fork, if the child changes a variable that was declared before the fork, does the parent's copy of that variable change?

**Answer:** no

---

**Q3 (Multiple Choice).** Consider a fork example with two printf statements in the parent branch and two in the child branch. Which statement about the output ordering is correct?

- A) All parent output must appear before all child output
- B) All child output must appear before all parent output
- C) The order of statements within each branch is preserved, but statements from different branches can be interleaved
- D) The output order is completely random with no constraints

**Answer:** C

---

**Q4 (Multiple Choice).** Why is it important for the child process to return (or exit) inside a for loop that calls fork()?

- A) To prevent the child from continuing the loop and creating its own child processes
- B) To send the return value to the operating system
- C) To free the child's memory immediately
- D) To ensure the parent process runs first

**Answer:** A

---

## Module 5, Lesson 8: Signals in Linux Systems

**Q1 (Short Answer).** What signal is sent to the foreground process when the user presses Ctrl+C at the terminal?

**Answer:** SIGINT

---

**Q2 (Multiple Choice).** Which of the following signals CANNOT be overridden by a custom signal handler?

- A) SIGINT and SIGCHLD
- B) SIGKILL and SIGSTOP
- C) SIGFPE and SIGSEGV
- D) SIGALRM and SIGCONT

**Answer:** B

---

**Q3 (Short Answer).** What signal is sent from a child process to its parent when the child terminates or is stopped?

**Answer:** SIGCHLD

---

**Q4 (Multiple Choice).** What is the default action for the SIGCHLD signal?

- A) Terminate the process
- B) Stop the process until SIGCONT
- C) Ignore the signal
- D) Dump core and terminate

**Answer:** C

---

## Module 5, Lesson 9: Signal Management

**Q1 (Multiple Choice).** How are pending signals represented in a process's context?

- A) As a linked list of signal objects
- B) As a bit flag where each bit represents one of the 30 signals
- C) As an array of signal handler pointers
- D) As entries in the exception table

**Answer:** B

---

**Q2 (Short Answer).** What function from the C signal library is used to install a signal handler for a specific signal?

**Answer:** signal()

---

**Q3 (Multiple Choice).** When calling the `kill()` function, what happens if the `pid` argument is set to 0?

- A) The signal is sent only to the calling process
- B) The signal is sent to all processes in the calling process's group
- C) The signal is ignored
- D) The function returns an error

**Answer:** B

---

**Q4 (Short Answer).** What constant do you pass as the handler argument to `signal()` to restore the default behavior for a signal?

**Answer:** SIG_DFL

---

## Module 5, Lesson 10: Blocking and Unblocking Signals

**Q1 (Short Answer).** What function is used to block or unblock signals in a process?

**Answer:** sigprocmask()

---

**Q2 (Multiple Choice).** Which `sigprocmask()` action replaces the entire current blocked signal set with the provided mask?

- A) SIG_BLOCK
- B) SIG_UNBLOCK
- C) SIG_SETMASK
- D) SIG_REPLACE

**Answer:** C

---

**Q3 (Multiple Choice).** What does the function `sigemptyset(&mask)` do?

- A) Fills the mask with all signals set to 1 (blocked)
- B) Creates an empty signal mask with all bits set to 0
- C) Deletes a specific signal from the mask
- D) Checks if a signal is a member of the mask

**Answer:** B

---

**Q4 (Short Answer).** What function adds a specific signal to a signal set mask?

**Answer:** sigaddset()

---

## Module 5, Lesson 11: Writing Signal Handlers

**Q1 (Multiple Choice).** Why should global variables shared between a signal handler and the main program be declared with `volatile sig_atomic_t`?

- A) To make the variable accessible from other processes
- B) To ensure atomic reads and writes so the handler and main program do not corrupt the variable
- C) To allow the variable to be stored in a register
- D) To make the variable read-only

**Answer:** B

---

**Q2 (Short Answer).** Which output function should be used inside a signal handler instead of `printf()` because it is async-signal-safe?

**Answer:** write()

---

**Q3 (Multiple Choice).** Why is `printf()` not recommended for use inside a signal handler?

- A) It is too slow for signal handlers
- B) It is not async-signal-safe and may cause undefined behavior if interrupted
- C) It cannot print to the terminal from a signal handler
- D) It requires too many arguments

**Answer:** B

---

**Q4 (Multiple Choice).** Signal handlers are invoked:

- A) Only when the program explicitly calls them
- B) At predictable, scheduled intervals
- C) By the operating system at any point during program execution
- D) Only during system calls

**Answer:** C

---

## Module 5, Lesson 12: Signal Handler Examples

**Q1 (Multiple Choice).** In the sigsimple.c example, what message is printed when the user presses Ctrl+C?

- A) "Goodbye!"
- B) "Signal received!"
- C) "Ouch!"
- D) "Interrupted!"

**Answer:** C

---

**Q2 (Short Answer).** In the `write(STDOUT, mess, 7)` call used in the signal handler example, what does the first argument (value 1) represent?

**Answer:** standard output

---

**Q3 (Multiple Choice).** In the sigflag.c example, what technique is used to communicate between the signal handler and the main program loop?

- A) Shared memory between processes
- B) A pipe between the handler and main
- C) A volatile sig_atomic_t global flag variable
- D) A return value from the handler function

**Answer:** C

---

**Q4 (Multiple Choice).** When a fork happens, what is true about the installed signal handler?

- A) Only the parent retains the signal handler
- B) Only the child inherits the signal handler
- C) Both parent and child have the signal handler registered
- D) Neither process retains the signal handler after fork

**Answer:** C

---

## Module 5 Quiz

**Q1 (Multiple Choice).** What is the term for an abrupt change in control flow caused by an external event such as a hardware timer or disk I/O notification?

- A) Control transfer
- B) Context switch
- C) Exceptional control flow (ECF)
- D) System call

**Answer:** C

---

**Q2 (Multiple Choice).** Which class of exception is synchronous, intentional, and commonly used for system calls?

- A) Interrupt
- B) Trap
- C) Fault
- D) Abort

**Answer:** B

---

**Q3 (Short Answer).** What is the exception number for a page fault on Linux/x86-64 systems?

**Answer:** 14

---

**Q4 (Multiple Choice).** What creates the illusion that each process has exclusive use of the processor?

- A) Virtual memory
- B) Logical control flow with interleaving and context switching
- C) The exception table
- D) Signal handlers

**Answer:** B

---

**Q5 (Short Answer).** What is the term for the technique the OS uses to map each process's addresses to actual physical memory addresses?

**Answer:** virtual memory

---

**Q6 (Multiple Choice).** What value does `fork()` return in the parent process upon success?

- A) 0
- B) -1
- C) The parent's own PID
- D) The child's PID

**Answer:** D

---

**Q7 (Short Answer).** What is the term for a terminated child process that has not yet been reaped by its parent?

**Answer:** zombie process

---

**Q8 (Multiple Choice).** Which function is used to reap a terminated child process and retrieve its exit status?

- A) fork()
- B) execve()
- C) waitpid()
- D) getpid()

**Answer:** C

---

**Q9 (Multiple Choice).** If a parent process terminates before its child, what happens to the child process?

- A) The child is immediately terminated
- B) The child becomes a child of the init process
- C) The child becomes a zombie permanently
- D) The child's PID is reassigned

**Answer:** B

---

**Q10 (Short Answer).** What signal number is SIGKILL?

**Answer:** 9

---

**Q11 (Multiple Choice).** When using the `kill` command to send a signal to all processes in a process group with group ID 15111, which syntax is correct?

- A) `kill -9 15111`
- B) `kill -9 -15111`
- C) `kill -15111 -9`
- D) `kill --group 15111 -9`

**Answer:** B

---

**Q12 (Short Answer).** What function is used to create an empty signal set mask before adding individual signals to it?

**Answer:** sigemptyset()

---

**Q13 (Multiple Choice).** Which of the following correctly describes why variables shared between a signal handler and the main program should use `volatile sig_atomic_t`?

- A) It makes the variable thread-safe across multiple processes
- B) It ensures atomic access and prevents the compiler from optimizing away reads/writes
- C) It allocates the variable in kernel memory space
- D) It makes the variable immutable after initialization

**Answer:** B

---

**Q14 (Multiple Choice).** After fork() is called in a program that has an installed signal handler, which processes have the handler registered?

- A) Only the parent process
- B) Only the child process
- C) Both parent and child processes
- D) Neither process; handlers must be reinstalled after fork

**Answer:** C

---

**Q15 (Multiple Choice).** What is the key difference between SIGSTOP and SIGTSTP?

- A) SIGSTOP can be caught by a handler but SIGTSTP cannot
- B) SIGTSTP is sent from the terminal (Ctrl+Z) and can be caught; SIGSTOP cannot be caught by a handler
- C) They are identical in behavior
- D) SIGSTOP resumes a process while SIGTSTP suspends it

**Answer:** B

---

## Module 6, Lesson 1: Threads vs. Processes

**Q1 (Multiple Choice).** Which of the following is SHARED among all threads within the same process?

- A) The stack
- B) CPU registers
- C) The program counter
- D) Heap memory

**Answer:** D

---

**Q2 (Short Answer).** What is the term for a thread that is sometimes used because threads are cheaper to create and context-switch than full processes?

**Answer:** lightweight process

---

**Q3 (Multiple Choice).** A process creates three additional threads using pthread_create(). How many total stacks exist within that process?

- A) 1
- B) 3
- C) 4
- D) It depends on the operating system

**Answer:** C

---

**Q4 (Multiple Choice).** Which of the following is a reason to prefer fork() over threads?

- A) Lower creation overhead
- B) Easier communication via shared variables
- C) Strong isolation so a bug in one task cannot crash another
- D) Faster context switching

**Answer:** C

---

## Module 6, Lesson 2: Creating and Joining Threads

**Q1 (Short Answer).** What is the name of the pthreads function used to create a new thread?

**Answer:** pthread_create()

---

**Q2 (Multiple Choice).** What is the correct signature for a function that can be passed as the start routine to pthread_create()?

- A) int func(int arg)
- B) void func(void *arg)
- C) void *func(void *arg)
- D) void *func(int arg)

**Answer:** C

---

**Q3 (Multiple Choice).** A programmer creates 5 threads in a for loop, passing `&i` (the address of the loop variable) as the argument to each thread. What problem does this cause?

- A) A segmentation fault
- B) A race condition where threads may read the wrong value of i
- C) A compiler error because int* cannot be cast to void*
- D) A deadlock

**Answer:** B

---

**Q4 (Short Answer).** What pthreads function is analogous to waitpid() and blocks until a specified thread terminates?

**Answer:** pthread_join()

---

## Module 6, Lesson 3: Race Conditions

**Q1 (Multiple Choice).** The C statement `counter++` compiles to how many distinct machine-level operations?

- A) 1
- B) 2
- C) 3
- D) 4

**Answer:** C

---

**Q2 (Short Answer).** What is the name for a section of code that accesses shared data and must not be executed by more than one thread at a time?

**Answer:** critical section

---

**Q3 (Multiple Choice).** Two threads each increment a shared counter 1,000,000 times without synchronization. Which of the following best describes the expected final value?

- A) Exactly 2,000,000 every time
- B) Exactly 1,000,000 every time
- C) An unpredictable value less than or equal to 2,000,000
- D) A compiler error because concurrent writes are not allowed

**Answer:** C

---

**Q4 (Multiple Choice).** Which of the following does NOT fix a race condition on a shared variable?

- A) Protecting access with a mutex
- B) Declaring the variable as volatile
- C) Using a semaphore to enforce mutual exclusion
- D) Accumulating in a thread-local variable and updating the shared variable under a lock

**Answer:** B

---

## Module 6, Lesson 4: Mutexes

**Q1 (Short Answer).** What macro is used to statically initialize a pthread mutex declared at global scope?

**Answer:** PTHREAD_MUTEX_INITIALIZER

---

**Q2 (Multiple Choice).** What happens when a thread calls pthread_mutex_lock() on a mutex that is already held by another thread?

- A) The function returns an error code immediately
- B) The calling thread blocks until the mutex is released
- C) The calling thread terminates
- D) The mutex is forcibly taken from the other thread

**Answer:** B

---

**Q3 (Multiple Choice).** Deadlock requires four conditions to hold simultaneously. Which of the following is the most practical condition to break in order to prevent deadlock?

- A) Mutual exclusion
- B) Hold and wait
- C) No preemption
- D) Circular wait

**Answer:** D

---

**Q4 (Short Answer).** What pthreads function attempts to acquire a mutex without blocking if the mutex is already held?

**Answer:** pthread_mutex_trylock()

---

## Module 6, Lesson 5: Condition Variables and Semaphores

**Q1 (Multiple Choice).** Why must the condition in a pthread_cond_wait() pattern be checked with a while loop instead of an if statement?

- A) The compiler requires a while loop for condition variables
- B) pthread_cond_wait() can return due to spurious wakeups, so the condition must be rechecked
- C) An if statement causes undefined behavior with pthreads
- D) A while loop is faster than an if statement

**Answer:** B

---

**Q2 (Short Answer).** What semaphore function decrements the counter and blocks if the counter is zero?

**Answer:** sem_wait()

---

**Q3 (Multiple Choice).** A semaphore is initialized with a value of 1. What synchronization primitive does it behave like?

- A) A condition variable
- B) A reader-writer lock
- C) A mutex
- D) A barrier

**Answer:** C

---

**Q4 (Multiple Choice).** In the producer-consumer problem using condition variables, the producer signals `not_empty` after inserting an item. What does the consumer signal after removing an item?

- A) not_empty
- B) not_full
- C) mutex
- D) done

**Answer:** B

---

## Module 6, Lesson 6: Classic Concurrency Problems

**Q1 (Multiple Choice).** In the Dining Philosophers problem with 5 philosophers, the naive solution (each philosopher picks up their left fork then their right fork) can deadlock. What is the deadlock scenario?

- A) All 5 philosophers pick up their left fork simultaneously and then all wait for their right fork
- B) One philosopher picks up both forks and never puts them down
- C) Two adjacent philosophers grab the same fork at the same time
- D) The operating system kills one of the threads

**Answer:** A

---

**Q2 (Short Answer).** In the resource ordering solution to the Dining Philosophers problem, what rule do all philosophers follow when picking up forks?

**Answer:** lower-numbered fork first

---

**Q3 (Multiple Choice).** In the Reader-Writer problem, which statement is correct about the access rules?

- A) Only one reader can read at a time
- B) Multiple writers can write simultaneously if no readers are active
- C) Multiple readers can read simultaneously, but writers need exclusive access
- D) Readers and writers can access the data simultaneously as long as a mutex is held

**Answer:** C

---

**Q4 (Short Answer).** In a reader-preference solution to the Reader-Writer problem, which type of thread can potentially starve because new readers keep arriving?

**Answer:** writers

---

## Module 6 Quiz

**Q1 (Multiple Choice).** Which of the following is PRIVATE to each thread (not shared with other threads in the same process)?

- A) Global variables
- B) Heap memory allocated with malloc
- C) The stack
- D) Open file descriptors

**Answer:** C

---

**Q2 (Short Answer).** What compiler/linker flag must be used when compiling a C program that uses the pthreads library?

**Answer:** -lpthread

---

**Q3 (Multiple Choice).** A thread function needs to return a computed integer result to the calling thread via pthread_join(). Which approach is correct?

- A) Return the address of a local variable on the thread's stack
- B) Allocate memory with malloc, store the result, and return the pointer
- C) Use printf to print the result
- D) Write the result to stderr

**Answer:** B

---

**Q4 (Multiple Choice).** The operation `counter++` on a shared variable is not thread-safe because it is:

- A) A single atomic operation
- B) A read-modify-write sequence that can be interrupted between steps
- C) A write-only operation
- D) Protected by the compiler automatically

**Answer:** B

---

**Q5 (Short Answer).** What term describes the situation where two or more threads are each waiting for a lock held by the other, so none can make progress?

**Answer:** deadlock

---

**Q6 (Multiple Choice).** Which of the following correctly describes the behavior of pthread_cond_wait(&cond, &mutex)?

- A) It locks the mutex, then waits on the condition variable
- B) It atomically releases the mutex and blocks on the condition variable; upon return, the mutex is re-acquired
- C) It destroys the condition variable and unlocks the mutex
- D) It signals the condition variable and locks the mutex

**Answer:** B

---

**Q7 (Short Answer).** In the pthreads semaphore API, what function increments the semaphore counter and potentially wakes a waiting thread?

**Answer:** sem_post()

---

**Q8 (Multiple Choice).** In the bounded-buffer producer-consumer problem using semaphores, three semaphores are used: empty (initialized to BUFFER_SIZE), full (initialized to 0), and mutex (initialized to 1). What does the `empty` semaphore count?

- A) The number of items in the buffer
- B) The number of empty slots available in the buffer
- C) The number of producer threads
- D) The number of consumer threads waiting

**Answer:** B

---

**Q9 (Multiple Choice).** What is the most practical strategy to prevent deadlock when a program must acquire multiple mutexes?

- A) Use only one thread so deadlock is impossible
- B) Always acquire locks in a consistent global order
- C) Declare all mutexes as volatile
- D) Use sleep() to reduce contention

**Answer:** B

---

**Q10 (Short Answer).** What pthreads type provides a built-in reader-writer lock, allowing multiple concurrent readers or one exclusive writer?

**Answer:** pthread_rwlock_t

---

**Q11 (Multiple Choice).** In the Dining Philosophers problem with 5 philosophers and 5 forks, one deadlock prevention strategy uses a semaphore initialized to 4. What does this semaphore control?

- A) The number of forks available
- B) The maximum number of philosophers that can attempt to pick up forks at the same time
- C) The number of meals each philosopher eats
- D) The number of threads the OS can schedule

**Answer:** B

---

**Q12 (Multiple Choice).** Consider this thread code:

```c
pthread_mutex_lock(&lock);
if (error_condition) {
    return NULL;
}
/* do work */
pthread_mutex_unlock(&lock);
```

What bug does this code contain?

- A) The mutex is initialized incorrectly
- B) The mutex is never locked
- C) The mutex is not unlocked before returning in the error case, causing other threads to block forever
- D) The mutex should be a semaphore instead

**Answer:** C

---

## Module 7, Lesson 1: File Descriptors and Low-Level I/O

**Q1 (Multiple Choice).** Every process starts with three file descriptors already open. What are their numbers and purposes?

- A) 0 = stdout, 1 = stdin, 2 = stderr
- B) 0 = stdin, 1 = stdout, 2 = stderr
- C) 1 = stdin, 2 = stdout, 3 = stderr
- D) 0 = stdin, 1 = stderr, 2 = stdout

**Answer:** B

---

**Q2 (Short Answer).** What value does `open()` return on failure?

**Answer:** -1

---

**Q3 (Multiple Choice).** Which combination of flags would you pass to `open()` to create a new file for writing, erasing any existing contents?

- A) `O_RDONLY | O_CREAT`
- B) `O_WRONLY | O_CREAT | O_TRUNC`
- C) `O_WRONLY | O_APPEND`
- D) `O_RDWR | O_TRUNC`

**Answer:** B

---

**Q4 (Short Answer).** When `read()` returns 0, what does that indicate?

**Answer:** end of file (EOF)

---

## Module 7, Lesson 2: The FILE API and Directories

**Q1 (Multiple Choice).** Why is the buffered FILE* API (e.g., `fgetc()`) generally faster than calling `read(fd, &ch, 1)` repeatedly?

- A) `fgetc()` uses a faster CPU instruction than `read()`
- B) `fgetc()` reads a large chunk into an internal buffer with a single `read()` system call and serves subsequent requests from the buffer
- C) `fgetc()` bypasses the kernel entirely
- D) `fgetc()` compresses the data before reading it

**Answer:** B

---

**Q2 (Short Answer).** What function forces buffered output to be written to the underlying file descriptor immediately?

**Answer:** fflush()

---

**Q3 (Multiple Choice).** Which set of functions is used to iterate over directory entries in C?

- A) `fopen()` / `fgets()` / `fclose()`
- B) `opendir()` / `readdir()` / `closedir()`
- C) `open()` / `read()` / `close()`
- D) `scandir()` / `seekdir()` / `rewinddir()`

**Answer:** B

---

**Q4 (Short Answer).** What macro do you use to test whether a file's `st_mode` (from `stat()`) indicates a regular file?

**Answer:** S_ISREG()

---

## Module 7, Lesson 3: TCP/IP and Socket Basics

**Q1 (Multiple Choice).** Which of the following is NOT a property of TCP?

- A) Reliable delivery (retransmits lost packets)
- B) Ordered delivery (bytes arrive in order)
- C) Message boundaries (each send is a discrete message)
- D) Connection-oriented (requires a handshake)

**Answer:** C

---

**Q2 (Short Answer).** What function converts a 16-bit port number from host byte order to network byte order?

**Answer:** htons()

---

**Q3 (Multiple Choice).** A network connection is uniquely identified by a 4-tuple. What are its components?

- A) Source MAC, destination MAC, source IP, destination IP
- B) Source IP, source port, destination IP, destination port
- C) Protocol, source IP, destination IP, port
- D) Source IP, destination IP, subnet mask, gateway

**Answer:** B

---

**Q4 (Short Answer).** What value do you set `sin_family` to in a `struct sockaddr_in` for IPv4?

**Answer:** AF_INET

---

## Module 7, Lesson 4: Building a Server

**Q1 (Multiple Choice).** What is the correct order of system calls for a TCP server?

- A) `bind()`, `socket()`, `listen()`, `accept()`
- B) `socket()`, `listen()`, `bind()`, `accept()`
- C) `socket()`, `bind()`, `listen()`, `accept()`
- D) `socket()`, `connect()`, `listen()`, `accept()`

**Answer:** C

---

**Q2 (Short Answer).** What socket option should you set before `bind()` to allow immediate port reuse after a server restarts?

**Answer:** SO_REUSEADDR

---

**Q3 (Multiple Choice).** When `accept()` successfully returns, what does the return value represent?

- A) The number of bytes available to read
- B) A new file descriptor for the specific client connection
- C) The original listening socket's file descriptor
- D) The client's port number

**Answer:** B

---

**Q4 (Short Answer).** What arguments do you pass to `socket()` to create a TCP socket over IPv4?

**Answer:** AF_INET, SOCK_STREAM, 0

---

## Module 7, Lesson 5: Clients and Multi-Client Servers

**Q1 (Multiple Choice).** A TCP client's lifecycle differs from a server's. Which system calls does a client NOT need to make?

- A) `socket()` and `close()`
- B) `bind()` and `listen()`
- C) `read()` and `write()`
- D) `connect()` and `close()`

**Answer:** B

---

**Q2 (Short Answer).** In a threaded server, why must the client file descriptor be passed to the handler thread via a heap-allocated pointer rather than a pointer to a stack variable?

**Answer:** race condition

---

**Q3 (Multiple Choice).** In the threaded echo server, after calling `pthread_create()` for a new client handler, the main thread calls `pthread_detach(tid)`. What does this accomplish?

- A) It forces the thread to terminate immediately
- B) It allows the thread's resources to be automatically reclaimed when it finishes, without requiring `pthread_join()`
- C) It prevents the thread from accessing shared memory
- D) It moves the thread to a different process

**Answer:** B

---

**Q4 (Short Answer).** In a server using `fork()` instead of threads, both parent and child have copies of the client file descriptor. How many processes must close the client file descriptor?

**Answer:** both

---

## Module 7, Lesson 6: From Echo Server to Web Server

**Q1 (Multiple Choice).** An HTTP request line has three components. What are they?

- A) Status code, reason phrase, version
- B) Method, path, version
- C) Host, port, path
- D) Version, content-type, content-length

**Answer:** B

---

**Q2 (Short Answer).** What HTTP status code indicates that the requested file was not found?

**Answer:** 404

---

**Q3 (Multiple Choice).** In the minimal web server, what function is used to get the file's size for the `Content-Length` header?

- A) `fread()`
- B) `strlen()`
- C) `stat()`
- D) `sizeof()`

**Answer:** C

---

**Q4 (Short Answer).** What is the correct `Content-Type` header value for an HTML file?

**Answer:** text/html

---

## Module 7 Quiz

**Q1 (Multiple Choice).** In Unix, when a process opens its first file (after the three standard streams), what file descriptor number will it typically receive?

- A) 0
- B) 1
- C) 3
- D) 10

**Answer:** C

---

**Q2 (Short Answer).** What header file must you include to use `open()` in C?

**Answer:** fcntl.h

---

**Q3 (Multiple Choice).** A program reads a file one byte at a time using `read(fd, &ch, 1)`. Another version uses `fgetc()` with a `FILE*`. Why is the `fgetc()` version significantly faster?

- A) `fgetc()` uses DMA to bypass the CPU
- B) `fgetc()` reads a large block into a user-space buffer with one system call and serves individual bytes from the buffer
- C) `fgetc()` does not actually read from disk
- D) `read()` always reads the entire file into memory first

**Answer:** B

---

**Q4 (Multiple Choice).** Which transport layer protocol provides reliable, ordered, byte-stream delivery?

- A) UDP
- B) IP
- C) TCP
- D) HTTP

**Answer:** C

---

**Q5 (Short Answer).** What special IP address means "the local machine" (loopback) in IPv4?

**Answer:** 127.0.0.1

---

**Q6 (Multiple Choice).** You write 500 bytes to a TCP socket with a single `write()` call. How might the receiver's `read()` calls return those bytes?

- A) Exactly one `read()` returning 500 bytes, guaranteed
- B) Any combination of `read()` calls whose byte counts sum to 500
- C) Exactly 500 `read()` calls of 1 byte each
- D) Two `read()` calls of 250 bytes each

**Answer:** B

---

**Q7 (Short Answer).** In the server socket lifecycle, which system call marks a socket as passive (willing to accept incoming connections)?

**Answer:** listen()

---

**Q8 (Multiple Choice).** A threaded server passes `&client_fd` (a stack variable) to `pthread_create()`, where `client_fd` is reassigned on the next loop iteration. What kind of bug does this introduce?

- A) Memory leak
- B) Deadlock
- C) Race condition
- D) Stack overflow

**Answer:** C

---

**Q9 (Short Answer).** In an HTTP response, what does the `Content-Length` header specify?

**Answer:** size of the body in bytes

---

**Q10 (Multiple Choice).** The web server checks for `..` in the requested file path. What attack does this prevent?

- A) SQL injection
- B) Cross-site scripting
- C) Directory traversal
- D) Buffer overflow

**Answer:** C

---

**Q11 (Short Answer).** What function converts a human-readable IP address string (e.g., "192.168.1.1") into binary network format suitable for `struct sockaddr_in`?

**Answer:** inet_pton()

---

**Q12 (Multiple Choice).** Which field of `struct dirent` contains the name of a directory entry?

- A) `d_ino`
- B) `d_name`
- C) `d_type`
- D) `d_off`

**Answer:** B

---

## Module 8, Lesson 1: Random Access Memory (RAM)

**Q1 (Multiple Choice).** SRAM uses 6 transistors per bit and is used in CPU caches, while DRAM uses a capacitor and a single transistor. Which correctly describes why DRAM requires periodic refreshing but SRAM does not?

- A) DRAM transistors degrade over time and must be replaced
- B) DRAM stores bits as charge on capacitors, which leak over time; SRAM uses a bistable circuit that holds its state as long as power is supplied
- C) DRAM operates at a lower voltage and loses state more easily
- D) SRAM is refreshed automatically by the CPU pipeline

**Answer:** B

---

**Q2 (Short Answer).** What type of RAM is used for CPU caches (L1, L2, L3)?

**Answer:** SRAM

---

**Q3 (Multiple Choice).** The CPU communicates with memory through the memory bus. Which of the following is NOT one of the three logical parts of the memory bus?

- A) Address bus
- B) Data bus
- C) Control bus
- D) Cache bus

**Answer:** D

---

**Q4 (Short Answer).** What is the term for the growing disparity between CPU speed and memory access speed that motivates the memory hierarchy?

**Answer:** processor-memory gap

---

## Module 8, Lesson 2: Locality

**Q1 (Multiple Choice).** Which of the following best describes temporal locality?

- A) Accessing memory locations that are physically close together on the DRAM chip
- B) A memory location that was recently accessed will most likely be accessed again soon
- C) A memory location that was recently accessed will most likely have nearby memory locations accessed soon
- D) Accessing memory in the same order it was allocated

**Answer:** B

---

**Q2 (Short Answer).** In C, iterating over a 2D array with the column index varying in the inner loop (e.g., `a[i][j]` where `j` is the inner loop variable) produces what stride pattern?

**Answer:** stride-1

---

**Q3 (Multiple Choice).** Consider summing a 2D array. Version 1 uses row-major traversal (inner loop varies `j`) and Version 2 uses column-major traversal (inner loop varies `i`). For large N, which statement is true?

- A) Both versions have the same performance because they do the same number of additions
- B) Version 2 is faster because column access has better temporal locality
- C) Version 1 can be 5-20 times faster than Version 2 due to better spatial locality
- D) Version 1 is slower because it accesses memory sequentially

**Answer:** C

---

**Q4 (Short Answer).** What is the general rule relating stride size to spatial locality?

**Answer:** smaller stride means better spatial locality

---

## Module 8, Lesson 3: Memory Caches

**Q1 (Multiple Choice).** When the CPU needs a value and that value is found in one of the caches, this is called a ___. When the value must be fetched from RAM, it is called a ___.

- A) page hit; page miss
- B) hit; miss
- C) fetch; stall
- D) load; store

**Answer:** B

---

**Q2 (Short Answer).** What is the typical size of a cache line on modern CPUs?

**Answer:** 64 bytes

---

**Q3 (Multiple Choice).** In a direct-mapped cache, two different memory blocks that map to the same cache line cause one to evict the other. What is this type of miss called?

- A) Cold miss
- B) Capacity miss
- C) Conflict miss
- D) Compulsory miss

**Answer:** C

---

**Q4 (Multiple Choice).** A write-back cache policy waits until a cache line is evicted before writing modified data to main memory. What mechanism does the cache use to know whether a line has been modified?

- A) A tag bit
- B) A valid bit
- C) A dirty bit
- D) A reference counter

**Answer:** C

---

## Module 8, Lesson 4: Optimization - Why and When?

**Q1 (Multiple Choice).** According to Amdahl's Law, if 80% of a program's runtime is in a single function and you make that function 4x faster, what is the overall speedup?

- A) 4.0x
- B) 3.2x
- C) 2.5x
- D) 1.25x

**Answer:** C

---

**Q2 (Short Answer).** What is the first step in the recommended optimization workflow, before any profiling or performance tuning?

**Answer:** write correct code first

---

**Q3 (Multiple Choice).** The "90/10 rule" in optimization refers to which observation?

- A) 90% of bugs are found in the first 10% of testing
- B) Roughly 90% of execution time is spent in 10% of the code
- C) Optimized code runs 90% faster 10% of the time
- D) 90% of optimizations are applied at compile time

**Answer:** B

---

**Q4 (Short Answer).** Who is credited with the quote "premature optimization is the root of all evil"?

**Answer:** Donald Knuth

---

## Module 8, Lesson 5: gcc Optimization Levels and Limitations

**Q1 (Multiple Choice).** What is the standard industry optimization level for production builds with gcc?

- A) -O0
- B) -O1
- C) -O2
- D) -O3

**Answer:** C

---

**Q2 (Short Answer).** What is the term for the situation where two pointers might point to the same memory location, preventing the compiler from optimizing?

**Answer:** memory aliasing

---

**Q3 (Multiple Choice).** Consider the following two functions:

```c
void twiddle1(long *xp, long *yp) {
    *xp += *yp;
    *xp += *yp;
}

void twiddle2(long *xp, long *yp) {
    *xp += 2*(*yp);
}
```

Why doesn't gcc optimize `twiddle1` into `twiddle2`?

- A) The multiplication in `twiddle2` is slower than two additions
- B) `xp` and `yp` could point to the same memory location, making the two functions produce different results
- C) gcc never optimizes pointer arithmetic
- D) The two functions always produce the same result, but gcc has a bug

**Answer:** B

---

**Q4 (Short Answer).** What gcc flag is used to compile code for easier debugging, producing assembly that closely follows the C source?

**Answer:** -Og

---

## Module 8, Lesson 6: How to Measure Performance

**Q1 (Multiple Choice).** When you run `time ./program` and see `real 0m5.2s`, `user 0m4.8s`, `sys 0m0.3s`, what does the `user` time represent?

- A) The total wall-clock time from start to finish
- B) The CPU time spent executing the program's own code in user mode
- C) The time the program spent waiting for user input
- D) The CPU time spent in the kernel on behalf of the program

**Answer:** B

---

**Q2 (Short Answer).** What gcc flag must be used to enable profiling instrumentation for use with gprof?

**Answer:** -pg

---

**Q3 (Multiple Choice).** When benchmarking a program, you should run it multiple times. Which measurement should you typically record?

- A) The maximum runtime
- B) The average runtime
- C) The minimum runtime
- D) The median runtime

**Answer:** C

---

**Q4 (Short Answer).** What does CPE stand for, as used in the textbook to measure code efficiency?

**Answer:** cycles per element

---

## Module 8, Lesson 7: How to Optimize Code

**Q1 (Multiple Choice).** What is wrong with the following loop, and why does it cause a severe performance problem?

```c
for (int i = 0; i < strlen(str); i++) { ... }
```

- A) `strlen` returns a `size_t`, which is incompatible with `int i`
- B) `strlen` is called on every iteration, scanning the entire string each time, making the loop O(n^2) instead of O(n)
- C) `strlen` modifies the string, causing undefined behavior
- D) The loop will run one iteration too many because `strlen` includes the null terminator

**Answer:** B

---

**Q2 (Short Answer).** In the notation "5 x 2 loop unrolling," what do the numbers 5 and 2 represent?

**Answer:** 5 iterations per loop pass and 2 accumulators

---

**Q3 (Multiple Choice).** Why does using a local accumulator variable instead of writing directly through a pointer improve performance?

- A) Local variables are allocated on the heap, which is faster
- B) Local variables can be kept in registers, avoiding repeated memory reads and writes
- C) The pointer version causes compiler errors
- D) Local variables use less stack space

**Answer:** B

---

**Q4 (Short Answer).** In C, two-dimensional arrays are stored in memory in what order?

**Answer:** row-major order

---

## Module 8, Lesson 8: Cache-Aware Programming

**Q1 (Multiple Choice).** Loop tiling (blocking) improves cache performance for matrix multiplication by:

- A) Reducing the total number of arithmetic operations
- B) Breaking the computation into small sub-blocks that fit in the cache, so data is reused before being evicted
- C) Converting column-major access to row-major access
- D) Using SIMD instructions to process multiple elements at once

**Answer:** B

---

**Q2 (Short Answer).** When organizing data for a computation that iterates over all particles but only accesses x-coordinates, which data layout provides better spatial locality: Array of Structures (AoS) or Structure of Arrays (SoA)?

**Answer:** Structure of Arrays

---

**Q3 (Multiple Choice).** Consider this struct:

```c
struct Example {
    char  a;     // 1 byte
    int   b;     // 4 bytes
    char  c;     // 1 byte
    double d;    // 8 bytes
};
```

Due to alignment padding, the total size of this struct is 24 bytes instead of 14. Which reordering of the fields would minimize padding?

- A) `char a; char c; int b; double d;`
- B) `double d; int b; char a; char c;`
- C) `int b; double d; char a; char c;`
- D) `char a; double d; char c; int b;`

**Answer:** B

---

**Q4 (Short Answer).** A data value is naturally aligned when its memory address is a multiple of its size. At what byte boundary must a `double` (8 bytes) be aligned?

**Answer:** 8-byte boundary

---

## Module 8 Quiz

**Q1 (Multiple Choice).** DRAM stores each bit as a charge on a tiny capacitor paired with a single transistor. Approximately how many transistors per bit does SRAM use?

- A) 1
- B) 2
- C) 4
- D) 6

**Answer:** D

---

**Q2 (Short Answer).** What is the approximate access time range for DRAM in nanoseconds?

**Answer:** 50-100 nanoseconds

---

**Q3 (Multiple Choice).** A program contains the following loop:

```c
int sum = 0;
for (int i = 0; i < n; i++)
    sum += a[i];
```

Which variable exhibits the best temporal locality?

- A) `a[i]` because each array element is accessed once
- B) `sum` because it is read and written on every iteration
- C) `n` because it never changes
- D) `i` because it increments predictably

**Answer:** B

---

**Q4 (Multiple Choice).** Which cache mapping scheme allows a memory block to be placed in any cache line, but is rarely used due to the cost of searching the entire cache?

- A) Direct-mapped
- B) Set associative
- C) Fully associative
- D) Write-through

**Answer:** C

---

**Q5 (Short Answer).** In a write-back cache, what bit is used to track whether a cache line has been modified and needs to be written to main memory when evicted?

**Answer:** dirty bit

---

**Q6 (Multiple Choice).** According to Amdahl's Law, if you optimize a function that accounts for only 5% of a program's total runtime, what is the maximum possible overall speedup, regardless of how fast you make that function?

- A) 5%
- B) 20%
- C) 50%
- D) 95%

**Answer:** A

---

**Q7 (Short Answer).** What is the standard industry gcc optimization flag for production builds?

**Answer:** -O2

---

**Q8 (Multiple Choice).** The function `f()` is defined in a separate file and uses a global counter. Why won't gcc optimize `f() + f() + f() + f()` into `4 * f()`?

- A) gcc cannot perform multiplication on function return values
- B) The function may have side effects, causing each call to return a different value
- C) gcc always inlines functions from other files
- D) Addition is faster than multiplication on modern CPUs

**Answer:** B

---

**Q9 (Multiple Choice).** When using the `time` command, a CPU-bound program will typically show which relationship between the output fields?

- A) `real` >> `user + sys`
- B) `user` approximately equals `real`
- C) `sys` >> `user`
- D) `real` equals exactly `user + sys`

**Answer:** B

---

**Q10 (Short Answer).** What profiler, available on Linux systems, requires compiling with the `-pg` flag and produces output to a file called `gmon.out`?

**Answer:** gprof

---

**Q11 (Multiple Choice).** Putting `strlen(str)` directly in the condition of a for loop that iterates over a string of length N causes the loop to effectively perform how many total character inspections?

- A) N
- B) 2N
- C) N log N
- D) N^2

**Answer:** D

---

**Q12 (Multiple Choice).** In a blocked (tiled) matrix multiplication with block size B, how should B be chosen?

- A) B should equal the matrix dimension N
- B) B should be chosen so that three B x B sub-matrices fit in the L1 data cache
- C) B should always be 2 for maximum loop unrolling
- D) B should equal the cache line size in bytes

**Answer:** B

---

**Q13 (Short Answer).** When a program accesses column 0 of a row-major 2D array with N columns by iterating over rows, what is the stride of that access pattern?

**Answer:** stride-N

---

**Q14 (Multiple Choice).** A struct has fields ordered `char, int, char, double` and takes 24 bytes due to padding. After reordering to `double, int, char, char`, the struct takes only 16 bytes. What general rule for field ordering minimizes padding?

- A) Alphabetical order
- B) Order fields from smallest to largest
- C) Order fields from largest to smallest
- D) Group all pointer fields together

**Answer:** C

---

**Q15 (Multiple Choice).** Which of the following is NOT a valid reason to skip optimizing a program?

- A) The program already runs fast enough for the user's needs
- B) The program produces incorrect output and needs debugging first
- C) A profiler shows that 78% of time is spent in one function
- D) The optimization would make the code much harder to maintain for a negligible speed gain

**Answer:** C

---

## Module 9, Lesson 1: Virtual Memory

**Q1 (Multiple Choice).** What hardware component translates virtual addresses to physical addresses before a memory access proceeds?

- A) The ALU (Arithmetic Logic Unit)
- B) The TLB (Translation Lookaside Buffer)
- C) The MMU (Memory Management Unit)
- D) The CPU cache controller

**Answer:** C

---

**Q2 (Short Answer).** On a system with 4 KB pages, how many bits of a virtual address are used for the page offset?

**Answer:** 12 bits

---

**Q3 (Multiple Choice).** A program accesses a virtual page whose valid bit in the page table entry is 0. What happens next?

- A) The MMU returns a zero value to the CPU
- B) The access proceeds using the physical page number stored in the PTE
- C) A page fault exception is triggered and the OS page fault handler runs
- D) The TLB is flushed and the access is retried

**Answer:** C

---

**Q4 (Short Answer).** What is the term for the condition where the system is constantly swapping pages in and out because the working sets of all active processes exceed physical memory?

**Answer:** thrashing

---

## Module 9, Lesson 2: Static and Dynamic Linking

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

**Answer:** B

---

**Q2 (Short Answer).** In the linker's symbol resolution rules, what is the difference between a "strong" symbol and a "weak" symbol? Give an example of each in C.

**Answer:** A strong symbol is a function or an initialized global variable (e.g., `int x = 5;`). A weak symbol is an uninitialized global variable (e.g., `int x;` with `-fcommon`). If the linker finds one strong and one weak with the same name, the strong symbol wins.

---

**Q3 (Multiple Choice).** A statically linked "Hello, World" program is ~900 KB, while the dynamically linked version is ~16 KB. Why is the static version so much larger?

- A) The static version includes debug symbols; the dynamic version does not
- B) The static version includes a copy of the entire C library in the executable
- C) The dynamic version is compressed
- D) The static version includes the Linux kernel

**Answer:** B

---

**Q4 (Short Answer).** Briefly explain the role of the PLT and GOT in dynamic linking.

**Answer:** The PLT (Procedure Linkage Table) contains code stubs per external function. The GOT (Global Offset Table) stores runtime addresses. On first call, the PLT invokes the dynamic linker to fill the GOT; subsequent calls read directly from the GOT.

---

## Module 9, Lesson 3: Dynamic Memory Allocation

**Q1 (Multiple Choice).** Which function allocates memory for an array and initializes all bytes to zero?

- A) `malloc()`
- B) `realloc()`
- C) `calloc()`
- D) `free()`

**Answer:** C

---

**Q2 (Short Answer).** In the malloc implementation, what data structure maintains the list of available (unallocated) blocks on the heap?

**Answer:** free list

---

**Q3 (Multiple Choice).** A heap has three free blocks of 8 bytes each, scattered between allocated blocks. A call to `malloc(20)` fails even though there are 24 bytes of total free memory. What type of fragmentation is this?

- A) Internal fragmentation
- B) External fragmentation
- C) Page fragmentation
- D) Stack fragmentation

**Answer:** B

---

**Q4 (Short Answer).** When a block is freed, the allocator checks whether adjacent blocks are also free and merges them into a single larger block. What is this process called?

**Answer:** coalescing

---

## Module 9, Lesson 4: Debugging Memory Errors with Valgrind

**Q1 (Multiple Choice).** Valgrind reports: `Invalid read of size 4` at line 8, and says the address is `0 bytes inside a block of size 4 free'd` at line 7. What type of memory error is this?

- A) Buffer overflow
- B) Memory leak
- C) Use after free (dangling pointer)
- D) Double free

**Answer:** C

---

**Q2 (Short Answer).** What compiler flag must you use when compiling a program so that Valgrind can report source file names and line numbers?

**Answer:** -g

---

**Q3 (Multiple Choice).** You run `valgrind --leak-check=full ./myprogram` and the leak summary shows "definitely lost: 400 bytes in 1 blocks" and "indirectly lost: 200 bytes in 5 blocks." What does "indirectly lost" mean?

- A) Memory that was freed twice
- B) Memory that is only reachable through a "definitely lost" block
- C) Memory that was allocated by the operating system, not by the program
- D) Memory that was corrupted by a buffer overflow

**Answer:** B

---

**Q4 (Short Answer).** What Valgrind flag do you use to trace an uninitialized value back to the allocation where it originated?

**Answer:** --track-origins=yes

---

## Module 9, Lesson 5: Garbage Collection

**Q1 (Multiple Choice).** Object A points to object B, and object B points back to object A. No other references to A or B exist. Which garbage collection technique will fail to reclaim this memory?

- A) Mark-and-sweep
- B) Reference counting (without a cycle detector)
- C) Generational GC
- D) Copying collector

**Answer:** B

---

**Q2 (Short Answer).** Explain the two phases of mark-and-sweep garbage collection.

**Answer:** In the mark phase, the collector starts from roots (stack, globals, registers) and marks all reachable objects. In the sweep phase, it walks the heap and frees any unmarked object.

---

**Q3 (Multiple Choice).** Why can't C use a moving/compacting garbage collector?

- A) C programs are too slow for garbage collection
- B) C does not have a heap
- C) C allows raw pointer arithmetic, so the runtime cannot find and update all pointers to a moved object
- D) Moving objects would change their hash codes

**Answer:** C

---

**Q4 (Short Answer).** The generational hypothesis states that "most objects die young." How does a generational garbage collector exploit this observation?

**Answer:** It divides the heap into young and old generations, collects the young generation frequently (fast, since most are dead), and promotes survivors to the old generation which is collected rarely.

---

## Module 9 Quiz

**Q1 (Multiple Choice).** Every pointer value you see in a C program is a:

- A) Physical address
- B) Virtual address
- C) Segment offset
- D) Cache line address

**Answer:** B

---

**Q2 (Short Answer).** What is the typical size of a virtual memory page on most modern systems?

**Answer:** 4 KB

---

**Q3 (Multiple Choice).** Which of the following is NOT stored in a page table entry (PTE)?

- A) Valid bit
- B) Physical page number
- C) Permission bits (read/write/execute)
- D) The process's PID

**Answer:** D

---

**Q4 (Multiple Choice).** In static linking, what is a `.a` file?

- A) An assembly source file
- B) An archive (collection) of `.o` object files
- C) A shared object loaded at runtime
- D) An ASLR configuration file

**Answer:** B

---

**Q5 (Short Answer).** In dynamic linking, what command shows which shared libraries an executable depends on?

**Answer:** ldd

---

**Q6 (Multiple Choice).** A program calls `malloc(20)` and receives a 32-byte block due to alignment requirements. The 12 unused bytes inside the allocated block are an example of:

- A) External fragmentation
- B) Internal fragmentation
- C) A memory leak
- D) A buffer overflow

**Answer:** B

---

**Q7 (Short Answer).** What value does `malloc()` return if the memory allocation fails?

**Answer:** NULL

---

**Q8 (Multiple Choice).** You run Valgrind and see: `Invalid write of size 4` at a line containing `arr[i] = value;`, and "Address is 0 bytes after a block of size 20 alloc'd." What kind of bug is this?

- A) Use after free
- B) Memory leak
- C) Heap buffer overflow (writing past the end of an allocated block)
- D) Double free

**Answer:** C

---

**Q9 (Multiple Choice).** Which garbage collection technique cannot reclaim memory involved in a reference cycle (without an additional cycle detector)?

- A) Mark-and-sweep
- B) Reference counting
- C) Copying collector
- D) Generational GC

**Answer:** B

---

**Q10 (Short Answer).** In mark-and-sweep garbage collection, what are the three types of roots that the mark phase starts from?

**Answer:** stack variables, global/static variables, CPU registers

---

**Q11 (Multiple Choice).** Why can't C use a compacting or moving garbage collector to eliminate external fragmentation?

- A) C does not support heap allocation
- B) C programs run too slowly for compaction
- C) C allows raw pointer arithmetic, so the runtime cannot reliably find and update all pointers to a moved object
- D) The C standard forbids garbage collection

**Answer:** C

---

**Q12 (Multiple Choice).** A process tries to access a virtual address that is in the kernel space region. What happens?

- A) The access succeeds because the kernel space is always mapped
- B) A page fault loads the kernel page into the process's address space
- C) A segmentation fault (SIGSEGV) occurs and the process is typically terminated
- D) The TLB redirects the access to physical memory

**Answer:** C

---

## Module 10, Lesson 1: What a Kernel Does

**Q1 (Multiple Choice).** When a user program executes the `syscall` instruction on x86-64 Linux, what happens to the CPU's privilege level?

- A) It remains in ring 3 (user mode)
- B) It switches from ring 0 (kernel mode) to ring 3 (user mode)
- C) It switches from ring 3 (user mode) to ring 0 (kernel mode)
- D) It switches from ring 3 to ring 1

**Answer:** C

---

**Q2 (Short Answer).** On x86-64 Linux, in which CPU register does the C library wrapper place the system call number before executing the `syscall` instruction?

**Answer:** %rax

---

**Q3 (Multiple Choice).** During a context switch on Linux, the kernel saves all register values and memory mapping information into a per-process data structure. What is this data structure called?

- A) Process table entry
- B) Task struct
- C) Page table
- D) System call table

**Answer:** B

---

**Q4 (Short Answer).** What is the name of the default process scheduler used in the Linux kernel?

**Answer:** Completely Fair Scheduler

---

## Module 10, Lesson 2: Monolithic Kernels

**Q1 (Multiple Choice).** In a monolithic kernel, how do internal subsystems communicate with each other?

- A) Through IPC message passing via ports
- B) Through direct function calls within the same address space
- C) Through shared files on disk
- D) Through user-space library wrappers

**Answer:** B

---

**Q2 (Short Answer).** What single category of code accounts for more than half of the total Linux kernel codebase (over 15 million lines)?

**Answer:** device drivers

---

**Q3 (Multiple Choice).** Loadable kernel modules (LKMs) in Linux allow code to be loaded into the running kernel at runtime. Which statement about LKMs is TRUE?

- A) A loaded module runs in user mode (ring 3) for safety
- B) A loaded module is isolated from the rest of the kernel and cannot corrupt kernel memory
- C) A loaded module runs in kernel mode (ring 0) with full access to all kernel data structures
- D) A loaded module cannot be removed once loaded without rebooting

**Answer:** C

---

**Q4 (Short Answer).** What is the term for the kernel equivalent of a crash, where the system halts because it can no longer trust its own state?

**Answer:** kernel panic

---

## Module 10, Lesson 3: Microkernel Architectures

**Q1 (Multiple Choice).** Which of the following services does a microkernel typically provide directly?

- A) File systems, device drivers, and networking
- B) IPC, minimal process/thread management, and minimal memory management
- C) TCP/IP networking stack and socket management
- D) Device drivers and the Virtual File System (VFS) layer

**Answer:** B

---

**Q2 (Short Answer).** What is the name of the microkernel that has been formally verified -- mathematically proven to match its specification?

**Answer:** seL4

---

**Q3 (Multiple Choice).** Jochen Liedtke's L4 microkernel achieved IPC performance approximately how many times faster than the Mach microkernel?

- A) 2 times faster
- B) 5 times faster
- C) 20 times faster
- D) 100 times faster

**Answer:** C

---

**Q4 (Short Answer).** In MINIX 3, what is the name of the component that detects when a device driver has crashed and automatically restarts it?

**Answer:** reincarnation server

---

## Module 10, Lesson 4: Tradeoffs and Modern Approaches

**Q1 (Multiple Choice).** Apple's XNU kernel is considered a hybrid because it combines which two major components?

- A) The L4 microkernel and Linux networking code
- B) The Mach microkernel and BSD (FreeBSD) code running together in kernel space
- C) The QNX Neutrino microkernel and Windows NT executive
- D) The seL4 verified microkernel and MINIX drivers

**Answer:** B

---

**Q2 (Short Answer).** What type of kernel architecture compiles an application and the OS libraries it needs into a single binary that runs directly on hardware or a hypervisor, with no user/kernel separation?

**Answer:** unikernel

---

**Q3 (Multiple Choice).** Which Linux technology allows users to load small, verified programs into the kernel that run safely in a sandboxed environment?

- A) Loadable kernel modules (LKMs)
- B) Docker containers
- C) eBPF
- D) Seccomp-BPF

**Answer:** C

---

**Q4 (Short Answer).** What programming language has the Linux kernel begun accepting (starting in 2022) alongside C, whose type system and ownership model prevent memory-safety bugs at compile time?

**Answer:** Rust

---

## Module 10 Quiz

**Q1 (Multiple Choice).** What hardware mechanism prevents user-mode programs from executing privileged instructions or accessing kernel memory?

- A) The system call table
- B) CPU privilege levels (protection rings)
- C) The process scheduler
- D) Virtual file system abstraction

**Answer:** B

---

**Q2 (Short Answer).** In a monolithic kernel like Linux, how many mode switches (user-to-kernel and back) are required for a file read operation?

**Answer:** 2

---

**Q3 (Multiple Choice).** Which of the following is a major disadvantage of the monolithic kernel design?

- A) Slow communication between kernel subsystems due to IPC overhead
- B) A bug in any kernel component (such as a device driver) can crash the entire system
- C) Inability to support loadable modules at runtime
- D) Very small trusted computing base that limits functionality

**Answer:** B

---

**Q4 (Short Answer).** In a microkernel architecture, device drivers and file systems run as processes in which CPU privilege mode?

**Answer:** user mode

---

**Q5 (Multiple Choice).** A microkernel-based file read requires multiple IPC message exchanges. What is the primary performance concern compared to a monolithic kernel?

- A) The file system server cannot access the disk at all
- B) Each IPC exchange requires mode switches and message copying, adding latency
- C) The microkernel must recompile drivers every time they are used
- D) User-space servers cannot use virtual memory

**Answer:** B

---

**Q6 (Short Answer).** What microkernel-based real-time operating system, now owned by BlackBerry, is widely used in automobiles, medical devices, and nuclear power plants?

**Answer:** QNX

---

**Q7 (Multiple Choice).** Which of the following correctly describes a unikernel?

- A) A kernel that supports exactly one file system type
- B) A single binary combining an application and only the OS components it needs, running without user/kernel separation
- C) A monolithic kernel stripped down to remove unused system calls
- D) A microkernel that has been formally verified

**Answer:** B

---

**Q8 (Multiple Choice).** Docker containers on Linux achieve process isolation using kernel features such as namespaces and cgroups. How does this isolation differ from microkernel-based isolation?

- A) Container isolation is enforced by hardware privilege levels; microkernel isolation is software-only
- B) Container isolation is enforced by kernel software mechanisms; microkernel isolation is enforced by hardware privilege levels separating components into different address spaces
- C) There is no meaningful difference
- D) Container isolation is stronger because Linux is a larger, more tested codebase

**Answer:** B

---

**Q9 (Short Answer).** Approximately how many lines of C code is the seL4 microkernel, which enabled its full formal verification?

**Answer:** 10,000

---

**Q10 (Multiple Choice).** The CHERI hardware research project adds capabilities to pointers checked by the CPU on every memory access. How could this technology affect the monolithic vs. microkernel tradeoff?

- A) It would make microkernels faster by speeding up IPC
- B) It could give monolithic kernels fine-grained, hardware-enforced isolation between components without separate address spaces or IPC overhead
- C) It would eliminate the need for virtual memory entirely
- D) It would make formal verification of Linux feasible

**Answer:** B
