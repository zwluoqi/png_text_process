gs -dSAFER -dQUIET -dNOPLATFONTS -dNOPAUSE -dBATCH -sOutputFile="export/xxoo%d.jpg" -sDEVICE=jpeg -r144  -dUseTrimBox -dFirstPage=1 book/test/KXJJ-396.pdf
#   -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dUseCIEColor


# gs -dSAFER -dQUIET -dNOPLATFONTS -dNOPAUSE -dBATCH \
#   # When converting multiple-page PDFs you should add "%d" to the filename-string 
#   # which will be replaced with the sequence-number of the file
#   -sOutputFile="xxoo.png" \
#   # Create a PNG-File with alpha-transparency
#   -sDEVICE=pngalpha
#   # resolution in DPI
#   -r72 \ 
#   # Use high grade text antialiasing. Can be 0, 1, 2 or 4
#   -dTextAlphaBits=4 \
#   # Use high grade graphics anti-aliasing. Can be 0, 1, 2 or 4
#   -dGraphicsAlphaBits=4 \
#   # If you are converting a CMYK-PFD to RGB-color you should use CIE-Color
#   -dUseCIEColor \
#   # use the PDFs Trim-Box to define the final image
#   -dUseTrimBox \
#   # start converting on the first side of the PDF
#   -dFirstPage=1 \
#   # convert only until the first page of the PDF
#   -dLastPage=1 \
#   # Path to the file you want to convert
#   gpu_pro_360/GPU-PRO-360_Guide-to GPGPU-(PDFDrive).pdf