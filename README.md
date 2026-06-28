# Random-password-python
# Random Password Generator 

A simple password generator written in Python.  
The program creates a random 8-character password using letters, numbers, and special characters.

## Features

- Generates a random password
- Password length: 8 characters
- Uses letters, numbers, and symbols
- Simple and lightweight

## Requirements

- Python 3.13.7x

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yasinMlpy/Random-password-python
```

2. Go to the project folder:

```bash
cd (name folder)
```

3. Run the program:

```bash
python Random-Password.py
```

## Example Output

```text
Your new password: a#8Df$2P
```

## Code Example

```python
import random

password = "asdpuhasdpoiuahdaoihdai0sdh..."
random_password = ""

for i in range(8):
    random_password += random.choice(password)

print("Your new password:", random_password)
```

## Author

Created by Yasin
