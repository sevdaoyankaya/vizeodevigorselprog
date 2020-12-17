# Soru 4.
num3digit = 352
occurCheck = ""
for i in str(num3digit):
	occurCount = str(num3digit).count(i)
	if (occurCount > 1):
		occurCheck += i
		if (occurCheck.count(i) == 1):
			print(i + " sayısı " + str(occurCount) + " defa kullanılmıştır")
if (len(occurCheck) == 0):
	print("Tekrarlayan sayı bulunmadı")