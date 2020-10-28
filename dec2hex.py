#!/usr/bin/env python3
# dec2hex.py	
def dec2hex(dec):
	hexValue = hex(dec)
	hexS = str(hex(dec))
	h = hexS.replace('0x' , '')
	print(dec,hexValue,h) # debug

def main():
	hexString = dec2hex(10)
	hexString = dec2hex(245)
	
main()

'''
functions 
return a string from a function
string function replace
'''
