
TEST_DATA = [{
    "title": "listing-1 : pokemon line up",
    "location": "tokyo, shibuya",
    "offered pay": "1000Yen",
    "date and time": "Oct 22, 2026, Friday, 3:00PM",
    "poster": "jay-r bangit",
    "description":"line up for pokemon release in yodabashi camera, shibuya branch"
},{
    "title": "listing-2 : one piece biccamera queue",
    "location": "tokyo, ueno",
    "offered pay": "1000Yen",
    "date and time": "Oct 22, 2026, Friday, 3:00PM",
    "poster": "yya antiporda",
    "description":"line up for one piece release in biccamera, ueno branch"
},{
    "title": "listing-3 : nike release queue",
    "location": "tokyo, harajuku",
    "offered pay": "7,000 Ten",
    "date and time": "Oct 22, 2026, Friday, 3:00PM",
    "poster": "jay-r bangit",
    "description":"line up for sneaker release in nike, harajuku branch"
}
]

TEST_TRANSACTIONS = [
{
    "title": "listing-3 : nike release queue",
    "location": "tokyo, harajuku",
    "offered pay": "7,000 Ten",
    "date and time": "Oct 22, 2026, Friday, 3:00PM",
    "transacting with": "test_user_123",
    "status": "Active",
    "got the item": "n/a"
},{
    "title": "listing-2 : one piece queue",
    "location": "tokyo, ueno",
    "offered pay": "5,000 Ten",
    "date and time": "Oct 22, 2026, Friday, 3:00PM",
    "transacting with": "test_user_abc",
    "status": "Completed",
    "got the item": "False"
}
]

MARKET_RECOMMENDATIONS = [
{
    "title": "one piece OP-15",
    "listed in": "ebay",
    "listing price": "10,000 Yen",
    "markup" : "40%",
    "listed date and time": "Oct 22, 2026, Friday, 3:00PM",
    "lister": "scalper_123",
},
{
    "title": "one piece OP-16",
    "listed in": "facebook market place",
    "listing price": "8,000 Yen",
    "markup" : "50%",
    "listed date and time": "Oct 22, 2026, Friday, 3:00PM",
    "lister": "scalper_numbah_wan",
},
{
    "title": "one piece luffy manga",
    "listed in": "facebook market place",
    "listing price": "22,000 Yen",
    "markup" : "35%",
    "listed date and time": "Oct 22, 2026, Friday, 3:00PM",
    "lister": "scalper_bois",
}
]

TEST_CHAT_DATA = [{
    "role": "Poster",
    "name": "You",
    "text": "Hey, San ka na?"
},{
    "role": "Worker",
    "name": "pila boy",
    "text": "OTW, be there in 10 mins"
}
]