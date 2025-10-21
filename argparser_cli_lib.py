# A framework for building customized commands for tooling purposes

import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument("name", help="is it so much to ask")
parser.add_argument("--greet", action="store_true", help="enter name please")
parser.add_argument("--politics", help="are you politically conscious", action="store_true")
#print(parser.__init__())
args = parser.parse_args()

if args.greet:
    print(f"hello {args.name}")
elif args.politics:
    print(f"politics is not good for you {args.name}")
else:
    print(f"rude man no greeting, {args.name}")

#time.sleep(10)