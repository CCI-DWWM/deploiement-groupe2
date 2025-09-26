
import smtplib, ssl
import os
from dotenv import load_dotenv
from email.message import EmailMessage
load_dotenv()

ADRESS_EMITTEUR = os.getenv('EMAIL_ADRESS_EMITTEUR')
ADRESS_RECEIVER = os.getenv('EMAIL_ADRESS_RECEIVER')
PSWD = os.getenv('EMAIL_PASSWORD')

# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465
# on rentre les informations sur notre adresse e-mail
email_address = ADRESS_EMITTEUR 
email_password = PSWD





#============  ============#
msg = EmailMessage()
#============ Suject, object, from, to and content ============#
msg['Subject'] = f"Risque d'innondation"
msg['From'] = ADRESS_EMITTEUR
msg['To'] = ADRESS_RECEIVER
msg.set_content("""\
Attention le niveau de l'eau à dépasser la limite de 5 métres.
""")



# on crée la connexion
context = ssl.create_default_context()
def sendEmail():
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
        server.login(email_address, email_password)
  # envoi du mail
        server.send_message(msg)
        print('Email envoyé')