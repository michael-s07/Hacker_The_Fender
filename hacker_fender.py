import csv
with open('passwords.csv', newline='') as password_file:
  password_csv=csv.DictReader(password_file)
  compromised_user=[]
  for password_row in password_csv:
    compromised_user.append(password_row['Username'])
  print(compromised_user)

with open("compromised_users.txt", 'w') as compromised_user_file:
  for c in compromised_user:
    compromised_user_file.write(c)
#Notifying the Boss
import json

with open("boss_message.json",'w') as boss_message:
  boss_message_dict={}
  boss_message_dict['recipent']="The Boss"
  boss_message_dict['message']="Mission Success"
  json.dump(boss_message_dict,boss_message)

with open("passwords.csv",'w') as new_passwords_obj:
  slash_null_sig="""
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  
  """
  slash_null_sig=new_passwords_obj


