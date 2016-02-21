#!/usr/bin/python

import getopt
import sys


def main(argv):
    n = 0
    k = 0
    try:
        opts, args = getopt.getopt(argv, "n:k:")
    except getopt.GetoptError:
        print 'app.py: -n <characters> -k <pairs>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-n':
            try:
                n = int(arg)
            except:
                print 'The -n parameter should be a number'
                sys.exit(2)

            if any([n <= 0, n >= 50]):
                print 'n shoul be positive and lower than 51'
                sys.exit()

        elif opt == '-k':
            try:
                k = int(arg)
            except:
                print 'The -k parameter should be a number'
                sys.exit(2)

            if any([k < 0, k < (1 + (n * ((n - 1) / 2)))]):
                print 'k shoul be positive and lower than (1 + (n * ((n - 1)/2)))'
                sys.exit()

    print 'n: ', n
    print 'k: ', k


if __name__ == "__main__":
    main(sys.argv[1:])
