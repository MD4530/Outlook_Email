# a= 1708194645.1026292
# a=1708240009.1613967
# a= 1708244335.525097
# a=1708272077.007982

# import json

# o365_Token_data=""
# with open(r"o365_token.txt") as text:
#     a=text.read()
#     o365_Token_data=json.loads(a)

# # a=o365_Token_data["expires_at"]
a=1709048455.4430487

from datetime import datetime
dt_obj = datetime.fromtimestamp(a)
curr =datetime.now()
curr =curr.timestamp()

print("date_time:",curr )




# https://login.microsoftonline.com/fa9af012-fc87-437c-8a05-d5404aa323da/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.Send+https%3A%2F%2Fgraph.microsoft.com%2FMail.Read&state=1PIVOO3q5oPIXB5MRlp8evQbJlSxM4&access_type=offline

# https://login.microsoftonline.com/fa9af012-fc87-437c-8a05-d5404aa323da/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsofton


# https://login.microsoftonline.com/fa9af012-fc87-437c-8a05-d5404aa323da/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.Read+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send&state=CyCvHUdXTIOYC5PZzJ8bHY4wnpiGe2&access_type=offline

# https://login.microsoftonline.com/common/oauth2/nativeclient?code=0.ARgAEvCa-of8fEOKBdVASqMj2oDewaR3PkhApbpfzu6vwogYANI.AgABAAIAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P9uFyVTJvkLujDQ1__IvCe6Pkh7DWAdzy84FZ8B6msqF8V9EEYVzZgFk24Ut2HIiRqHKWORcKqi77KmN2jTG0_UW5fQFDRN0N-i7-dWs9nLnmcTFMzl_6C9vFcfdJgDLbsTNlhBw8xvlCSzALs3NUhXMseOUn5SWXO-MzyPuTWgVT2FUKsyn4nSdXkRcKQ9NL4p-X3sFyrz7xNjJ-zSm5gVXUWWnr4dndJ7UiKpO_hC_cLUDxH6DONB-lvCCNVyQAxeDC2xMYEKDa1STHPpXF247pUJKkIVF5_uGflKJyFsPXPei04LTeFaG4u1Gnz2zC7KEpu8HofkeA-QugiSk8cE_i9bOdsjD744S0EYMptrURroSYQ7eZ2KNYBPiDwipJ0Ck604DIqLyFiVRHlNgUjFqkiHyNpuu366NYWXW0Ua68sDMC9YzkrfiX5ozbkceqVmJS7cAvWfmVxtiyMnQTbQONF-3TmRj4eHu0elHYeq1-JkvrzXqt4sNeFWE3haNfQ23zw_Opj1CK80dVePl_rkfcMVdgo1E-VCx3x2mTuE0nLX3nlRhc0LwsUGUC2U6lxnFnEIcgruwJhnrfd5pP2xUWOSMUXBijY69EqxJCC93DuM5-sE_aGZbukZMg8oOI2AUGiP5ajK7FTMFVT6LTLixnnOjNfU_W6wPBv94YFENDmXoKDed9tlUFzGtRk_kJlA4JYFxt1AP2_8HeKTeO67AKJNTyNZspY&state=CyCvHUdXTIOYC5PZzJ8bHY4wnpiGe2&session_state=5ca477db-5ac3-4850-a801-0b565919a00a


