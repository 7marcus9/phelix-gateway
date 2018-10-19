#!/usr/bin/env python3
import pretixApi
results = pretixApi.getAll()['results']

print("order\tsecret\tcheckin_allowed\tattention\tredeemed\tpaid\titemId\tvariationId\tattendeeName")
def boolV(val):
	if val:
		return "1"
	return "0"

for x in results:
#	print(x['order'] + "\t" + x['secret'] + "\t" + boolV(x['checkin_allowed']) + "\t" + boolV(x['attention']) + "\t" + boolV(x['redeemed']) + "\t" + boolV(x['paid']) + "\t" + int(x['item_id']) + "\t" + int(x['variation_id']))
	print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(x['order'], x['secret'], boolV(x['checkin_allowed']), boolV(x['attention']), boolV(x['redeemed']), boolV(x['paid']), x['item_id'], x['variation_id'], x['attendee_name']))
