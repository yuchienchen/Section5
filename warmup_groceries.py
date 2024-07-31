def main():
    # groceries = {
    # 'safeway': {'eggs': 1, 'coconut milk': 3}, 
    # 'costco': {'croissant': 12}
    # }

    groceries = {}
    store = input("Please enter a store: ")

    # add empty inner dict
    while store not in groceries:
        # If the user enters a blank line, break out of the loop and stop asking for input
        if store == "":
            break

        groceries[store] = {}
        store = input("Please enter a store: ")
    
    print(groceries)
    print(groceries.keys())

    inner = groceries[store]
    item = input("Please enter an item: ")
    num = int(input("Please enter a num: "))
    if item not in inner:
        if store == 'safeway' and item == 'eggs':
            inner[item] = num
        
    print(groceries)
        

    # for key, value in groceries.items():
    #     print(key)
    #     print(value)
    #     if key == 'safeway':
    #         value['eggs'] = 3
    #         value['flour'] = 1
    #     if key == 'target':
    #         value['sugar cookies'] = 1        


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