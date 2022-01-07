from collections import OrderedDict

def encode_string(input_string):
    """
    Method to return encoded string
    :param input_string:
    :return:
    """
    output_string = ""
    # Get the unique string with order maintained
    unique_string = "".join(OrderedDict.fromkeys(input_string))
    # Check for the characters from unique string and there count in input string
    for char in unique_string:
        if char not in output_string:
            output_string = output_string + char + str(input_string.count(char))
    return output_string

if __name__ == '__main__':
    # Take an input string
    input_string = input("Please Enter Input String: ")
    encoded_string = encode_string(input_string)
    print(f"Output: {encoded_string}")


#===================================================================================================
#                                        OUTPUT                                                    #
#===================================================================================================
#C:\Users\manoj\AppData\Local\Programs\Python\Python39\python.exe C:/Users/manoj/Desktop/tech9/encode_string.py
#Please Enter Input String: wwwwfffffccccckddddecslll
#Output: w4f5c6k1d4e1s1l3
