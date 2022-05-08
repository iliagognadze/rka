
def convert_text_to_ascii(text):
    txt_list = list(text)
    converted = []
    for item in txt_list:
        converted.append(ord(item))
    return converted

def convert_to_8bit(converted_list):
    bin_list = []
    for item in converted_list:
        converted_txt = bin(item)
        sliced = converted_txt[2:]
        while len(sliced) < 8:
            sliced = "0"+sliced
        bin_list.append(sliced)
    return bin_list

def xor_operation(ascii_list, key):
    xor_operated_list = []
    for item in ascii_list:
        xor_operated_list.append(item ^ key)
    return xor_operated_list

def reverse(text_list):
    reversed_list = []
    for item in text_list:
        reversed_list.append(item[::-1])
    return reversed_list

def convert_8bit_to_text(binary_list):
    converted_chars = []
    for item in binary_list:
        converted_chars.append(chr(int((item), 2)))
    return converted_chars

def rka(text, key):
    return convert_8bit_to_text(reverse(convert_to_8bit(xor_operation((convert_text_to_ascii(text)), key))))

# implementation can be faster than this. too many iterations.
print(rka("TEST", 23))