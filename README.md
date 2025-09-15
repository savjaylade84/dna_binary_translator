## Binary to DNA or Vice Versa <br>

#### tools that translate binary to dna or vice versa in direct or in file <br>

#### Note: i use 4 bits as representation for each letters in dna. <br>

#### Package Userd
- argparse

#### How to Use It <br>
``` python3 dna_bin.py [option (type of translation/type of data)] [string]/[file] ```

translate binary to dna in direct string <br>
``` python3 dna_bin.py -ds [string] ```

translate dna to binary in direct string <br>
``` python3 dna_bin.py -bs [string] ```

translate binary to dna in file <br>
``` python3 dna_bin.py -df [file] ```

translate dna to binary in file <br>
``` python3 dna_bin.py -bf [file] ```

#### Optional Arguments <br>

```-h```,```--help```         show this help message and exit <br>
```-s```,```--string```       string of binary/dna <br>
```-f```,```--file```         file that contain binary/dna <br>
```-d```,```--dna```          translate binary to dna <br>
```-b```,```--binary```       translate dna to binary <br>
