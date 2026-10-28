import sys

# Check the number of command-line arguments (file name + exactly one more)
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# The file name typed
filename = sys.argv[1]

# The file must end in .py
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    # Open the file for reading (closes automatically at the end of the block)
    with open(filename) as file:
        # Counter for lines of code
        count = 0

        # Go through the file one line at a time
        for line in file:
            # Remove leading whitespace so "    # comment" is detected as a comment
            stripped = line.lstrip()

            # Skip blank lines (only whitespace) and comment lines (start with #)
            if stripped == "" or stripped.startswith("#"):
                continue

            # Anything else counts as a line of code
            count += 1
except FileNotFoundError:
    # open() raises this if the file doesn't exist
    sys.exit("File does not exist")

# Print the final number of lines of code
print(count)
