class ConstraintErrors(str):
    DUPLICATED_USER_ADDRESS = "Duplicated addresses are not allowed."
    NO_DIGITS_IN_POSTAL_CODE = "Postal code must be numeric or alphanumeric."

    def __str__(self) -> str:
        return str.__str__(self)
