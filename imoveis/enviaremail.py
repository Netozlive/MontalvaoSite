import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(usuario, imovel, corretor, link):
	# me == my email address
	# you == recipient's email address
	me = "montalvaoimoveis.sistema@outlook.com"
	you = "netocorp05@gmail.com"

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Link"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = f"Prezado,o usuário \n {usuario}\n foi direcionado ao corretor {corretor}. Endereço do imóvel:\n{imovel.rua}"
	html = f"""\
	<html>
	<head></head>
	<body>
		<p>Hi!<br>
		O usuário {usuario} está entrando em contato com o corretor {corretor} <br>
		Este é o <a href="{imovel}">imóvel</a> de interesse.
		</p>
	</body>
	</html>
	"""

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)
	# Send the message via local SMTP server.
	mail = smtplib.SMTP('smtp.outlook.com', 587)

	mail.ehlo()

	mail.starttls()

	mail.login('montalvaoimoveis.sistema@outlook.com', 'sacmontalvao4489')
	mail.sendmail(me, you, msg.as_string())
	mail.quit()
	return()