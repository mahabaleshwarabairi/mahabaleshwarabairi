# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:31:43 2020

@author: Mahabaleshwara.Bairi
"""

c={'I':'NEW DEHI',
   'UK':'London'}
print ('\n  the capital of india is: %s' %c['I']) ##print single item
c['japan']='Tokyo'
print ('\n There are %d in the dist:' %len(c)) ## lenth of dist
print('\n')
for country,capital in c.items ():  ## loop and get key pair values 
    print ('capital of %s is %s'%(country,capital))

c['pak']='lahore'
print ('\n there are %d pair in disct' %len(c))

print('\n')

for country,capital in c.items ():  ## loop and get key pair values 
    print ('capital of %s is %s'%(country,capital)) 
    
print('\n')

print ('deleting the dist')
del c['pak']
print('\n')


for country,capital in c.items ():  ## loop and get key pair values 
    print ('capital of %s is %s'%(country,capital))
print('\n')

print ('Checking the id in dist and display')

if 'I' in c:
    print ("capital of india is %s" %c['I'])
    
    



    