#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ast import FloorDiv
from distutils.log import warn
import linecache
from logging import error
import os
import os.path
import re
import subprocess
import argparse
import shutil
import sys
import easyocr
#ch_tra,ch_sim


writeinfo=''''''

booktxt ='''|0|field|name|download|
'''

sub = '## {}  '
book = '- {} | {}  '


d = 'book/'
t = 'images/'
reader = None
def process():        
    if not os.path.exists(t):
        os.mkdir(t)
    folders = [os.path.join(d, o) for o in os.listdir(
        d) if os.path.isdir(os.path.join(d, o))]
    # folders.sort()

    startBookId = 0
    for folderName in os.listdir(d):
        if folderName=='_srcs':
            continue
        startBookId += 10000
        bookId = startBookId
        folder = os.path.join(d, folderName)
        if os.path.isdir(folder):
            # igonre .D file
            if folderName.startswith('.'):
                continue
        
            print(folder)
            
            # thisSub = sub.format(folderName)
            # readme += thisSub+'\n'

            targetFolder = os.path.join(t, folderName)
            if not os.path.exists(targetFolder):
                os.mkdir(targetFolder)
            for file in  os.listdir(folder):
                #only process pdf file
                if not file.endswith('.pdf'):
                    continue

                bookId += 1
                sourceFileName = os.path.join(folder, file) 
                
                
                file = file.replace(' ','-')
                targetFileName = os.path.join(folder, file) 
                
                if sourceFileName != targetFileName:
                    os.rename(sourceFileName,targetFileName)
                        
                fileDir = os.path.join(targetFolder, file) .replace('.pdf','')
                if not os.path.exists(fileDir):
                    os.mkdir(fileDir)
                print(file+' file')
                txtName = os.path.join(targetFolder, file) .replace('.pdf','.txt')
                #had write txt continue
                if os.path.exists(txtName):
                    print(file+' file had done')
                    continue
                writeinfo =''
                pngName = os.path.join(fileDir, file).replace('.pdf','_%d.jpg')
                shaderCommand = '''gs -dSAFER -dQUIET -dNOPLATFONTS -dNOPAUSE -dBATCH -sOutputFile=\"'''+pngName+'''\" -sDEVICE=jpeg -r144  -dUseTrimBox -dFirstPage=1 '''+targetFileName
                # print(shaderCommand)
                returnCode = subprocess.call(shaderCommand, shell=True)
                if returnCode !=0 :
                    error(targetFileName+" result:"+str(returnCode) )
                else:
                    print(pngName+' processed')
                    for jpgFileName in  os.listdir(fileDir):
                        if not jpgFileName.endswith('.jpg'):
                            continue
                        
                        jgpFilePath = os.path.join(fileDir, jpgFileName)
                        print(jgpFilePath+' processed')
                        txtFilePath = jgpFilePath.replace('.jpg','.txt')
                        info=''
                        if os.path.exists(txtFilePath):
                            info = open(txtFilePath, "r").read()
                            print(jgpFilePath+' had processed done:'+info)
                        else:
                            result = reader.readtext(jgpFilePath,detail = 0)
                            info  = str(result)
                            print(jgpFilePath+' result:'+info)
                            open(txtFilePath, "w").write(info)

                        # open('text_ocr.txt',"w").write(str(result))
                        thisBook = book.format(jpgFileName,info)
                        writeinfo += thisBook+'\n'
                open(txtName, "w").write(writeinfo)

                # break



if __name__ == "__main__":
    if len(sys.argv) >= 2:
        d = sys.argv[1]
        t = d+'/../images'
    else:
        error('no argument,please input like:  get_png_text.app \{pdfpath\} ch_sim ')
        
    
    if len(sys.argv) >= 3:
        if sys.argv[2] =='ch_sim':
            reader = easyocr.Reader(['ch_sim','en'],gpu=True) # this needs to run only once to load the model into memory
        else:
            reader = easyocr.Reader(['ch_tra','en'],gpu=True) # this needs to run only once to load the model into memory
        print('load reader')
    else:
        reader = easyocr.Reader(['ch_tra','en'],gpu=True) # this needs to run only once to load the model into memory

    process()