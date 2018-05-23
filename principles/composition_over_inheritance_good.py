# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:51:08 2018

@author: Reuben

This example illustrates why composition is generally preferred over
inheritance .

Example from http://masnun.com/2016/04/19/composition-over-inheritance.html

"""


class GmailProvider:
    def send(self, msg):
        return "Sending `{}` using Gmail".format(msg)
 
 
class YahooMailProvider:
    def send(self, msg):
        return "Sending `{}` using Yahoo Mail!".format(msg)
 
 
class EmailClient:
    email_provider = GmailProvider()
    
    def setup(self):
        return "Initialization and configurations"
 
    def set_provider(self, provider):
        self.email_provider = provider
 
    def send_email(self, msg):
        return self.email_provider.send(msg)
 

def demonstrate():
    client = EmailClient()
    client.setup()
     
    ret_a = client.send_email("Hello World!")
    print(ret_a)
    
    # Now, we can just set a different provider, without having to 
    # create a new email client instance.
    
    client.set_provider(YahooMailProvider())
    ret_b = client.send_email("Hello World!")
    print(ret_b)