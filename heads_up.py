import random

# Name of the file to read in
FILE_NAME = 'cswords.txt'

def main():
    # Milestone #1: First, load all of the words from the file cswords.txt into a list.
    vocab = []
    with open(FILE_NAME) as file:
        for line in file: # for-each loop gives lines one at a time
            vocab.append(line.strip())
            #print(line.strip()) # strip removes whitespace at the start or end
    # for i in range(len(vocab)): 
    #     print(vocab[i])
    
    # Milestone #2: Then, show a randomly chosen word from the list
    # Milestone #3: Repeat: wait for the user to hit enter, then show another word.

    while True:
        chosen_value = random.choice(vocab) # comes with ‘import random’
        print(chosen_value)
        user = input('Please press enter')
        
        # max_index = len(vocab)- 1
        # index = random.randint(0, max_index)
        # user = input(vocab[index])


if __name__ == '__main__':
    main()
