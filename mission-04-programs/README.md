# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to explore how computers translate and execute programming source code into machine instructions. This includes authoring and running a basic Python script from the command line, understanding the roles of compilers versus interpreters, and contrasting their translation models, runtime performance, and output artifacts.

---

## 2. Work completed
- Authored a working Python script named `hello.py` inside `mission-04-programs/`.
- Executed `hello.py` from the terminal using the Python 3 interpreter (`python3 hello.py`) and verified stdout output (`Hello from Python`).
- Constructed a comparative analysis table evaluating compilers and interpreters across translation timing, output artifacts, language examples, and architectural advantages.
- Provided a clear synthesis explaining how modern runtime environments execute code.

---

## 3. Commands / tools used
- `python3 hello.py`: Invoked the CPython 3 runtime interpreter to compile and execute the script.
- Terminal text streams to observe standard output and exit codes.

---

## 4. My understanding

### Task 4.1 — Create and run a Python program
- Created file: `mission-04-programs/hello.py`
```python
print("Hello from Python")
```
- **Execution command:** `python3 hello.py`
- **Output:**
```
Hello from Python
```
- **Observation:** When Python executes `hello.py`, the source code is read, parsed into an Abstract Syntax Tree (AST), compiled into Python bytecode in memory, and interpreted by the Python Virtual Machine (PVM) line by line, printing the string immediately to the console without producing a standalone machine binary.

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translation occurs entirely **before** program execution in an upfront compilation build phase. | Translation occurs **at runtime**, reading, translating, and executing statements line by line or block by block. |
| **Typical output** | An independent, standalone native executable binary (e.g., ELF on Linux, Mach-O on macOS, `.exe` on Windows) containing machine instructions directly readable by the CPU. | Direct in-memory execution results; no persistent native machine code binary is output (often produces intermediate bytecode caches like `.pyc`). |
| **One example** | **C** (using `gcc` or `clang`), **C++**, **Rust**, or **Go**. | **Python** (CPython), **Ruby**, or classic **JavaScript** (in simple engines). |
| **One advantage** | **High runtime execution performance:** Because machine code is generated and optimized beforehand, the CPU executes it natively without runtime translation overhead. | **Rapid development and portability:** Code can be written, tested, and modified interactively without lengthy recompilation cycles, running on any system with the interpreter installed. |

#### Detailed Explanation of Differences
A **compiler** translates the entire human-readable high-level source code into low-level native CPU machine instructions before the program is ever launched. This means syntax errors and type mismatches are caught early during compilation, and the resulting executable can run at maximum hardware speed independently of the compiler toolchain.

In contrast, an **interpreter** processes source code on the fly during program execution, translating instructions into actions as it encounters them. This enables immediate feedback, interactive debugging, and cross-platform flexibility, but incurs higher computational overhead because translation happens alongside execution. Modern languages like Python use a hybrid model: compiling source code to intermediate bytecode, which is then dynamically interpreted by a virtual machine.

---

## 5. Difficulties faced
- Differentiating between pure interpreted languages and modern virtual-machine-based languages (such as Python or Java) which perform an internal compilation step to intermediate bytecode before interpreting.

## 6. How I resolved them
- Clarified that while Python does compile source code into bytecode, it is classified as an interpreted language because the bytecode is executed inside a software runtime environment (the Python Virtual Machine) rather than directly by physical CPU hardware registers.

---

## 7. Evidence / files
- Python program: [hello.py](file:///Users/kakul/Desktop/digital-detective-8017/mission-04-programs/hello.py)
- Mission documentation: [README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-04-programs/README.md)

---

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub
