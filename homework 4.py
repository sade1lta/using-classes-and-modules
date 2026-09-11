def file_type(s):
    index_dot = str.rfind(s, '.')
    if index_dot == -1:
        type_of_file = '"'
    else:
        type_of_file = s[index_dot + 1:]
    
    if type_of_file == '':
        type_of_file = '"'
    
    return type_of_file

s = 'foo.'
print(file_type(s))