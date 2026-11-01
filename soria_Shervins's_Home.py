from vpython import *

scene.title = "My Dream House"
scene.width = 1200
scene.height = 700
scene.background = vector(0.5, 0.8, 1)
scene.center = vector(4, 2, 0)
scene.forward = vector(0.1, -0.45, -1)
scene.range = 22

cream = vector(0.95, 0.93, 0.85)
wood = vector(0.8, 0.6, 0.4)
darkwood = vector(0.4, 0.25, 0.1)
pipe_blue = vector(0.2, 0.4, 0.9)

ground = box(pos=vector(4, -0.25, 0), size=vector(70, 0.5, 50), color=vector(0.2, 0.6, 0.2))
driveway = box(pos=vector(14, 0.03, 14), size=vector(8, 0.1, 12), color=vector(0.5, 0.5, 0.5))
path = box(pos=vector(-1, 0.03, 13), size=vector(2, 0.1, 10), color=vector(0.7, 0.65, 0.55))

floor1 = box(pos=vector(0, 0.1, 0), size=vector(20, 0.2, 16), color=wood)
floor2 = box(pos=vector(14, 0.1, 0), size=vector(8, 0.2, 16), color=vector(0.45, 0.45, 0.45))

backwall = box(pos=vector(4, 3, -8), size=vector(28.4, 6, 0.4), color=cream)
leftwall = box(pos=vector(-10, 3, 0), size=vector(0.4, 6, 16.4), color=cream)
rightwall = box(pos=vector(18, 3, 0), size=vector(0.4, 6, 16.4), color=cream)

frontwall1 = box(pos=vector(-6, 3, 8), size=vector(8, 6, 0.4), color=cream, opacity=0.35)
frontwall2 = box(pos=vector(5, 3, 8), size=vector(10, 6, 0.4), color=cream, opacity=0.35)
frontwall3 = box(pos=vector(-1, 5.25, 8), size=vector(2, 1.5, 0.4), color=cream, opacity=0.35)
frontwall4 = box(pos=vector(14, 5.25, 8), size=vector(8, 1.5, 0.4), color=cream)
frontwall5 = box(pos=vector(10.25, 2.25, 8), size=vector(0.5, 4.5, 0.4), color=cream)
frontwall6 = box(pos=vector(17.75, 2.25, 8), size=vector(0.5, 4.5, 0.4), color=cream)

garagedoor = box(pos=vector(14, 2.25, 8.1), size=vector(7, 4.5, 0.15), color=vector(0.9, 0.9, 0.9))
gline1 = box(pos=vector(14, 1, 8.2), size=vector(7, 0.08, 0.05), color=vector(0.5, 0.5, 0.5))
gline2 = box(pos=vector(14, 2.25, 8.2), size=vector(7, 0.08, 0.05), color=vector(0.5, 0.5, 0.5))
gline3 = box(pos=vector(14, 3.5, 8.2), size=vector(7, 0.08, 0.05), color=vector(0.5, 0.5, 0.5))

garagewall1 = box(pos=vector(10, 3, -2), size=vector(0.3, 6, 12), color=cream)
garagewall2 = box(pos=vector(10, 3, 7), size=vector(0.3, 6, 2), color=cream)
garagewall3 = box(pos=vector(10, 5.25, 5), size=vector(0.3, 1.5, 2), color=cream)

wall_a = box(pos=vector(-4, 3, -7), size=vector(0.3, 6, 2), color=cream)
wall_b = box(pos=vector(-4, 3, -1), size=vector(0.3, 6, 6), color=cream)
wall_c = box(pos=vector(-4, 3, 6), size=vector(0.3, 6, 4), color=cream)
lintel_a = box(pos=vector(-4, 5.25, -5), size=vector(0.3, 1.5, 2), color=cream)
lintel_b = box(pos=vector(-4, 5.25, 3), size=vector(0.3, 1.5, 2), color=cream)
midwall = box(pos=vector(-7, 3, 0), size=vector(6, 6, 0.3), color=cream)

roof = box(pos=vector(4, 6.2, 0), size=vector(28.8, 0.4, 16.8), color=vector(0.35, 0.35, 0.4))

