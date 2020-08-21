# wonderfulbilibili
项目名： 神奇电波。

简介：实际上是本人经历了长时间宅家生活以及疾病缠身的情况下，产生一点抑郁倾向，于是想着做一个可以对自己说一些暖心（中二）语言的程序。程序调用了网络上开源的api，也算是python小程序从设计到调用功能到打包发布全过程都有了，后面更新教程，对刚学python的小白友好的一个实战经验吧（笑）

## 第0步，确保你的电脑安装了python

python是最适合所有非科班编程爱好者的语言之一！圈内人士常说‘人生苦短，我选python’就是因为python具有简单实用的特性！

首先，如果你的电脑上没有安装python，可以访问下面的链接选择合适的安装方式。

[python的安装和环境配置](https://www.runoob.com/python/python-install.html)

安装python只是使用python强大功能的前提条件，python真正的能量在于繁多的功能模块（库），如何为python插上翅膀？选择适合的库进行安装和使用，这是飞翔的感觉！(完全小白可以跳过这一步，后面代码中会有提示你需要什么库，到时候针对性的安装。)

[python模块安装](https://docs.python.org/zh-cn/3.7/installing/index.html)



## 第一步，请安装qtcreator

无论你使用的是mac/win，你都可以选择下载qtcreator作为你用来可视化订制你的图形界面的工具。你可以简单的通过拖拉‘小组件’的方式定制出你需要的app界面！

无论你用的Windows or Mac or Linux，你都可以通过这种方式安装：[qtcreator下载和安装](https://blog.csdn.net/weixin_38090427/article/details/83827678)当然，对于mac用户而言，homebrew（确切的说是brew cask）带来的便捷化安装更省心。[brew的安装和使用](https://www.jianshu.com/p/fdfa9b8e29f8?utm_campaign=hugo&utm_medium=reader_share&utm_content=note)

~~ps:我个人用的brew cask安装的，如果上一个方法有什么问题请不要问我，这个链接是我百度来的（笑）~~

哦，对了，如果你用的windows，，你还可以直接获取pyqt5模块的工具，其中自带了图形化界面设计的工具。~~mac也可以但是安装到哪儿了真的不好找qaq~~这个方法的话请自行百度pyqt5的安装配置吧，本项目用的pyside2替代了pyqt5的功能。

## 第二步，将设计好的ui文件转换为py文件

实际上就是一行命令的事情，不过我还是建议你们看一下别人写的博客，有助于深入掌握。（文件名可以自定哦～本项目使用的就是form.ui）

```
`pyside2-uic mainwindow.ui > ui_mainwindow.py`
```

[pyside2ui转换和使用](https://blog.csdn.net/ssspppfff/article/details/104454665)

## 第三步，写一个对应的功能性py文件。

现在，请观察我的仓库的文件（release下的），你会发现除了form.ui之外没什么明确知道干啥用的，让我解释一下：ui_form.py就是上一步生成的对应的py文件，存储了相关的解main信息。以后我们要通过main.py(release文件夹下的main.py)文件中的代码对这个界面中的组件的功能进行设定。你无需关心ui_form.py的内容，现在，把视线转向main.from,我会为你详细讲解真正work的东西。

```
import sys
import json
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import requests
from ui_form import Ui_mainform
```

让我解释一下：import是python导入功能模块使用的语句，上面分队对应导入系统模块，json模块。。。等等。json是用于解析json数据的包，pyside2是qt所依赖的包，其中最后一行导入的是你刚刚做出来的ui的信息，这样我们才能在这个文件中对里面的组件进行设定。

```
self.ui.getbilibili.clicked.connect(self.getbili)
```

这行代码联系了按钮（我设计的按钮的id为getbilibili）和功能函数（getbili）

之后我们对功能函数进行设计，点击按钮就能执行相应的功能了！

```
def getbili(self):
        r=requests.get("https://v1.hitokoto.cn/")
        msg=json.loads(r.text)
        self.ui.showarea.setText(msg["hitokoto"])
```

通过request.get方法 访问了我们调用的开源api，这是我们获取随机句子的地址。如果你想玩其他的api可以百度“有趣的api”。由于返回值是json格式的，然后我们就通过json.loads解析了返回的结果，最后我们把对应的文本部分的内容，也就是msg["hitokoto"]（这是由于你所调用的api决定的，这里调用的api对应的返回值中文本字典的key就是hitokoto，如果你的python基础不好的话看不懂也不要紧，稍微学一下python字典相关的内容就好）放在我们设定的显示文本的地方就好啦。

Main.py代码中其他部分都是用于显示界面的代码，无需关心～~~其实我也讲不明白~~

## 第四步，运行一下试试？

通过在当前文件夹下打开终端或命令行，输入python3 main.py。看一下能不能成功！~~大概率不能~~

如果你的电脑提示你没有某个模块的话，不要慌，作为一个入门级程序员，一定要学会面向百度编程，当然，结果是让你安装对应的模块。如何安装就请往前翻一下hhhh

当然不能成功运行的另一个原因是你的代码出了问题，你可以根据出现的问题百度解决，也可以向我咨询（如果我有空的话）。这个问题没办法预判，因此这里不作更多说明了。

## 第五步，打包和发布。

哦，今天实在是有点累，上午去医院打了12针，身心俱疲，反正现在star也少的很（3个其中还有来自女友的支持）想看的人也不多。有空再来更新吧~~大概率会更新但也许不会~~ 

### 最后 如果要联系我

请通过GitHub留下的电子邮件地址或者直接在本仓库发起issue



