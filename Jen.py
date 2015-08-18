#!/usr/local/bin/python

import itertools
import string
from string import maketrans

print """
                ____
               |    | ____   ____   ____ ___.__.
               |    |/ __ \ /    \ /    <   |  |
           /\__|    \  ___/|   |  \   |  \___  |
           \________|\___  >___|  /___|  / ____|
                         \/     \/     \/\/

 Jenny is a bespoke password generator.

 Simply feed Jenny's plant as many words as you like seporated by a
 space and she will spit out a password list based on those words.

             Author: Darryl Lane  |  Twitter: @darryllane101

 Example Usage:

              Feed Me Seymour!: First second third
"""

words = raw_input("Feed Me Seymour!: ")
parts = words.split()

specials = "] [ ? / < ~ # ` ! @ $ % ^ & * ( ) + = } | : ; ' , > { " + " "

def add_numbers(parts):
    values = list(range(1,7))
    mangled = []
    for part in parts:
        l = []
        val = ''
        for value in values:
            val += str(value)
            mangled.append(part + val)
    return mangled

def add_specials(mangled_list):
    special_list = specials.split()
    mangled = []
    for special in special_list:
        l = []
        val = ''
        for word in mangled_list:
            val += str(word)
            mangled.append(word + special)
    return mangled

def add_parts(words):
	mangled = []
	mangled_fupper = []
	mangled_upper = [word[:1].upper() + word[1:] for word in words]
	mangled_lower = [word[:1].lower() + word[1:] for word in words]
	mangled_prep = [word[:1].lower() + word[1:] for word in words]
	for s in itertools.permutations(mangled_upper):
		mangled.append(''.join(s))
	for s in itertools.permutations(mangled_lower):
		mangled.append(''.join(s))
	for s in itertools.permutations(mangled_prep):
			mangled_fupper.append(''.join(s))
	for s in mangled_fupper:
		mangled.append(string.capwords(s))
	for word in words:
			mangled.append(word)
	return mangled

def add_leet(words):
	old_chars = ['a', 't', 'e', 'i', 's', 'o']
	new_chars = ['4', '7', '3', '1', '5', '0']
	trs = maketrans(''.join(old_chars), ''.join(new_chars))
	mangled_leet = [s.translate(trs) for s  in  words]

	return mangled_leet


mangled_numbers = add_numbers(parts)
mangled_specials = add_specials(mangled_numbers)
mangled_parts = add_parts(parts)
number_mangle = add_numbers(mangled_parts)
specials_mangle = add_specials(number_mangle)
mangled_leet = add_leet(mangled_parts)


for item in mangled_numbers:
    print item
for item in mangled_specials:
    print item
for item in mangled_parts:
	print item
for item in number_mangle:
	print item
for item in specials_mangle:
	print item
for item in mangled_leet:
	print item

