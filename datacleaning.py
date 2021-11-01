# 这是林图图写给莫天琦的一个小工具。
# 希望淇淇在工作之余也能照顾好自己身体！
# （如果还需要别的需要，一定要找我哦！）
# 2021-09-14 封装记录
# 优化：
# 1.新增自动排序功能
# 2.删除第二次去重，合并到第一次，加快了去重速度
# 2021-10-29 优化记录
# 1.新增功能泛类目映射
# 2021-10-30 优化记录
from numpy import str_
import pandas as pd
from tkinter import *
from tkinter import filedialog
import re
import sys
import  ahocorasick

def first_wash():
    num = int(inp1.get())
    df = pd.read_excel(filePath1)
    i = 0
    regex = re.compile('\(.+?\)')

    while 1:
        if len(df) == i + 1:
            df.iloc[i,2] = df.iloc[i].values[2] + "1"
            break
        else:
            if df.iloc[i].values[0] == '':  # 避免了NaN
                df.iloc[i,0] = 'VK'
            if not isinstance(df.iloc[i].values[0],int):
                df.iloc[i,0] = df.iloc[i].values[0].lower() # 大写转为小写
            df.iloc[i,0] = regex.sub('', str(df.iloc[i].values[0]))  # 去括号
            df.iloc[i,0] = re.sub(u"\\（.*?）", "", df.iloc[i].values[0].encode('utf-8').decode())
            if df.iloc[i].values[0] == '':  # 避免了NaN
                df.iloc[i,0] = 'VK'
            if i % 100 == 0:
                print("去括号第",i)
            i = i + 1
    df = df.sort_values(by='行标签')
    i = 0
    city_list = []
    city_dict = {}
    while 1:
        j = i + 1
        city_list = []
        city_dict = {}
        city_list.append(df.iloc[i].values[2])
        city_dict[df.iloc[i].values[2]] = 1
        if i % 100 == 0:
            print("去重第",i)
        if len(df) == i + 1:
            break
        else:
            while 1:
                if j + 1 >= len(df):
                    break
                if df.iloc[j].values[0] == df.iloc[i].values[0] or df.iloc[j].values[0][:num] == df.iloc[i].values[0][:num]:
                    if df.iloc[j].values[2] in city_list:
                        city_list.append(df.iloc[j].values[2]) # 将城市名加入到 list 中
                        city_dict[df.iloc[j].values[2]] = city_dict[df.iloc[j].values[2]] + 1  # 更新门店数
                    else:
                        city_list.append(df.iloc[j].values[2]) # 将城市名加入到 list 中
                        city_dict[df.iloc[j].values[2]] = 1  # 更新门店数
                    df.iloc[i,2] = str(city_dict)
                    df.iloc[i,1] = df.iloc[i].values[1] + df.iloc[j].values[1]  # 则将门店数加入到第一个
                    df = df.reset_index(drop=True)
                    df = df.drop(index=j)   # 并删除该行
                    continue
                else:
                    break
            i = i + 1
    df = df.sort_values(by='行标签')
    df.to_excel(filePath2+"/result.xlsx")
    lb = Label(root, text="清洗完成！", justify=LEFT)
    lb.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
    print("清洗完成！")

def readLocalFile():
    global filePath1
    filePath1 = filedialog.askopenfilename()
    lb3 = Label(root, text=filePath1, justify=LEFT)
    lb3.place(relx=0.2, rely=0.1, relwidth=1, relheight=0.1)

def putLocalFile():
    global filePath2
    filePath2 = filedialog.askdirectory()
    lb3 = Label(root, text=filePath2, justify=LEFT)
    lb3.place(relx=0.2, rely=0.3, relwidth=1, relheight=0.1)

