def is_isogram(string):
	not_counted_characters = ' -_'
	lis = [string.lower().count(i) if i not in not_counted_characters else 0 for i in string.lower()]
	if len(lis)==0:
		return True
	elif max(lis) > 1:
		return False
	else:
		return True

