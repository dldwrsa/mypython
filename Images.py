
import Image, ImageFilter
import ImageEnhance, ImageChops

im = Image.open('niel.jpg')
#im = im.rotate(-15)
#im.show()

print im.format, im.size, im.mode

##region = region.transpose(Image.ROTATE_180)
##region.paste(region, box)
##'''

flip = Image.open('bib.jpg')
flip = flip.transpose(Image.FLIP_LEFT_RIGHT)  # rotates it horisontally
#flip.show()

enhancing = ImageEnhance.Contrast(flip)
enhancing.enhance(1.5)
#enhancing.show()
#____________

##alph = Image.blend('weerlig.jpg', 'bib.jpg', 0.5)
##alph.show()

##box = (100,10,50,50)
##region = enhancing.crop(box)
##region.show()

#splitting = im.split()
#.show()

#imout = im.filter(ImageFilter.CONTOUR)
#imout.show()
#imout = im.filter(ImageFilter.FIND_EDGES)
#imout.show()
#imout = im.filter(ImageFilter.EMBOSS)
#imout.show()


#duplicate
##ima = Image.open('bib.jpg')
##ImageChops.duplicate(ima)
##img = Image.open('weerlig.jpg')
##
##ImageChops.lighter(ima,img)
##out = max(ima,img)
##out.show()

##import CrackCode
##img = Image.open('weerlig.jpg')
##CrackCode('weerlig.jpg', 100)
##print cc.area(img)

import Image, ImageDraw
##im = Image.open("bib.jpg")
##draw = ImageDraw.Draw(im)
##draw.line((0, 0) + im.size, fill=128)
##draw.line((0, im.size[1], im.size[0], 0), fill=128)
##del draw
##im.show()
### write to stdout
####im.save(sys.stdout, "PNG")
##
##imag = Image.open("weerlig.jpg")
##enh = ImageEnhance.Sharpness(imag)
##enh.enhance(20)

import ImageOps
#imag = Image.open("weerlig.jpg")
#n = ImageOps.equalize(imag)

#imag = Image.open("weerlig.jpg").convert("L;l")
#n = ImageOps.deform(imag)
#imag.show()

#import ImageStat
#s = ImageStat.Stat(imag)
#stat.count(s)





# new photo
im = Image.open("weerlig.jpg").convert("1")
im = im.rotate(-10)
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.show()

















