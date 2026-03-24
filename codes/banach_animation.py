from manim import *
import numpy as np
import random

config.background_color = WHITE
dark_red = "#9A0000"
light_red = "#9A000045"
dark_pink = "#9C1568"
light_pink = "#9C15686F"
dark_blue = "#336699"
medium_blue = "#7597BE"
light_blue = "#33669962"
dark_green = "#5E913B"
light_green = "#5D913B66"
dark_orange = "#E66914"
light_orange = "#E668149B"
dark_purple = "#5802A6"
light_purple = "#5702A68C"
dark_terquise = "#02A6A1"
dark_not_green = "#46A602"
axes_background_color = "#D3D3D3"
topics_backGround_color = "#0D113EFF"

class TitleScene(Scene):

    def construct(self):

        self.scene1()

    def scene1(self):
        colors = [dark_pink, dark_blue, dark_red, dark_green, dark_orange]

        plane = NumberPlane(
            y_range=[-6, 10, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=10,
            x_length=15,
        ).move_to(DOWN)

        axes = Axes(
            y_range=[-6, 10, 1],
            x_range=[-10, 10, 1],
            x_length=15,
            y_length=10,
            axis_config={
                "color": BLUE,
                "include_ticks": False,
                "tip_length": 0.25,
                "tip_shape": StealthTip,
            }
        ).move_to(DOWN)

        nums = []
        dot_locs = [
            axes.c2p(-6,-1),
            axes.c2p(-5,4),
            axes.c2p(3,1),
            axes.c2p(1,6),
            axes.c2p(0,0),
        ]
        for i in range(5):
            num = MathTex(str(i + 1), color=colors[i]).scale(2)
            num.move_to(dot_locs[i])
            nums.append(num)

        nums_group = VGroup(*nums)

        # random.seed(42)
        arrows = []
        vec = [
            axes.c2p(-3,3),
            axes.c2p(-8,7),
            axes.c2p(7,-2),
            axes.c2p(8,8),
            axes.c2p(-2,6),
        ]
        for i in range(5):
            arrow = Arrow(
                start=nums[i].get_center(),
                end=vec[i],
                color=colors[i],
                stroke_width=5,
                tip_length=0.25,
                tip_shape=StealthTip
            )
            arrows.append(arrow)

        arrows_group = VGroup(*arrows)

        functions = [
            lambda x: 4 * np.sin(x),
            lambda x: 2.5 * np.cos(x),
            lambda x: np.exp(0.2 * x),
            lambda x: np.log(abs(x)+1),
            lambda x: np.sin(x) + np.cos(2*x)
        ]

        graphs = []
        for i in range(5):
            g = axes.plot(functions[i], color=colors[i])
            g.scale(1.4).shift(2 * UP)
            graphs.append(g)

        graphs_group = VGroup(*graphs)


        self.play(Create(plane))

        self.play(Write(nums_group), run_time=1.5)

        self.play(
            FadeTransform(nums_group, arrows_group),
            run_time=1.5
        )

        self.play(
            FadeTransform(arrows_group, graphs_group),
            run_time=1.5
        )

        self.wait(1)

        image = ImageMobject("images/stefan_banach.png").scale(0.3)
        self.play(
            FadeOut(graphs_group),
        )
        self.add(image)

        self.wait(1)


        name1_text = Text("Stefan",color=BLACK,font="mistral",font_size=80).next_to(image,UP,buff=0.3).shift(1*LEFT)
        name2_text = Text("Banach",color=BLACK,font="mistral",font_size=80).next_to(name1_text,RIGHT,buff=0.1)
        name_text = VGroup(name1_text,name2_text)
        date_text = Text("1892 – 1945",color=BLACK,font="mistral",font_size=75).next_to(image,DOWN,buff=0.3)
        krakov_text =Text("Kraków",color=dark_blue,font="mistral",font_size=60).to_corner(UL)
        selfTaught_text =Text("Self-taught",color=dark_orange,font="mistral",font_size=70).next_to(image,RIGHT,buff=0.3)
        subject_text =Text("Engineering",color=dark_pink,font="mistral",font_size=60).next_to(selfTaught_text,DOWN,buff=0.6)
        krakov_park_text =Text("Kraków's Planty park",color=dark_green,font="mistral",font_size=45).next_to(image,LEFT,buff=0.2).shift(2*UP)
        integral_text =Text("Lebesgue integral",color=dark_terquise,font="mistral",font_size=60).next_to(image,RIGHT,buff=0.2)
        hugo_text =Text("Hugo Steinhaus",color=BLACK,font="mistral",font_size=70).next_to(integral_text,DOWN,buff=0.3)
        otto_text =Text("Otto Nikodym",color=BLACK,font="mistral",font_size=60).next_to(krakov_park_text,DOWN,buff=0.3)
        cafe_text =Text("Scottish Café",color=dark_purple,font="mistral",font_size=55).next_to(image,RIGHT,buff=0.3)

        self.play(
            Write(name_text),
            Write(date_text),
        )
        self.play(
            Write(krakov_text),
        )
        self.wait(0.5)
        name2_text.set_color(dark_red)
        self.wait(0.5)
        name2_text.set_color(BLACK)
        self.wait(0.5)
        self.play(
            FadeOut(krakov_text),
            Write(subject_text),
        )
        self.wait(0.5)
        self.play(
            Write(selfTaught_text),
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(VGroup(*[subject_text,selfTaught_text]), krakov_park_text),
        )
        self.wait(0.5)
        self.play(
            Write(otto_text),
            # Write(integral_text),
        )
        self.wait(0.5)
        self.play(
            Write(integral_text),
        )
        self.play(
            TransformMatchingShapes(otto_text, hugo_text),
        )
        # self.wait(0.5)
        image2 = ImageMobject("images/come up with.png").scale(2).next_to(hugo_text,DOWN,buff=0.3)
        self.add(image2)
        self.wait(0.5)
        self.play(
            FadeOut(VGroup(*[krakov_park_text, integral_text, hugo_text])),
            FadeOut(image2),
        )
        self.wait(0.5)
        self.play(
            Write(cafe_text),
        )
        self.wait(0.5)
        self.play(
            FadeOut(VGroup(*[cafe_text, name_text, date_text])),
            FadeOut(plane),
            FadeOut(image),
        )
        self.wait(1)



