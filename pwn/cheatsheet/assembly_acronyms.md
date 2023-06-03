- What is a stack?
	- This refers to the region of memory used to manage function calls, local variables, and other data within a program's execution.

Here are a few key aspects of the stack in binary exploitation:

1. Stack Layout: The stack is typically organized in a contiguous block of memory. It grows downwards, with the top of the stack being the highest memory address and the bottom of the stack being the lowest memory address. The stack layout consists of stack frames, where each frame corresponds to a function call and holds parameters, local variables, return addresses, and other information.
    
2. Stack Pointer (SP): The stack pointer is a register that points to the top of the stack. It keeps track of the current position within the stack. When a function is called, the stack pointer is adjusted to allocate space for the function's stack frame. As functions return, the stack pointer is readjusted to remove the frame and restore the previous state.
    
3. Function Prologue and Epilogue: When a function is called, it performs a series of operations to set up its stack frame. This is known as the function prologue. It typically involves preserving the previous frame pointer (if applicable), adjusting the stack pointer, and saving any necessary register values. The function epilogue is executed upon return and restores the previous state.
    
4. Local Variables: Local variables of a function are allocated on the stack. They are typically accessed relative to the stack pointer or base pointer (BP). If a buffer or array is allocated on the stack without proper bounds checking, it can be vulnerable to buffer overflow attacks.
    
5. Return Addresses: When a function is called, the address of the instruction following the function call (return address) is pushed onto the stack. This allows the program to resume execution at the appropriate location after the function call completes. Manipulating return addresses is a common technique in exploits, such as overwriting them to redirect program execution.
    
6. Stack Overflows: Stack overflows occur when data is written beyond the allocated buffer space on the stack, leading to potential memory corruption. By overflowing a buffer with carefully crafted input, an attacker can overwrite return addresses, control program flow, and potentially execute arbitrary code.

## Important terms on assembly/binary exp

1. X86: Intel x86
    
    - A popular architecture used in many modern CPUs, known for its CISC (Complex Instruction Set Computer) design.
2. ARM: Advanced RISC Machine
    
    - A widely used architecture known for its RISC (Reduced Instruction Set Computer) design, commonly found in mobile devices and embedded systems.
3. ASLR: Address Space Layout Randomization
    
    - A security technique that randomizes the memory layout of a process to make it harder for attackers to exploit memory vulnerabilities.
4. DEP: Data Execution Prevention
    
    - A security feature that prevents the execution of code from certain memory regions, such as the stack or heap, to mitigate against code injection attacks.
5. ROP: Return-Oriented Programming
    
    - A technique used in exploit development where existing code fragments, known as gadgets, are chained together to execute arbitrary instructions.
6. GOT: Global Offset Table
    
    - A data structure used in compiled programs to support dynamic linking by storing addresses of global variables and functions.
7. PLT: Procedure Linkage Table
    
    - A data structure used in compiled programs to support dynamic function calls by providing a layer of indirection for resolving function addresses.
8. FPU: Floating Point Unit
    
    - A specialized component in CPUs that handles floating-point arithmetic operations.
9. SSE: Streaming SIMD Extensions
    
    - A set of CPU instructions that perform SIMD (Single Instruction, Multiple Data) operations on packed data, often used for multimedia processing and scientific calculations.
10. EIP: Extended Instruction Pointer
    
    - A register in the x86 architecture that holds the memory address of the next instruction to be executed.
11. ESP: Extended Stack Pointer
    
    - A register in the x86 architecture that holds the memory address of the top of the stack.
12. EBP: Extended Base Pointer
    
    - A register in the x86 architecture that is commonly used as a frame pointer for referencing function parameters and local variables on the stack.
13. RAX, RBX, RCX, RDX: General-purpose registers
    
    - Registers in the x86_64 architecture that can be used for various purposes, such as holding data, addresses, or function return values.

## More...
1. PC: Program Counter
    - A register that holds the memory address of the next instruction to be fetched and executed.

2. SP: Stack Pointer
    - A register that holds the memory address of the top of the stack.

3. IP: Instruction Pointer 
    - A register that holds the memory address of the next instruction to be executed in some architectures.

4. ISR: Interrupt Service Routine  
    - A special routine that is executed in response to an interrupt signal from a hardware device.

5. ABI: Application Binary Interface 
    - A specification that defines the calling convention, register usage, stack layout, and other aspects of how programs interact with the operating system and libraries.

6. ISA: Instruction Set Architecture
    - The set of instructions and their encoding that a particular processor or CPU supports.

7. NOP: No Operation  
    - An instruction that performs no operation and is used as a placeholder or for timing purposes.

8. CMP: Compare
    - An instruction that compares two values and sets flags based on the result of the comparison.

9. JMP: Jump
    - An instruction that transfers control to a different location in the program.

10. CALL: Call Subroutine
    - An instruction that transfers control to a subroutine or function.

11. RET: Return
    - An instruction that returns control from a subroutine to the calling code.

12. MOV: Move 
    - An instruction that copies data from one location to another.

13. ADD: Add
    - An instruction that performs addition on two values.

14. SUB: Subtract
    - An instruction that performs subtraction of two values.

15. AND: Logical AND
    - An instruction that performs bitwise AND on two values.

16. OR: Logical OR
    - An instruction that performs bitwise OR on two values.

17. XOR: Exclusive OR
    - An instruction that performs bitwise XOR on two values.

18. SHR: Shift Right
    - An instruction that shifts the bits of a value to the right.

19. SHL: Shift Left
    - An instruction that shifts the bits of a value to the left.

20. LDR: Load Register  
    - An instruction that loads a value from memory into a register.

21. STR: Store Register
    - An instruction that stores a value from a register into memory.

22. HLT: Halt
    - An instruction that halts the execution of the program.

23. JNZ: Jump Not Zero
    - An instruction that performs a conditional jump to a specified location if the zero flag is not set (i.e., the result of the previous operation was not zero).

24. JE: Jump if Equal
    - An instruction that performs a conditional jump to a specified location if the zero flag is set (i.e., the result of the previous operation was zero).

25. JG: Jump if Greater
    - An instruction that performs a conditional jump to a specified location if the greater flag is set (i.e., the result of the previous operation was greater than zero).

26. JL: Jump if Less
    - An instruction that performs a conditional jump to a specified location if the less flag is set (i.e., the result of the previous operation was less than zero).

27. JGE: Jump if Greater or Equal
    - An instruction that performs a conditional jump to a specified location if the greater or equal flag is set.

28. JLE: Jump if Less or Equal
    - An instruction that performs a conditional jump to a specified location if the less or equal flag is set.

29. LOOP: Loop
    - An instruction that performs a conditional jump to a specified location while a counter is not zero.

30. PUSH: Push onto Stack
    - An instruction that pushes a value onto the top of the stack.

31. POP: Pop from Stack
    - An instruction that removes and retrieves the top value from the stack.
