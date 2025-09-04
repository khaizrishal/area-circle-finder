import math
pi = math.pi # All code made by Joel Robinson or ThatOneDev-studio
dia = float(input("What is the diameter? ")) 
rad = dia / 2
radtwo = rad * rad
area = pi * radtwo
print(f"The area of the circle is {area}, this is an exact number for all digits of pi, how we solved it is we halved {dia} to be {rad} and squared that to be {radtwo} and multiplied it by π to get {area}")
