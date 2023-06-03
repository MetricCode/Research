# GDB CheatSheet!

1. Starting GDB:
    - `gdb <executable>`: Start GDB and load the specified executable for debugging.

2. Setting breakpoints:
    - `break <function>`: Set a breakpoint at the specified function.
    - `break <file>:<line>`: Set a breakpoint at the specified line in a file.
    - `break *<address>`: Set a breakpoint at the specified memory address.

3. Running the program:
     - `run`: Start or restart the program.
    - `run <arguments>`: Start the program with the specified arguments.
    - `continue` or `c`: Continue program execution after hitting a breakpoint.

4. Stepping through the code:
    - `next` or `n`: Execute the next line, stepping over function calls.
    - `step` or `s`: Execute the next line, stepping into function calls.
    - `finish`: Execute until the current function returns.

5. Examining variables and memory:
    - `print <variable>` or `p <variable>`: Print the value of the specified variable.
    - `info locals`: Display all local variables in the current scope.
    - `info registers`: Display the contents of CPU registers.
    - `x/<format> <address>`: Examine memory at the specified address using the specified format (e.g., `x/8xw <address>`).

6. Backtrace and stack:
    - `backtrace` or `bt`: Display the current call stack.
    - `frame <number>`: Switch to the specified frame in the call stack.
    - `up` or `down`: Move up or down the call stack.

7. Modifying program execution:
    - `set <variable> = <value>`: Modify the value of a variable.
    - `return`: Force an early return from the current function.
    - `signal <signal>`: Send a signal to the program (e.g., `signal SIGINT`).

8. Debugging multi-threaded programs:
    - `info threads`: Display information about all threads.
    - `thread <id>`: Switch to the specified thread.
    - `break <function> thread <thread-id>`: Set a breakpoint in a specific thread.

9. Miscellaneous: 
    - `display <variable>`: Print the value of a variable at each step.
    - `info breakpoints`: List all active breakpoints.
    - `delete <number>`: Delete the specified breakpoint.
    - `quit` or `q`: Quit GDB.
