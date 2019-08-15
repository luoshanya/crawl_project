import smtplib


def send_email(subject, content, username="dev@abc.com", password="abc123"):
    mailhost = "smtp.exmail.qq.com"
    mailport = 465
    fromaddr = "dev@bishijie.com"
    toaddrs = ["aaa@qq.com", "bbb@qq.com"]
    # toaddrs = ["chensong@bishijie.com"]
    try:
        smtp = smtplib.SMTP_SSL(mailhost, mailport)
        smtp.login(username, password)
        msg = 'Subject: {}\n\n{}'.format(subject, content)
        smtp.sendmail(fromaddr, toaddrs, bytes(msg, encoding='utf-8'))
    except Exception as e:
        # print(e)
        logging.error("send mail failed! error={}, subject={},content={}".format(e,subject,content))