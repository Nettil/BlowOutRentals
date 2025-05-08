"""
@author Nathan Lee
@date 5/8/25
"""
from  django.shortcuts import render
from django.http import HttpResponse


def trumpetPageView(request,name, trumpet_name, email_address) :
      info={
          "customer_name": name,
          "trumpet_name": trumpet_name,
          "email_address": email_address,

}
      return render(request,'inventory/trumpet.html',info)
    #  sOutput = f'<html><head><link href=\"https://fonts.cdnfonts.com/css/public-pixel\" rel=\"stylesheet\"><title>Contact Us</title></head><body style=" background-color:charcoal;font-family: \'Public Pixel\', sans-serif;"><p style="color:gray; font-size:26px; padding:10px;"><b>Contact Us </b><p style="font-size:18px; background-color:#ADEBB3; border-radius:30px; padding-top:10px; font-size:16px; padding-left:10px; padding-right:10px; padding-bottom:realtive;">{first_name} {last_name},  we will contact you at {email_address}</p><div style="color:gray; padding:10px;font-size:16px;"><p><b>Explore</b></p><div style="color:black;font-size:16px; background-color:#ADEBB3; border-radius:30px; padding-top:10px; font-size:16px; padding-left:10px; padding-right:10px; padding-bottom:realtive;"><li><a href=/>Site Index</a></li><li><a href=/about>About Us</a></li><li><a href=/contacts>Contact Us</a></li></ul><br></div></body></html>'
    #  return HttpResponse(sOutput)

def instrumentsPageView(request,instrument_name, price, stock) :
      item_info={
          "item_name": instrument_name,
          "price": price,
          "stock": stock,

}
      return render(request,'inventory/trumpet.html',item_info)
