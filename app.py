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


with open("/Users/a0000/mywork/commonLLM/opensource/nnnew/Transcript-benchmark-quickstart/dataset-cn/sam-22.txt", 'r') as file:
    # 逐行读取内容
    for line in file:
        # 打印每一行的内容（去除末尾的换行符）
        if line.startswith("("):
            line = line.split(") ")[1].strip()
            askGPT3(line)
            print()


            # print(line.strip())
        


