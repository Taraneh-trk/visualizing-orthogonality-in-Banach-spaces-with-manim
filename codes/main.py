from manim import *

def StyleSetter_BasedOnTextType(text_type:str):
        if text_type == "title":
            return {"font_size": 48, "color": WHITE, "weight": BOLD, "should_center": True, "font": "Arial"}
        elif text_type == "subtitle":
            return {"font_size": 36, "color": WHITE, "weight": ITALIC}
        else:
            return {"font_size": 24, "color": WHITE}

class TextScene:
    def __init__(self, phase:int, text:str, wait_time:int, type:str="normal"):
        self.phase = phase
        self.text =  Text(text, **StyleSetter_BasedOnTextType(type))
        self.wait_time = wait_time

class DisplayScene(Scene):
    def construct(self):
        # add scence 1
        # ------------------------------ 
        # 1-1 : title
        text_title = TextScene(1, "Kinds of Orthogonality in Banach Spaces", 2, "title")
        self.play(FadeIn(text_title.text))
        self.wait(text_title.wait_time)

        # 1-2 : transition to Banach Spaces  
        # 1 . split title to 2 part ( .. + Banach Spaces (**change this parts color to BLUE_E) ) 
        # 2 . move the second part to top center
        # 3 . fade out the other

        text_banach = Text("Banach Spaces", **StyleSetter_BasedOnTextType("title"))
        text_banach.move_to(text_title.text.get_center())
        self.play(Transform(text_title.text, text_banach))
        self.play(FadeOut(text_banach))
        self.play(text_title.text.animate.to_edge(UP))
        self.wait(text_title.wait_time)


        