from dataclasses import dataclass
from typing import List
from medicare_utils.exceptions import MedicareValidationError

@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]

    def raise_if_invalid(self):
        """Raise MedicareValidationError if validation failed."""
        if not self.is_valid:
            raise MedicareValidationError(", ".join(self.errors))

def validate(medicare_number: str) -> ValidationResult:
    """Validate a Medicare number based on length, check digit, and issue number.

    Returns:
        ValidationResult: An object containing a boolean and list of error messages.
    """
    errors = []
    number = medicare_number.strip().replace(" ", "")

    if not number.isdigit():
        errors.append("non-digit characters present")
        return ValidationResult(False, errors)

    if len(number) != 10:
        if len(number) < 10:
            errors.append("too short")
        else:
            errors.append("too long")
        return ValidationResult(False, errors)

    base_digits = [int(d) for d in number[:8]]
    check_digit = int(number[8])
    issue_number = int(number[9])

    if number[0] not in '23456':
        errors.append("invalid starting digit")
    if not (1 <= issue_number <= 9):
        errors.append("invalid issue number")

    weights = [1, 3, 7, 9, 1, 3, 7, 9]
    total = sum(d * w for d, w in zip(base_digits, weights))
    expected_check_digit = (total % 10)

    if check_digit != expected_check_digit:
        errors.append("invalid check digit")

    is_valid = not errors
    return ValidationResult(is_valid=is_valid, errors=errors)

def is_valid(medicare_number: str) -> bool:
    """Check if a Medicare number is valid. Returns True or False."""
    return validate(medicare_number).is_valid
