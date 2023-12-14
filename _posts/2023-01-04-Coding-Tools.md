---
layout: post
title: (En) Configure Coding Tools de novo
categories: Coding-Issues
description: 
keywords: 配置写代码的历程
---

For me, the computer rookie, in order to take advantage of different **packages** in **python**, I mis-operated my computer and broke it, and finally had to reinstalled the operating system. **Here I recorded the procedures of configuring coding tool from a system-reinstalled computer** as a **manual**. I currently use **Windows 10**, the process applies to Windows although I may soon switch to Mac.

My operating system only support one language and I don't know exactly the English translations for the procedures. So I use bracket for Chinses translations.

## Trigger (how was it broken)

The results on a paper I wanted to reproduce need a new package of python. After installation, it  did not work. Since I had repeatedly installed python and Anaconda on my laptop before, which might cause problems, I wanted to completely uninstall python and Anaconda. After deleting some files on the C drive, I found that cmd (command line) was not working. When I went online to investigate the problems, I found that the problem was getting more and more outrageous, and then I decided to reinstall the operating system. At this time, the my computer could be turned on and  most softwares worked normally.

### Reinstall the operating system

1. **Update your back up important files.** (I assume that everyone has a good habit of backing up files regularly, in this age of high dependence on computers, so that months and years of research are not at risk of lost.) If the following steps run smoothly, this step is not necessary but still highly recommended.
2. Start Menu(开始菜单) -> Settings(设置) -> Update and Safety(更新和安全) -> Recovery(恢复) -> Reset this Computer(重置此电脑).
3. I recommend "Keep my files"(保留我的文件) than "Delete all contents" (删除所有内容), then after reset, all applications will  be uninstalled but your files will be remained. It might take 1~3 hours to reset. Then you will have a brand new computer! Let's configure coding tools *de novo*!

## Install Anaconda for Python

I didn't get exposed to coding before college (even didn't have a personal computer), and I am always a computer rookie. When I first got my PC, I installed python. In my late sophomore year of college, I installed Anaconda and Spyder (IDE I use for python), I also tried to install Tersonflow for a math modeling contest but failed. In my freshman year for PhD, I installed pip to install new packages for python. Note that I **don't recommend** the above procedure! What I did on my "new computer" are following:

1. **Install Anaconda.** Note that if you install Anaconda first, you can use python and don't need to install python afterwards! This is the website where you can [download Anaconda](https://www.anaconda.com/). Suppose your **destination folder** is *C:\Users\slnsi\anaconda3*. I will use \<C:\Users\slnsi\anaconda3\> to denote things you need to change to yours in the following paragraphs!

2. **Configure environment variables.** This computer(此电脑) -> properties(属性) -> Advanced System Settings(高级系统设置) -> Advance(高级) -> environment variables(环境变量)  -> Path(in system variable)(Path (在系统变量里)) -> edit(编辑) -> new(新建): add the following: 

   ```
   <C:\Users\slnsi\anaconda3>
   
   <C:\Users\slnsi\anaconda3>\Scripts
   
   <C:\Users\slnsi\anaconda3>\Library\mingw-w64\bin
   
   <C:\Users\slnsi\anaconda3>\usr\bin
   
   <C:\Users\slnsi\anaconda3>\Library\bin
   ```

   *I am not sure whether this is necessary, but I did it. I checked my path afterwards and couldn't find them (because I forgot to save the changes), but it seems my anaconda still works well! Anyway I re-added those variables later.

3. **Test whether it works!** Search for **Anaconda Navigator** and find whether you can enter the page. Search for **Anaconda Prompt** and type these two lines in sequence:

   ```
   conda info
   conda --version
   ```

   and see whether the right answers are shown!

## Use Spyder and Jupyter Notebook as IDE

Personally I use both **Spyder** and **Jupyter Notebook** as IDEs (集成开发环境). After installing Anaconda, you have then automatically and don't need to install them again. And I send desktop shortcuts (发送桌面快捷方式) of these IDEs.  

