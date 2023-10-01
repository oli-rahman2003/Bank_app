#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Account:
        def __init__(self, accountNumber, balance):
            self.accountNumber = accountNumber
            self.balance = balance
            
        def get_balance(self):
            return self.balance

        def set_balance(self, new_balance):
            if new_balance >= 0:
                self.balance = new_balance
                
        def get_account_number(self):
            return self.accountNumber
        
        def set_account_number(self, account_number):
            self.accountNumber = account_number
            
        def print_account_info(self):
            print(f"Account Number: {self.accountNumber}, Balance: {self.balance}")
            


# In[28]:


account = Account(123, 500)


# In[29]:


account.get_balance()


# In[30]:


account.set_balance(600)


# In[31]:


account.get_balance()


# In[32]:


account.get_account_number()


# In[33]:


account.set_account_number(456)


# In[34]:


account.get_account_number()


# In[35]:


account.print_account_info()

