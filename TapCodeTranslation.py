def tap_code_translation(text):
    text = text.replace('k','c')
    res = ''
    alph = "abcdefghijlmnopqrstuvwxyz"
    for i in text:
        if (alph.index(i)+1) % 5 == 0:
            f = (alph.index(i)+1)//5
            sec = 5
        else:
            f = ((alph.index(i)+1)//5)+1
            sec = ((alph.index(i)+1)%5)
        res += '.'*f + ' ' + '.'*sec + ' '
    print(res)
    return res[:len(res)-1]

tap_code_translation("dot")
