# pdf duplicator

This program helps me save glossy paper when I print PCB images from Eagle PCB Cad. I can get a row of pcb images at bottom of page, to cut off. Next time I increase vshift and use the same paper again.

`python duplicate.py <infilepath> <inithshift> <hshift> <vshift>`

Reads infile and creates a new file containing the contents of infile duplicated horizontally until it reaches the right edge.

Output file is named as infilepath with -duplicated before extension.

## parameters

<<<<<<< HEAD
infilepath - a pdf file
inithshift [mm] - horizontal shift, with positive in the right direction
hshift [mm] - horizontal shift between each duplicated
vshift [mm] - vertical shift of image top, up from bottom edge - higher value is in the upward direction

## example

python duplicate.py document1.pdf 0 50 40
=======
- infilepath - a pdf file
- inithshift [mm] - initial horizontal shift, with positive in the right direction
- hshift [mm] - horizontal shift between each duplicate
- vshift [mm] - vertical shift of image top, up from bottom edge - higher value is in the upward direction
>>>>>>> 0d1122a384a65bfd433b544a02d5a063f275bf51
