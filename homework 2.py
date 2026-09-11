def date_of_birth(ssn):
    y = int(ssn[4:6])
    if ssn[6] == '+':
        y += 1800
    elif ssn[7]== '-':
        y += 1900
    else:
        y += 2000
    m = int(ssn[2:4])
    d = int(ssn[0:2])
    return(y, m, d)
print(date_of_birth('140598+abcd')) 