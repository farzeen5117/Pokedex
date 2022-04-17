def reverse_string(str):
	string = ""
	for i in str:
		string = i + string
		print(string)
	return string

user_string = "farzeen"
print(reverse_string(user_string))