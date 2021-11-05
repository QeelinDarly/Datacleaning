# Datacleaning
datacleaning tools for Business analysis

This program is made for Vicky's work. You can use it, too.

# Attention
Before you use it. Please change your excel's format.

The first column is your target store name. If you want to use wash, you need change A1 name as '行标签', but if you just use pan category mapping, please forget it.

The second column is the number of target store, default is 1. Program will merge the same name store and sum numbers.

The third column is the local of your target store. We have not use it now, but we want to count it.

Please leave the forth column blank, because we will add the result of pan category mapping in here. Of cause, if you don't use it, forget it.

# Usage
Before you build it, you need to have right environment. You need have python3 and numpy、 pandas、 ahocorasick-python、 openpyxl.

```python
pip3 install numpy
pip3 install pandas
pip3 install ahocorasick-python
pip3 install openpyxl
```

And after that, you can build it by this:

```python
pip3 install pyinstaller
pyinstaller -F datacleaning.py
```

You can use it now, and executable program is in file dist.

The first buttom, you can read excel file path by it.

The second button, you can choose the path to save your result file. The result file name is result.xlsx

You can select the exact number of characters in text, the program will merge your store name by it.

If you just want to use pan category mapping, you can blank the text. But if you want to use datacleaning, you must fill it.

# 数据清洗
该数据清洗工具是为了商业分析

这个程序是为了Vicky的工作而开发的，公开代码后，您也可以免费使用它。

# 注意事项
在你使用该程序之前，请改变你的Excel格式。

第一列是你的目标店名。如果你想用数据清洗，请你在A1单元格写入‘行标签’，但是如果你只使用泛类目映射，请无视它。

第二列是目标店铺的门店数，默认为1。程序将会合并所有名字相同的店名。

第三列是你目标店铺的地址。我们暂时没有使用这个字段，但是我们将在未来推出统计店铺地址的功能。

请将第四列空出，因为我们需要将泛类目映射的结果写在这里。当然，如果你不用这个功能，请无视它。

# 使用方法
在你编译它之前，你需要有正确的环境。你需要有python3和它的一系列库，如numpy、pandas、ahocorasick-python、openpyxl。

```python
pip3 install numpy
pip3 install pandas
pip3 install ahocorasick-python
pip3 install openpyxl
```

在这之后，你就可以编译了：

```python
pip3 install pyinstaller
pyinstaller -F datacleaning.py
```

你能在编译之后，在你的目录下的dist目录中，找到可执行程序，并使用它。

读取EXCEL路径按钮可以读取你要清洗的EXCEL路径。

结果存放按钮可以设定你要存放结果的位置。结果的文件名为result.xlsx

你能选择你想要精确的字符数，存放在精确字符数的框内，程序会根据你的精确字符数，合并你的店名。

如果你只想使用泛类目映射，你可以将精确字符数的框空出。但是如果你要使用数据清洗，就必须填写这个框。
