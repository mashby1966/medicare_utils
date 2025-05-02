
import re
import random

def _is_ihi_number(candidate: str) -> bool:
    """Check if a string structurally resembles an IHI number."""
    return bool(re.fullmatch(r"800360\d{9}\d", candidate))

def validate_ihi(ihi: str) -> bool:
    """
    Validate an IHI number using the Luhn checksum.
    
    Args:
        ihi (str): 16-digit IHI string.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not _is_ihi_number(ihi):
        return False

    reversed_digits = list(map(int, reversed(ihi[:-1])))  # Exclude check digit
    check_digit = int(ihi[-1])

    even_sum = 0
    odd_sum = 0

    for i, d in enumerate(reversed_digits):
        if i % 2 == 0:
            doubled = d * 2
            odd_sum += doubled - 9 if doubled > 9 else doubled
        else:
            even_sum += d

    total = even_sum + odd_sum
    calculated = (10 - (total % 10)) % 10

    return check_digit == calculated


def generate_ihi(iin: str = "800360") -> str:
    """
    Generate a valid IHI number.

    Args:
        iin (str): The first 6 digits of the IHI (default: '800360').

    Returns:
        str: A valid 16-digit IHI number.
    """
    if not re.fullmatch(r"\d{6}", iin):
        raise ValueError("IIN must be a 6-digit numeric string.")

    iai = f"{random.randint(0, 999_999_999):09d}"  # 9-digit random IAI
    base = iin + iai

    reversed_digits = list(map(int, reversed(base)))
    even_sum = 0
    odd_sum = 0

    for i, d in enumerate(reversed_digits):
        if i % 2 == 0:
            doubled = d * 2
            odd_sum += doubled - 9 if doubled > 9 else doubled
        else:
            even_sum += d

    total = even_sum + odd_sum
    check_digit = (10 - (total % 10)) % 10

    return base + str(check_digit)