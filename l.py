from manim import *
from math import *
class test(Scene):
	def construct(self):
		name = Tex("WhyNot").to_edge(UL, buff=0.7)
		cir = Circle(2, WHITE).shift(LEFT *3)
		sq = Square(2, color=BLUE, fill_color=DARK_BLUE, fill_opacity=0.75).to_edge(DR)
		self.play(Write(name))
		self.play(Create(cir))
		self.play(DrawBorderThenFill(sq), run_time=2)
		self.wait()
		self.play(name.animate.to_edge(UR), run_time=2)
		self.play(sq.animate.rotate(PI / 3), cir.animate.scale(0.5), run_time=2)
		self.play(Unwrite(name))
		self.wait()


class axes(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        self.add(ax, graph)
        self.wait()

class updaters(Scene):
	def construct(self):
			num = MathTex("ln(2)")
			box = always_redraw(lambda: SurroundingRectangle(num, color=BLUE, fill_color=GRAY, fill_opacity=0.25, buff=0.5))
			name = always_redraw(lambda: Tex("WhyNot").next_to(box, DOWN, buff=0.2))
			self.play(Create(VGroup(num, box, name)))
			self.play(num.animate.shift(RIGHT * 2), run_time=2)
			self.wait()

class Cirlewithregulator(Scene):
	def construct(self):
		k = ValueTracker(5)
		num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))
		box = Square(5, color=BLUE, fill_color=DARK_BLUE, fill_opacity=0.5).scale(0.5).to_corner(RIGHT, buff=1)
		cirl = always_redraw(lambda: Circle(k.get_value(), color=BLUE, fill_color=DARK_BLUE, fill_opacity=0.5).scale(0.4).to_corner(LEFT, buff=1))
		self.play(Create(num), run_time=2)
		self.play(DrawBorderThenFill(box), DrawBorderThenFill(cirl), run_time=2)
		self.play(k.animate.set_value(1), box.animate.rotate(PI / 3), run_time=5, rate_function=smooth)
		self.play(k.animate.set_value(5), box.animate.rotate(-PI / 3), run_time=5, rate_function=smooth)
		self.play(Uncreate(cirl), Uncreate(box), run_time=2)
		self.wait()

class graphing(Scene):
	def construct(self):
		plane = NumberPlane(x_range=[-1, 1, 0.25], x_length=7, y_range=[-10, 10, 10], y_length=8)
		prob = plane.plot(lambda x : tan(x) / sin(x), x_range = (-1, 1) , color = GREEN)
		self.play(DrawBorderThenFill(plane))
		self.play(Create(prob))

class circle(Scene):
	def construct(self):
		cir = Circle(2, BLACK, fill_color=DARK_BLUE, fill_opacity=0.75);
		cir2 = Circle(1.5, DARK_BLUE, fill_color=BLACK, fill_opacity=1);
		cir3 = Circle(0.05, BLACK, fill_color=BLACK, fill_opacity=1);
		s1 = Line(start=LEFT * 2, end=RIGHT * 2)
		s2 = Line(start=UP * 2, end=DOWN * 2)
		s3 = Line(start=UL * 1.04, end=DR * 1.04)
		s4 = Line(start=UR * 1.04, end=DL * 1.04)
		# s4 = Line(start=UR * 1.04, end=DL * 1.04)
		self.play(DrawBorderThenFill(cir), run_time=2)
		self.play(Create(s1), Create(s2))
		self.play(Create(s3), Create(s4))
		self.play(Create(cir3))
		self.play(DrawBorderThenFill(cir2), run_time=3)
		self.wait()