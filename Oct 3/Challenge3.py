#modification
#status = {
#"William" : "Online"
#"John" : "Offline"
#"Mary" : "Online"
#"Benjamin" : "Online"
#"Alex" : "Offline"
#"Christ" : "Online"
#}


def online_count(dict):
    count = 0
    for name,status in dict.items():
        if status == "Online":
            count += 1
    return count


statuses = {
    "William": "Online",
    "John":"Offline",
    "Mary": "Online",
    "Benjamin":"Online",
    "Alex": "Offline",
    "Christy":"Online"
}

print(online_count(statuses))