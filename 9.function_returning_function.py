def cylinder_vol(r):
    pi = 3.141
    def get_vol(h):
        return pi * r**2 * h
    return get_vol

radius = 10
height = 10
new_height = 20

#Calling the main function twice by assigning an object to function
find_volume = cylinder_vol(radius)

print find_volume(height)
print find_volume(new_height)
