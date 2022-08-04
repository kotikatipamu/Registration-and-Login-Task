#!/usr/bin/env python
# coding: utf-8

# In[90]:


ids = {
    "kittu@gmail.com" : "Kittu1995#",
    "koti@gmail.com":"Koti@1995"
}


# In[91]:


print("Enter your Mail-ID : ")
mail = input()
mail.split()
spl = "1234567890!@#$%^&*()-+"
spl1 = "!@#$%^&*()-+=_<>"
num = "1234567890"
alp = "qwertyuiopasdfghjklzxcvbnm"
calp = "QWERTYUIOPASDFGHJKLZXCVBNM"
a = mail.find("@")
b = mail[:a]
for i in spl :
    if i[0] != spl :
        if '@' in mail:
            if '.' in mail:
                
                if '@.' in mail:
                    print("""'.' can't be follwed by '@' """)
                else:
                    if mail in ids:
                        print('enter password')
                        passwd = input()
                        if ids[mail] == passwd :
                            print(" welcome you have logged in")
                        else:
                            print("worng password")
                        
                        
                       
                    else:
                        print('register your ac')
                        print('your mail-id not registered, if you want register type :yes')
                        choice = input()
                        if choice =="yes":
                            sv = mail
                            print('enter new password, it should contain cap,num,spl-char')
                            password =input()
                            l, u, p, d = 0, 0, 0, 0
                            c = len(password)
                            if c>5 and c<16 :
                                for j in password:
                                    if j in spl:
                                        l = l+1 
                                    if j in spl1:
                                        u =u+1
                                    if j in alp:
                                        p=p+1
                                    if j in calp:
                                        d = d+1
                                if l>0 and u>0 and p>0 and d>0 :
                                    print('valid password')
                                ids.update({mail: password})
                                break
                                
                               
                            else:
                                print("len is too short or lengthy")
                                 
                        else:
                             print("please reg to use  mail")
                        
                        break
            else:
                print("'.' is miissing")
        else:
            print("@ is missing")
    else:
        print(" starting word should not be spl char")
        
        


# In[ ]:





# In[ ]:




