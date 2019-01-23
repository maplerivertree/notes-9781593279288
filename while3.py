#while3 take_order_program -- filling a dictionary with user_inputs

orders = {}

still_guests_with_no_order = True



while still_guests_with_no_order:
	name = input("Input this Guest's name: ")
	order = input("What was ordered by this Guest: ")

	# THIS IS WRONG; should not have quotation for /name/orders['name'] = order

	orders[name]=order
	more = input("\nAny more orders? (yes/no)")
	if more == 'no':
		still_guests_with_no_order = False
     
for v, k in orders.items():
	print(str(v)+".."+str(k))