# iOS_Auto_Archive


### The English README
#### what is it?
A simple python script to generate iOS IPA file &amp; plist file automaticly.

#### what's it for?
For me, it can help us distribute the $299-Applications inside our company, for testing group and product managers.

#### what do I have to do before I use it?
Well, first you need to know how to run python script.

Then, you need to edit the *ios_auto_archive.py* file and change the *PROJECT_DIRECTORY*'s value to *YOU PROJECT DIRECTORY*, and *APP_DOWNLOAD_URL*'s value to *YOU APP DOWNLOAD URL*. Here's an example:

```python
# PROJECT_DIRECTORY is your project path, write down the root directory path to your project will do just fine, but don't forget the last "/"
PROJECT_DIRECTORY = "/Users/EricTang/Documents/XcodeWorkspace/Helloworld/"
# APP_DOWNLOAD_URL is your download url, no need to type the ipa file name, but don't forget the last "/"
APP_DOWNLOAD_URL = "www.whatever.com/download/"
```

One more thing, add "DailyBuild" in your Xcode project, you can add this by "select the Project and then Duplicate 'Release' Configuration, rename the Configuration to DailyBuild". Shown as below:

![img](http://7vzo2i.com1.z0.glb.clouddn.com/052182PA6171B6V20.png-img.normal)

#### how to use it?
OK, that'll be easy, just simple run

```python
python3 ios_auto_archive.py
```
and you'll get what you need.

#### TODO
- 1. Add a simple server to distribute the Testing iOS Application in local area network.
- 2. Add alert(SMS or Email)
- 3. anything that came out of my mind maybe...

#### Update
##### 2015/05月/26
First commit


### 中文版README
#### 这个项目是什么？
就是一个特别简单的可以用来自动将iOS工程打包成IPA文件并且自动生成对应的plist文件的python脚本。

#### 它可以用来干啥？
对我而言，这个可以用来帮我在公司内部分发299刀的应用，可以让我更方便的分发给测试组啊或者产品经理们。

#### 我在使用之前有啥需要准备的么？
首先，你得知道如何运行python脚本。

然后嘞，你需要修改*ios_auto_archive.py*文件，把其中的*PROJECT_DIRECTORY*的值改成*你的Xcode工程路径*，把*APP_DOWNLOAD_URL*的值改成*你的APP下载URL*，下面我们来举个例子：

```python
# 把PROJECT_DIRECTORY的值替换成你的Xcode工程的根目录即可，但是别忘了最后一个"/"符号
PROJECT_DIRECTORY = "/Users/EricTang/Documents/XcodeWorkspace/Helloworld/"
# 把APP_DOWNLOAD_URL替换成你的APP下载地址，无需填写IPA文件的名字，但是别忘了最后一个"/"符号
APP_DOWNLOAD_URL = "www.whatever.com/download/"
```
还有一件事儿，你需要在你的Xcode工程中添加名为DailyBuild的配置，很简单，首先选中项目，然后点击Configurations下的加号，选择“Duplicate Release Configuration”这一项，然后将新添加的配置重命名为DailyBuild，如下图所示：

![img](http://7vzo2i.com1.z0.glb.clouddn.com/052182PA6171B6V20.png-img.normal)

#### 如何使用
这个很容易，配置完成之后，只需要在终端中运行如下命令：

```python
python3 ios_auto_archive.py
```
即可。

#### TODO列表
- 1. 添加一个简单的WebServer用于实现内网的iOS应用分发
- 2. 添加通知（通过短信或者Emaile方式）
- 3. 嗯，可能会添加我脑子里蹦出来的稀奇古怪的想法

#### 更新记录
##### 2015/05月/26
第一次提交