# Image Resizing(get fullinfo from google) ---
#      using Seam carving using OpenCV
#      Bicubic Interpolation-OpenCV
#      interpolation algorithms include the nearest neighbor, bilinear, bicubic
#      Mahotas – Resizing Image
#      Image Resizing in Matlab

# Choice of Interpolation Method for Resizing:
#
#      cv2.INTER_AREA: This is used when we need to shrink an image.
#      cv2.INTER_CUBIC: This is slow but more efficient.
#      cv2.INTER_LINEAR: used when zooming is required.Default interpolation technique in OpenCV.
# Syntax: cv2.resize(source, dsize, dest, fx, fy, interpolation)
