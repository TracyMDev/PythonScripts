#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create a dictionary of loans and thier amounts
loan_dict = [
 {'name':'Ideal','TotalAmount':2808.31,'Pay':1309.74},
 {'name':'Discover','TotalAmount':4392.34,'Pay':138.91},
 {'name':'UHEAA','TotalAmount':4891.68,'Pay':340.89},
 {'name':'Amex','TotalAmount':4969.68,'Pay':135},
 {'name':'Navient','TotalAmount':8947.93,'Pay':131.95},
 {'name':'CapitalOne','TotalAmount':10853.02,'Pay':274}
]

#total_payment = 959.74

print(loan_dict)


# In[2]:


loan_dict[1]


# In[4]:


for x in loan_dict:
    print(x['name'])


# In[5]:


for x in loan_dict:
    print(x)


# In[6]:


sum = 0

for x in loan_dict:
   
    #print(x['name']+" "+ str(x['TotalAmount']))
    
    print("The amount due for " + x['name'] + " is: " + str(x['TotalAmount']))
    #
    print("\tThe current monthly payment is: " + str(x["Pay"]))
    
    #set the incremented payment amounts      
    
    if sum == 0:
        sum = x["Pay"]
    else:
        sum = sum + x["Pay"] #add the previous sum
    
    print(f"\tIncremented payment will be {sum:.2f}")
    
    pay_off_months = x['TotalAmount']/sum
    
    adju_total = x['TotalAmount'] - (pay_off_months * x["Pay"])
    
    
    
    print(f"This will take {pay_off_months:2f} months to pay off")
    
    
    
    


# In[ ]:





# In[ ]:




