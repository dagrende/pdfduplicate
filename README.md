# pdf duplicator

`python duplicate.py <infilepath> <inithshift> <hshift> <vshift>`

Reads infil and creates a new file containing the contents of infile duplicated horizontally until it reaches the right edge.

Output file is named as infilepath with -duplicated before extension.

parameters

infilepath - a pdf file
inithshift [mm] - horizontal shift, with positive in the right direction
hshift [mm] - horizontal shift between each duplicated
vshift [mm] - vertical shift of image top, up from bottom edge - higher value is in the upward direction
