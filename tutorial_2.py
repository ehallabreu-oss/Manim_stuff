from manim import *

class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range = [0, 5, 1], y_range = [0,3,1],
        x_length = 5, y_length = 3,
        axis_config = {"include_tip": True, "numbers_to_exclude":[0]}
        ).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = 'x', y_label='f(x)')

        graph = axes.plot(lambda x: x**0.5, color=YELLOW, x_range=[0,5])
        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time=3)

class Graphing(Scene):
    def construct(self):

        my_plane = NumberPlane(x_range = [-6,6], x_length = 5,
        y_range=[-10,10], y_length=5)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)

        my_function = my_plane.plot(lambda x: 0.1*(x-5)*x*(x+5),
        x_range=[-6,6], color=GREEN_B)

        area = my_plane.get_area(graph = my_function,
        x_range = [-5,5], color = [BLUE, YELLOW])

        label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(
            my_plane, UP, buff=0.2)
        
        horiz_line = Line(
            start = my_plane.i2gp(0, my_function),
            end = my_plane.i2gp(-2, my_function),
            stroke_color=YELLOW, stroke_width=5)
        
        self.play(DrawBorderThenFill(my_plane))
        self.play(Create(my_function))
        self.play(Write(label))
        self.play(FadeIn(area))
        self.play(Create(horiz_line))
        
        


