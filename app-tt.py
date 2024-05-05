## 第二次加工(从result-cn之后...)

from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-"

def askGPT3(mprompt):
    sprompt = """
重写整理内容为更易于中国人阅读的样子，包括段落修正、句子逻辑修正、翻译不通顺的之处重新表达意译，注意输出忠于原文的完整内容，保持原文意思不变，并且满足以下条件:
- 遵循以下常见的 AI 相关术语词汇对应表(原文 -> 重写后输出）：
  * Transformer -> Transformer
  * Token -> Token
  * LLM/Large Language Model -> 大语言模型
  * Zero-shot -> 零样本
  * Few-shot -> 少样本
  * AI Agent -> AI 智能体
  * AGI -> 通用人工智能
  * 法学硕士 -> 大语言模型
  * 快速工程 -> prompt工程
  * 即时工程 -> prompt工程
  * 检索增强生成 -> 检索增强生成（RAG）
  * 令牌 -> token
  * RAG -> 检索增强生成（RAG）
  * 微调 -> fine-tuning
  * 涡轮增压 -> Turbo
  * 性能 -> 效果

    """
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": sprompt},
        {"role": "user", "content": mprompt}
    ]
    )
    result = completion.choices[0].message.content.strip()
    print(result)
    print()
    return(result)


with open("/Users/a0000/mywork/commonLLM/opensource/nnnew/Transcript-benchmark-quickstart/temp-cn/openai-t.txt", 'r') as file:
    # 逐行读取内容
    for line in file:
        if len(line) > 2:
            askGPT3(line)
            print()



