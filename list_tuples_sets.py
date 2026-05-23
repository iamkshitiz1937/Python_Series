courses = ['Physics', 'Maths', 'Computer', 'English']
courses_2 = ['Programming', 'Chemistry']

num = [2,4,5,3,6,1]

# courses.append('Programming')
# courses.insert(0, 'Chemistry')

courses.extend(courses_2)

courses.remove('Maths')
# pop removes the last index and returns the value
popped = courses.pop()

# courses.reverse()
# courses.sort()

sorted_courses = sorted(courses)

num.sort(reverse=True)
print(num)

print(popped)
print(courses)
print(courses.index('Physics'))
print('Maths' in courses)
print(sorted_courses)
# print(courses[:2])
# print(courses[2:])

print(min(num))
print(max(num))
print(sum(num))

# enumerate function returns two values the index and the value
for index, course in enumerate(courses):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)

# tuples
tuple_1 = ('Physics', 'Maths', 'Computer', 'English')
tuple_2 = tuple_1

# tuples cannot be changes as it is immutable compared to lists which is mutable
# tuple_1[0] = 'Chemistry'
print(tuple_1)


# sets 
# sets removes any duplicate value by default
# cs_courses = {'Physics', 'Maths', 'Computer', 'English', 'Maths'}
cs_courses = {'Physics', 'Maths', 'Computer', 'English'}
cyber_courses = {'Physics', 'Maths', 'chemistry', 'English'}
print( 'Maths' in cs_courses)
print(cs_courses.intersection(cyber_courses))
print(cs_courses.difference(cyber_courses))
print(cs_courses.union(cyber_courses))

# creating empty list
empty_list = []
empty_list = list()

# creating empty tuple
empty_tuple = ()
empty_tuple = tuple()

# creating empty set
empty_set = {} # this does not creates an empty set but a directionary
empty_set = set()
