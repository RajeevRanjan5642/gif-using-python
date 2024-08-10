# import version 3 of the imageio library
import imageio.v3 as iio

#  create a list of the image files
filenames = ['./images/cat-1.png','./images/cat-2.png',
             './images/cat-3.png'];

# create an empty list to store actual image data 
# from these files
images = [];

# read the image using .imread() method into images 
# list
for filename in filenames:
    images.append(iio.imread(filename));

# use imwrite method to turn the images into a GIF
iio.imwrite('gif/cat.gif',images,duration=500,loop=0);

# team.gif is name for the gif file to be created

# duration means how long each picture should show 
# in the gif in milliseconds

# loop means how many times the GIF should repeat 
# (0 means it keeps looping forever)



