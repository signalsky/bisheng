import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from read_email import process_email_file


def send_email(sender_email, sender_password, receiver_email, subject, content, is_html=False, cc_emails=None,
               bcc_emails=None, attachments=None):
    """
    使用腾讯企业邮箱发送邮件

    参数:
    sender_email (str): 发件人邮箱地址
    sender_password (str): 发件人邮箱授权码
    receiver_email (str or list): 收件人邮箱地址，可以是单个字符串或列表
    subject (str): 邮件主题
    content (str): 邮件内容
    is_html (bool): 邮件内容是否为HTML格式，默认为False
    cc_emails (list): 抄送邮箱列表，默认为None
    bcc_emails (list): 密送邮箱列表，默认为None
    attachments (list): 附件路径列表，默认为None
    """
    # 处理收件人列表
    if isinstance(receiver_email, str):
        receiver_email = [receiver_email]

    # 处理抄送列表
    cc_emails = cc_emails or []
    # 处理密送列表
    bcc_emails = bcc_emails or []

    # 创建邮件对象
    message = MIMEMultipart()
    message['From'] = Header(sender_email)
    message['To'] = Header(", ".join(receiver_email))
    message['Subject'] = Header(subject, 'utf-8')

    # 添加抄送
    if cc_emails:
        message['Cc'] = Header(", ".join(cc_emails))

    # 设置邮件内容
    content_type = 'html' if is_html else 'plain'
    message.attach(MIMEText(content, content_type, 'utf-8'))

    # 添加附件
    if attachments:
        for attachment_path in attachments:
            try:
                with open(attachment_path, 'rb') as file:
                    # 创建附件对象
                    attachment = MIMEText(file.read(), 'base64', 'utf-8')
                    attachment['Content-Type'] = 'application/octet-stream'
                    # 获取文件名
                    filename = attachment_path.split('/')[-1]
                    # 处理中文文件名
                    attachment['Content-Disposition'] = f'attachment; filename="{Header(filename, "utf-8").encode()}"'
                    message.attach(attachment)
            except Exception as e:
                print(f"添加附件 {attachment_path} 失败: {e}")

    # 所有收件人（包括抄送和密送）
    all_recipients = receiver_email + cc_emails + bcc_emails

    try:
        # 连接到腾讯企业邮箱SMTP服务器
        server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        server.login(sender_email, sender_password)
        # 发送邮件
        server.sendmail(sender_email, all_recipients, message.as_string())
        server.quit()
        print("邮件发送成功")
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False


if __name__ == "__main__":
    # 发件人邮箱信息
    sender_email = "yangguozheng@deepzo.tech"  # 替换为你的邮箱地址
    sender_password = "qhvc9bQjY2rY7qSi"  # 替换为你的邮箱授权码

    # 邮件主题和内容
    subject = "十倍效率，十分之一成本：您的企业 AI 转型方案"
    content = content = """
    <html>
        <head>
            <style>
              p {
                max-width: 910px;
                text-indent: 2em;
                margin-bottom: 15px;
                font-size: 16px;
              }
              .highlight {
                background-color: #fffacd; /* 浅黄色背景 */
                font-weight: bold;
              }
              .red {
                color: red;
                font-weight: bold;
              }
            </style>
        </head>
        <body>
            <p>贵公司您好，很抱歉打扰到您，请允许我进行短暂的自我介绍：</p>
            <p>我是上海灼见智能科技有限公司的创始人杨国拯，我在大模型领域已经工作6年，已经为53家企业定制以及部署过各类私有化大模型，有着丰富的合作经验。</p>
            <p>根据对贵公司的深入了解以及对贵公司应用场景的观察，贵公司需要定制一个适用于企业内部的私有化大模型来进行降本增效。私有化大模型会根据公司内部的情况以及结合贵公司内部资料/信息/知识库来进行高效工作，有了私有化AI大模型之后，贵公司可以将原本的人员数量压缩到十分之一，且工作效率可以翻十倍，真正实现降本增效。</p>
            <p>贵公司<span class="red">如果自己取训练</span>企业内部私有化大模型，则需要消耗大量算力资源，成本会在<span class="red">300-500万</span>，且效果可能不会理想；但我们可以根据贵公司的应用场景，来为贵公司定制最适合的私有化大模型，<span class="red">几个只要个位数</span>，而且一次部署，永久使用！并附带模型维护优化等服务。</p>
            <br>
            <p>如果您对此感兴趣，请来联系我📞 ：<span class="highlight">13162753141</span>（微信/手机同号），期待贵公司的回复。</p>
            <p><a href="http://47.116.179.127:9011/">客户案例，首次点开较慢</a></p>
        </body>
    </html>
    """

    # 发送邮件（HTML格式）
    # processed_emails = process_email_file(r"C:\Users\guozh\Desktop\mail\邮箱1.txt")
    processed_emails = ['ygz3141@qq.com']
    for receiver_email in processed_emails:
        send_email(
            sender_email,
            sender_password,
            receiver_email,
            subject,
            content,
            is_html=True,  # 设置为True表示HTML格式
            # cc_emails=["cc@example.com"],  # 抄送列表
            # bcc_emails=["bcc@example.com"],  # 密送列表
            # attachments=["path/to/your/file.txt"]  # 附件列表，替换为实际文件路径
        )
