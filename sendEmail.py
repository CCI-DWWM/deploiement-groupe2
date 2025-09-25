import smtplib, ssl
import os
from dotenv import load_dotenv
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
# on rentre les informations sur le destinataire
email_receiver = ADRESS_RECEIVER
# Corps de l'email
email_content = 'fuyez !!!!!!'
# on crée la connexion
context = ssl.create_default_context()
def sendEmail():
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
        server.login(email_address, email_password)
  # envoi du mail
        server.sendmail(email_address, email_receiver, email_content)