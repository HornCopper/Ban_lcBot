import httpx
import json

bots = ["40001", "40002", "40003", "40004", "40005"]

groups = {}

group_members = {}

prefix = "http://192.168.3.18:{port}/{action}"

# {"group_members": { "40001": { "111111111": [ {"nickname": "aaa", "uin": bbb} ] } } }

for bot_port in bots:
    data = httpx.get(prefix.format(port=bot_port, action="get_group_list")).json()
    groups[bot_port] = []
    for each_group in data["data"]:
        groups[bot_port].append(each_group["group_id"])
    
for bot_port in bots:
    group_members[bot_port] = {}
    for group_id in groups[bot_port]:
        group_members[bot_port][str(group_id)] = []
        data = httpx.get(prefix.format(port=bot_port, action=f"get_group_member_list?group_id={group_id}")).json()
        try:
            for i in data["data"]:
                ...
        except:
            print(bot_port)
            print(group_id)
            print(data)
        for user in data["data"]:
            group_members[bot_port][str(group_id)].append({"user_id": user["user_id"], "nickname": user["nickname"]})

cache = open("./output.json", encoding="utf-8", mode="w")
cache.write(json.dumps(group_members, ensure_ascii=False))
cache.close()