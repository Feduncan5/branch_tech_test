import requests
import json
import pandas as pd


###Import JSON
randomUsers = requests.get('https://randomuser.me/api/?results=500').json()

###Seperate JSON
gender={"gender":[],"email":[]}
name={"name":[]}
location={"location":[]}
login={"login":[]}
dob={"dob":[]}
registered={"registered":[]}
phone={"phone":[],"cell":[],"email":[]}
id={"id":[]}
picture={"picture":[]}
nat={"nat":[],"email":[]}

for i in randomUsers['results']:
    gender["gender"].append(i['gender']),
    gender["email"].append(i['email']),
    name["name"].append(i['name']),
    location["location"].append(i['location']),
    login["login"].append(i['login']),
    dob["dob"].append(i['dob']),
    registered["registered"].append(i['registered']),
    phone["phone"].append(i['phone']),
    phone["cell"].append(i['cell']),
    phone["email"].append(i['email']),
    id["id"].append(i['id']),
    picture["picture"].append(i['picture']),
    nat["nat"].append(i['nat']),
    nat["email"].append(i['email'])

##Gender Dataframe
gender_df = pd.DataFrame(data=gender)
#print(gender_df.head(10))

###Name Dataframe
name2={"title":[],"first":[],"last":[], "email":[]}
for i in name['name']:
    name2["title"].append(i['title']),
    name2["first"].append(i['first']),
    name2["last"].append(i['last']),

for i in randomUsers['results']:
    name2["email"].append(i['email'])

name_df=pd.DataFrame(data=name2)
#print(name_df.head(10))

#print(location.values())
###Location Dataframe
location2={"street":[],"coordinates":[],"timezone":[]}
for i in location['location']:
    location2["street"].append(i['street']),
    location2["coordinates"].append(i['coordinates']),
    location2["timezone"].append(i['timezone']),

#print(location2.keys())
location3={"number":[],"name":[],"city":[],"state":[],"country":[],"postcode":[],"latitude":[],"longitude":[],"offset":[],"description":[], "email":[]}
#print(location2["street"][0])
for i in location2['street']:
    location3["number"].append(i['number'])
    location3["name"].append(i['name'])

for i in location2['coordinates']:
    location3["latitude"].append(i['latitude'])
    location3["longitude"].append(i['longitude'])

for i in location2['timezone']:
    location3["offset"].append(i['offset'])
    location3["description"].append(i['description'])

for i in location['location']:
    location3["city"].append(i['city']),
    location3["state"].append(i['state']),
    location3["country"].append(i['country']),
    location3["postcode"].append(i['postcode']),

for i in randomUsers['results']:
    location3["email"].append(i['email'])

location_df=pd.DataFrame(data=location3)
##Renaming Columns
location_df = location_df.rename(columns={"name":"street_name"})
location_df = location_df.rename(columns={"number":"street_number"})
location_df = location_df.rename(columns={"latitude":"coordinates_latitude"})
location_df = location_df.rename(columns={"longitude":"coordinates_longitude"})
location_df = location_df.rename(columns={"offset":"timezone_offset"})
location_df = location_df.rename(columns={"description":"timezone_description"})
#print(location_df.head(10))

###Login Dataframe
login2={"uuid":[],"username":[],"password":[],"salt":[],"md5":[],"sha1":[],"sha256":[], "email":[]}
for i in login['login']:
    login2["uuid"].append(i['uuid']),
    login2["username"].append(i['username']),
    login2["password"].append(i['password']),
    login2["salt"].append(i['salt']),
    login2["md5"].append(i['md5']),
    login2["sha1"].append(i['sha1']),
    login2["sha256"].append(i['sha256']),

for i in randomUsers['results']:
    login2["email"].append(i['email'])

login_df=pd.DataFrame(data=login2)
#print(login_df.head(10))

###DOB Dataframe
dob2={"date":[],"age":[], "email":[]}
for i in dob['dob']:
    dob2["date"].append(i['date']),
    dob2["age"].append(i['age']),

for i in randomUsers['results']:
    dob2["email"].append(i['email'])

dob_df=pd.DataFrame(data=dob2)
##Renaming Columns
dob_df = dob_df.rename(columns={"date":"date_of_birth"})
#print(dob_df.head(10))

###Registered Dataframe
registered2={"date":[],"age":[], "email":[]}
for i in registered['registered']:
    registered2["date"].append(i['date']),
    registered2["age"].append(i['age']),

for i in randomUsers['results']:
    registered2["email"].append(i['email'])

registered_df=pd.DataFrame(data=registered2)
##Renaming Columns
registered_df = registered_df.rename(columns={"date":"registered_date"})
registered_df = registered_df.rename(columns={"age":"registered_age"})
#print(registered_df.head(10))

###Phone Dataframe
phone_df = pd.DataFrame(data=phone)
#print(phone_df.head(10))

###ID Dataframe
id2={"name":[],"value":[], "email":[]}
for i in id['id']:
    id2["name"].append(i['name']),
    id2["value"].append(i['value']),

for i in randomUsers['results']:
    id2["email"].append(i['email'])

id_df=pd.DataFrame(data=id2)
##Renaming Columns
id_df = id_df.rename(columns={"name":"id_type"})
#print(id_df.head(10))

###Picture Dataframe
picture2={"large":[],"medium":[],"thumbnail":[], "email":[]}
for i in picture['picture']:
    picture2["large"].append(i['large']),
    picture2["medium"].append(i['medium']),
    picture2["thumbnail"].append(i['thumbnail']),

for i in randomUsers['results']:
    picture2["email"].append(i['email'])

picture_df=pd.DataFrame(data=picture2)
#print(picture_df.head(10))

###Nat Dataframe
nat_df = pd.DataFrame(data=nat)
#print(nat_df.head(10))

###Export Dataframes as CSV's

gender_csv=gender_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/gender.csv", index=False)
name_csv=name_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/name.csv", index=False)
location_csv=location_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/location.csv", index=False)
login_csv=login_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/login.csv", index=False)
dob_csv=dob_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/dob.csv", index=False)
registered_csv=registered_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/registered.csv", index=False)
phone_csv=phone_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/phone.csv", index=False)
id_csv=id_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/id.csv", index=False)
picture_csv=picture_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/picture.csv", index=False)
nat_csv=nat_df.to_csv(path_or_buf="C:/Users/fedun/OneDrive/Documents/branch_tech_test/nat.csv", index=False)


















