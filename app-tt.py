## 第二次加工(从result-cn之后...)

from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-"

def askGPT3(mprompt):
    sprompt = """
    下面内容是粗译的结果，请整理意译，使之更符合中国人阅读理解习惯，注意说人话。
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
    return(result)


with open("/Users/a0000/mywork/commonLLM/opensource/nnnew/Transcript-benchmark-quickstart/temp-cn/ready-01-t.txt", 'r') as file:
    # 逐行读取内容
    for line in file:
        if len(line) > 2:
            askGPT3(line)
            print()



