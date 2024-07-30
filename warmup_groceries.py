def main():

    groceries = {
    'safeway': {'eggs': 1, 'coconut milk': 3}, 
    'costco': {'croissant': 12}
    }

    groceries['target'] = {}

    for key, value in groceries.items():
        print(key)
        print(value)
    print(groceries)

        # sub_dict = value
        # for key, value in sub_dict.items():
        #     print(key)
        #     print(value)
        #     target['sugar cookies'] = 1
        # print(sub_dict)
    


    # groceries['target'] = {'sugar cookies': 1}
    # print(groceries)
    # print()

    # groceries['safeway'] = {'eggs': 3, 'coconut milk': 3, 'flour': 1}
    # print(groceries)



if __name__ == '__main__':
    main()