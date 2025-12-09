#W6A9
def nhap_hai_dictionary():
    """
    Nhập vào hai dictionary từ người dùng.
    """
    print("Nhập dictionary thứ nhất (ví dụ: {'key1': 'value1', 'key2': 2}):")
    dict1_str = input()
    dict1 = eval(dict1_str)

    print("Nhập dictionary thứ hai (ví dụ: {'key3': 'value3', 'key4': 4}):")
    dict2_str = input()
    dict2 = eval(dict2_str)
    
    # Start with dict2
    dict3 = {}
    for i in dict2:
        dict3[i] = dict2[i]
    
    # Add dict1, handling duplicates
    for i in dict1:
        if i not in dict3:  # ✅ Fixed: check if KEY is in dict3
            dict3[i] = dict1[i]
        else:
            dict3[i] += dict1[i]
            
    return dict3

dict3 = nhap_hai_dictionary()
print(dict3)
