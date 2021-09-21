import argparse

# parser = argparse.ArgumentParser(description='sample app',fromfile_prefix_chars='@')
#
# parser.add_argument('-a',action='store_true',default=False)
# parser.add_argument('-b',action='store',dest='b')
# parser.add_argument('-c',action='store',dest='c',type=int)
#
# print(parser.parse_args(['@abc.txt']))

parser = argparse.ArgumentParser()
parser.add_argument('--three',nargs=3)
parser.add_argument('--optional',nargs='?')
parser.add_argument('--one-or-more',nargs='*')

print(parser.parse_args())