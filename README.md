# iris_helpers

Helper utilities for IRIS API.

## IHI Utilities

### `validate_ihi(ihi: str) -> bool`
Checks whether the IHI number is structurally valid and passes the Luhn checksum calculation.

### `generate_ihi(iin: str = "800360") -> str`
Generates a valid random 16-digit IHI number.
- `iin`: Optional 6-digit string (default: `'800360'`)
- Returns a valid IHI number with checksum.

## Medicare Utilities

### `format_medicare_number(medicare_number: str) -> str`
Formats a 10-digit Medicare number as `XXXX XXXX X X`. Raises a `MedicareValidationError` if the input is not exactly 10 digits.

### `validate(medicare_number: str) -> ValidationResult`
Validates a Medicare number's length, start digit, issue number, and check digit.
Returns a `ValidationResult` object with:
- `is_valid`: `True` if the number is valid
- `errors`: list of strings describing validation failures

### `is_valid(medicare_number: str) -> bool`
Returns `True` or `False` based on whether the Medicare number passes validation.

### `generate(base_number: str, issue_number: int) -> str`
Generates a valid Medicare number from an 8-digit base and issue number (1–9). Calculates the correct check digit.

### `generate_random(seed: int = None) -> str`
Returns a random, valid Medicare number (optionally using a seed for reproducibility).

### `generate_many(count: int, seed: int = None) -> List[str]`
Returns a list of `count` valid Medicare numbers.

## Installation

Install the latest version from GitHub:

```bash
pip install git+https://github.com/mashby1966/iris_helpers.git@main
```

## Example Usage

```python
from iris_helpers.config import config
from iris_helpers.api import getIRISData
from iris_helpers.ihi import generate_ihi, validate_ihi
from iris_helpers.formatter import format_medicare_number
from iris_helpers.validator import validate

# Example Medicare number validation
number = "1234567890"
result = validate(number)
print("Valid?" , result.is_valid)
if not result.is_valid:
    print("Errors:", result.errors)

# Generate and validate IHI
ihi = generate_ihi()
print("Generated IHI:", ihi)
print("IHI Valid?", validate_ihi(ihi))

# Fetch sample IRIS data
df = getIRISData("QuestionnaireItem")
print(df.head())
```
