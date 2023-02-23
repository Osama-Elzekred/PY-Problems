def minion_game(string):

    vowels = ['O', 'A', 'I', 'U', 'E']

    kevin, stuart = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:

            kevin += len(string)-i
        else:
            stuart += len(string)-i

    if kevin > stuart:
        print(f"Kevin {kevin}", end="")
    elif kevin < stuart:
        print(f"Stuart {stuart}", end="")
    else:
        print("Draw ", end="")


if __name__ == '__main__':
    s = input()
    minion_game(s)
