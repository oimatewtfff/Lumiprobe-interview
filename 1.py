def counter(string):
	lower_string = string.lower()
	results = {}

	for char in lower_string:
		results[char] = lower_string.count(char.lower())

	max_value = max(results.values())

	return [k for k, v in results.items() if v == max_value][0], max_value

print(counter('aaaAAAbc'))
