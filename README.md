# Recognising Text in Images Using EasyOCR

This [MLHub](https://mlhub.ai) package uses the EasyOCR package for
Python, available through PyPI, to perform optical character
recognition (OCR) from images.

The EasyOCR pacakge is available from
<https://github.com/JaidedAI/EasyOCR>.

This MLHub package source code is available from
<https://github.com/gjwgit/easyocr>.


## Quick Start

```console
$ ml ocr easyocr https://sharpie51.files.wordpress.com/2010/02/street_sign_for_abbey_road_in_westminster_london_england_img_1461.jpg
```

## Usage

- To install mlhub (Ubuntu):

		$ pip3 install mlhub
		$ ml configure

- To install, configure, and run the demo:

		$ ml install   easyocr
		$ ml configure easyocr
		$ ml readme    easyocr
		$ ml commands  easyocr
		$ ml demo      easyocr
		
- Command line tools:

	    $ ml ocr easyocr <path>  [-l <lang> ...]

Languages supported include: 
en (default), ch_sim, th, 

The output format per line is: <certainty>,<bounding box>,<text>

## Demonstrations

![](https://sharpie51.files.wordpress.com/2010/02/street_sign_for_abbey_road_in_westminster_london_england_img_1461.jpg
```console
$ ml ocr easyocr https://sharpie51.files.wordpress.com/2010/02/street_sign_for_abbey_road_in_westminster_london_england_img_1461.jpg
0.96,323 276 1326 276 1326 628 323 628,ABBEY
0.98,303 624 1144 624 1144 988 303 988,ROAD
0.94,1270 642 1956 642 1956 962 1270 962,NW8
0.5,670 1111 1797 1111 1797 1279 670 1279,OF WESTMINSTER
0.94,345 1135 625 1135 625 1275 345 1275,CITY
```

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png/220px-SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png)
```console
$ ml ocr easyocr https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png/220px-SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png -l th en
0.0,47 9 179 9 179 49 47 49,ทมข้แพพ้กทร็์
0.31,77 49 147 49 147 65 77 65,sim  cave
0.2,45 81 183 81 183 119 45 119,ภหมากพริก
0.11,61 119 167 119 167 135 61 135,phu mak prik
0.34,65 151 161 151 161 195 65 195,ภูหินปูน
0.11,67 191 159 191 159 207 67 207,phu hin pun
```

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Toronto_-_ON_-_Cecil_Street.jpg/1200px-Toronto_-_ON_-_Cecil_Street.jpg)
Identify both Simplified Chinese and English (option is `-l ch_cim en`):
```console
$ ml ocr easyocr https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Toronto_-_ON_-_Cecil_Street.jpg/1200px-Toronto_-_ON_-_Cecil_Street.jpg -l ch_sim en
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
0.86,294 173 653 173 653 313 294 313,CECIL
0.79,748 174 916 174 916 308 748 308,ST.
0.97,765 309 935 309 935 447 765 447,街
0.18,283 317 723 317 723 453 283 453,施 素
0.51,563 469 653 469 653 529 563 529,60
```