window1 = box(pos=vector(-7, 3.5, 8.25), size=vector(3, 2.2, 0.1), color=vector(0.6, 0.85, 1), opacity=0.5)
window2 = box(pos=vector(3, 3.5, 8.25), size=vector(5, 2.5, 0.1), color=vector(0.6, 0.85, 1), opacity=0.5)
window3 = box(pos=vector(8, 3.5, 8.25), size=vector(2.5, 2.5, 0.1), color=vector(0.6, 0.85, 1), opacity=0.5)
frame1 = box(pos=vector(-7, 3.5, 8.3), size=vector(3.2, 0.1, 0.05), color=darkwood)
frame2 = box(pos=vector(3, 3.5, 8.3), size=vector(5.2, 0.1, 0.05), color=darkwood)
frame3 = box(pos=vector(8, 3.5, 8.3), size=vector(2.7, 0.1, 0.05), color=darkwood)

for i in range(5):
    p1 = box(pos=vector(-7 + i * 4, 7.1, -4), size=vector(3.4, 0.12, 2.2), color=vector(0.1, 0.15, 0.5))
    p1.rotate(angle=radians(25), axis=vector(1, 0, 0))
    p2 = box(pos=vector(-7 + i * 4, 7.1, 2), size=vector(3.4, 0.12, 2.2), color=vector(0.1, 0.15, 0.5))
    p2.rotate(angle=radians(25), axis=vector(1, 0, 0))

gp1 = box(pos=vector(12, 7.1, 0), size=vector(3.4, 0.12, 2.2), color=vector(0.1, 0.15, 0.5))
gp1.rotate(angle=radians(25), axis=vector(1, 0, 0))
gp2 = box(pos=vector(16, 7.1, 0), size=vector(3.4, 0.12, 2.2), color=vector(0.1, 0.15, 0.5))
gp2.rotate(angle=radians(25), axis=vector(1, 0, 0))

solarlabel = label(pos=vector(4, 10, -4), text="Solar Panels", height=14, box=False)

battery = box(pos=vector(-12.5, 0.75, -6.5), size=vector(2, 1.5, 1), color=vector(0.9, 0.8, 0.1))
battery2 = box(pos=vector(-12.5, 1.6, -6.5), size=vector(1.2, 0.3, 0.8), color=vector(0.2, 0.2, 0.2))
batterylabel = label(pos=vector(-12.5, 3, -6.5), text="Battery Bank", height=12, box=False)
wire = cylinder(pos=vector(-12.5, 1.5, -6.5), axis=vector(0, 0, 0.1), radius=0.05, color=color.red)

wellring = cylinder(pos=vector(-14, 0, 5), axis=vector(0, 1.2, 0), radius=1.2, color=vector(0.5, 0.5, 0.5))
wellwater = cylinder(pos=vector(-14, 1.0, 5), axis=vector(0, 0.05, 0), radius=1.0, color=vector(0.1, 0.3, 0.9))
post1 = cylinder(pos=vector(-15.1, 1.2, 5), axis=vector(0, 1.9, 0), radius=0.08, color=darkwood)
post2 = cylinder(pos=vector(-12.9, 1.2, 5), axis=vector(0, 1.9, 0), radius=0.08, color=darkwood)
wellroof = box(pos=vector(-14, 3.1, 5), size=vector(2.6, 0.12, 1.6), color=vector(0.7, 0.15, 0.1))
welllabel = label(pos=vector(-14, 4.5, 5), text="Deep Well", height=12, box=False)

pipe1 = cylinder(pos=vector(-14, 0.3, 3.8), axis=vector(0, 0, -5.8), radius=0.1, color=pipe_blue)
pipe2 = cylinder(pos=vector(-14, 0.3, -2), axis=vector(0, 3.2, 0), radius=0.1, color=pipe_blue)
pipe3 = cylinder(pos=vector(-14, 3.5, -2), axis=vector(4, 0, 0), radius=0.1, color=pipe_blue)

