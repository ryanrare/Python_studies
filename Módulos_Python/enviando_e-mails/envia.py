from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'SEUEMAIL'
minha_senha = 'SUASENHA'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Ryan Victor', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'SEUNOME'
msg['to'] = 'EMAILQUEVAIENVIAR@GMAIL.COM'
msg['subject'] = 'ASSUNTO EM QUESTAO'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
       smtp.ehlo()
       smtp.starttls()
       smtp.login(meu_email, minha_senha)
       smtp.send_message(msg)
    except Exception as e:
       print('email nao enviado')
       print('error;', e)

