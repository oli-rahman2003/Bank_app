#!/usr/bin/env python
# coding: utf-8

# In[19]:


from Account import Account 

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.list_of_accounts = []
    
    def set_username(self, newUsername):
        self._username = newUsername
    
    def get_username(self):
        return self.username
    
    def set_password(self, newPassword):
        self.password = newPassword
    
    def get_password(self):
        return self.password
        
    def add_account(self, account):
        if type(account) == Account:
            self.list_of_accounts.append(account)
            
    def remove_account(self, account_number):
        for account in self.list_of_accounts:
            if account_number == account.get_account_number():
                self.list_of_accounts.remove(account)
            
    def print_list_of_accounts(self):
        for account in self.list_of_accounts:
            account.print_account_info()
            
    def print_specific_account(self, account_number):
        for account in self.list_of_accounts:
            if account_number == account.get_account_number():
                account.print_account_info()
            
    def print_customer_info(self):
        print(f"Username: {self.username}, Password: {self.password}")


# In[20]:


customer1 = Customer("oli_rahman", "password")


# In[21]:


customer1.get_username()


# In[22]:


customer1.set_username("shah")


# In[23]:


customer1.get_username()


# In[24]:


customer1.set_password("wordpass")


# In[25]:


customer1.get_password()


# In[26]:


account1 = Account(123, 400)


# In[27]:


customer1.add_account(account1)


# In[28]:


account2 = Account(456, 700)


# In[29]:


customer1.add_account(account2)


# In[30]:


customer2 = Customer("hans", "solo")


# In[31]:


account3 = Account(987, 1000000)


# In[32]:


customer2.add_account(account1)


# In[33]:


customer2.print_list_of_accounts()


# In[34]:


customer2.remove_account(987)


# In[35]:


customer2.print_specific_account(456)

