import os, sys, md5

print '\t########################################'
print '\t#	MD5 ENCRYPTER & DECRYPTER	#'
print '\t#	Write And Coded By Aditya	#'
print '\t#		   A.K.A		#'
print '\t#	       Mr. Problema		#'
print '\t#	www.github.com/problema1928	#'
print '\t########################################'

def md5encrypt():
	tampan = raw_input("type word for hash: ")
	hash = md5.new()
	hash.update(tampan)
	print hash.hexdigest()

def md5decrypt():
	tampan2 = raw_input("type hash for decrypt: ")
	wordlist = raw_input("type wordlist file path: ")
	try:
		words = open(wordlist, "r")
	except(IOError):
		print 'wordlist not found'
		sys.exit(1)
	words = words.readlines()
	for word in words:
		hash = md5.new(word[:-1])
		result = hash.hexdigest()
		if tampan2 == result:
			print 'cracked! word is: ',word

print "1) Md5 encrypter"
print "2) Md5 decrypter"
user = int(raw_input("select tools number(1/2): "))
if user == 1:
	md5encrypt()
elif user == 2:
	md5decrypt()
else:
	print 'wrong number!!'
