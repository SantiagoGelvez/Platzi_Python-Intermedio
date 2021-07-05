def run():
    
    # for i in range(1,101):
    #     print(i,' elevado al cuadrado es ', i**2)

    squares = []
    for i in range(1,101):
        if (i**2)%3 != 0:
            squares.append(i**2)
    print(squares)


if __name__ == '__main__':
    run()