def viewJinjaFilter(x):
	if x is None:
		return ''
	if isinstance(x, bool):
		return 'yes' if x else 'no'
	return x