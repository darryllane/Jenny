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
file_name = str(raw_input("\nDo you want to save this data to a file? \nBlank = NO | /path/filename = YES: "))
parts = words.split()

specials = "] [ ? / < ~ # ` ! @ $ % ^ & * ( ) + = } | : ; ' , > { " + " "

def write_file(data_list, file_name):
        try:
                with open(file_name, "a") as f:
                        for item in data_list:
                                f.write(item + "\n")
                                f.close
        except Exception as e:
                print e
                exit()

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
        indi_mangled = []
        mangled = []
        mangled_fupper = []
        mangled_upper = [word[:1].upper() + word[1:] for word in words]
        mangled_lower = [word[:1].lower() + word[1:] for word in words]
        mangled_prep = [word[:1].lower() + word[1:] for word in words]
        for s in itertools.permutations(mangled_upper, 3):
                mangled.append(''.join(s))
        for s in itertools.permutations(mangled_lower, 3):
                mangled.append(''.join(s))
        for s in itertools.permutations(mangled_prep, 3):
                mangled_fupper.append(''.join(s))
        for s in mangled_fupper:
                mangled.append(string.capwords(s))
        for word in words:
                mangled.append(word)
        
        for s in itertools.permutations(mangled_upper, 2):
                indi_mangled.append(''.join(s))
        for s in itertools.permutations(mangled_lower, 2):
                indi_mangled.append(''.join(s))
        for s in itertools.permutations(mangled_prep, 2):
                indi_mangled.append(''.join(s))
        for s in mangled_fupper:
                indi_mangled.append(string.capwords(s))
        for word in words:
                indi_mangled.append(word)
                
        joined_list = mangled + indi_mangled
        
        return joined_list

def add_leet(words):
        old_chars = ['a', 't', 'e', 'i', 's', 'o']
        new_chars = ['4', '7', '3', '1', '5', '0']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_leetALL = [s.translate(trs) for s  in  words]
        
        old_chars = ['a']
        new_chars = ['4']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_leetA = [s.translate(trs) for s  in  words] 
        
        old_chars = ['t']
        new_chars = ['7']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_someleetT = [s.translate(trs) for s  in  words] 
        
        old_chars = ['e']
        new_chars = ['3']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_someleetE = [s.translate(trs) for s  in  words]         
        
        old_chars = ['s']
        new_chars = ['5']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_someleetS = [s.translate(trs) for s  in  words]
        
        old_chars = ['i']
        new_chars = ['1']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_someleetI = [s.translate(trs) for s  in  words]    
        
        old_chars = ['o']
        new_chars = ['0']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_someleetO = [s.translate(trs) for s  in  words]
        
        old_chars = ['a']
        new_chars = ['@']
        trs = maketrans(''.join(old_chars), ''.join(new_chars))
        mangled_someleetAT = [s.translate(trs) for s  in  words]    
        
        mangled_leet = mangled_leetALL + mangled_leetA + mangled_leetALL + mangled_someleetAT + mangled_someleetE + mangled_someleetI + mangled_someleetO + mangled_someleetS + mangled_someleetT

        return mangled_leet


mangled_numbers = add_numbers(parts)
mangled_specials = add_specials(mangled_numbers)
mangled_parts = add_parts(parts)
number_mangle = add_numbers(mangled_parts)
specials_mangle = add_specials(number_mangle)
mangled_leet = add_leet(mangled_parts)

all_list = mangled_leet + mangled_numbers + mangled_parts + mangled_specials + specials_mangle + number_mangle
all_list.sort()

if file_name == '':
        file_name = None

for item in all_list:
        print item
        
if file_name is not None:
        write_file(all_list, file_name)
        
