from multiprocessing.dummy import current_process
import hikari
import lightbulb
import time
from datetime import datetime
import requests
import json
import keep_alive
import os

cookie = os.getenv("ROBLOSECURITY")

groupID = 7501334 #Group ID for LGBTQ+ Family
url = 'https://groups.roblox.com/v2/groups/' + str(groupID) + '/join-requests?sortOrder=Asc&limit=10' #The API endpoint I'm using, formated to the above variable
authurl = 'https://auth.roblox.com/v2/login' #AUthenitaction endpoint
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
claimGroupURL = "https://groups.roblox.com/v1/groups/" + str(groupID) + "/claim-ownership"
deleteRequestsURL = "https://groups.roblox.com/v1/groups/7501334/join-requests"
rankURL = "https://groups.roblox.com/v1/groups/" + str(groupID) + "/users/"
shoutURL = "https://groups.roblox.com/v1/groups/" + str(groupID) + "/status"

def xsrf(): #Gets an authentication token 
    xsrfRequest = requests.post(authurl, cookies={
        '.ROBLOSECURITY': cookie
    }) #"Asks" for the token and provides the login cookie to authenticate
    return xsrfRequest.headers["x-csrf-token"] #Returns the token
xsrf = xsrf()
print(xsrf)

def claimGroup(): #Claims the group every second
    groupClaimer = requests.post(claimGroupURL, headers={
        'User-Agent': userAgent,
        'x-csrf-token': xsrf
    }, cookies={
        '.ROBLOSECURITY': cookie
    })
    return groupClaimer

def deleteRequests():
    declineRequests = requests.delete(deleteRequestsURL, headers={
        "User-Agent": userAgent,
        "x-csrf-token": xsrf
    }, cookies={
        ".ROBLOSECURITY": cookie
    }, data={
        "UserIds": [
            1617976104,
            1508292822,
            2436685760,
            2229204507,
            2796147013,
            3040138087,
            1617976104,
            1879756333,
            3807066600,
            3743968919,
            7660391,
            3550366501,
            3547378538,
            3571520424,
            2459350928,
            1480792717,
            2821900710,
            2825660191,
            193991878,
            1879756333,
            1944229476,
            2849359137,
            2812472507,
            2620823401,
            2816799912,
            2796147013,
            3038961259,
            2952236753,
            3063754717,
            1175748299,
            727801468,
            3105581948,
            69879168,
            3192984896,
            1469651297,
            2917878646,
            2659084391,
            1622667369,
            2379483862,
            3277454880,
            1941196582,
            2255151236,
            3274405938,
            2374561085,
            1996400379,
            530569007,
            2947046526,
            2639322466,
            837802681,
            3427490985,
            914965472,
            200371028,
            2064186687,
            591872745,
            2294691186,
            3160455565,
            2674049979
            ,2325709877,
            21812353,
            3341025664,
            3553982244,
            3423278193,
            1404513875,
            422349030,
            2258545188,
            3743968919,
            7660391,
            3550366501,
            3547378538,
            3571520424,
            1480792717,
            2459350928,
            2821900710,
            2825660191,
            193991878,
            1879756333,
            1944229476,
            2849359137,
            3063754717,
            1175748299,
            727801468,
            310558194,
            69879168,
            3192984896,
            1469651297,
            2917878646,
            2659084391,
            1622667369,
            2379483862,
            3277454880,
            1941196582,
            2255151236,
            3274405938,
            2374561085,
            3215460585,
            530569007,
            2947046526,
            2639322466,
            837802681,
            3427490985,
            914965472,
            200371028,
            2064186687,
            591872745,
            2294691186,
            3160455565,
            2674049979,
            2325709877,
            21812353,
            3341025664,
            3553982244,
            3423278193,
            1404513875,
            422349030,
            2258545188,
            2999764533,
            3127800910,
            2287745243,
            2406467175,
            3205896354,
            1140847215,
            2884757011,
            3609185286,
            3379908101,
            2603795054,
            2766154096,
            2229957259,
            3637826701,
            2644088939,
            3233055887,
            862104237,
            3288376001,
            3046708596,
            1117793592,
            3036516799,
            185923454,
            2630966075,
            3743968919,
            7660391,
            1480792717,
            1488216712,
            1966236854
        ]
    })
    return declineRequests

