import random
import turtle as t


k_list = [(226, 226, 225), (236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233),
          (239, 208, 94), (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115),
          (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127),
          (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180),
          (15, 25, 24), (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4), (185, 195, 196),
          (253, 12, 5), (251, 10, 11), (58, 65, 69), (124, 130, 128), (121, 131, 133)]

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.teleport(-240, -250)
tim.penup()
tim.pensize(5)
for _ in range(10):
    for i in range(10):
        tim.dot(20, random.choice(k_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)
tim.hideturtle()
screen = t.Screen()
screen.exitonclick()

# import color gram
# k_list = []
# k = color gram.extract("DHS4591_771_0.jpg", 500)
# for i in k:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color = (r, g, b)
#     #print(color)
#     k_list.append(color)
# print(k_list)
