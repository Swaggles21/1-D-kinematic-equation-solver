#solving the first equation vf=vi+a*t

print("this program can solve for a variable with the  1-D kinematic equations:")
print("please put 6789 for the variable that you want to solve for")
print("please put 3456 for the variable that will not be used")
print("You cannot type a number for every input or it will not work (the algebra can only be done if there is a missing value)")

v_i = float(input("type a number to represent initial velocity value: "))
a = float(input("type a number to represent acceleration value: "))
t = float(input("type a number to represent time value: "))
v_f = float(input("type a number to represent final velocity value: "))
d = float(input("type a number to represent distance value:"))

#x = float
var1 = v_i
var2 = a
var3 = t
var4 = int
var4 = v_f
var5 = v_f - v_i
var6 = v_i**2+2*a*d
var7 = a*2*d-v_f**2
var8 = v_f**2
var9 = v_i**2
var10 = var8 - var9
var11 = .5*a
var12 = var11* t**2
var13 = var12+t*v_i
var14 = v_f + v_i
var15 = var14 / 2
var16 = v_i * t
var17 = -2+v_i
var18 = 2*d
var19 = var17 + var18
var20 = t
var21 = d/t-v_i
var22 = var21*2
var23 = 2 * d
var24 = var23/t
var25 = .5*a
var26 = d / var25
#sqrt = x**(.5)

#def start_over():
    #RESTART: /media/pi/F860-40EA/kinematic equations in python/solve all kinematic equations.py 
    #os.execl(sys.executable, sys.executable, *sys.argv)
    
#def equation1_solve_for_v_f():
    #if you solving for final velocity with vi, a, and t
    #print(t*a+v_i)

#first equation: vf = vi + a*t
if v_f == 6789 and d == 3456:
    print(a*t+v_i)

if v_i == 6789 and d == 3456:
    print(a*t-v_f)

if a == 6789 and d == 3456:
    print((v_f-v_i)/t)

if t == 6789 and d == 3456:
    print((v_f-v_i)/a)

#second equation: vf^2 = vi^2 + 2*a*d
if v_f == 6789 and t == 3456:
    print(var6**(.5))

if v_i == 6789 and t == 3456:
    print(-var7**(.5))

if a == 6789 and t == 3456:
    print((var10/d)/2)

if d == 6789 and t == 3456:
    print((var10/a/2))
#third equation: d = vi*t + .5*a* t^2
if d == 6789 and v_f == 3456:
    print(v_i*t+a*.5*t**2)

if v_i == 6789 and v_f == 3456:
    print(var13)

if a == 6789 and v_f == 3456:
    print(var22/t)

if t == 6789 and v_f == 3456:
    print(var26**(.5))

# fourth equation: d = (vi + vf)/2 * t
if d == 6789 and a == 3456:
    print(var15*t)

if v_i == 6789 and a == 3456:
    print(var24-v_f)

if v_f == 6789 and a == 3456:
    print(var24-v_i)

if t == 6789 and a == 3456:
    print(d/((v_i+v_f)/2))
    

print("All the left over floppy discs left over will take over the world in the year of 2060")

#onkey(start_over, "r")
#python does order of ops different it folows rules
    

