import random
from typing import List
from medicare_utils.exceptions import MedicareValidationError

def generate(base_number: str, issue_number: int) -> str:
    """Generate a valid Medicare number given a base number and issue number.

    Args:
        base_number (str): 8-digit base number as a string.
        issue_number (int): Issue number from 1 to 9.

    Returns:
        str: A full 10-digit valid Medicare number.

    Raises:
        MedicareValidationError: If the base number or issue number is invalid.
    """
    if len(base_number) != 8 or not base_number.isdigit():
        raise MedicareValidationError("Base number must be 8 digits")
    if not (1 <= issue_number <= 9):
        raise MedicareValidationError("Issue number must be between 1 and 9")

    weights = [1, 3, 7, 9, 1, 3, 7, 9]
    base_digits = [int(d) for d in base_number]
    total = sum(d * w for d, w in zip(base_digits, weights))
    check_digit = (total % 10)

    return f"{base_number}{check_digit}{issue_number}"

def generate_random(seed: int = None) -> str:
    """Generate a valid random Medicare number."""
    if seed is not None:
        random.seed(seed)

    first_digit = str(random.choice([2, 3, 4, 5, 6]))
    other_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
    base_number = first_digit + other_digits
    issue_number = random.randint(1, 9)

    return generate(base_number, issue_number)

def generate_many(count: int, seed: int = None) -> List[str]:
    """Generate a list of valid random Medicare numbers."""
    if seed is not None:
        random.seed(seed)
    return [generate_random() for _ in range(count)]
