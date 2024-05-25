'''
Created on Aug 24, 2021

@author: Cyrus
'''

######################
### PYTHON IMPORTS ###
######################

import json
import subprocess

#################
### FUNCTIONS ###
#################

def leading_zeros(num, num_of_digits):
    '''Adds leading zeros to a string that's supposed to be a certain number of digits in length'''
    if(isinstance(num, int)):
        if(num < 0):
            num += 0x10000
        num = str(hex(num))[2:].upper()
    while (len(num) < num_of_digits):
        num = "0" + num
    return num

def read_json(json_file_dir):
    '''Reads contents of a JSON file into a dictionary and returns that dictionary'''
    with open(json_file_dir, "r") as jf:
        json_content = json.load(jf)
    return json_content

def dump_json(json_file_dir, use_this_dict):
    '''Reads contents of a JSON file into a dictionary and returns that dictionary'''
    with open(json_file_dir, "w+") as jf:
        json_content = json.dump(use_this_dict, jf, indent = 4)

# def apply_patch(xdelta_path, old_file_path, delta_file_path, new_file_path):
#     # xdelta -d -s old_file delta_file decoded_new_file
#     cmd = f"{xdelta_path}xdelta.exe -d -s {old_file_path} {delta_file_path} {new_file_path}"
#     print(cmd)
#     subprocess.Popen(cmd.split(), shell=True).communicate()
# 
# def create_patch(xdelta_path, old_file_path, new_file_path, delta_file_path):
#     # xdelta -e -s old_file new_file delta_file
#     cmd = f"{xdelta_path}xdelta.exe -e -s {old_file_path} {new_file_path} {delta_file_path}"
#     subprocess.Popen(cmd.split(), shell=True).communicate()

def possible_negative(int_val):
    '''If value would be a negative hex value (greater than 0x8000), converts to negative. Otherwise returns initial value'''
    if(int_val > 0x8000):
        int_val -= 0x10000
    return int_val

def fit_for_hex(int_val):
    '''Prepares value for hex conversion'''
    int_val %= 0x10000
    return int_val

def get_address_endpoints(file_bytes, addr):
    """Goes to address (found in Banjo's Backpack) and address 8 bytes after to find the start and end of a setup file"""
    addr_int = int(addr, 16)
    byte_list = [f"{file_bytes[addr_int + byte_num]:02x}" for byte_num in range(16)]
    
    address1 = int("".join(byte_list[:4]), 16) + 0x10CD0
    address2 = int("".join(byte_list[8:12]), 16) + 0x10CD0
    
    return address1, address2