def changeShoutFun(shoutText):
    changeShout = requests.patch(shoutURL, headers={
        "User-Agent": userAgent,
        "x-csrf-token": xsrf
    }, cookies={
        ".ROBLOSECURITY": cookie
    }, data={
        "message": shoutText
    })
    return changeShout

def whatRank(ranktype):
    if ranktype == "supporter":
        return 47032930
    elif ranktype == "gay":
        return 47033494
    elif ranktype == "lesbian":
        return 47033590
    elif ranktype == "bisexual":
        return 47034218
    elif ranktype == "transgender":
        return 47034323
    elif ranktype == "pansexual":
        return 47034527
    elif ranktype == "asexual":
        return 47072605
    elif ranktype == "nonbinary":
        return 47079279
    elif ranktype == "questioning":
        return 48687950
    elif ranktype == "demisexual":
        return 49125077
    elif ranktype == "genderfluid":
        return 51468171
    elif ranktype == "polysexual":
        return 51468291
    elif ranktype == "omnisexual":
        return 51601102
    elif ranktype == "abrosexual":
        return 52275831
    elif ranktype == "demigender":
        return 52368914
    elif ranktype == "aromantic":
        return 53165446
    elif ranktype == "furry":
        return 54855398
    elif ranktype == "other":
        return 55561801
    elif ranktype == "agender":
        return 60841743
    elif ranktype == "bigender":
        return 60867931
    elif ranktype == "trigender":
        return 60868096
    elif ranktype == "pangender":
        return 61800394
    elif ranktype == "polyamorous":
        return 61800404
    else:
        return "Fail"

def userRanking(requestID, rankType): 
    print(rankType)
    rankuser = requests.patch(rankURL + requestID, headers={
        "User-Agent": userAgent,
        "x-csrf-token": xsrf,
        "Content-Type": "application/json"
    }, cookies={
        ".ROBLOSECURITY": cookie
    }, json={
        'roleId': rankType
    })
    return rankuser

bot = lightbulb.BotApp(
    token=os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=(785618905665896478)
)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

@bot.command
@lightbulb.option('time', 'Type 0 for immediately or a give an hour in 24 hour time (i.e. 2:00 AM = 2, 5:00 PM = 17, 12 AM = 24', type=int)
@lightbulb.option('whatshout', 'String to be shouted out', type=str)
@lightbulb.command('shout', 'Queues shout')
@lightbulb.implements(lightbulb.SlashCommand)
async def shout(ctx):
    print("Success")
    now = datetime.now()

    if ctx.options.time == 0:
        changeShoutFun(ctx.options.whatshout)
    elif type(ctx.options.time) is int:
        if ctx.options.time >= 1 and ctx.options.time <= 24:
            current_hour = int(now.strftime("%H"))
            current_minute = int(now.strftime("%M"))
            shoutTime = ctx.options.time
            current_hour *=60
            current_minute *= 60
            shoutTime *= 60
            current_hour *= 60
            shoutTime *= 60
            shoutTime -= current_hour
            shoutTime -= current_minute
            time.sleep(shoutTime)
            changeShoutFun(ctx.options.whatshout)
    else:
        await ctx.respond("Invalid data")

    await ctx.respond('Success!')


@bot.command
@lightbulb.command('denybanlist', 'Denies entry to anyone on the ban list')
@lightbulb.implements(lightbulb.SlashCommand)
async def banlist(ctx):
    print ("Success")
    issuccessful = deleteRequests()
    if issuccessful == "<Response [400]>":
        await ctx.respond("Success!")
    else:
        await ctx.respond(issuccessful)

@bot.listen(hikari.GuildMessageCreateEvent)
async def detectUserRankRequest(event):
    request = event.content
    request2= event.content
    if "|" in request:
      genderRequest = request.split("|")[0]
      requestID = request2.split("|")[1]
      gender = whatRank(genderRequest)
      if gender != "Fail":
          print(userRanking(requestID, gender))
      else:
        print("Fail!")

keep_alive.keep_alive()
bot.run()
