def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    if not starts_with_two_letters(s):
        return False

    if not numbers_only_at_end(s):
        return False

    return True


def starts_with_two_letters(s):
    return s[0].isalpha() and s[1].isalpha()


def numbers_only_at_end(s):
    # This stays "no" until we spot the first digit
    seen_a_digit = "no"

    for char in s:

        if char.isdigit():
            # This character is a number

            if seen_a_digit == "no":
                # This is the first digit
                if char == "0":
                    return False
                seen_a_digit = "yes"

            # if seen_a_digit was already "yes", nothing to do,
            # this digit is fine, just keep going

        else:
            # This character is a letter

            if seen_a_digit == "yes":
                # We already passed a digit earlier,
                # so a letter here is NOT allowed
                return False

    # If we got through the whole plate without returning False,
    # it's valid
    return True


if __name__ == "__main__":
    main()
