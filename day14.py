from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = 'kongbotao@live.com'
    receivers = '675573267@qq.com'
    message = MIMEText('示例邮件', 'plain', 'utf-8')
    message['From'] = Header('孔博涛', 'utf-8')
    message['To'] = Header('kbt', 'utf-8')
    message['Subject'] = Header('示例邮件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender, 'password')
    smtper.sendmail(sender, receivers, message.as_string())
    print('发送完成')

if __name__ == '__main__':
    main()