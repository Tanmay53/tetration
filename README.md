# Tetration

The 4th Hyperoperation. Tetrate numbers and watch them being solved.

## Installation

```cmd
pip install tetration
```

## Usage

```python
from tetration import tetrate, tetrate_solve

print(tetrate(2, 3))
# 16

# To tetrate and show the solution steps
tetrate_solve(2, 3) # 16
# ((2)^2)^2
# (2)^4
# 16

```