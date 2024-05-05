# Transcript Benchmark Quickstart: Speech-to-Text for Entrepreneurial Insights
## 建议的适用范围
 - 斯坦福等的创业课，出文字稿。
 - TEDx的创业课，出文字稿。
 - 名人过往发言（5年前、10年前），sam altman、steven jobs、musk elon ，出文字稿。
## （从演讲视频到演讲文字稿）的常用步骤
1. 在youtube上下载字幕(如下图），优先看[ 观看人数高、创业相关 ]
<img width="1608" alt="image" src="https://github.com/zgimszhd61/Transcript-benchmark-quickstart/assets/114722053/663a796b-f06a-4067-8b06-64fda27b5d29">

3. 存储内容，提供给app.py，调用GPT3.5进行翻译.

4. 内容分享到本repo的Issue ，或者私信@seclink添加分享. ( https://twitter.com/seclink )

5. 有新Idea，请联系联系@seclink交流. ( https://twitter.com/seclink )


## 常用PROMPT
### 整理内容
```
重写整理内容为更易于中国人阅读的样子，包括段落修正、句子逻辑修正、翻译不通顺的之处重新表达意译，注意输出忠于原文的完整内容，保持原文意思不变，并且满足以下条件:
- 以下是常见的 AI 相关术语词汇对应表（English -> 中文）：
  * Transformer -> Transformer
  * Token -> Token
  * LLM/Large Language Model -> 大语言模型
  * Zero-shot -> 零样本
  * Few-shot -> 少样本
  * AI Agent -> AI 智能体
  * AGI -> 通用人工智能
  * 法学硕士 -> 大语言模型
---------
{}
```


### 从答案反推问题
```
下面的文章之中，主要回答的是AI领域的哪几个具体问题？举出5个的例子
-------
{}
```

### 启发的金句
```
下面的内容中，哪几句是最给人启发的断言和金句？举出5个的例子
---------
{}
```