def panCategoryMapping():
    d = {'蔬':'生鲜果蔬', '果':'生鲜果蔬', '菜市':'生鲜果蔬', '蟹':'生鲜果蔬', '肉':'生鲜果蔬','集贸市场':'生鲜果蔬',\
        '药房':'药店/医疗销售',\
        '超市':'超市便利', '便利':'超市便利', '盒马':'超市便利', \
        '花鸟':'鲜花', '花艺':'鲜花', '花店':'鲜花', '花屋':'鲜花', '花房':'鲜花', '鲜花':'鲜花', '花卉':'鲜花',\
        '书':'书店',\
        '眼睛':'眼镜店',\
        '宠物':'宠物',\
        '中医':'医疗服务', '医院':'医疗服务', '医务':'医疗服务', '门诊':'医疗服务', '诊所':'医疗服务', '保健':'医疗服务', '爱康国宾':'医疗服务', '美年大健康':'医疗服务', '体检中心':'医疗服务', '康复中心':'医疗服务', '健康管理':'医疗服务',\
        '酒店':'酒旅', '民宿':'酒旅', \
        '轰趴':'景点/文化娱乐', '酒吧':'景点/文化娱乐', '剧':'景点/文化娱乐', '密室':'景点/文化娱乐', '洗浴':'景点/文化娱乐', '团建':'景点/文化娱乐',\
        '车行':'汽车养护', '电动车':'汽车养护',\
        '女装':'服装', '男装':'服装', '服饰':'服装', '服装':'服装', '鞋':'服装',\
        '化妆品':'美妆', '美妆':'美妆', '名妆':'美妆', '屈臣氏':'美妆', '莎莎':'美妆',\
        '百货':'百购', '购物中心':'百购', '奥特莱斯':'百购', '商厦':'百购', '商场':'百购',\
        '数码':'数码家电', '家电':'数码家电', '电器':'数码家电', '手机':'数码家电',\
        '家具':'家具家居', '家居':'家具家居', '全屋定制':'家具家居', '照明':'家具家居', '床垫':'家具家居', '灯具':'家具家居', '窗帘':'家具家居', '软装':'家具家居',\
        '美珍香':'食品', '零食':'食品', '休闲食品':'食品', '来伊份':'食品', '三只松鼠':'食品', '百草味':'食品', '良品铺子':'食品', '老婆大人':'食品', '盐津铺子':'食品', '优品铺子':'食品', '都市铺子':'食品', '集品铺子':'食品', '九品铺子':'食品', '恰货铺子':'食品', '熙品铺子':'食品', '欣品铺子':'食品', '李雷与韩梅梅':'食品', '零小闲':'食品', '魔呀':'食品', '怡佳仁':'食品', '悠百佳':'食品', '临期':'食品',\
        '母婴':'母婴', '孕婴童':'母婴', '童装':'母婴', '童鞋':'母婴',\
        '烟酒':'酒水', '酒':'酒水',\
        '茶叶':'茶叶', '茶行':'茶叶', '茶庄':'茶叶'}
    df = pd.read_excel(filePath1)
    i = 0
    regex = re.compile('\(.+?\)')
    while 1:
        if len(df) == i + 1:
            df.iloc[i,2] = df.iloc[i].values[2] + "1"
            break
        else:
            if df.iloc[i].values[0] == '':  # 避免了NaN
                df.iloc[i,0] = 'VK'
            if not isinstance(df.iloc[i].values[0],int):
                df.iloc[i,0] = df.iloc[i].values[0].lower() # 大写转为小写
            df.iloc[i,0] = regex.sub('', str(df.iloc[i].values[0]))  # 去括号
            df.iloc[i,0] = re.sub(u"\\（.*?）", "", df.iloc[i].values[0].encode('utf-8').decode())
            if df.iloc[i].values[0] == '':  # 避免了NaN
                df.iloc[i,0] = 'VK'
            theTree = ahocorasick.AhoCorasick("蔬", "果", "菜市", "蟹", "肉","集贸市场",\
            "药房",\
            "超市", "便利", "盒马", \
            "花鸟", "花艺", "花店", "花屋", "花房", "鲜花", "花卉",\
            "书",\
            "眼睛",\
            "宠物",\
            "中医", "医院", "医务", "门诊", "诊所", "保健", "爱康国宾", "美年大健康", "体检中心", "康复中心", "健康管理",\
            "酒店", "民宿", \
            "轰趴", "酒吧", "剧", "密室", "洗浴", "团建",\
            "车行", "电动车",\
            "女装", "男装", "服饰", "服装", "鞋",\
            "化妆品", "美妆", "名妆", "屈臣氏", "莎莎",\
            "百货", "购物中心", "奥特莱斯", "商厦", "商场",\
            "数码", "家电", "电器", "手机",\
            "家具", "家居", "全屋定制", "照明", "床垫", "灯具", "窗帘", "软装",\
            "美珍香", "零食", "休闲食品", "来伊份", "三只松鼠", "百草味", "良品铺子", "老婆大人", "盐津铺子", "优品铺子", "都市铺子", "集品铺子", "九品铺子", "恰货铺子", "熙品铺子", "欣品铺子", "李雷与韩梅梅", "零小闲", "魔呀", "怡佳仁", "悠百佳", "临期",\
            "母婴", "孕婴童", "童装", "童鞋",\
            "烟酒", "酒",\
            "茶叶", "茶行", "茶庄")
            result = theTree.search(df.iloc[i].values[0])
            if len(result) != 0:
                result = list(result)
                word = d[result[0]]
                df.loc[i,3] = word
            if i % 100 == 0:
                print("泛类目映射第",i)
            i = i + 1
    df.to_excel(filePath2+"/result.xlsx")
    lb = Label(root, text="泛类目映射完成！", justify=LEFT)
    lb.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
    print("泛类目映射完成！")
    

# def categoryMapping():
#     print()

root = Tk()
root.geometry('500x240')
root.title('数据清洗工具')

lb1 = Label(root, text='读取Excel路径：')
lb1.place(relx=0, rely=0.1, relwidth=0.3, relheight=0.1)
lb2 = Label(root, text='存放Excel路径：')
lb2.place(relx=0, rely=0.3, relwidth=0.3, relheight=0.1)
lb3 = Label(root, text='精确字符数')
lb3.place(relx=0, rely=0.6, relwidth=0.3, relheight=0.1)

btn1 = Button(root, text='数据清洗', command=first_wash)
btn1.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.2)
btn2 = Button(root, text='读取EXCEL路径', command=readLocalFile)
btn2.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
btn3 = Button(root, text='结果存放路径', command=putLocalFile)
btn3.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
btn4 = Button(root, text='泛类目映射', command=panCategoryMapping)
btn4.place(relx=0.7, rely=0.6, relwidth=0.2, relheight=0.2)
# btn5 = Button(root, text='类目映射', command=categoryMapping)
# btn5.place(relx=0.8, rely=0.6, relwidth=0.2, relheight=0.2)

inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.1)

root.mainloop()
