import os, sys, base64

print "\t########################################"
print "\t#	 Base64 encode & decoded	#"
print "\t#	Write and coded by aditya	#"
print "\t#	          A.K.A			#"
print "\t#	      Mr. Problema		#"
print "\t#		INDONESIA		#"
print "\t########################################"

def encode():
	tampan = raw_input("type word for hash: ")
	print "success!!, hash is ",base64.b64encode(tampan)

def decode():
	tampan2 = raw_input("type hash for crack: ")
	print "success!!, word is ", base64.b64decode(tampan2)

print "1) Base64 encode"
print "2) Base64 decode"
user = int(raw_input("select tools: "))
if user == 1:
	encode()
elif user == 2:
	decode()
else:
	print "wrong number"
