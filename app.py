from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-"

def askGPT3(mprompt):
    sprompt = """
    下面内容是粗译的结果，请整理意译，使之更符合中国人阅读理解习惯，注意说人话。
    """
    client = OpenAI()
    try:
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
    except:
        print(mprompt)


with open("/Users/a0000/mywork/commonLLM/opensource/nnnew/Transcript-benchmark-quickstart/dataset-cn/ready-01.txt", 'r') as file:
    # 逐行读取内容
    for line in file:
        # 打印每一行的内容（去除末尾的换行符）
        if line.startswith("("):
            line = line.split(") ")[1].strip()
            askGPT3(line)
            print()