"""
@author Nathan Lee
@date 5/8/25
"""
from  django.shortcuts import render
from django.http import HttpResponse
def indexPageView(request) :
    #sOutput = f'<html><link href=\"https://fonts.cdnfonts.com/css/public-pixel\" rel=\"stylesheet\"><head><title>Welcome</title></head><body style=\"background-color:charcoal; font-family: \'Public Pixel\', sans-serif;\"><p style=\"color:lime; font-size:42px\"><b>NexaByte Interactive Studios</b><br><div style="color:gray; padding:10px;font-size:16px;"><p><b>Explore</b></p><div style="color:black;font-size:16px; background-color:#ADEBB3; border-radius:30px; padding-top:10px; font-size:16px; padding-left:10px; padding-right:10px; padding-bottom:realtive;"><li><a href=/>Site Index</a></li><li><a href=/about>About Us</a></li><li><a href=/contacts>Contact Us</a></li></ul><br></div><p style="background-color:#ADEBB3; border-radius:30px; padding-top:10px; font-size:16px; padding-left:10px; padding-right:10px;">Welcome Adventurers!</p></body></html>'
    #return HttpResponse(sOutput)
    return render(request,'homepages/index.html')
def aboutPageView(request) :
    context={
        "trumpet":"",
    }
            # sOutput = f'<html><head><link href=\"https://fonts.cdnfonts.com/css/public-pixel\" rel=\"stylesheet\"><title>About Us</title></head><body style="background-color:charcoal; font-family: \'Public Pixel\', sans-serif;\"><p style="color:gray; font-size:28px; align:center;"><b>About NexaByte Interactive</b></p><p style="color:Black; background-color:#ADEBB3; border-radius:30px; padding-top:10px; font-size:16px; padding-left:10px; padding-right:10px; padding-bottom:20px;"><b style="color:lime; font-size:20px;"><i>NexaByte Interactive</i></b> is a small indie game studio that creates story driven games for various genres including Roguelites, Dungeon crawlers, Action RPGs, Action-adventures, and more! We focus on creating engaging worlds and stories rendered in classic 16 bit graphics reminiscent of older titles such as The Legend of Zelda, Golden Sun, Secret of Mana, Ultima Underworld, and Hexen, while incorporating more modern mechanics from newer titles such as Caveblazers, Barony. Wizard of Legend, Noita, and many other modern influences. Here at Nexabyte Studios, we want every game to invoke a nostalgic sense of exploration and anticipation for the next discovery. We hope you\'re ready for the next Byte! </p><div style="color:gray; padding:10px;font-size:16px;"><p><b>Explore</b></p><div style="color:black;font-size:16px;background-color:#ADEBB3; border-radius:30px; padding-top:10px; font-size:16px; padding-left:10px; padding-right:10px; padding-bottom:realtive;"><li><a href=/>Site Index</li><li><a href=/about>About Us</li></a><li><a href=/contacts/#>Contact Us</a></li></ul><br></div></body></html>'
        #return HttpResponse(sOutput)
    return render(request,'homepages/about.html',context)