# https://login.microsoftonline.com/common/oauth2/nativeclient?code=0.ARgAEvCa-of8fEOKBdVASqMj2oDewaR3PkhApbpfzu6vwogYANI.AgABAAIAAAAmoFfGtYxvRrNriQdPKIZ-AgDs_wUA9P8bqLi2NOInf-O0JaxzsevEvmBeP2mcliRJv-xBegpFeg3Lbu4ShbSEizmf2YMcY1ZkG7ShvUL3LQvycchOiRc9xPFH7bk4OXv6Hq8ue7fnmn8EWJKgjd_S-llSvzRrsTB54utEKG725W9eXGRyWfq64MfqOEJfe4CA21T_V-lsKqUqnqSGlf1MinnSr91qmJnVYL5Beixfz2nbxU5OWO-qyF6gjNM3MdgmrqPpwZGgs0APH7ejCSfF_9o42Ctgv-jkC4P2uUy3H2GOdkTvlX5WZ_omysRzrezotyuJn_JaM-27dsip4TY5kmV6XyGai2oNRC5j09oZRjK6k5DEXEGE0bEl0fWrkv4_BYmqIzUGbOaqIdqCrHygH7VERtGZvFLxUEZpONkwHwzClqyQQj2s1lTRjnmSI0TN-HPaWtsY_Bbtk5hgjn9CB3WJ9w7tIPUEaX3lC8y0nvkmF0d9d-25hAC1PYlUnfnjFjnqrSy4K8SvW3tVbabRk7JOAzztVAjSNs4TH29WJa1TwjExMlvUDeEd8sSppmjhAif_6HEHChR8N3aS7XJUeDMiTL6_c6h7nK8bhzgqQ7l6rNpp1jW-zkZziau0nM098e9N3V2BnnUZG8C0tDb9WTMMmNVOLXnSWjPpzvljY_dHa5sqkitFMMf4trB8FKEQvpobRoFyUKazsquP_3FcmHCOjrF-n7ylygn9m3Q7KBQGe6hYMpz3gpnNJgpzTw&state=YUMBZ5YyBA6VaIeVsQwo4HDdzea1Jg&session_state=5ca477db-5ac3-4850-a801-0b565919a00a

# https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=https%3A%2F%2Fgraph.microsoft.com%2FUser.Read+https%3A%2F%2Fgraph.microsoft.com%2FMail.ReadWrite+offline_access+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send&state=THDRa6DH9ix0bk4ehc4cdkKWRsG5jh&access_type=offline



# https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.ReadWrite+offline_access+https%3A%2F%2Fgraph.microsoft.com%2FUser.Read+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send&state=crmZbeokgrU77GPPLSB8dyGntyqXzv&access_type=offline

# https://login.microsoftonline.com/common/oauth2/nativeclient?error=invalid_request&error_description=AADSTS50194%3a+Application+%27a4c1de80-3e77-4048-a5ba-5fceeeafc288%27(outlook-auth-app)+is+not+configured+as+a+multi-tenant+application.+Usage+of+the+%2fcommon+endpoint+is+not+supported+for+such+applications+created+after+%2710%2f15%2f2018%27.+Use+a+tenant-specific+endpoint+or+configure+the+application+to+be+multi-tenant.+Trace+ID%3a+d83b5bf4-fca0-4f29-8532-913f080ab201+Correlation+ID%3a+5119e769-676f-4866-82fd-b3aa4d40fe64+Timestamp%3a+2024-02-18+06%3a45%3a29Z&state=crmZbeokgrU77GPPLSB8dyGntyqXzv

# https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=offline_access+https%3A%2F%2Fgraph.microsoft.com%2FMail.ReadWrite+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send+https%3A%2F%2Fgraph.microsoft.com%2FUser.Read&state=HFT8mUalhQT1tP3cLtbeKnyof2Ml3P&access_type=offline
# https://login.microsoftonline.com/common/oauth2/nativeclient?error=invalid_request&error_description=AADSTS50194%3a+Application+%27a4c1de80-3e77-4048-a5ba-5fceeeafc288%27(outlook-auth-app)+is+not+configured+as+a+multi-tenant+application.+Usage+of+the+%2fcommon+endpoint+is+not+supported+for+such+applications+created+after+%2710%2f15%2f2018%27.+Use+a+tenant-specific+endpoint+or+configure+the+application+to+be+multi-tenant.+Trace+ID%3a+d83b5bf4-fca0-4f29-8532-913ff413b201+Correlation+ID%3a+5948c10d-b853-4a83-b281-3114f9d9be72+Timestamp%3a+2024-02-18+06%3a46%3a41Z&state=HFT8mUalhQT1tP3cLtbeKnyof2Ml3P


