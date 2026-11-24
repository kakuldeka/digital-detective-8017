# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand low-level data representation in computer systems. This involves performing manual conversions across Decimal (base 10), Binary (base 2), and Hexadecimal (base 16), validating each conversion using Python's interactive functions, authoring an interactive CLI converter program (`number_converter.py`), and analyzing character encoding standards (ASCII vs. UTF-8).

---

## 2. Work completed
- Calculated manual, step-by-step mathematical conversions for all 7 assigned problems.
- Verified manual calculations using Python built-in conversion functions (`bin()`, `hex()`, `int()`).
- Developed, tested, and documented an interactive script (`number_converter.py`) that accepts decimal integers and outputs formatted binary and hexadecimal representations.
- Executed and validated the converter against three test numbers: 42, 255, and 1024.
- Researched ASCII character codes for uppercase 'A' and lowercase 'a' and evaluated character encoding paradigms.

---

## 3. Commands / tools used
- `python3`: Used interactively and non-interactively to verify number conversions.
- Python built-in functions:
  - `bin(x)`: Converts an integer to a binary string prefixed with `0b`.
  - `hex(x)`: Converts an integer to a hexadecimal string prefixed with `0x`.
  - `int(string, base)`: Parses a string representation in the specified base into a decimal integer.
  - `ord(char)`: Returns the Unicode/ASCII integer code point of a given character.

---

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | **Successive Division by 2:**<br>• $13 \div 2 = 6$ remainder **1** (LSB)<br>• $6 \div 2 = 3$ remainder **0**<br>• $3 \div 2 = 1$ remainder **1**<br>• $1 \div 2 = 0$ remainder **1** (MSB)<br>Reading remainders from bottom to top: **$1101_2$**<br>*Check:* $(1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) = 8 + 4 + 0 + 1 = 13_{10}$. |
| **Convert decimal 25 to binary** | **Successive Division by 2:**<br>• $25 \div 2 = 12$ remainder **1** (LSB)<br>• $12 \div 2 = 6$ remainder **0**<br>• $6 \div 2 = 3$ remainder **0**<br>• $3 \div 2 = 1$ remainder **1**<br>• $1 \div 2 = 0$ remainder **1** (MSB)<br>Reading remainders from bottom to top: **$11001_2$**<br>*Check:* $(1 \times 16) + (1 \times 8) + (0 \times 4) + (0 \times 2) + (1 \times 1) = 16 + 8 + 1 = 25_{10}$. |
| **Convert binary 1010 to decimal** | **Positional Powers of 2:**<br>• $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>• $= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$<br>• $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$. |
| **Convert binary 1101 to decimal** | **Positional Powers of 2:**<br>• $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>• $= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$<br>• $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$. |
| **Convert hexadecimal A to decimal** | **Base 16 Digit Value:**<br>• In hexadecimal, letters represent values 10 through 15: $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$.<br>• Digit $\text{A} = (10 \times 16^0) = \mathbf{10_{10}}$. |
| **Convert hexadecimal 1F to decimal** | **Positional Powers of 16:**<br>• $(1 \times 16^1) + (\text{F} \times 16^0)$<br>• $= (1 \times 16) + (15 \times 1)$<br>• $= 16 + 15 = \mathbf{31_{10}}$. |
| **Convert binary 1111 to hexadecimal** | **Group of 4 bits (Nibble):**<br>• Decimal value: $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$.<br>• Decimal 15 maps directly to hex symbol **$\mathbf{F_{16}}$** (or $\mathbf{0xF}$). |

---

### Task 5.2 — Verify using Python

| Expression Tested | Python Output | Matches Manual Calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | **Yes** — matches $1101_2$ |
| `bin(25)` | `'0b11001'` | **Yes** — matches $11001_2$ |
| `int('1010', 2)` | `10` | **Yes** — matches $10_{10}$ |
| `int('1101', 2)` | `13` | **Yes** — matches $13_{10}$ |
| `int('A', 16)` | `10` | **Yes** — matches $10_{10}$ |
| `int('1F', 16)` | `31` | **Yes** — matches $31_{10}$ |
| `hex(0b1111)` | `'0xf'` | **Yes** — matches $\text{F}_{16}$ |

---

### Task 5.3 — Build a small number converter

#### How `number_converter.py` Works
The program prompts the user for a decimal integer via `input()`. It validates that the string contains digits using `int()`. It then calls:
- `bin(num)`: Generates the binary representation prefixed with `0b`. The raw bitstring is obtained via slice `[2:]`.
- `hex(num)`: Generates the hexadecimal representation prefixed with `0x`. An uppercase formatted representation is obtained via `.upper()`.
- Error handling with a `try...except ValueError` block gracefully handles non-numeric inputs.

#### Test Results

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **42** | `0b101010` (raw: `101010`) | `0x2a` (uppercase: `2A`) |
| **255** | `0b11111111` (raw: `11111111`) | `0xff` (uppercase: `FF`) |
| **1024** | `0b10000000000` (raw: `10000000000`) | `0x400` (uppercase: `400`) |

---

### Task 5.4 — How is text stored?

#### 1. ASCII Decimal Codes for 'A' and 'a'
- Uppercase **'A'**: Decimal code **65** (`0b01000001`, `0x41`)
- Lowercase **'a'**: Decimal code **97** (`0b01100001`, `0x61`)
- *Note:* The difference between lowercase and uppercase in ASCII is exactly $32$ ($2^5$), meaning toggling the 6th bit flips case.

#### 2. Why computers need an encoding standard
Computers operate fundamentally on electrical binary states (0s and 1s) and have no native concept of letters or symbols. An encoding standard establishes an agreed-upon dictionary mapping arbitrary characters to specific numeric codes, guaranteeing that text stored by one program or operating system is interpreted and displayed identically by any other system in the world.

#### 3. Character not part of basic ASCII
The Indian Rupee symbol **`₹`** (Unicode code point `U+20B9`, encoded in UTF-8 as bytes `0xE0 0xA4 0xB9`) or the Euro symbol **`€`** (`U+20AC`). Basic ASCII is a 7-bit encoding restricted to codes 0 through 127 (English alphabet, numbers, basic symbols, and control codes) and cannot represent currency symbols or international scripts.

---

## 5. Difficulties faced
- Handling the prefix string (`0b` and `0x`) returned by Python's built-in `bin()` and `hex()` functions when displaying raw bit and nibble sequences to users.
- Ensuring the conversion script handled non-integer inputs gracefully without unhandled tracebacks.

## 6. How I resolved them
- Used string slicing (`[2:]`) to provide both standard programming notation (`0b...` / `0x...`) and clean raw bit/hex representations.
- Wrapped user inputs in a structured `try...except ValueError` validation block.

---

## 7. Evidence / files
- Conversion script: [number_converter.py](file:///Users/kakul/Desktop/digital-detective-8017/mission-05-numbers-data/number_converter.py)
- Mission documentation: [README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-05-numbers-data/README.md)

---

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub
