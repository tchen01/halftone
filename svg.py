import math
import cairo
from PIL import Image, ImageDraw
    
def ave_color(xx, yy, n, img):
  r, g, b = 0, 0, 0
  count = 0
  for x in range(xx, xx+n):
    for y in range(yy, yy+n):
      count += 1
      p = img.getpixel( (x,y) )
      r+= p[0]
      g+= p[1]
      b+= p[2]
  r /= count
  g /= count
  b /= count
  v = (r + g + b)/3
  c = (r, g, b, v)
  return c
  

def scan(img, step):
  b = 10

  ww = img.size[0]
  hh = img.size[1]
  block = int( ww / step )
  width = block * step
  height = hh // block * block
  w = int(width/block)
  h = int(height/block)
  img = img.crop((0, 0, width, height))
  
  print('<?xml version="1.0" encoding="UTF-8"?>')
  print('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+str(w * b)+'pt" height="'+str(h * b)+'pt" viewBox="0 0 ',w * b, h * b,'" version="1.1">')
  print('<g id="surface1">')

  for x in range(0, width, block):
    for y in range(0, height, block):
      darkness = 1 - ave_color(x, y, block, img)[3]/255
      radius = int(darkness * 1.1 / 2 * b * 10000) / 10000
      print('<circle cx="'+str(b* (x/block+.5))+'" cy="'+str(b* (y/block+.5))+'" r="'+str(radius)+'" fill="black" />')
      
  print('</g></svg>')
     

im = Image.open( 'b.jpg' )
scan(im, 80)




