# JPEGcheck
A small python module to check jpeg headers
This little bit of code came to me while I was downloading a large set of images for training a dataset.
Some of the downloaded images did not seem to be JPEG files, so I searched the internet to find some simple solution.
Since I couldn't find any, I coded this tiny module.

To use:
Put the JpegCheck.py in the same dir.
from JpegCheck import jpegcheck
jpegcheck("file.jpg")

The function will return True if it is a jpeg file, else False
