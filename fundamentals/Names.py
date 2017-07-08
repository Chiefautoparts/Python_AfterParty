students = [
	{"first_name": "Michael", "last_name": "Jordan"},
	{"first_name": "John", "last_name": "Rosales"},
	{"first_name": "Mark", "last_name": "Guillen"},
	{"first_name": "KB", "last_name": "Tonel"}

]

users = {
	'Students': [
		{"first_name": "Michael", "last_name": "Jordan"},
		{"first_name": "John", "last_name": "Rosales"},
		{"first_name": "Mark", "last_name": "Guillen"},
		{"first_name": "KB", "last_name": "Tonel"}
	],
	'Instructors': [
		{'first_name': 'Michael', 'last_name': 'Choi'},
		{'first_name': 'Martin', 'last_name': 'Puryear'}
	]
}

def display_students(arr):
	for student in students:
		print student["first_name"], student["last_name"]




def display_all(users):
	for x in users:
		count = 0
		print x
		for people in users[x]:
			count +=1
			first_name = people['first_name'].upper()
			last_name = people['last_name'].upper()
			length = len(first_name) + len(last_name)
			print "{} - {} {} - {}".format(count, first_name, last_name, length)

display_students(students)
display_all(users)