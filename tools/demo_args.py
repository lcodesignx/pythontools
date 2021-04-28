#!/usr/bin/env python3
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def run_parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument(
            "num",
            help="the fibonacci number you wish to calculate",
            type=int
    )
    parser.add_argument(
            '-o',
            '--output',
            help='output result to a file',
            action='store_true'
    )
    args = parser.parse_args()
    result = fib(args.num)
    if args.verbose:
        print(f'The {args.num}th fib number is {result}')
    elif args.quiet:
        print(result)
    else:
        print(f'fib({args.num}) = {result}')

    if args.output:
        with open('fib.txt', 'a') as f_obj:
            f_obj.write(f'{args.num}th : {result}\n')

if __name__ == '__main__':
    run_parse()
