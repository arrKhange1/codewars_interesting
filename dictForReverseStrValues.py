def DNA(x):
    reverse_dict = {'A':'T', 'T':'A','G':'C','C':'G'}
    return ''.join([reverse_dict[i] for i in x])
print(DNA('ATTGC'))
