# var declaration
var = 0
print (var)

# Function gets its own local copy of variable
# To preserve change of a variable in the function use global keyword
def function():
	var = "b"
	print(var)

function()
print (var)

# delete variable
del var