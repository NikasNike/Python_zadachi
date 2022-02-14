str = 'ффвалпри лолабв щшврщы абвшг'
print(str)

tr = str.split()

[tr.remove(word) for word in tr [:] if 'абв' in word]
print(tr)


