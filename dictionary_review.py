def main():
    classes = {'CS106A': 5, 'PSYCH1': 5, 'PWR1': 4}

    for key in classes:
        value = classes[key]
        print(value)
    print()

    for value in classes.values():
        print(value)

if __name__ == '__main__':
    main()