from manim import *

def StyleSetter_BasedOnTextType(text_type:str):
        if text_type == "title":
            return {"font_size": 48, "color": WHITE, "weight": BOLD, "should_center": True, "font": "Arial"}
        elif text_type == "subtitle":
            return {"font_size": 40, "color": WHITE}
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

        text_title = TextScene(1, "Kinds of Orthogonality in Banach Spaces", 1, "title")
        self.play(FadeIn(text_title.text))
        self.wait(text_title.wait_time)

        # 1-2 : transition to Banach Spaces  
        # 1 . split title to 2 part ( .. + Banach Spaces (**change this parts color to BLUE_E) ) 
        # 2 . move the second part to top center
        # 3 . fade out the other

        text_banach = Text("Banach Spaces", **StyleSetter_BasedOnTextType("title"))
        text_banach.move_to(text_title.text.get_center()).set_font_size(58)
        self.play(Transform(text_title.text, text_banach))
        self.play(FadeOut(text_banach))
        self.play(text_title.text.animate.to_edge(UP))
        self.wait(1)


        # add scene 2
        # ------------------------------
        # 2-1 : defination of Banach Spaces (which is a a complete normed space.)
        text_banachDefination = TextScene(2, "A Complete Normed Space.", 1, "subtitle")
        text_banachDefination.text.move_to(text_title.text.get_center() + DOWN*2)
        self.play(Write(text_banachDefination.text))
        self.wait(text_banachDefination.wait_time)

        # 2-2 : delete "A" from defination and split the rest to 2 parts (Complete + Normed Space)
        text_normedSpace = Text("Normed Space", **StyleSetter_BasedOnTextType("subtitle"))
        text_complete = Text("Complete", **StyleSetter_BasedOnTextType("subtitle"))
        text_normedSpace.move_to(text_banachDefination.text.get_center() + RIGHT*2)
        text_complete.move_to(text_banachDefination.text.get_center() + LEFT*2)
        text_normed_complete_group = VGroup(text_normedSpace, text_complete)
        self.play(Transform(text_banachDefination.text, text_normed_complete_group))

        # 2-3 : make normed space faint and bold Complete
        self.play(
            FadeOut(text_banachDefination.text),
            FadeIn(text_complete),
            FadeIn(text_normedSpace)
        )

        self.play(
            text_normedSpace.animate
                .set_color(GRAY_C)
                .set_opacity(0.1)
                .set_font_size(34),

            text_complete.animate
                .set_weight(BOLD)
                .set_font_size(48)
        )

        self.wait(1)

        