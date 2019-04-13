import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int,
                    help="the first number")
parser.add_argument("y", type=int,
                    help="the second number")
parser.add_argument("-a", "--action", action='store', type=str, choices=['*', '/', '-', '+', '**'],
                    help="calculate numbers")
parser.add_argument("-v", "--verbose", action='store_true',
                    help="calculate numbers")

args = parser.parse_args()
if args.action == '*':
    answer = args.x * args.y
elif args.action == '/':
    answer = args.x / args.y
elif args.action == '+':
    answer = args.x + args.y
elif args.action == '-':
    answer = args.x - args.y
elif args.action == '**':
    answer = args.x ** args.y


if args.verbose:
    print(args.x, args.action, args.y, ' ', '=', ' ', answer)
else:
    print(answer)