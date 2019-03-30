from PIL import Image

im = Image.open("space_wallpaper_steg.png")
width, height = im.size
pix = im.load()

def decode():
    c = ''
    st = ''
    binary_c = ''
    for x in range(width):
        for y in range(height):
            # get pixel rgb
            r,_,_ = pix[x, y]

            # convert red int to binary
            binary_r = format(r, 'b').zfill(8)

            # if one byte
            if len(binary_c) == 8:
                # convert byte to int
                int_c = int(binary_c, 2)

                # convert int to ascii
                c = chr(int_c)

                # appends character to string only if it's not '>'
                if c == '>':
                    return st
                st += c

                # clear byte for new character
                binary_c = ''

            binary_c += binary_r[-2:]

print('Calculating...')
data = decode()
print('Done.')

f = open('binarydata.txt', 'w')
f.write(data)
f.close()

print('Data saved in "binarydata.txt"')