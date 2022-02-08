from manim import *
class r(Scene):
    def construct(self):
        circle = Circle(radius = 2.1415)
        circle.set_fill(GREEN, opacity=0.4)
        square = Square(side_length=2)
        square.set_fill(ORANGE, opacity=0.8)
        triangle = Triangle()
        triangle.set_fill(PINK, opacity=1)
        square.next_to(circle, RIGHT, buff=0.5)
        triangle.next_to(circle, LEFT, buff=0.5)
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(3)