import re


def normalize_email(email):
    """规范化邮箱格式"""
    # 去除前后空格
    email = email.strip()
    # 将邮箱转换为小写
    email = email.lower()
    # 处理常见的错误后缀
    email = re.sub(r'@qq\.com$', '@qq.com', email)
    email = re.sub(r'@qq\.con$', '@qq.com', email)
    email = re.sub(r'@qq\.c0m$', '@qq.com', email)
    email = re.sub(r'@163\.com$', '@163.com', email)
    email = re.sub(r'@126\.com$', '@126.com', email)
    email = re.sub(r'@139\.com$', '@139.com', email)
    # 其他常见邮箱后缀规范化
    email = re.sub(r'@([a-z0-9]+)\.([a-z]{2,})$', lambda m: f"@{m.group(1)}.{m.group(2)}".lower(), email)
    return email


def is_valid_email(email):
    """检查是否为有效的邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def process_email_file(filename):
    """处理邮箱文件"""
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # 分割每行的邮箱，可能是制表符或逗号分隔
            emails = re.split(r'[\t,]', line.strip())
            # 处理每个邮箱
            processed_emails = []
            for email in emails:
                email = email.strip()
                if not email or email == '-':
                    continue
                # 规范化邮箱
                normalized = normalize_email(email)
                if is_valid_email(normalized):
                    processed_emails.append(normalized)
            if processed_emails:
                result.append(processed_emails)
    return result


# 使用示例
if __name__ == "__main__":
    filename = r"C:\Users\guozh\Desktop\mail\邮箱1.txt"  # 替换为你的文件名
    processed_emails = process_email_file(filename)

    # 打印结果
    for i, emails in enumerate(processed_emails, 1):
        print(f"第{i}行: {emails}")

