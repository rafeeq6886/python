import imageio.v3 as iio

filenames = ['IMG-20250807-WA0003.jpg', 'IMG-20250807-WA0004.jpg','IMG-20250807-WA0005.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('london.gif', images, duration = 200, loop = 0)
