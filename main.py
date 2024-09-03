def Caesarcipher(plainText, shift) :
    translatedText = ''

alphabet_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'A', 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: 'N', 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z'}

    
def char_shift(char, shift) :
        if 'A' <= char <= 'z':
            print('the number is within accaptable range because the ascci value is ' + str(ord(char)))
            return chr(ord(char) + shift)
        else:
            print("the number is not within accaptable range" + str(ord(char)))
            return None

def index_of_value(dict, key_to_find):
    try:
        return list(dict.values()).index(key_to_find) + 1
    except ValueError:
        return -1

def char_shift_use_dic(char, shift):
     if char in alphabet_dict.values():
        old_index = index_of_value(alphabet_dict, char)
        shifted_index = ((old_index) + shift) % 52
        print(shifted_index)
        newValue = alphabet_dict.get(shifted_index)  
        return newValue
     else:
         return 'invalid char'   
          


print(char_shift_use_dic('Z', 1))