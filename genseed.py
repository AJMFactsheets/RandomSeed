import random

# Check seed info here: https://panda4994.github.io/seedinfo/seedinfo.html
def genDigit():
	return random.randint(0,9)


doLoop = 1


while doLoop:
	stringSeed = ""
	signBool = random.randint(0,1)
	if signBool == 0:
		stringSeed += "-"
	
	#stringSeed += str(random.randint(0,1))
	
	#for x in range(19):
	#	stringSeed += str(genDigit())
	stringSeed += str(random.getrandbits(63))
	
	longSeed = int(stringSeed)
	
	if longSeed <= 9223372036854775806 and longSeed >= -9223372036854775807:
		doLoop = 0

print (stringSeed)