## Install Tensorflow for datascience

Then it is easy to install packages for python! You search for documentations of the package and follow the steps. In this manual, open your **Anaconda Prompt** and follow *Installing via conda*, but **not** *Installing via pip*!

Personally I use **Tensorflow** for datascience. I followed the steps on [this page](https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/). Open your **Anaconda Prompt** and type

```
conda create -n tf tensorflow
conda activate tf
```

check whether the installation is successful in the tf environment by (also in **Anaconda Prompt**)

```
python
import tensorflow as tf
```

and it **shouldn't** be "ModuleNotFoundError: No module named 'tensorflow'"

*Note that your Tensorflow is installed in a new **environment** called "tf". In fact I really don't know the point of creating a new environment for it... I just followed the steps.

### Install Spyder and Jupyter Notebook in the new environment

Switch the environment in **Anaconda Prompt** by 

```
conda activate tf
```

and then type in sequence

```
conda install spyder
conda install jupyter
```

### Use Tensorflow in Spyder and Jupyter Notebook

Switch the environment in **Anaconda Prompt** by

```
conda activate tf
```

Then you type

```
spyder
jupyter notebook
```

to use tensorflow in the new environment in **Spyder** or **Jupyter Notebook** respectively. If you don't do this, you can't *import tensorflow*. In your default environment, base, it will be "ModuleNotFoundError: No module named 'tensorflow'".

Well done!

### Updating

[2023/09/06 Update] I updated my Spyder following the instruction 

![Coding_Update](\images\blog\Coding_Update.JPG)

When using Anaconda Prompt to update, **run as administrator (以管理员身份运行)** to avoid failure!!! There are two choices for Anaconda Prompt. This is for updating everything installed by Anaconda, and your Spyder is included

```
conda update anaconda
```

And if you want to only update Spyder to a certain version (i.e. 5.4.3 version here), use

```
conda instsll spyder=5.4.3
```

## Restart coding by C++

Beside python and MATLAB, I also use C++ for intense simulations, in order to speed up. I installed **MinGW** as my C++ code complier ([download here](https://sourceforge.net/projects/mingw/)). After reinstalling the operator system, I was surprised that MinGW was still there! So it may mean that I was not configuring my coding tools *de novo*!

But note that you still need to **configure the environment variable** again to use MinGW. This computer(此电脑) -> properties(属性) -> Advanced System Settings(高级系统设置) -> Advance(高级) -> environment variables(环境变量)  -> Path(in system variable)(Path (在系统变量里)) -> edit(编辑) -> new(新建): add: 

```
C:\MinGW\bin
```

Personally I use **Visual Studio Code** as my C++ IDE. I needed to reinstall it. Don't forget to install the **C/C++ extension** to help with your coding!

When I started to compile my code, I found warning like

```
\Script.ps1 : File C:\Users\slnsi\Documents\WindowsPowerShell\profile.ps1 cannot be loaded because running scripts is disabled
  on this system. For more information, see about_Execution_Policies at
  https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ 'C:\Users\slnsi\Documents\WindowsPowerShell\profile.ps1'
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
```

To address this, search for **Windows PowerShell** and **run as administrator**, and type in sequence:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Y
```

and then you can compile and run your C++ code!

Well done! You have a brand new computer for scientific computing!

## Acknowledgement

I would like to thank graduate student Zhi Zhang, Thomas Tsangaris and Brett Min for discussing the problems of python code, B Kell, Seshu Iyengar and Prof Andreas Hilfinger for discussing the problems of C++ code. Also, thank Duncan Kirby and Prof Anton Zilman about introducing tensorflow in coding.

## Possible Issues

I am a computer rookie and I know nothing about what I was doing. I am confident that the following steps will make your computer a good tool for scientific computation, but I am not sure whether some steps are not necessary. If you have more information to share and help me to improve this manual, don't hesitate to email me! Thanks in advance!