tankleg1 = box(pos=vector(-15, 1.5, -3), size=vector(0.2, 3, 0.2), color=darkwood)
tankleg2 = box(pos=vector(-13, 1.5, -3), size=vector(0.2, 3, 0.2), color=darkwood)
tankleg3 = box(pos=vector(-15, 1.5, -1), size=vector(0.2, 3, 0.2), color=darkwood)
tankleg4 = box(pos=vector(-13, 1.5, -1), size=vector(0.2, 3, 0.2), color=darkwood)
tankplatform = box(pos=vector(-14, 3.05, -2), size=vector(2.6, 0.1, 2.6), color=darkwood)
tank = cylinder(pos=vector(-14, 3.1, -2), axis=vector(0, 2, 0), radius=1.2, color=vector(0.3, 0.7, 0.9), opacity=0.7)
tanklabel = label(pos=vector(-14, 6.5, -2), text="Water Tank", height=12, box=False)

bathfloor = box(pos=vector(-7, 0.22, -4), size=vector(5.8, 0.05, 7.8), color=vector(0.75, 0.9, 0.95))
tub = box(pos=vector(-8, 0.6, -7), size=vector(4, 1.2, 1.4), color=color.white)
tubwater = box(pos=vector(-8, 1.15, -7), size=vector(3.6, 0.1, 1), color=vector(0.4, 0.7, 1))
tubtap = cylinder(pos=vector(-10, 1.3, -7), axis=vector(0.5, 0, 0), radius=0.07, color=vector(0.7, 0.7, 0.7))

toiletbase = box(pos=vector(-5, 0.4, -7.2), size=vector(0.8, 0.8, 1.2), color=color.white)
toilettank = box(pos=vector(-5, 1.0, -7.8), size=vector(0.9, 1.2, 0.3), color=color.white)
toiletseat = cylinder(pos=vector(-5, 0.8, -7), axis=vector(0, 0.08, 0), radius=0.45, color=vector(0.9, 0.9, 0.9))

sinkcabinet = box(pos=vector(-9.5, 0.8, -3), size=vector(1, 1.6, 1.8), color=darkwood)
sinktop = box(pos=vector(-9.5, 1.65, -3), size=vector(1.1, 0.1, 1.9), color=color.white)
sinktap = cylinder(pos=vector(-9.8, 1.7, -3), axis=vector(0, 0.5, 0), radius=0.05, color=vector(0.7, 0.7, 0.7))
mirror = box(pos=vector(-9.75, 3, -3), size=vector(0.05, 1.8, 1.4), color=vector(0.7, 0.9, 1))

showerglass1 = box(pos=vector(-6.3, 2.5, -1.6), size=vector(0.05, 4.5, 2.6), color=vector(0.7, 0.9, 1), opacity=0.3)
showerglass2 = box(pos=vector(-5.15, 2.5, -2.9), size=vector(2.3, 4.5, 0.05), color=vector(0.7, 0.9, 1), opacity=0.3)
showertray = box(pos=vector(-5.15, 0.28, -1.6), size=vector(2.3, 0.1, 2.6), color=vector(0.85, 0.85, 0.85))
showerpipe = cylinder(pos=vector(-4.5, 0, -0.5), axis=vector(0, 4.5, 0), radius=0.08, color=vector(0.7, 0.7, 0.7))
showerarm = cylinder(pos=vector(-4.5, 4.5, -0.5), axis=vector(0, 0, -0.8), radius=0.06, color=vector(0.7, 0.7, 0.7))
showerhead = cylinder(pos=vector(-4.5, 4.45, -1.3), axis=vector(0, 0.1, 0), radius=0.3, color=vector(0.8, 0.8, 0.8))
bathlabel = label(pos=vector(-7, 7, -4), text="Bathroom", height=12, box=False)

carpet = box(pos=vector(-7, 0.22, 4), size=vector(5.8, 0.05, 7.8), color=vector(0.15, 0.15, 0.25))
desktop = box(pos=vector(-9, 1.5, 4), size=vector(1.8, 0.12, 6), color=darkwood)
deskleg1 = box(pos=vector(-8.3, 0.75, 1.2), size=vector(0.1, 1.5, 0.1), color=darkwood)
deskleg2 = box(pos=vector(-8.3, 0.75, 6.8), size=vector(0.1, 1.5, 0.1), color=darkwood)
deskleg3 = box(pos=vector(-9.9, 0.75, 1.2), size=vector(0.1, 1.5, 0.1), color=darkwood)
deskleg4 = box(pos=vector(-9.9, 0.75, 6.8), size=vector(0.1, 1.5, 0.1), color=darkwood)

