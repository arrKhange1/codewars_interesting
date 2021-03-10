str1 = "10.0.0.0"
str2 = "10.0.0.50"
def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)

print(ips_between(str1, str2))



