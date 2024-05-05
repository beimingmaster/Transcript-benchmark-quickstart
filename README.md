# Transcript-benchmark-quickstart
## 常用步骤
1. 在youtube上下载字幕(如下图），优先看[ 观看人数高、创业相关 ]
<img width="1608" alt="image" src="https://github.com/zgimszhd61/Transcript-benchmark-quickstart/assets/114722053/663a796b-f06a-4067-8b06-64fda27b5d29">

2. 存储内容，提供给app.py，调用GPT3.5进行翻译.

3. 内容分享到Issue.

## 常用PROMPT
### 整理内容
```
重写整理内容为更易于中国人阅读的样子，包括段落修正、句子逻辑修正、翻译不通顺的之处重新表达意译，注意输出忠于原文的完整内容，保持原文意思不变.ZZZZ
---------
{}
```


### 从答案反推问题
```
下面的文章之中，主要回答的是AI领域的哪几个具体问题？举出5个以上的例子
-------
{}
```

### 启发的金句
```
下面的内容中，哪几句是最给人启发的断言和金句？
---------
{}
```