monitor1 = box(pos=vector(-9.6, 2.3, 4), size=vector(0.1, 1.2, 2), color=color.black)
screen1 = box(pos=vector(-9.53, 2.3, 4), size=vector(0.05, 1.05, 1.85), color=vector(0.2, 0.8, 1))
stand1 = cylinder(pos=vector(-9.6, 1.56, 4), axis=vector(0, 0.15, 0), radius=0.15, color=color.black)

monitor2 = box(pos=vector(-9.6, 2.3, 2.1), size=vector(0.1, 1.2, 2), color=color.black)
screen2 = box(pos=vector(-9.53, 2.3, 2.1), size=vector(0.05, 1.05, 1.85), color=vector(0.9, 0.3, 0.8))
monitor2.rotate(angle=radians(-25), axis=vector(0, 1, 0))
screen2.rotate(angle=radians(-25), axis=vector(0, 1, 0), origin=monitor2.pos)
stand2 = cylinder(pos=vector(-9.6, 1.56, 2.1), axis=vector(0, 0.15, 0), radius=0.15, color=color.black)

monitor3 = box(pos=vector(-9.6, 2.3, 5.9), size=vector(0.1, 1.2, 2), color=color.black)
screen3 = box(pos=vector(-9.53, 2.3, 5.9), size=vector(0.05, 1.05, 1.85), color=vector(0.3, 0.9, 0.4))
monitor3.rotate(angle=radians(25), axis=vector(0, 1, 0))
screen3.rotate(angle=radians(25), axis=vector(0, 1, 0), origin=monitor3.pos)
stand3 = cylinder(pos=vector(-9.6, 1.56, 5.9), axis=vector(0, 0.15, 0), radius=0.15, color=color.black)

tower = box(pos=vector(-9.4, 2.2, 7), size=vector(0.8, 1.3, 0.5), color=vector(0.1, 0.1, 0.1))
towerglass = box(pos=vector(-9.0, 2.2, 7), size=vector(0.02, 1.1, 0.4), color=vector(0.6, 0.2, 0.9), opacity=0.6)
towerlight = sphere(pos=vector(-9.0, 2.7, 7), radius=0.08, color=color.green, emissive=True)

keyboard = box(pos=vector(-8.8, 1.6, 4), size=vector(0.5, 0.05, 1.6), color=vector(0.2, 0.2, 0.2))
mouse = box(pos=vector(-8.8, 1.6, 5.2), size=vector(0.25, 0.06, 0.15), color=vector(0.1, 0.1, 0.1))
mousepad = box(pos=vector(-8.8, 1.57, 5.2), size=vector(0.7, 0.02, 0.8), color=vector(0.6, 0.1, 0.1))

chairbase = cylinder(pos=vector(-7.8, 0.2, 4), axis=vector(0, 0.1, 0), radius=0.5, color=color.black)
chairpole = cylinder(pos=vector(-7.8, 0.3, 4), axis=vector(0, 0.7, 0), radius=0.08, color=color.black)
chairseat = box(pos=vector(-7.8, 1.0, 4), size=vector(1.2, 0.15, 1.2), color=color.red)
chairback = box(pos=vector(-7.2, 1.8, 4), size=vector(0.15, 1.6, 1.2), color=color.red)

shelf = box(pos=vector(-4.5, 2.5, 6.5), size=vector(0.4, 5, 2.5), color=darkwood)
shelfbook1 = box(pos=vector(-4.75, 3.5, 6.5), size=vector(0.1, 0.8, 2), color=color.blue)
shelfbook2 = box(pos=vector(-4.75, 2.5, 6.5), size=vector(0.1, 0.8, 2), color=color.orange)
shelfbook3 = box(pos=vector(-4.75, 1.5, 6.5), size=vector(0.1, 0.8, 2), color=color.green)

