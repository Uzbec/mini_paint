def rect(HEIGHT,WIDTH,BACKGROUND_CHAR):
    for i in range(HEIGHT):
        if i == 0 or i == HEIGHT - 1:
            for j in range(WIDTH):
                print(BACKGROUND_CHAR, end='')
        else:
            print(BACKGROUND_CHAR, end='')
            for j in range(1, WIDTH - 1):
                print(' ', end='')
            print(BACKGROUND_CHAR, end='')
        print()




