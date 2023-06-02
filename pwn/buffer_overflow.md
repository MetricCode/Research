## What is a buffer overflow?

### First things first, what is a buffer?
- A buffer is a temporary storage area used to hold data while it being worked upon/processed.
- Writing data beyond an allocated memory block’s bounds can crash the program, corrupt data, or allow an attacker to execute malicious code.

_Continuation..._
- A buffer *overflow/buffer overrun* occurs when a system writes more data to a buffer than it can hold.
- Buffer overflows result to excess data being available/data loss and this writes the data to the adjacent memory.
- We can take advantage of a buffer overflow by injecting specifically tailored  code that can be executed while in memory.
- A buffer overflow can also be triggered when inputs of the wrong size are supplied to the running program. This is because designers assume all inputs are smaller than the threshold size and create a buffer to fit that size.

*NB* : There are many ways to exploit buffer overflow vulnerabilities. There are also many ways to prevent a buffer overflow attacks which are prone to errors.

- The C and C++ programming languages are often associated with understanding buffer overflows for several reasons. They lack built-in protection against accessing data anywhere in memory space, let alone overwriting data or source code. They also fail to automatically check whether data written to an array such as a buffer is within its bounds.
- Bounds checking is possible with C and C++, but it demands additional processing time and code to prevent buffer overflows. Safer operating systems deploy a range of strategies in buffer overflow mitigation, such as space layout randomization, or intentionally creating space between destination buffers and writing actions called canaries or stack canaries into them for more effective monitoring of the issue.


__Hands on....__

#### 1). Dynamically Linked...

- This is the process of connecting a program/binary with the required libraries/dependencies during runtime.
- In dynamic linking, the necessary libraries are not included in the final binary file of the program but are instead linked dynamically when the program is executed.
- This means that a program contains references to external libraries or shared objects that are needed to execute certain functions or access specific resources.
- These references are typically resolved by the operating system's dynamic linker/loader at runtime. The dynamic linker/loader locates and loads the required libraries into memory, resolves the references, and establishes the necessary connections between the program and the libraries.

**Pros of dynamic linking**

- Allows for efficient use of system resources by sharing common libraries among multiple programs. 
- Enables easier updates and maintenance since changes in the shared libraries can be propagated to all programs that use them without recompiling them individually.
- Reduces the size of the executable file, as it only includes the program-specific code and data.

__NB__: Exploiting a dynamically linked program may involve manipulating the behavior of the dynamic linker/loader or exploiting vulnerabilities within the shared libraries themselves.

#### 2). Statically Linked...

- This means that all the libraries and dependencies it requires to run are combined and included directly within the executable file.
- the necessary code from external libraries is embedded into the program during the compilation phase, resulting in a standalone binary that does not rely on external libraries at runtime. 

__Pros of statically linked binaries..__

- Portability: Since all the required libraries are bundled within the executable, the program can be executed on different systems without relying on specific library versions or configurations. This simplifies the deployment process and ensures consistent behavior across different environments.

- Independence: A statically linked program does not rely on the presence or availability of external libraries. It can be executed on systems that do not have the required libraries installed, eliminating the need to distribute or manage separate library dependencies.

- Performance: Static linking can improve performance as it eliminates the overhead of dynamic linking and runtime library resolution. The program has direct access to all its dependencies, leading to faster startup times and potentially improved overall execution speed.

- Security: Static linking can enhance security by reducing the attack surface. Since the program does not rely on external libraries that may have vulnerabilities, it mitigates the risk of exploitation through vulnerable library versions or malicious library substitution.

__Cons of Statically Linked....__

- Increased file size: Including all the necessary libraries within the executable file can significantly increase its size. This may be a concern when distributing or downloading the program, particularly in resource-constrained environments.

- Lack of flexibility: Since the program carries its dependencies, it may not take advantage of updates or bug fixes in external libraries without recompiling and redistributing the entire program. This can make it more challenging to keep the program up to date.
  
- License considerations: Statically linking libraries into a program may have implications for license compliance. Some open-source libraries have specific licensing requirements that govern their distribution and use.

#### 3). Not stripped...

- Stripping is a post-compilation step that removes various debugging and symbol information from the binary, resulting in a smaller file size and potentially making it more challenging to analyze or reverse engineer.
- This means that the binary executable/object file ahs not undergone the process of stripping...
- When a binary is "not stripped," it means that the debugging symbols and other information are still present in the binary file.
- The presence of symbols and debug information makes it easier to identify functions, variables, and data structures within the binary.

#### 4). Stripped...

- When a binary is "stripped," the debugging symbols and other metadata that aid in program analysis, such as function names, variable names, and line numbers, are typically removed.
- Stripping a binary involves removing various types of information, including:

1. Debugging symbols: These symbols provide names and information about functions, variables, and data structures within the code. They are useful for debugging and symbol resolution during development but are not necessary for the functioning of the program.
    
2. Line numbers: Information about the mapping between the source code and the compiled binary, including line numbers, is typically removed during stripping.
    
3. Symbol table: The symbol table contains a list of all the symbols in the binary, including function and variable names. Stripping removes this table, making it harder to identify specific functions or variables within the binary.
    
4. Compiler-specific metadata: Some compilers include additional metadata in the binary, such as compiler flags or optimization information. Stripping removes these compiler-specific details.

__Pros of stripping__

- Reduces the file size, making the program more efficient to distribute and load into memory.
- Makes reverse engineering and analysis more challenging, as crucial information for understanding the code's structure and logic is removed.

__NB__: Stripping a binary does not make it completely immune to reverse engineering or analysis. Dynamic analysis, code tracing, or behavior analysis can be performed to understand the binary's behavior, even without the presence of debugging symbols.
