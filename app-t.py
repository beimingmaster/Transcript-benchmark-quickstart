# 可能可废弃.

from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-"

def askGPT3(mprompt):
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "重写整理内容为更易于中国人阅读的样子，包括段落修正、句子逻辑修正、翻译不通顺的之处重新表达意译，注意输出忠于原文的完整内容，保持原文意思不变"},
        {"role": "user", "content": mprompt}
    ]
    )
    result = completion.choices[0].message.content.strip()
    print(result)
    return(result)

mmtext = ""
with open("/Users/a0000/mywork/commonLLM/opensource/nnnew/Transcript-benchmark-quickstart/dataset-cn/openai-06.txt", 'r') as file:
    for line in file:
        if line.startswith("("):
            line = line.split(") ")[1].strip()
            if line.endswith("。"):
                mmtext = mmtext + line + "\n\n"
            else:
                mmtext = mmtext + line
lines = mmtext.split("\n\n")
for item in lines:
    askGPT3(item)
    print()

            # print(line.strip())
        



