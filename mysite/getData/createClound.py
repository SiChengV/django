import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


def ciyun():
    text = open("C:/Users/SiChengZ/OneDrive/桌面/django/mysite/getData/text2", "rb").read()
    # 结巴分词
    wordlist = jieba.cut(text, cut_all=True)
    wl = " ".join(wordlist)
    # print(wl)#输出分词之后的txt


    # 把分词后的txt写入文本文件
    # fenciTxt  = open("fenciHou.txt","w+")
    # fenciTxt.writelines(wl)
    # fenciTxt.close()


    # 设置词云
    wc = WordCloud(background_color="black",  # 设置背景颜色
                   # mask = "图片",  #设置背景图片
                   max_words=2000,  # 设置最大显示的字数
                   # stopwords = "", #设置停用词
                   font_path="simfang.ttf",
                   # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
                   max_font_size=200,  # 设置字体最大值
                   random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                    width=2000,height=1200,
                    min_font_size=20,
                   )
    myword = wc.generate(wl)  # 生成词云

    # 展示词云图
    # plt.imshow(myword)
    # plt.axis("off")
    # plt.show()
    myword.to_file('C:/Users/SiChengZ/OneDrive/桌面/django/mysite/static/search/img/ciyun.png')