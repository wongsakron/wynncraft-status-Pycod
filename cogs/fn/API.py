import requests

def data_player(name_player):
    req = requests.get(f'https://api.wynncraft.com/v2/player/{name_player}/stats')
    i = req.json()
    web = f'https://wynncraft.com/stats/player/{name_player}'
    status = i['data'][0]
    a = status['characters']
    keyclass = [*a][0] #! showkey index 0 in dict
    classes = a[keyclass]
    level  =  str(classes['level'])
    classes = classes['type']
    name = status['username']
    firstjoin = status['meta']['firstJoin']
    x = status['guild']
    nameguild = x['name'] 
    rankguild = x['rank']
    tag = status['meta']['tag']['value']
    name = name.capitalize()
    firstjoin = firstjoin[:10]
    classes = classes.capitalize()
    rankguild = rankguild.capitalize()
    data_player ={
        "class" : classes,
        "level" : level,
        "name" : name,
        "first" : firstjoin,
        "guild" : nameguild,
        "rank" : rankguild,
        "tag" : tag,
        "web" : web
    }
    return data_player

def data_guilde(name):
        URl1 = "https://wynncraft.com/stats/guild/"
        URl2 = "https://api.wynncraft.com/public_api.php?action=guildStats&command="
        banners = "https://wynn-guild-banner.herokuapp.com/banners/"
        req = requests.get("https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=guild&timeframe=alltime")
        i = req.json()
        x = i['data']
        for i in x:
            prefix = i['prefix']
            if name == prefix:
                try:
                    war = i['warCount']
                except:
                    war = "None"
                name1 = i['name']
                level = i['level']
                created = i['created']
                member = i['membersCount']
                req = requests.get(f'{URl2}{name1}')
                r = req.json()
                owner = r['members'][0]['name']
                url = name1.split()
                url = "%20".join(url)
                banners = banners + url
                url = URl1 + url
                created = created[:10]
                break

        data_guilde={
            "name" : name1,
            "prefix" : prefix,
            "level" : level,
            "created" : created,
            "war" : war,
            "member" : member,
            "owner" : owner,
            "url" : url,
            "banners" : banners
        }
        return data_guilde
def data_wc(start,end):
        req = requests.get('https://api.wynncraft.com/public_api.php?action=onlinePlayers')
        data = req.json()
        wc = [*data]
        wc.remove("YT") ; wc.remove("request")
        wc = [int(i[2:]) for i in wc]
        wc1 = sorted(wc)
        wc = []
        count = []
        for i in range(start-1,end):
            x = "WC"+str(wc1[i])
            wc.append(x)  
            count.append(len(data[x]))

        return count,wc


    
if __name__ == "__main__":
        name ="wongsakron"
        guilde = "LBL"
        print(data_player(name))
        print(data_guilde (guilde))
        start = 2
        end = 20
        count,wc = data_wc(start=start,end=end)
        for i in range(len(wc)):
            print(f'{wc[i]} == {count[i]}')