pclabel = label(pos=vector(-7, 7, 4), text="PC Room", height=12, box=False)

rug = box(pos=vector(3, 0.22, 4.5), size=vector(7, 0.05, 5), color=vector(0.6, 0.2, 0.2))
sofabase = box(pos=vector(3, 0.6, 6.8), size=vector(5, 1.2, 1.8), color=vector(0.2, 0.3, 0.6))
sofaback = box(pos=vector(3, 1.6, 7.5), size=vector(5, 1.4, 0.5), color=vector(0.2, 0.3, 0.6))
sofaarm1 = box(pos=vector(0.7, 1, 6.8), size=vector(0.5, 1.6, 1.8), color=vector(0.15, 0.25, 0.5))
sofaarm2 = box(pos=vector(5.3, 1, 6.8), size=vector(0.5, 1.6, 1.8), color=vector(0.15, 0.25, 0.5))
pillow1 = box(pos=vector(1.8, 1.4, 6.6), size=vector(0.7, 0.7, 0.2), color=color.yellow)
pillow2 = box(pos=vector(4.2, 1.4, 6.6), size=vector(0.7, 0.7, 0.2), color=color.orange)

coffeetable = box(pos=vector(3, 0.6, 4.5), size=vector(2.5, 0.15, 1.2), color=darkwood)
coffeeleg1 = box(pos=vector(2, 0.3, 4.1), size=vector(0.1, 0.6, 0.1), color=darkwood)
coffeeleg2 = box(pos=vector(4, 0.3, 4.1), size=vector(0.1, 0.6, 0.1), color=darkwood)
coffeeleg3 = box(pos=vector(2, 0.3, 4.9), size=vector(0.1, 0.6, 0.1), color=darkwood)
coffeeleg4 = box(pos=vector(4, 0.3, 4.9), size=vector(0.1, 0.6, 0.1), color=darkwood)
cup = cylinder(pos=vector(3, 0.68, 4.5), axis=vector(0, 0.3, 0), radius=0.15, color=color.white)

tvstand = box(pos=vector(3, 0.5, 1.5), size=vector(4, 1, 1), color=darkwood)
tv = box(pos=vector(3, 2.3, 1.5), size=vector(3.5, 2, 0.2), color=color.black)
tvscreen = box(pos=vector(3, 2.3, 1.62), size=vector(3.3, 1.8, 0.05), color=vector(0.1, 0.2, 0.4))
tvstandpole = box(pos=vector(3, 1.2, 1.5), size=vector(0.3, 0.4, 0.2), color=color.black)

plantpot = cylinder(pos=vector(9, 0.2, 6.5), axis=vector(0, 0.8, 0), radius=0.5, color=vector(0.6, 0.3, 0.1))
plantleaves = sphere(pos=vector(9, 1.8, 6.5), radius=0.9, color=vector(0.1, 0.5, 0.1))
plantstem = cylinder(pos=vector(9, 1, 6.5), axis=vector(0, 0.8, 0), radius=0.06, color=vector(0.3, 0.2, 0.1))

lamppole = cylinder(pos=vector(0, 0.2, 5.5), axis=vector(0, 3, 0), radius=0.07, color=color.black)
lampshade = sphere(pos=vector(0, 3.4, 5.5), radius=0.45, color=color.yellow, emissive=True)

livinglabel = label(pos=vector(3, 7, 4), text="Living Room", height=12, box=False)

counter = box(pos=vector(4, 0.9, -7.3), size=vector(8, 1.8, 1.2), color=darkwood)
countertop = box(pos=vector(4, 1.85, -7.3), size=vector(8.1, 0.1, 1.3), color=vector(0.15, 0.15, 0.15))
cabinets = box(pos=vector(3.5, 4.5, -7.6), size=vector(7, 1.4, 0.8), color=wood)
cabinetline1 = box(pos=vector(1.2, 4.5, -7.18), size=vector(0.05, 1.4, 0.02), color=darkwood)
cabinetline2 = box(pos=vector(3.5, 4.5, -7.18), size=vector(0.05, 1.4, 0.02), color=darkwood)
cabinetline3 = box(pos=vector(5.8, 4.5, -7.18), size=vector(0.05, 1.4, 0.02), color=darkwood)
fridge = box(pos=vector(9, 2.2, -7.3), size=vector(1.4, 4.4, 1.3), color=vector(0.8, 0.8, 0.85))
fridgeline = box(pos=vector(9, 3, -6.64), size=vector(1.4, 0.05, 0.02), color=color.black)
fridgehandle = box(pos=vector(8.4, 3.5, -6.62), size=vector(0.06, 0.8, 0.06), color=color.black)

