# TODO: Write recursive reverse_string() function here.
def reverse_string(s):
    """Return the reverse of the string s."""
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


if __name__ == "__main__":
    in_str = input()
    result_str = reverse_string(in_str)
    print(f'Reverse of "{in_str}" is "{result_str}".')
