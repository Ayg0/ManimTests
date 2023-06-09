from manim import *

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
		self.play(k.animate.set_value(1), box.animate.rotate(PI / 3), run_time=5)
		self.play(k.animate.set_value(5), box.animate.rotate(-PI / 3), run_time=5)
		self.play(Uncreate(cirl), Uncreate(box), run_time=2)
		self.wait()
		# self.play(num.animate.shift(RIGHT * 4), run_time=2)
