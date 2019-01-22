#lists in dictionaries

channel_owners = {'Max' : ['onsite','gateway'], 
				'Shannon' : ['onsite'], 
				'Joshua' : ['paid search','seo',
				'associates','display','social']
				}
print(channel_owners)

for v,k in channel_owners.items():
	print(v + "'s channels are " + str(k))