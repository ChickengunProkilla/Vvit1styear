def calculate_rectangle(width, height):
    return(width*height)
def calculate_perimeter(width, height):
    return((width+height)*2)
def describe_rectangle(width, height, unit='см'):
    return((width,unit),(height,unit))
print(describe_rectangle(12,15))
print(describe_rectangle(17,32,'м'))