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
  print( w, h )
  img = img.crop((0, 0, width, height))
  

  surface = cairo.SVGSurface('out.svg', b * w, b * h)
  ctx = cairo.Context (surface)

  for x in range(0, width, block):
    for y in range(0, height, block):
      darkness = 1 - ave_color(x, y, block, img)[3]/255
      radius = darkness * 1.1 / 2 * b
      print(x, y, radius)
      ctx.arc (b* (x/block+.5), b*(y/block+.5), radius, 0, 2*math.pi) # Arc(cx, cy, radius, start_angle, stop_angle)
      ctx.fill()
      ctx.close_path ()
      ctx.stroke ()
     

im = Image.open( 'b.jpg' )
scan(im, 80)




