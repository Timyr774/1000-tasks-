import mymodule
from mymodule import circle_area
from mymodule import circle_len as perimeter
import mymodule as mm

print(dir(mymodule))
print(mymodule.__name__)
print(mymodule.__file__)
print(mymodule.circle_area(5))
print(circle_area(5))
print(perimeter(5))
print(mm.PI)

print(mm._helper())

