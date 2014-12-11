#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2

'''
Converts CSV files into a LaTeX table body.
'''

import argparse
import csv

def main():
    options = _parse_args()

    rows = []
    output = []

    with open(options.input) as f:
        if options.split:
            for line in f:
                line = line.replace("#", "%")
                line = line.strip()
                rows.append(line.split())
        else:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
                

    for row in rows:
        output.append(options.linestart + ' & '.join(row) + r' \\' +
                      options.lineend)

    with open(options.output, 'w') as f:
        f.write('\n'.join(output))
        f.write('\n')


def _parse_args():
    """
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',
                        help='Input CSV file')
    parser.add_argument('output',
                        help='Output TeX file')
    parser.add_argument('--linestart', default='',
                        help='Prepend to each line')
    parser.add_argument('--lineend', default='',
                        help='Append to each line')
    parser.add_argument('--delimiter', default=' ',
                        help='Field delimiter in CSV mode')
    parser.add_argument('--split', action='store_true',
                        help='Just split at the given token')

    return parser.parse_args()


if __name__ == "__main__":
    main()
