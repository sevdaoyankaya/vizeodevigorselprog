# Soru 5.
msg = "receive-150-0-1"
msgArr = msg.split("\n")
sepCount = 0
def printStates(codeType, mData):
	if ((int(mData[0]) >= 0 and int(mData[0]) <= 255) and (int(mData[1]) >= 1 and int(mData[1]) <= 4) and (int(mData[2]) >= 0 and int(mData[2]) <= 1) and ((len(mData) == 4 and int(mData[3]) >= 0 and int(mData[3]) <= 1) or len(mData) == 3)):
		print("Kod Tipi: " + codeType + " - Giden")
		if (int(mData[0]) >= 0 and int(mData[0]) <= 50):
			print("Sinyal Gucu: " + mData[0] + " - Cok Zayif")
		elif (int(mData[0]) >= 51 and int(mData[0]) <= 100):
			print("Sinyal Gucu: " + mData[0] + " - Zayif")
		elif (int(mData[0]) >= 101 and int(mData[0]) <= 150):
			print("Sinyal Gucu: " + mData[0] + " - Orta")
		elif (int(mData[0]) >= 151 and int(mData[0]) <= 200):
			print("Sinyal Gucu: " + mData[0] + " - Guclu")
		elif (int(mData[0]) >= 201 and int(mData[0]) <= 255):
			print("Sinyal Gucu: " + mData[0] + " - Cok Guclu")
		else:
			print("Sinyal Gucu: Gecersiz")
		if (int(mData[1]) == 1):
			print("Cihaz: " + mData[1] + " - Televizyon")
		elif (int(mData[1]) == 2):
			print("Cihaz: " + mData[1] + " - Camasir Makinesi")
		elif (int(mData[1]) == 3):
			print("Cihaz: " + mData[1] + " - Buzdolabi")
		elif (int(mData[1]) == 4):
			print("Cihaz: " + mData[1] + " - Firin")
		else:
			print("Cihaz: Gecersiz")
		if (int(mData[2]) == 0):
			print("Durumu: " + mData[2] + " - Off")
		elif (int(mData[2]) == 1):
			print("Durumu: " + mData[2] + " - On")
		else:
			print("Durumu: Gecersiz")
		if (len(mData) == 4):
			if (int(mData[3]) == 0):
				print("Cevap: " + mData[3] + " - Istenmiyor")
			elif (int(mData[3]) == 1):
				print("Cevap: " + mData[3] + " - Isteniyor")
			else:
				print("Cevap: Gecersiz")
	else:
		print("Error: ikinci bolum hatali")
for i in msgArr:
	if (len(i) > 0):
		msgChunk = i.split("-")
		codeType = msgChunk.pop(0)
		sepCount += 1
		if (sepCount > 1):
			print("------")
		if (codeType == "send"):
			if (len(msgChunk) != 4):
				print("Error: ikinci bolum hatali")
			else:
				printStates(codeType, msgChunk)
		elif (codeType == "receive"):
			if (len(msgChunk) != 3):
				print("Error: ikinci bolum hatali")
			else:
				printStates(codeType, msgChunk)
		else:
			print("Error: send ya da receive icermiyor")