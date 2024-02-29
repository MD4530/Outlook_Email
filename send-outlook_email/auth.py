
##This is just of authenticate###

# in order to use outlook you must have to authenticate
# once you run code it will give an consent url 
# then past the url into the browser ** Make Sure copy is CORRECT not the broken ***(Past in the text file)** 
# it will generate the tocken in the url ***long than past url make sure not broken**  ***(Past in the text file)
# copy the url and past as a input where programs run

####try ####
###until you the see this mesg ***Authentication Flow Completed. Oauth Access Token Stored. You can now use the API.***

# once authentication done then you use outlook


# from O365 import Account, FileSystemTokenBackend


# credentials  = ("a4c1de80-3e77-4048-a5ba-5fceeeafc288",'6f12c033-c886-4719-b424-1a9faaa30137')

# token_backend = FileSystemTokenBackend(token_path='my', token_filename='o365_token.txt')

# scops=["https://graph.microsoft.com/Mail.Read", "https://graph.microsoft.com/Mail.Send"]

# account = Account(credentials, auth_flow_type='credentials', tenant_id="fa9af012-fc87-437c-8a05-d5404aa323da")
# if account.authenticate(scopes=scops, ):
#     print(account)


# ########################working ###################################
# from O365 import Account

# credentials = ("a4c1de80-3e77-4048-a5ba-5fceeeafc288")
# scops=["https://graph.microsoft.com/Mail.Read", "https://graph.microsoft.com/Mail.Send"]

# account = Account(credentials, auth_flow_type='public', tenant_id="fa9af012-fc87-437c-8a05-d5404aa323da")

# if account.authenticate(scopes=scops):
#     print("Authenticated!")  
# ########################end  ###################################
if __name__ =="__main__":
       print ("python -> running outlook -> auth") 
       import importlib.util
       import subprocess
       package =["openpyxl", "O365"]
       for pa in package:
              if (spec := importlib.util.find_spec(pa)) is not None:
                     print(f"{pa!r} has imported")
              else:
                     print(f"can't find the {pa!r} module")
                     subprocess.call(['pip3', 'install', pa])
                     
       from O365 import Account
       id ='01fced37-a3fb-435c-ac41-61b04bf7f588'
       passWord='f2adc092-21f2-44a6-8cc2-8d08592bf238'
       tId= "fa9af012-fc87-437c-8a05-d5404aa323da"
       # credentials = (id, "")

       scops=[
              "https://graph.microsoft.com/Mail.Read", "https://graph.microsoft.com/Mail.Send", "offline_access"]

       account = Account(id, auth_flow_type='public', tenant_id=tId)

       if account.authenticate(scopes=scops):
              print("Authenticated!")



