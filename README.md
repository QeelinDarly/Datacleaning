# Datawash
datawash tools for Business analysis

This program is made for Vicky's work. You can use it, too.

# 数据清洗
该数据清洗工具是为了商业分析

这个程序是为了Vicky的工作而开发的，公开代码后，您也可以免费使用它。

# Attention
Before you use it. Please change your excel's format.

The first column is your target store name. If you want to use wash, you need change A1 name as '行标签', but if you just use pan category mapping, please forget it.

The second column is the number of target store, default is 1. Program will merge the same name store and sum numbers.

The third column is the local of your target store. We have not use it now, but we want to count it.

Please leave the forth column blank, because we will add the result of pan category mapping in here. Of cause, if you don't use it, forget it.

# 注意事项
在你使用该程序之前，请改变你的Excel格式。

第一列是你的目标店名。如果你想用数据清洗，请你在A1单元格写入‘行标签’，但是如果你只使用泛类目映射，请无视它。

第二列是目标店铺的门店数，默认为1。程序将会合并所有名字相同的店名。

第三列是你目标店铺的地址。我们暂时没有使用这个字段，但是我们将在未来推出统计店铺地址的功能。

请将第四列空出，因为我们需要将泛类目映射的结果写在这里。当然，如果你不用这个功能，请无视它。

# Usage
Before you build it, you need to have right environment. You need have python3 and numpy、 pandas、 tkinter、 ahocorasick-python、 openpyxl.

```python
pip install numpy
pip install pandas
pip install tkinter
pip install ahocorasick-python
pip install openpyxl
```

And after that, you can build it by this:

```python
pip install pyinstaller
pyinstaller -F datawash.py
```

You can use it now, and executable program is in file dist.

# 使用方法
在你编译它之前，你需要有正确的环境。你需要有python3和它的一系列库，如numpy、pandas、tkinter、ahocorasick-python、openpyxl。

```python
pip install numpy
pip install pandas
pip install tkinter
pip install ahocorasick-python
pip install openpyxl
```

在这之后，你就可以编译了：

```python
pip install pyinstaller
pyinstaller -F datawash.py
```

你能在编译之后，在你的目录下的dist目录中，找到可执行程序，并使用它。