stove = box(pos=vector(5.5, 1.95, -7.3), size=vector(1.6, 0.05, 1), color=color.black)
burner1 = cylinder(pos=vector(5.1, 1.98, -7.5), axis=vector(0, 0.03, 0), radius=0.25, color=color.red)
burner2 = cylinder(pos=vector(5.9, 1.98, -7.5), axis=vector(0, 0.03, 0), radius=0.25, color=color.red)
burner3 = cylinder(pos=vector(5.1, 1.98, -7.1), axis=vector(0, 0.03, 0), radius=0.2, color=color.red)
burner4 = cylinder(pos=vector(5.9, 1.98, -7.1), axis=vector(0, 0.03, 0), radius=0.2, color=color.red)
pot = cylinder(pos=vector(5.1, 2.0, -7.5), axis=vector(0, 0.5, 0), radius=0.3, color=vector(0.7, 0.7, 0.7))

kitchensink = box(pos=vector(1.5, 1.95, -7.3), size=vector(1.5, 0.05, 0.9), color=vector(0.7, 0.7, 0.75))
kitchentap = cylinder(pos=vector(1.5, 1.95, -7.7), axis=vector(0, 0.6, 0), radius=0.05, color=vector(0.7, 0.7, 0.7))

island = box(pos=vector(5, 0.9, -3.5), size=vector(5, 1.8, 1.4), color=wood)
islandtop = box(pos=vector(5, 1.85, -3.5), size=vector(5.2, 0.1, 1.6), color=color.white)

stool1 = cylinder(pos=vector(3.5, 0, -2), axis=vector(0, 1.3, 0), radius=0.08, color=color.black)
stoolseat1 = cylinder(pos=vector(3.5, 1.3, -2), axis=vector(0, 0.15, 0), radius=0.35, color=color.red)
stool2 = cylinder(pos=vector(5, 0, -2), axis=vector(0, 1.3, 0), radius=0.08, color=color.black)
stoolseat2 = cylinder(pos=vector(5, 1.3, -2), axis=vector(0, 0.15, 0), radius=0.35, color=color.red)
stool3 = cylinder(pos=vector(6.5, 0, -2), axis=vector(0, 1.3, 0), radius=0.08, color=color.black)
stoolseat3 = cylinder(pos=vector(6.5, 1.3, -2), axis=vector(0, 0.15, 0), radius=0.35, color=color.red)

fruitbowl = cylinder(pos=vector(5, 1.9, -3.5), axis=vector(0, 0.25, 0), radius=0.4, color=color.white)
apple1 = sphere(pos=vector(4.9, 2.25, -3.5), radius=0.15, color=color.red)
apple2 = sphere(pos=vector(5.15, 2.25, -3.4), radius=0.15, color=color.green)

kitchenlabel = label(pos=vector(5, 7, -5), text="Kitchen", height=12, box=False)

car = box(pos=vector(14, 0.9, 0), size=vector(2, 0.8, 4.2), color=vector(0.8, 0.1, 0.1))
carcabin = box(pos=vector(14, 1.6, -0.3), size=vector(1.8, 0.7, 2.2), color=vector(0.7, 0.05, 0.05))
carwindow = box(pos=vector(14, 1.65, -0.3), size=vector(1.85, 0.5, 2.0), color=vector(0.6, 0.85, 1), opacity=0.6)
wheel1 = cylinder(pos=vector(12.85, 0.45, 1.4), axis=vector(0.3, 0, 0), radius=0.45, color=color.black)
wheel2 = cylinder(pos=vector(14.85, 0.45, 1.4), axis=vector(0.3, 0, 0), radius=0.45, color=color.black)
wheel3 = cylinder(pos=vector(12.85, 0.45, -1.4), axis=vector(0.3, 0, 0), radius=0.45, color=color.black)
wheel4 = cylinder(pos=vector(14.85, 0.45, -1.4), axis=vector(0.3, 0, 0), radius=0.45, color=color.black)
headlight1 = sphere(pos=vector(13.4, 0.95, 2.1), radius=0.18, color=color.yellow, emissive=True)
headlight2 = sphere(pos=vector(14.6, 0.95, 2.1), radius=0.18, color=color.yellow, emissive=True)

