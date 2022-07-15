# PDF提取PNG及文字
本项目环境为：MacOS 10.14.5  
这个是一个从PDF中，将每页导出成图片，然后从图片中提取文字的小项目，并将文字按照固定模式写成markdown格式的文件  
项目环境不支持CUDA，所以提取文字速度感人    
希望看到的人用的是PC机或者M1以上Mac，这样默认是可以支持CUDA的。  
PS：如果PDF内容本身为文字性的，建议不要用OCR方案提取文字，而是直接使用下文提到的gs直接提取文字。  
## 0.效果
原图  
![康轩学习](https://workbooko1.oss-cn-hangzhou.aliyuncs.com/uPic/KXJJ-396_2.jpg)
结果  
```
['Topsu5`進階版', '康軒望召雜誌', '目次', '2', 'Top', '黑翅鳶上工婁!', "最近黑翅鳶界在流傳'只要站在農田中央的超高棲架'並幫忙農", '夫做點工作', '就能每天吃大餐', '拍網美炤呢!各位黑翅鳶夥伴', '', '趕快前進農田', '準備上工吧!', '*配合領域:國小社會六下 文明與科技生活]', '國中自然與生活科技一下[人類與環境]', 'Top 補充包', '11~14', '生態農業~很自然幄!', '在農地裡', '種植許多種類的農作物', '並且讓蔬菜', '和野草共同生長', '這就是生態農業', '為什麼要這', '麼做呢?讓生態研究員告訴你', '小樂祕密日記', '15 ~ 16', '搬家大作戰', '走進地球村', '17 ~ 20', "小樂準備搬離住+年的家'最近超級認", '澳洲野火燒死無尾熊', '真整理房間!這工作雖然辛苦;但好像', '澳洲野火不斷延燒', '新南威爾斯地區也傳', "打開了回憶寶盒'讓小樂想起很多有趣", "出火災災情'當地一處自然保護區中;甚", '的事情呢', '至有350隻無尾熊', '在火災中被燒死', '*配合領域', '社曾', '*配合領域:社會', '21', 'Top', '貝多芬的人生交響樂', "樂聖貝多芬喜歡組合樂器的聲音'譜出美妙的曲子;更擅長在樂譜上多加幾個音", "符`改變節奏'讓樂曲聽起來T很不一樣_", '也讓優雅的古典音樂', '變得更活潑', '0', '*配合領域:國小藝術與人文六下 音樂聯合國_', "國中藝術與人文二上'傾聽古典的樂音_", '社會任意門', '31 ~ 34', '管弦樂器知多少?', "由管弦樂團演出的交響曲'使用的樂器和演", '出的樂手,數量眾多.不同的樂音層層交', "織'讓曲子聽起來更加迷人 ,一起來認識這", '些管弦樂器吧 !', '新鮮事', '主題館']
```
## 1.安装Python3
官网下载Python安装即可，如果是mac，可以用brew安装  
```
brew install python3
```
## 2.安装pip
Python包管理器，方便后续安装需要的包
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
sudo python3 get-pip.py    # 运行安装脚本。
```
如果你已经安装过pip了，建议先进行升级，避免许多奇葩问题 
```
pip3 install --upgrade pip
```
## 3.安装ghostscript
这个库用来从PDF生成图片
```
brew install ghostscript
```
## 4.安装easyocr
A.图片中的文字识别库  
### A.pip安装
```
sudo pip3 install easyocr    # 运行安装脚本。
```
### B预编译版本安装
因为使用pip安装需要本机编译，速度感人，所以这里选用已经编译好的包  
下载地址：https://pypi.org/project/easyocr/#files  
## 5.运行Python代码提取图片和文字
将pdf文件扔到book目录下的子目录中，然后运行Python脚本即可...   
```
python3 get_png_text.py
```
## *问题归纳*
easyocr最新版本1.5.0用的对应opencv-python-handness为4.5.4.60版本，需要做一些修改才能编译成功  
### 1.import easyocr报错
```
ImportError: dlopen(/usr/local/lib/python3.9/site-packages/torch/_C.cpython-39-darwin.so, 2)
```
解决办法:更新libomp  
```
brew install libomp
```
### 2.安装opencv-python-handness报错
将source code下载到本地，通过‘python setup.py install’的形式安装，因为这样可以改setup.py的代码  
```
Not found: 'python/cv2/gapi/.*.py'
```
解决办法:  
opencv-python-headless-4.5.4.60版本 注释setup.py中部分代码:  
```
        # "cv2.gapi": [
        #     "python/cv2" + r"/gapi/.*\.py"
        # ],
```        
注释  
```
#from . import gapi
```
取消默认值  
```
            cmake_source_dir="",
            cmake_install_dir=cmake_install_reldir,
```