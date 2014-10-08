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
  

def scan(img, step, scale):
  w = img.size[0]
  h = img.size[1]
  block = int( w / step )
  width = block * step
  height = h // block * block
  print( w, h, width, height )
  img = img.crop((0, 0, width, height))
  
  image = Image.new('RGBA', (width*scale, height*scale))
  draw = ImageDraw.Draw(image)
  def circle(x, y, r):
    draw.ellipse((scale*(x-r), scale*(y-r), scale*(x+r), scale*(y+r) ), fill = 'black')

  for x in range(0, width , block):
    for y in range(0, height , block):
      darkness = 1 - ave_color(x, y, block, img)[3]/255
      radius = block / 2 * darkness * 1.25
      print(x, y, radius)
      
      circle( x+block/2, y+block/2, radius)

  image.save('c.png')

im = Image.open( 'c.jpg' )
scan(im, 150, 5)
