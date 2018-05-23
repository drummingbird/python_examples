# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:50:05 2018

@author: Reuben

This example illustrates why composition is generally preferred over
inheritance .

Example from http://masnun.com/2016/04/19/composition-over-inheritance.html

"""


class EmailClient:
    def setup(self):
        return "Initializions and configurations!"
 
    def send_email(self, msg):
        raise NotImplementedError("Use a subclass!")
 
 
class GmailClient(EmailClient):
    def send_email(self, msg):
        return "Sending `{}` from Gmail Client".format(msg)
 
 
class YahooMailClient(EmailClient):
    def send_email(self, msg):
        return "Sending `{}` from YMail! Client".format(msg)
 
 
def demonstrate():
    client = GmailClient()
    client.setup()
     
    ret_a = client.send_email("Hello!")
    print(ret_a)
     
    # If we want to send using Yahoo, we have to construct a new client
    # That's OK for a simple example, but can be a major headache for more 
    # complex classes.
     
    yahoo_client = YahooMailClient()
    yahoo_client.setup()
     
    ret_b = yahoo_client.send_email("Hello!")
    print(ret_b)
