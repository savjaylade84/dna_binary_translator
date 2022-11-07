

"""
    Author: John Jayson B. De Leon
    Github: savjaylade84
    Email:savjaylade84@gmail.com

    tools for translating dna to binary and vice versa

    usage: dna_bin [options] [string]/[file] 
"""

import argparse


parser =  argparse.ArgumentParser(
    description = '''python tools for translating dna to binary and vice versa ''',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=''' 
Author: John Jayson B. De Leon 
Email: savjaylade84@gmail.com 
Github: savjaylade84 
''',prog='python3 dna_bin.py',usage='%(prog)s [options] [string]/[file]'
)

parser.add_argument('-s','--string',help='string of binary/dna')
parser.add_argument('-f','--file',help='file that contain binary/dna')
parser.add_argument('-d','--dna',
                                    help='translate binary to dna',
                                    action='store_true',
                                    default=False)
parser.add_argument('-b','--binary',
                                    help='translate dna to binary',
                                    action='store_true',
                                    default=False)

args = parser.parse_args()


# binary representation in dna
bin_dna:dict = {
        'A':'0000',
        'C':'0001',
        'G':'0010',
        'T':'0011'
}

# dna representation in binary
dna_bin:dict = {
        '0000':'A',
        '0001':'C',
        '0010':'G',
        '0011':'T'
}


def dna_to_bin(dna:str) -> str:
 
    binary:list = []
    for code in dna.upper():
        for key,value in bin_dna.items():
            if code == key:
                binary.append(value)
    return ''.join(item for item in binary)


def bin_to_dna(binary:str) -> str:

    temp:str = ''
    dna:list = []
    for index in range(0,len(binary)+1):

        if len(temp) == 4:
            for key,value in dna_bin.items():
                if temp == key:
                    dna.append(value)
                    temp=''

        # this stop from out of bound of list
        if index == len(binary):
            break
                        
        temp += binary[index]
    return ''.join(item for item in dna)            


def get_file_content(filename:str) -> str:
    with open(filename,'r') as file:
        return str(file.read())

def set_file_content(filename:str,content:str) -> None:
    with open(filename,'w') as file:
        file.write(content)

if(args.string):
    if(args.dna):
        print(f'translation: {bin_to_dna(args.string)}')
    if(args.binary):
        print(f'translation: {dna_to_bin(args.string)}')
        
if(args.file):
    if(args.dna):
        set_file_content(args.file,bin_to_dna(get_file_content(args.file)))
    if(args.binary):
        set_file_content(args.file,dna_to_bin(get_file_content(args.file)))


