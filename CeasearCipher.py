alphabetLowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabetUppercaseCase = ["A","B","C","D","E","F","G","H","I","J","k","l","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ciphergrid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
cipher = raw_input()
shift = 0
iterate = 0

def CesarCipher(shift):
	





for elem in cipher:
	ciphergrid[iterate] = elem
	iterate = iterate + 1

for x in ciphergrid:
	print(x)
