import base58

with open('addresses.txt', 'r') as f:
	for adr58 in f:
		adr160 = base58.b58decode_check(adr58)
		open('RIPEMD160.txt', 'a').write(adr160.hex()[-40:] + '\n')
