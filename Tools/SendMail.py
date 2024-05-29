# 引入邮件模块
from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 邮件邮箱账户信息
mail_host = 'smtp.163.com'
mail_port = 25
mail_user = 'zhang1980060@163.com'
mail_pass = 'EHGINNXIHNCZEGTM'

# 邮件收发人信息
receiver = ['13061924124@wo.cn', '15524861813@wo.cn']

# 邮件正文内容
message = MIMEText('Python邮件批量发送测试', 'plain', 'utf-8')
message['From'] = Header('zhang1980060@163.com', 'utf-8')
message['To'] = Header('13061924124@wo.cn', 'utf-8')

# 发件人与收件人信息
message['Subject'] = Header('Python SMTP测试邮件', 'utf-8')

try:
    # 登录SMTP服务器，绑定邮件客户端
    smtpObj = smtplib.SMTP(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)
    for i in range(3):
        # 发送邮件
        smtpObj.sendmail(mail_user, receiver, message.as_string())
        print("邮件发送成功")
    smtpObj.quit()
    print("所有邮件发送成功")
except smtplib.SMTPException as e:
    print("邮件发送失败")
    print(str(e))