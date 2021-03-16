def timeConversion(s):
    # PM hour
    if s[-2:] == 'PM' :
        # remove PM
        s = s[:-2]
        if s[:2] != '12' :
            s = str(int(s[:2]) + 12 ) + s[2:]
    elif s[:-2] == 'AM' :
        # remove AM
        s = s[:-2]
        if s[:2] == '12' :
            s = '00' + s[2:]
    return f'{s}'

print(timeConversion('08:05:45AM'))