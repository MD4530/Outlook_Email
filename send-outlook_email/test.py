# from O365 import Account, Connection

# credentials = ('a4c1de80-3e77-4048-a5ba-5fceeeafc288')
# listOfEmail =['matiq2536@gmail.com', ]###'atiqzzaman@diit.info', "atiquzzaman_rc@ymail.com", "ma3766@drexel.edu"

# con =Connection(credentials, auth_flow_type='public', tenant_id="fa9af012-fc87-437c-8a05-d5404aa323da")
# token =con.refresh_token()

# print (token)


import ctypes
GetUserNameExW = ctypes.windll.secur32.GetUserNameExW
name_display = 3

size = ctypes.pointer(ctypes.c_ulong(0))
GetUserNameExW(name_display, None, size)

name_buffer = ctypes.create_unicode_buffer(size.contents.value)
GetUserNameExW(name_display, name_buffer, size)
print (name_buffer.value)




# import win32com.client as win32

# olApp = win32.Dispatch('Outlook.Application')
# olNS = olApp.GetNameSpace('MAPI')

# # construct email item object
# mailItem = olApp.CreateItem(0)
# mailItem.Subject = 'Hello 123'
# mailItem.BodyFormat = 1
# mailItem.Body = 'Hello There'
# mailItem.To = 'matiq2536@gmail.com'
# mailItem.Sensitivity  = 2
# # optional (account you want to use to send the email)
# mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('matiquz1@student.ccp.edu')))
# mailItem.Display()
# mailItem.Save()
# mailItem.Send()