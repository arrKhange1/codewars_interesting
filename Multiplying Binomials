def StringParsing(string):
    string = string.replace(' ', '')
    arr = [0]*2

    if string.count('x') == 0:
        print(1)
        return [0,int(string)]

    if string.find('x') != 0 and string[string.find('x')-1] != '-':
        arr[0] = int(string[:string.find('x')])
        if string.find('x') == len(string) -1:
            arr[1] = 0
            return arr
    elif string.find('x') != 0:
        arr[0] = -1
        if string.find('x') == len(string) -1:
            arr[1] = 0
            return arr
    else:
        arr[0] = 1
        if string.find('x') == len(string) -1:
            arr[1] = 0
            return arr
    arr[1] = int(string[string.find('x')+1:len(string)])


    return arr

def Pascal(n):
    arr = [[0]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            arr[i][0] = 1
            if i == j:
                arr[i][j] = 1
            elif i > 1 and arr[i][j] != 1:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr[n]

def Solve(str1 ,n):
    if n == 1:
        return str1

    res_str = ''
    str_coefs = StringParsing(str1)

    if str_coefs[1] == 0 and (str_coefs[0]**n != 1) :
        if str_coefs[0] != -1:
            return str(str_coefs[0]**n) + 'x^' + str(n)
        else:
            return '-x^' + str(n)
    elif str_coefs[1] == 0:
        return 'x^' + str(n)
    if str_coefs[0] == 0:
        return str(str_coefs[1]**n)

    pasc_coefs = Pascal(n)
    str_help = ''

    for i in range(n+1):
        main_coef = pasc_coefs[i]*(str_coefs[0]**(n-i))*(str_coefs[1]**i)

        if main_coef > 0:
            if i == 0:
                str_help = str(main_coef) + 'x^' + str(n - i)
            else:
                str_help = ' + ' + str(main_coef) + 'x^' + str(n-i)
        elif main_coef < 0:
            if i == 0 and main_coef != -1:
                str_help = '-' + str(main_coef * (-1)) + 'x^' + str(n - i)
            elif i == 0:
                str_help = '-x^' + str(n - i)
            else:
                str_help = ' - ' + str(main_coef*(-1)) + 'x^' + str(n-i)

        if (main_coef == 1 and i != n):
            str_help = str_help.replace(str_help[str_help.find('x')-1], '')

        elif (i == n-1):
            str_help = str_help.replace(str_help[str_help.find('^'):str_help.find('^') + 3], '')

        res_str += str_help


    return res_str[:res_str.find('x^0')]

str1 = '-2x+1'
StringParsing(str1)
print(Pascal(8))
print(Solve(str1,1))


