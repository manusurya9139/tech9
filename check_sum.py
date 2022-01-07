def check_sum(input_list, sum):
    """
    Method to check if key pair for k is present in the list
    :param input_list: type(list)
    :param sum: type(int)
    :return: ("true", "false")
    """
    for i in input_list:
        if sum - i in input_list:
            return "true"
    return "false"

if __name__ == '__main__':
    # Take values for input list
    input_list = input("Enter space separated integer values for input list: ")
    # Convert the list with interger list
    input_list = [int(i) for i in input_list.split()]
    # Get the value for Sum to check
    sum_to_check = int(input("Enter value to check the sum: "))
    output = check_sum(input_list, sum_to_check)
    print(f"Output: {output}")


#===================================================================================================
#                                        OUTPUT                                                    #
#===================================================================================================
#C:\Users\manoj\AppData\Local\Programs\Python\Python39\python.exe C:/Users/manoj/Desktop/Manu/tech9/check_sum.py
#Enter space separated integer values for input list: 10 5 3 7
#Enter value to check the sum: 17
#Output: true