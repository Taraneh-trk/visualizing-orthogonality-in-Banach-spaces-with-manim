from manim import *
import numpy as np

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
        # 2-1 : definition of Banach Spaces (which is a a complete normed space.)

        text_banachDefination = TextScene(2, "A Complete Normed Space.", 1, "subtitle")
        text_banachDefination.text.move_to(text_title.text.get_center() + DOWN*2)
        self.play(Write(text_banachDefination.text))
        self.wait(text_banachDefination.wait_time)

        # 2-2 : delete "A" from defination and split the rest to 2 parts (Complete + Normed Space)

        text_normedSpace = Text("Normed Space", **StyleSetter_BasedOnTextType("subtitle"))
        text_complete = Text("Complete Space", **StyleSetter_BasedOnTextType("subtitle"))
        text_normedSpace.move_to(text_banachDefination.text.get_center() + RIGHT*4)
        text_complete.move_to(text_banachDefination.text.get_center() + LEFT*4)
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

        # add scene 3
        # ------------------------------
        # 3-1 : definition of complete space (every Cauchy sequence converges in the space)

        self.play(
            FadeOut(text_normedSpace),
            text_complete.animate.move_to(text_title.text.get_center() + DOWN*0.95)
        )
        text_metricSpace = Text( "(X,d) \n\nMetric Space", **StyleSetter_BasedOnTextType("subtitle") ).move_to(text_complete.get_center() + DOWN*1.5 + LEFT*3).set_font_size(26)
        self.play(Write(text_metricSpace))
        self.wait(0.5)

        text_completeText = Text( "X \n\nComplete", **StyleSetter_BasedOnTextType("subtitle") ).move_to(text_complete.get_center() + DOWN*1.5 + RIGHT*3).set_font_size(26)

        arrow = Arrow(
            text_metricSpace.get_right()+RIGHT*0.2,
            text_completeText.get_left()+LEFT*0.2,
            buff=0,
            max_tip_length_to_length_ratio=0.2,
            max_stroke_width_to_length_ratio=0.2
        )
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        self.play(Write(text_completeText))
        self.wait(1)

        text_completeDefinitionText = Text("every Cauchy sequence in X\n\nconverges\n\nto a limit that belongs to X", **StyleSetter_BasedOnTextType("subtitle")).move_to(text_completeText.get_center() + DOWN*2.5).set_font_size(20)
        self.play(Write(Text("WHEN",**StyleSetter_BasedOnTextType("subtitle")).set_color(LIGHT_PINK).set_font_size(23).move_to(text_completeText.get_center() + DOWN*1.5)), Write(text_completeDefinitionText))
        self.wait(0.5)

        # 3-2 : add shape of Cauchy sequence converging to limit in X

        # 3-2-1: Transform circle into smooth shape with rounded corners

        shape_center = text_metricSpace.get_center() + DOWN*2.5
        circle = Circle(radius=1.7, color=BLUE).move_to(shape_center)
        self.play(Create(circle))
        self.wait(0.5)
        
        angles = np.linspace(0, 2*PI, 8, endpoint=False)
        radii =  [1.72, 1.7, 1.0, 1.6, 1.9, 1.85, 0.25, 1.8]
        
        points = [
            shape_center + np.array([radii[i] * np.cos(angles[i]), 
                     radii[i] * np.sin(angles[i]), 
                     0])
            for i in range(len(angles))
        ]
        
        smooth_shape = VMobject(color=BLUE)
        smooth_shape.set_points_smoothly(points + [points[0]])
        smooth_shape.close_path()
        
        self.play(Transform(circle, smooth_shape), run_time=2)
        self.wait(1)
        
        num_points = 10
        distances = [11.0, 7.0, 4.0, 1.65, 1.0, 0.5, 0.35, 0.22, 0.1, 0]  
        
        start_pos = shape_center + np.array([0.5, 0.7, 0])
        end_pos = shape_center + np.array([-0.7, -0.5, 0])

        all_positions = []
        for i in range(num_points):
            t = i / (num_points - 1)
            
            base_pos = start_pos + t * (end_pos - start_pos)
            
            direction = end_pos - start_pos
            perpendicular = np.array([-direction[1], direction[0], 0])
            if np.linalg.norm(perpendicular) > 0:
                perpendicular = perpendicular / np.linalg.norm(perpendicular)
            
            offset = perpendicular * distances[i] * np.sin(t * PI) * 0.5
            
            position = base_pos + offset
            all_positions.append(position)
        
        dots = []
        colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK, GOLD, WHITE]
        
        for i, pos in enumerate(all_positions):
            dot = Dot(point=pos, color=colors[i], radius=0.03)
            dots.append(dot)
            self.play(FadeIn(dot), run_time=0.1)
            self.wait(0.1)
        self.wait(1)
        
        final_circle = Circle(radius=0.12, color=WHITE, stroke_width=3).move_to(end_pos)
        self.play(text_completeDefinitionText[5:11].animate.set_color(ORANGE))
        self.wait(0.25)
        self.play(
            Create(final_circle), 
            text_completeDefinitionText[22:31].animate.set_color(YELLOW)
        )
        
        self.wait(2)