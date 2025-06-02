import os
import re

def extract_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 去除 Markdown 特殊内容
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)  # 代码块
        content = re.sub(r'`.*?`', '', content)  # 行内代码
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # 图片
        content = re.sub(r'\[.*?\]\(.*?\)', '', content)  # 链接
        content = re.sub(r'[#>*\-]', '', content)  # markdown符号
        return content

total_chinese = 0
total_english = 0
total_chars = 0

for root, dirs, files in os.walk('_posts'):
    for file in files:
        if file.endswith('.md'):
            text = extract_text(os.path.join(root, file))
            chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
            english_words = re.findall(r'\b[a-zA-Z]+\b', text)
            non_space_chars = re.findall(r'\S', text)

            total_chinese += len(chinese_chars)
            total_english += len(english_words)
            total_chars += len(non_space_chars)

print("中文字符数：", total_chinese)
print("英文单词数：", total_english)
print("总非空字符数（中英文标点等）：", total_chars)
