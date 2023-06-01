# spelling_correcter_en
## 实现英文文本纠错

1、通过spelling_correcter获取可能的所有替换候选

2、通过kenlm计算候选中的3-gram打分，将打分最高的当作最终替换结果。


## 使用方法

1、首先准备自己的单词词典，保存到data/count.txt，格式：每行一个单词，需要大写，例

head data/count.txt
APPLE
BOTTOMED
JUDIT
MYROVER
OVEREAGER
PINDER
PLASMATIC
VRCHLABI
HAPPY
HELLO

2、训练语言模型，获取arpa文件，保存到data/lm_binary.arpa；

3、获取词典单词Soundex值，执行 python3 tools/data/get_soundex_code.py 生成；

4、文本纠错，当前提供2种方式：

（1）基于编辑距离获取候选（性能好，速度慢）

     python3 tools/main_l_dis.py input.txt output.txt

（2）只获取发音相近候选单词（速度快）

     python3 tools/main_soundex.py input.txt output.txt

 其中input.txt为输入文本，格式ID + 空格 + 文本，output.txt为输出结果，例

    input.txt  ----> test 'M SO GLAD

    output.txt ----> test I'M SO GLAD


## 参考代码
https://github.com/percent4/-word-.git

https://github.com/kpu/kenlm
