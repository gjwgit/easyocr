# easyocr

https://github.com/JaidedAI/EasyOCR

```console
$ ml ocr easyocr <path> [-l <lang> ...]
```

Languages supported include: 
en (default), ch_sim, th, 


![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png/220px-SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png)
```console
$ ml ocr easyocr https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png/220px-SIM_CAVE_PHU_MAK_PRIK_PHU_HIN_PUN.png -l th en
0.0,47 9 179 9 179 49 47 49,ทมข้แพพ้กทร็์
0.31,77 49 147 49 147 65 77 65,sim  cave
0.2,45 81 183 81 183 119 45 119,ภหมากพริก
0.11,61 119 167 119 167 135 61 135,phu mak prik
0.34,65 151 161 151 161 195 65 195,ภูหินปูน
0.11,67 191 159 191 159 207 67 207,phu hin pun
20 Jul 15:47:54 gjw@yoga ~mlmodels/easyocr$ 
```
