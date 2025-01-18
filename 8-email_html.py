from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = str(open('senha', 'r').read())
from_email = '6ff1fcdbbd7ad8'
to_email = 'erickbarretodasilva@gmail.com'
subject = 'Curso Python'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body, subtype='html')

anexo = 'files/estrela.png'
print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

try:
    with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.sendmail("Private Person <from@example.com>", to_email, message.as_string())
    print("Email enviado com sucesso!") 
except Exception as e: 
    print(f"Ocorreu um erro: {e}")