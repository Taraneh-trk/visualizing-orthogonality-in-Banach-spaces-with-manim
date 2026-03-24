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

        title = Tex(
            "Banach Spaces",
            color=BLACK, font_size=80
        ).to_edge(UP)

        circle_metric = Circle(4,dark_pink,fill_color=dark_pink,fill_opacity=0.1)
        text_metric_space = MathTex(r"\text{Metric space}",color=dark_pink).scale(2).move_to(circle_metric.get_center()+2.3*UP)

        circle_norm = Circle(2.8,dark_purple,fill_color=dark_purple,fill_opacity=0.1).shift(1*DOWN)
        text_norm_space = MathTex(r"\text{Normed space}",color=dark_purple).scale(1.5).move_to(circle_norm.get_center()+1.3*UP)

        circle_banach = Circle(1.8,dark_orange,fill_color=dark_orange,fill_opacity=0.1).shift(1.8*DOWN)
        text_banach_space = MathTex(r"\text{Banach space}",color=dark_orange).scale(1.2).move_to(circle_banach.get_center()+0.2*UP)

        text_complete = Text("Complete", color=BLACK).to_edge(LEFT)
        rect_converge = SurroundingRectangle(
            text_complete,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        
        self.play(
            Write(text_norm_space),
            Create(circle_norm),
        )
        self.wait(0.5)
        self.play(
            Create(rect_converge),
            Write(text_complete),
        )
        self.wait(0.2)
        self.play(
            Write(text_banach_space),
            TransformFromCopy(circle_norm, circle_banach),
        )
        self.play(
            FadeOut(VGroup(*[text_complete, rect_converge])),
        )
        self.wait(0.5)
        self.play(
            Write(text_metric_space),
            TransformFromCopy(circle_norm, circle_metric),
        )
        self.wait(1)

        fade_out_list = [
            circle_metric,
            text_metric_space,
            text_norm_space,
            circle_norm,
            circle_banach,
            text_banach_space,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

        self.wait(1)