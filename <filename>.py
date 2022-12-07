1st task code

import re
validate=[]
validate1=r"^[0-9]{10}$"
validate2=r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
validate3=r"^[+][1][0-9]{10}$"
validate4=r"^[+][0-9]{3}-[0-9]{3}-[0-9]{4}$"
validate5=r"^[0-9]{3}[ ][0-9][3][ ][0-9]{4}$"
validate6=r"^[0-9]{3}.[0-9]{3}.[0-9]{4}$"
validate7=r"^[1]-[0-9]{3}-[0-9]{3}-[0-9]{4}$"
validate8=r"^[+][1][ ][0-9]{3}.[0-9]{3}.[0-9]{4}$"
validate9=r"^[(][0-9]{3}[)]-[0-9]{3}-[0-9]{4}$"
validate10=r"^[(][0-9]{3}[)][0-9]{3}-[0-9]{4}$"
phone_number=input()
validate.append(validate1)
validate.append(validate2)
validate.append(validate3)
validate.append(validate4)
validate.append(validate5)
validate.append(validate6)
validate.append(validate7)
validate.append(validate8)
validate.append(validate9)
validate.append(validate10)
flag=1
for i in validate:
    valid=re.search(i,phone_number)
    if valid:
        print("valid")
        flag=0
        break
if(flag==1):
    print("invalid")
