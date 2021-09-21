import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value', help='store simple value')
parser.add_argument('-c', action='store_const', dest='constant_value', const='value-to-store',
                    help='store constant value')
parser.add_argument('-t', action='store_true', default=False, dest='boolean_switch', help='set a switch to true')
parser.add_argument('-f', action='store_false', default=False, dest='boolean switch', help='set a switch to false')
parser.add_argument('-a', action="append", dest='collection', default=[], type=int,help='add repeated values to list')
parser.add_argument('-A', action='append_const', dest='const_collection', const='300',
                    help='add different values to list')
parser.add_argument('--version', action='version', version='1.0')
result = parser.parse_args()
print(result.simple_value)
print(result.collection)
print(result.const_collection)

