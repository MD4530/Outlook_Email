
## outlook-auth-app application will expire 2/14/26
###https://portal.azure.com -->
# extend: * login azure -> ***app resgistration  --> outlook-auth-app -> cretificate & secrets --> client secrets --> add new client
##scope offline_access is so important
# 
# Excel file
# templateFile =r"Q:\Manufacturing\Manheim\Shipping and Inventory\Manheim Raw Materials Inventory Transfer file - Live.xlsx"
# Q:\Sales\Estimating\Software\outlook_email\main.py

#### git Running Branch***************

#### first run the auth.py file to authenticate the user then run main

if __name__ =="__main__":
    print ("python -> running outlook -> main")
        
    import json
    from O365 import Account, Connection
    from datetime import datetime
    import sys
    import os
    from fileDateCheck import *
    import ctypes
    
    # default meaning it is running from windows schedule task 
    excelFileModifyUserNmae= "AES System"
    filePath=""
    
    # runTimeStoreFile =r"\\10.144.10.11\data\Sales\Estimating\Software\outlook_email\runTimeStore.xlsm"
    # o365_token_file= r"\\10.144.10.11\data\Sales\Estimating\Software\outlook_email\o365_token.txt"
    
    runTimeStoreFile =r"C:\Users\atiqu\Desktop\outlook_email\runTimeStore.xlsm"
    o365_token_file= r"C:\Users\atiqu\Desktop\outlook_email\o365_token.txt"
    
    try:
        excelFile= sys.argv[1]
        modifyerNameAndPath= excelFile.split("--") 
     
        if len(modifyerNameAndPath) ==2:
            excelFileModifyUserNmae =modifyerNameAndPath[0]
            filePath =modifyerNameAndPath[1]
    except:
        filePath =r"\\10.144.10.11\data\Sales\Estimating\Software\outlook_email\Manheim Raw Materials Inventory Transfer file - Brian.xlsm"
        # logged username
        GetUserNameExW = ctypes.windll.secur32.GetUserNameExW
        name_display = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameExW(name_display, None, size)

        name_buffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameExW(name_display, name_buffer, size)
        excelFileModifyUserNmae= name_buffer.value
        
    ###check and return modify date
    ###return type is an array
    fileCheckReturnData = fileCheck(filePath, runTimeStoreFile)

    if fileCheckReturnData:
        id ='01fced37-a3fb-435c-ac41-61b04bf7f588'
        passWord='f2adc092-21f2-44a6-8cc2-8d08592bf238'
        tId= "fa9af012-fc87-437c-8a05-d5404aa323da"
        
        credentials = (id, passWord)
        heading ="Overstock Items-Manheim File Update"
        acc= Account(id, auth_flow_type='public', tenant_id=tId)

        
        listOfEmail =['matiq@aesclean.com']
       
        ####___________________3 methods that res for sending, authenticate and token refresh
        def SendEmail (account):
            print ("Sending email  ---------------------------------")
            m_mailbox = account.mailbox(resource='system@aesclean.com')
            
            mail = m_mailbox.new_message()
            mail.to.add(listOfEmail)
            mail.subject = heading
            
            # for email attach
            # image =r"\\10.144.10.11\data\Sales\Estimating\Software\outlook_email\aesLogo.png"
            # mail.attachments.add(image)
            # # getting object of attached
            # att = mail.attachments[0] 
            # # this is super important for this to work.
            # att.is_inline = True
            # att.content_id = 'image.png'
           
            body = """
                <div>
                <p> Hi- </p>
                <p>  """ + excelFileModifyUserNmae + """: Manheim Raw Materials Inventory Transfer file updated at """ + str(fileCheckReturnData[0]) +"""  </p>
                </div>
                
                <br>
                <br> 
                
                <div>
                    <table>
                        <tbody>
                            <tr>
                                <td style="padding-right:10px">
                                    <span style="color:#007cc2;text-decoration:none;font-family:'Nunito Sans',sans-serif">
                                        <a href="https://www.aesclean.com/" style="color:#007cc2;text-decoration:none;font-family:'Nunito Sans',sans-serif" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.aesclean.com/&amp;source=gmail&amp;ust=1708277483349000&amp;usg=AOvVaw2-2UWWTw9Xb7Xr-WkEBpG2">
                                            <img src="https://www.aesclean.com/wp-content/themes/wp_theme_lyquix/images/logo.svg" 
                                            border="0" alt="AESLogoEmailSignature11579119834.png" height="44" width="200" class="CToWUd" data-bit="iit" jslog="32272; 1:WyIjdGhyZWFkLWY6MTczNjI3MTExNTQ2ODMwMjM4OCJd; 4:WyIjbXNnLWY6MTczODE3NTc5Mjc3Nzc1NDI5NSJd">
                                        </a>
                                    </span>
                                </td>
                                <td style="border-left:solid 1px #aad044;padding-left:10px">

                                    <span style="font-size:20px;font-family:tahoma,arial,helvetica,sans-serif;color:#000000;line-height:20px">
                                        <strong>AES System</strong>
                                    </span>
                                    <br>
                                        <span style="font-family:tahoma,arial,helvetica,sans-serif">
                                            <span style="font-size:14px;line-height:20px">W: </span>
                                            <span style="color:#00a3e2;font-size:14px;line-height:20px"><a href="https://www.aesclean.com/" style="color:#00a3e2;font-size:14px;line-height:20px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.aesclean.com/&amp;source=gmail&amp;ust=1708277483350000&amp;usg=AOvVaw0nbwZz1lg3JzRvR_OE8rjv">aesclean.com</a>
                                            </span>
                                        </span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <br>
                    <br> 
                    <p> </p>
                <div>"""

            mail.body = body
            re= mail.send()
            if re:
                print ("email send----------------------------------")
                fileCheckReturnData[1].save(runTimeStoreFile)
            else:
                return False

        def userAuthenticate():
            ##This is just of authenticate###
            # in order to use outlook you must have to authenticate
            # once you run code it will give an consent url 
            # then past the url into the browser ** Pay attention when copy the url ***sometime (Past in the text file) is the good idea** 
            # It will generate the tocken in the url ***long than past url make sure not broken**  ***(Past in the text file)
            # copy the url and past as a input where programs run

            ####try ####
            ###until you the see this mesg ***Authentication Flow Completed. Oauth Access Token Stored. You can now use the API.***
            scops=["https://graph.microsoft.com/Mail.Read", "https://graph.microsoft.com/Mail.Send", "offline_access"]
            account = Account(id, auth_flow_type='public', tenant_id=tId)
            if account.authenticate(scopes=scops):
                return True

        def RefreshToken():
            print ("Refreshing token---------")
            con =Connection(id, auth_flow_type='public', tenant_id=tId)
            token =con.refresh_token()
            return token

        token_expires_at=""
        if os.path.isfile(o365_token_file):   
            with open(o365_token_file) as text:
                a=text.read()
                o365_Token_data=json.loads(a)
                ex_tokenDate =o365_Token_data["expires_at"]
                token_expires_at = datetime.fromtimestamp(ex_tokenDate)
        else:
            print ("Token file not found")
            
        currDate =datetime.now()
        
        if acc.is_authenticated and (str(acc.get_current_user())== "System AESClean"):
            print ("User authenticated")
            if (currDate and token_expires_at) and (currDate > token_expires_at):
                print ("Token expire-----------------------")
                if  RefreshToken():
                    SendEmail(acc)
            else:
                SendEmail(acc)
        else:
            if userAuthenticate():
                if acc.is_authenticated:
                    if SendEmail(acc) == False:
                        print ("user is not authenticated, Please contract With **MD")
