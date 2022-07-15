import easyocr
open('text_ocr_test.txt',"w").write('my hello world')
#ch_tra,ch_sim
reader = easyocr.Reader(['ch_tra','en'],gpu=True) # this needs to run only once to load the model into memory
print('sdsa')
result = reader.readtext('images/KXJJ-3961.jpg',detail = 0)
print(result)
open('text_ocr.txt',"w").write(str(result))