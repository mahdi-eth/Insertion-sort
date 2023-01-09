def main(): 
    # Get a list and sort it
    insertion_sort(get_input())


def get_input():
    try:
        # Getting a list
        input_list = input(
            "Declare a bunch of numbers and seprate the items with commas to be sorted: \n")
        input_list = input_list.split(",")
        list = []
        for i in input_list:
            # Making the list ready
            list.append(int(i.strip()))
    except ValueError:
        print("Invalid")
        get_input()
        
    return list
        
        
def insertion_sort(list):
    # Declare sorted variable
    sorted_list = [list[0]]

    # Insertion sort
    for i in range(len(list) - 1):
        sorted_list.append(list[i + 1])
        if sorted_list[i] > sorted_list[i + 1]:
            for j in range(len(sorted_list) - 1, 0, -1):
                if sorted_list[j] < sorted_list[j - 1]:
                    sorted_list[j], sorted_list[j -
                                                1] = sorted_list[j - 1], sorted_list[j]
                else:
                    break

    # Print the sorted list
    print(sorted_list)


# Run the program
if __name__ == "__main__":
    main()
