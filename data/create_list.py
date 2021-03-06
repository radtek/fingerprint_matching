#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import re
import random
import sys

VALID_RANGE = 30
QUERY = 'query'
REFERENCE = 'reference'

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x<arr[0]]) + \
            [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

def get_valid_output_list(input_path):
    minutia_files = os.listdir(input_path)
    output_list = []
    for mf in minutia_files:
        match = re.findall(r'([0-9]+)[\s-]*\.txt', mf)
        if match:
            num = int(match[0])
            if num < VALID_RANGE:
                output_list.append(mf)
    return output_list

def create_order_list(input_path):
    output_list = get_valid_output_list(input_path)
    output_list = qsort(output_list)
    output_name = input_path.split('/')[-1] + '.txt'
    output_file = open(output_name, 'w')

    for i in range(len(output_list)):
        output_file.write(os.path.join(input_path, output_list[i]))
        output_file.write('\n')

def create_random_list(input_path, select_num):
    output_list = get_valid_output_list(input_path)
    output_name = input_path.split('/')[-1] + '.txt'
    output_file = open(output_name, 'w')

    random_list = []
    while len(random_list) < select_num:
        random_num = random.randrange(len(output_list))
        while random_num in random_list:
            random_num = random.randrange(len(output_list))
        random_list.append(random_num)
    print random_list

    for index in random_list:
        output_file.write(os.path.join(input_path, output_list[index]))
        output_file.write('\n')

if __name__ == '__main__':
    try:
        direct = sys.argv[1]
        select_num = int(sys.argv[2])
        query_path = os.path.join(direct, QUERY)
        reference_path = os.path.join(direct, REFERENCE)

        create_random_list(query_path, select_num)
        create_order_list(reference_path)
    except:
        print 'usage: ./create_list.py <directory> <select number>'