charger = box(pos=vector(17.7, 2, 3), size=vector(0.2, 1, 0.5), color=color.white)
chargerlight = sphere(pos=vector(17.57, 2.3, 3), radius=0.08, color=color.green, emissive=True)
cable = cylinder(pos=vector(17.6, 1.7, 3), axis=vector(-2.6, -0.8, -1.5), radius=0.04, color=color.black)

workbench = box(pos=vector(17.3, 1, -5), size=vector(1.2, 2, 3), color=darkwood)
toolbox = box(pos=vector(17.3, 2.2, -5.5), size=vector(0.8, 0.4, 1), color=color.red)
garagelabel = label(pos=vector(14, 7, -4), text="Garage", height=12, box=False)

treetrunk1 = cylinder(pos=vector(-22, 0, 14), axis=vector(0, 3, 0), radius=0.3, color=darkwood)
treeleaves1 = sphere(pos=vector(-22, 4.2, 14), radius=1.9, color=vector(0.1, 0.5, 0.15))
treetrunk2 = cylinder(pos=vector(-25, 0, -5), axis=vector(0, 3, 0), radius=0.3, color=darkwood)
treeleaves2 = sphere(pos=vector(-25, 4.2, -5), radius=1.9, color=vector(0.1, 0.5, 0.15))
treetrunk3 = cylinder(pos=vector(26, 0, -14), axis=vector(0, 3, 0), radius=0.3, color=darkwood)
treeleaves3 = sphere(pos=vector(26, 4.2, -14), radius=1.9, color=vector(0.1, 0.5, 0.15))
treetrunk4 = cylinder(pos=vector(28, 0, 14), axis=vector(0, 3, 0), radius=0.3, color=darkwood)
treeleaves4 = sphere(pos=vector(28, 4.2, 14), radius=1.9, color=vector(0.1, 0.5, 0.15))
treetrunk5 = cylinder(pos=vector(-8, 0, -18), axis=vector(0, 3, 0), radius=0.3, color=darkwood)
treeleaves5 = sphere(pos=vector(-8, 4.2, -18), radius=1.9, color=vector(0.1, 0.5, 0.15))

gardenbed = box(pos=vector(6, 0.15, -14), size=vector(8, 0.3, 2.5), color=vector(0.35, 0.2, 0.1))
for i in range(6):
    veggie = sphere(pos=vector(2.5 + i * 1.4, 0.55, -14), radius=0.3, color=vector(0.2, 0.7, 0.2))
gardenlabel = label(pos=vector(6, 2, -14), text="Vegetable Garden", height=12, box=False)

sun = sphere(pos=vector(35, 28, -20), radius=3, color=color.yellow, emissive=True)
cloud1 = sphere(pos=vector(-10, 20, -15), radius=2.5, color=color.white)
cloud2 = sphere(pos=vector(-7.5, 20, -15), radius=2, color=color.white)
cloud3 = sphere(pos=vector(-12.5, 20, -15), radius=2, color=color.white)
cloud4 = sphere(pos=vector(15, 23, -18), radius=2.5, color=color.white)
cloud5 = sphere(pos=vector(17.5, 23, -18), radius=2, color=color.white)

light1 = local_light(pos=vector(3, 5.5, 3), color=color.white * 0.5)
light2 = local_light(pos=vector(5, 5.5, -5), color=color.white * 0.5)
light3 = local_light(pos=vector(-9, 3, 4), color=color.cyan * 0.3)

print("welcome to my dream house")
print("right click and drag to turn, scroll to zoom")
while True:
    rate(30)