# https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.Send+https%3A%2F%2Fgraph.microsoft.com%2FMail.Read&state=gEux1zZ5aDiSyNEBcoBdnasHZmx3Og&access_type=offline&tenant_id=fa9af012-fc87-437c-8a05-d5404aa323da


# https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.Read+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send&state=5pDaECHFeh7VyloGftCP7Ql3tU3PZw&access_type=offline&tenant_id=fa9af012-fc87-437c-8a05-d5404aa323da


# https://login.microsoftonline.com/fa9af012-fc87-437c-8a05-d5404aa323da/oauth2/v2.0/authorize?response_type=code&client_id=a4c1de80-3e77-4048-a5ba-5fceeeafc288&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&scope=offline_access+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send+https%3A%2F%2Fgraph.microsoft.com%2FMail.Read&state=qrRo7W7Y3rqEKz4GkD8pxyneQinFIC&access_type=offline

# https://login.microsoftonline.com/common/oauth2/nativeclient?code=0.ARgAEvCa-of8fEOKBdVASqMj2oDewaR3PkhApbpfzu6vwogYANI.AgABAAIAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P_TohKzRV99QB_KtsH53qKyxAb0tYQunuVAop9_DF70Dggbda0iGumPr2R9AOZNA0utRMOn-Ncev0naAPul8vW3YhNxMoMxkP2f-bS_Qk6hh1cIrDAKRbgfcO9Qu_-qfmoIsd6kUwu0-m4kq5SUNiom_epQginzB-z5XzDgkp37fS2QFEmTL0BqYxsmkx6RRIvxZln4ASkmJRzhSR8dxaxSI1b85deQ1UO4vJWimu7r7nf4TELm4alxvdc6YEb6FzdjHv6gXNSOO5W1Q6KFW6dfO8rCMDWZyx2FJXgtnzmSdD0IFbN6HBTGiEPHzHTY-mdNyM0Bm3z3JPCBBeM1gKxcE53zXxenxZeYLDeYN4T7313bWyEm4p85nMyen_aPGU8PmaCRlS_NNfILdEYDJCnLmHFFW5yuoIU9dwIFMCAM7ta0C8ewp8N2jFPo_GqO7P1_DmvUj4_SWHNDeXBzhdnqyV6YDShYZXeEa8jEbGbVsbzwEHxysUY_OpDnkqBRWUxR4XzpQDjgOi2OZ1rmarQBPvMevMeGQIk9rdIeaqSWLBduS8ujGMXk31HVOYBznghDCP0LaEWKf7iCLqK97QLRHJaXpvwyV8ewDTToq5Z_SEoTScq-dJrU5C1cbkHp-BO6kDsMFU1i-R-gtJkBBXTJ43ShjWCcAevggfuXvVbjMwe358MHooU4k18RPMkaH61XhFZCuhUbSNvQFgeVURKahzhVFRTg6dAHXILjMYDph-xxYlU9pImbHw_7KxpmqdU-N1SA&state=qrRo7W7Y3rqEKz4GkD8pxyneQinFIC&session_state=5ca477db-5ac3-4850-a801-0b565919a00a

















# https://login.microsoftonline.com/common/oauth2/nativeclient?error=invalid_request&error_description=AADSTS50194%3a+Application+%27a4c1de80-3e77-4048-a5ba-5fceeeafc288%27(outlook-auth-app)+is+not+configured+as+a+multi-tenant+application.+Usage+of+the+%2fcommon+endpoint+is+not+supported+for+such+applications+created+after+%2710%2f15%2f2018%27.+Use+a+tenant-specific+endpoint+or+configure+the+application+to+be+multi-tenant.+Trace+ID%3a+d83b5bf4-fca0-4f29-8532-913ff413b201+Correlation+ID%3a+5948c10d-b853-4a83-b281-3114f9d9be72+Timestamp%3a+2024-02-18+06%3a46%3a41Z&state=HFT8mUalhQT1tP3cLtbeKnyof2Ml3P