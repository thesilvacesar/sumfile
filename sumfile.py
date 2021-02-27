import argparse
import engine.get_hash as hash

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="File for generate the hash")
parser.add_argument("--f", help="File for generate the hash")
args = parser.parse_args()

if args.f:
	hash.init(args.f)
else:
	file = input('[+] => File for generate the hash: ')
	hash.init(file)