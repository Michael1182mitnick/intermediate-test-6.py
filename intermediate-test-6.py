# Write a function to find the length of the longest substring without repeating characters in a given string.

def length_of_longest_substring(s):
    char_index_map = {}  # Dictionary to store the last seen index of characters
    max_length = 0
    start = 0  # Start index of the current substring

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            # If the character is already in the substring, update the start index
            start = char_index_map[char] + 1
        else:
            # Update the maximum length found so far
            max_length = max(max_length, i - start + 1)

        # Update the last seen index of the current character
        char_index_map[char] = i

    return max_length


# Example usage
input_string = input("Enter a string: ")
result = length_of_longest_substring(input_string)
print(
    f"The length of the longest substring without repeating characters is: {result}")
