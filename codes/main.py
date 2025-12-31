from manim import *

class HelloScene(Scene):
    def construct(self):
        text = Text("Hello Manim!")
        self.play(Write(text))