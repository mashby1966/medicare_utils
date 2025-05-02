from medicare_utils.exceptions import MedicareValidationError

def format_medicare_number(medicare_number: str) -> str:
    """Format the Medicare number as XXXX XXXX X X.

    Args:
        medicare_number (str): Raw 10-digit string or unformatted input.

    Returns:
        str: Formatted Medicare number.

    Raises:
        MedicareValidationError: If the number is not 10 digits.
    """
    digits = ''.join(filter(str.isdigit, medicare_number))
    if len(digits) != 10:
        raise MedicareValidationError("Medicare number must contain exactly 10 digits")
    return f"{digits[:4]} {digits[4:8]} {digits[8]} {digits[9]}"
