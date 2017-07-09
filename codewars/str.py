def is_isogram(string):
    for i in range(len(string)):
        for j in range(i+1 ,len(string)):
            if string[i].upper() == string[j].upper():
                return False
    return True


print(is_isogram("")) # true
print(is_isogram("Dermatoglyphics")) # true
print(is_isogram("isIsogram")) # false
print(is_isogram("moOse")) # false