# from cryptography.fernet import Fernet
#
# secret_key = 'TI31VYJ-ldAq-FXo5QNPKV_lqGTFfp-MIdbK2Hm5F1E='
#
#
# def encrypt_token(token: str) -> str:
#     """使用Fernet对称加密算法加密字符串"""
#     return Fernet(secret_key).encrypt(token.encode()).decode()
#
#
# def decrypt_token(encrypted_token: str) -> str:
#     """使用Fernet对称加密算法解密字符串"""
#     return Fernet(secret_key).decrypt(encrypted_token.encode()).decode()
#
#
# # 测试加密和解密
# password_original = "Mxc#20250516"
# encrypted = encrypt_token(password_original)
# decrypted = decrypt_token(encrypted)
#
# print(f"原始密码: {password_original}")
# print(f"加密后: {encrypted}")
# print(f"解密后: {decrypted}")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body):
    # QQ邮箱账号和授权码
    qq_email = 'ygz3141@qq.com'  # 替换为你的QQ邮箱
    qq_password = 'inuugfofpcxfbaba'  # 替换为你的授权码

    # 收件人邮箱
    to_email = 'ygz3141@qq.com'  # 收件人邮箱。监控提醒的话，可以填写xxxxxxx@qq.com

    # 创建邮件内容
    subject = subject  # 邮件标题
    body = body  # 邮件内容

    # 构造邮件
    msg = MIMEMultipart()
    msg['From'] = qq_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # 添加邮件内容
    msg.attach(MIMEText(body, 'plain'))

    try:
        # 连接QQ邮箱SMTP服务器
        server = smtplib.SMTP('smtp.qq.com', 587)  # QQ SMTP服务器及端口
        server.starttls()  # 启动TLS加密
        server.login(qq_email, qq_password)  # 登录

        # 发送邮件
        server.sendmail(qq_email, to_email.split(","), msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()  # 退出服务


send_email('hello', '你好，世界')

