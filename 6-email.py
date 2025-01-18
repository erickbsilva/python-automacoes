from email.message import EmailMessage
import smtplib
import ssl

password = str(open('senha', 'r').read())
from_email = '6ff1fcdbbd7ad8'
to_email = 'erickbarretodasilva@gmail.com'
subject = 'Curso Python'
body = '''
A melhor forma de prever o futuro é criá-lo.
Aprendendo a linguagem Python
'''

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)

try:
    with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.sendmail("Private Person <from@example.com>", to_email, message.as_string())
    print("Email enviado com sucesso!") 
except Exception as e: 
    print(f"Ocorreu um erro: {e}")