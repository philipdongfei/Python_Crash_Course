def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        '''
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        '''
    else:
        #Count approximate number of words in the file.
        count = contents.lower().count('the')
        print("the word 'the' appears " + str(count) + " in " + filename)
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")

if __name__ == "__main__":
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    for filename in filenames:
        count_words(filename)

