def main():
    classes = {'CS106A': 5, 'PSYCH1': 5, 'PWR1': 4}

    for key in classes:
        value = classes[key]
        print(value)
    print()

    for value in classes.values():
        print(value)
    print()

    print(classes['PSYCH1'])
    print()

    classes['CS106A'] = 3
    print(classes)
    print()

    classes['AMSTUD107'] = 4
    print(classes)

if __name__ == '__main__':
    main()