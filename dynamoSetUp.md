Name = made_up_users
Partition key = id 
Sort Key = username

read capacity = On-Demand 

make lambda - click create basic role 
print event and context
add lambda code - aks if everyone knows basic python

API 
HTTP 
leave cors for now

test api make call - get cors error
add cors to API 

Run again look at event and context objects - show cloudWatch

Add rest of lambda code 

Test again

error again go to cloud watch accessdeniederror 

go to IAM show roles and policies 
create dynamo policy 