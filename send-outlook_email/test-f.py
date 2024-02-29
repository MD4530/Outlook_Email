
# import requests

# response = (requests.get(r"https://login.microsoftonline.com/common/oauth2/nativeclient", "c573e4f9-6df2-4a29-bfca-0bd205bade55"))

# print (response.text())

# password = "d2c58e29-d5ce-43c3-bd87-540afbe316a5"
client_id ="c573e4f9-6df2-4a29-bfca-0bd205bade55"
credentials =(client_id)
from O365 import Account
account = Account(credentials,auth_flow_type='public')


print (account)


if account.authenticate(scopes=["api://c573e4f9-6df2-4a29-bfca-0bd205bade55/Mail.Read"]):
    print("Authenticated!") 

# import smtplib, ssl

# smtp_server = "smtp.office365.com"
# port = 587  # For starttls

# sender_email = "matiq@aesclean.com" 


# receiver_email="matiq2536@gmail.com"
# message="""\
# Subject: Hi there Test (2)

# This message is sent from Python ."""
# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
    
# print ("send")



# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit() 