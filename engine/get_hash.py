import os
import base64
import engine.misc as misc
from filehash import FileHash
import engine.layout as layout


def checksum(file, algo, base64 = False):
	sum = FileHash(algo)
	file_hash = sum.hash_file(file)

	if base64 != True:
		return file_hash
	else:
		return misc.b64(file_hash)


def b64hash(file):
	print(f'-' * 75)
	print('---> Base 64')
	print(f'-' * 75)

	print(
		"[+] MD 5 => " + checksum(file, 'md5', True),
		"\n[+] Sha 1 => " + checksum(file, 'sha1', True),
		"\n[+] CRC 32 => " + checksum(file, 'crc32', True),
		"\n[+] Sha 256 => " + checksum(file, 'sha256', True),
		"\n[+] Sha 512 => " + checksum(file, 'sha512', True),
		"\n[+] Adler 32 => " + checksum(file, 'adler32', True),
	)


def hexadecimal(file):
	print('---> Hexadecimal')
	print(f'-' * 75)

	print(
		"[+] MD 5 => " + checksum(file, 'md5'),
		"\n[+] Sha 1 => " + checksum(file, 'sha1'),
		"\n[+] CRC 32 => " + checksum(file, 'crc32'),
		"\n[+] Sha 256 => " + checksum(file, 'sha256'),
		"\n[+] Sha 512 => " + checksum(file, 'sha512'),
		"\n[+] Adler 32 => " + checksum(file, 'adler32'),
	)


def init (file):
	layout.header()

	hexadecimal(file)
	b64hash(file)
	
	layout.footer()

