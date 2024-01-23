import os


def decode(message_file):
    message_words = {}
    with open(message_file, "r") as file:
        for line in file:
            number, word = line.strip().split()
            number = int(number)
            message_words[number] = word

    max_number = max(message_words.keys())
    decoded_message = []
    for i in range(1, max_number + 1):
        if i * (i + 1) // 2 in message_words:
            decoded_message.append(message_words[i * (i + 1) // 2])

    return " ".join(decoded_message)


def main():
    file_path = os.path.join("coding_qual_input.txt")
    print(decode(file_path))
    # Note: for testing, please uncomment code below as needed
    # message = decode("my_message.txt")
    # print(message)


if __name__ == "__main__":
    main()

"""
Brief explanation on how the code above works:

1. Read the file: The function opens the file and reads each line.
2. Split lines: It splits each line into a number and a word.
3. Store in a dictionary: The number-word pairs are stored in a dictionary for easy retrieval.
4. Find maximum number: The maximum number in the dictionary determines the pyramid's size.
5. Decode message: It iterates through the pyramid structure, checking if a number is at the end of a line using the 
formula i * (i + 1) // 2. If so, it adds the corresponding word to the decoded message.
6. Join words: The decoded words are joined into a single string.
7. Return message: The function returns the decoded message string.
"""