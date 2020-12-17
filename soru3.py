# Soru 3.
txt = "USAK Universitesi"
search = "ver"
pos = txt.find(search)
if (pos > 0):
	pre = txt[pos - 1]
	post = txt[pos + len(search)]
	print(pre + search + post)
else:
	print("Aranan değer bulunamadı!")