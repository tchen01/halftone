from PIL import Image, ImageDraw

im = Image.open( "in.png" )
width = im.size[0]
height = im.size[1]

scale = 5
image = Image.new('RGBA', (width*scale, height*scale))
draw = ImageDraw.Draw(image)

def circle(x, y, r):
  draw.ellipse((scale*(x-r), scale*(y-r), scale*(x+r), scale*(y+r) ), fill = 'black', outline ='black')

#do u even use?
def bw( c ):
  sum = c[0] + c[1] + c[2]
  if ( sum < 383 ):
    return 1
  else:
    return 0
    
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
  #print( c )
  return c
  

def scan(img, step):
  block = int( width / step )
  print( block )
  for x in range(0, width, block):
    for y in range(0, height, block):
      print(x, y)
      darkness = 1 - ave_color(x, y, block, img)[3]/255
      radius = block / 2 * darkness * 1.4
      print( radius )
      
      circle( x+block/2, y+block/2, radius)


scan(im, 300)
#ave_color(0,0,100,im)
  
image.save('out.png')