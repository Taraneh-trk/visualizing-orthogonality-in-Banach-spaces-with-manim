from manim import *
import numpy as np
from math import *

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

class Part1_Scene(MovingCameraScene):
    #  Norm → Metric → Cauchy → Completeness → Banach
    #  Define Length → Create Distance → Chase Limits → Reach Completeness → Enter Banach
    topics = {
        0: "The Birth of Norms", #Norms on Vector Spaces
        1: "From Norms to Metrics", #How a Norm Generates a Metric?
        2: "Cauchy Sequences : The Mystery of Nearness", #What Does It Mean to Be Cauchy?  - Cauchy Sequences in Metric Spaces
        3: "Banach Spaces : The Kingdom of Completeness",
    }

    def auto_adjust_position(mobject, padding=0.5):
        frame_width = config.frame_width
        frame_height = config.frame_height
        
        shift_amount = np.array([0, 0, 0])
        
        if mobject.get_right()[0] > frame_width/2 - padding:
            overflow = mobject.get_right()[0] - (frame_width/2 - padding)
            shift_amount += LEFT * overflow
        
        if mobject.get_left()[0] < -frame_width/2 + padding:
            overflow = (-frame_width/2 + padding) - mobject.get_left()[0]
            shift_amount += RIGHT * overflow
        
        if mobject.get_top()[1] > frame_height/2 - padding:
            overflow = mobject.get_top()[1] - (frame_height/2 - padding)
            shift_amount += DOWN * overflow
        
        if mobject.get_bottom()[1] < -frame_height/2 + padding:
            overflow = (-frame_height/2 + padding) - mobject.get_bottom()[1]
            shift_amount += UP * overflow
        
        if np.any(shift_amount != 0):
            mobject.shift(shift_amount)
        
        return mobject

    def show_warning(self, body: MathTex,set_image=False):
        """Show warning message with box"""

        title_text = Text("❗Note❗", color=dark_red, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_red,
            fill_color=light_red,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )

        box.move_to(group.get_center())

        if set_image==True:
            # ex_mark_1 = ImageMobject("images/ex_mark_1_img.png").move_to(box.get_top()+ 3*LEFT + 1.5*UP ).scale(3)
            # self.add(ex_mark_1) 

            ex_mark_2 = ImageMobject("images/ex_mark_2_img.png").move_to(box.get_top()+ 1.5*UP ).scale(3)
            self.add(ex_mark_2)

            # arrow_0_0_down = CurvedArrow(
            #     start_point=box.get_corner(UR)+2*UP+1.5*LEFT,
            #     end_point=box.get_top()+1.0*RIGHT,
            #     angle=PI/2,
            #     color=light_red,
            # ).scale(1.5)
            # self.play(
            #     Create(arrow_0_0_down),
            #     run_time=1
            # )

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))

        if set_image==True:
            self.play(
                # FadeOut(arrow_0_0_down),
                # FadeOut(ex_mark_1),
                FadeOut(ex_mark_2)
            )

    def ask_question(self,body, return_notShow=False,set_image=False):
        """Show message with box to ask a question. """

        title_text = Text("🤔Question", color=dark_pink, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_pink,
            fill_color=light_pink,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            list_images = []
            if set_image==True:
                ex_mark_2 = ImageMobject("images/think_img.png").move_to(box.get_top()+ 0.1*UP ).scale(2.2)
                # self.add(ex_mark_2)
                self.wait(1)

                ex_mark_1 = ImageMobject("images/find_img.png").to_edge(DR).shift(0.5*LEFT).scale(2)
                # self.add(ex_mark_1)
                list_images+=[ex_mark_2, ex_mark_1]
            return group, box, *list_images
        
        if set_image==True:
            ex_mark_2 = ImageMobject("images/think_img.png").move_to(box.get_top()+ 0.1*UP ).scale(2)
            self.add(ex_mark_2)
            self.wait(1)

        self.play(Create(box), Write(group))

        self.wait(1)
        if set_image==True:
            ex_mark_1 = ImageMobject("images/find_img.png").to_edge(DR).shift(0.5*LEFT).scale(2)
            self.add(ex_mark_1)

        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))

        if set_image==True:
            self.play(
                FadeOut(ex_mark_2),
                FadeOut(ex_mark_1)
            )

    def show_minorPoint(self,body,return_notShow):
        """Show message with box to ask a question. """

        title_text = Text("Note", color=dark_blue, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_blue,
            fill_color=light_blue,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))

    def show_definition(self, definition: MathTex, total_title, retrun_notShow=False, what_is_defined=""):
        """Show definition with box"""

        title_text = Text(f"⚙️📃Definition {what_is_defined}", color=dark_green, font_size=36)

        group = VGroup(title_text, definition).arrange(DOWN, buff=0.3)
        
        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_green,
            fill_color=light_green,
            fill_opacity=0.15,
            width=group.width + 1,
            height=group.height + 0.8
        )

        new_position = total_title.get_center() + DOWN * (box.height)
        group.move_to(new_position)
        if group.is_off_screen():
            self.auto_adjust_position(group)
        
        box.move_to(group.get_center())

        if box.is_off_screen():
            self.auto_adjust_position(box)
        
        if retrun_notShow :
            return group,box
        
        self.play(Create(box), Write(group))
        self.wait(2)
        return group, box
    
    def show_conclusion(self,total_title,body,return_notShow=False):
        """Show message with box to conclude some thing. """

        title_text = Text("Conclusion", color= dark_orange, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color= dark_orange,
            fill_color=light_orange,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
    
    def show_example(self,total_title,body,title_text_for_box,return_notShow=False):
        """Show message with box to show some examples. """

        title_text = Text(title_text_for_box, color= dark_purple, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color= dark_purple,
            fill_color=light_purple,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
    
    def construct(self):

        # self.scene1()

        # self.scene2()

        # topic_number = 0
        # title = self.scene3(topic_number,True)

        # norm
        # self.scene4(title)

        # from norm to metrics
        topic_number = 1
        title = self.scene3(topic_number,False)

        self.scene5(title)

    def scene5_subScene0(self, title):
        """ constructing metrics with norms """
        # metric induced by the norm

        text_metric_space = MathTex(r"\text{Metric space}",color=dark_green).move_to(title.get_center()+DOWN).scale(2)
        text_metric_space_parts = MathTex(r"(",r"X",r",",r"d",r")",color=dark_blue,arg_separator="  ").move_to(text_metric_space.get_center()+1.6*DOWN).scale(2)
        rect_x = SurroundingRectangle(
            text_metric_space_parts[1],
            color=dark_pink,        
            buff=0.1,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_vector_space = MathTex(r"\text{Vector space}",color=dark_pink).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*LEFT).scale(2)
        rect_vec_x = SurroundingRectangle(
            text_vector_space,
            color=dark_pink,        
            buff=0.1,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_x = CurvedArrow(
            start_point=text_metric_space_parts[1].get_left()+0.1*LEFT,
            end_point=rect_vec_x.get_top()+0.2*UP,
            angle=PI/2,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        rect_d = SurroundingRectangle(
            text_metric_space_parts[3],
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_distance = MathTex(r"\text{Distance}",color=dark_orange).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        rect_distance = SurroundingRectangle(
            text_distance,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_d = CurvedArrow(
            start_point=text_metric_space_parts[3].get_right()+0.2*RIGHT,
            end_point=rect_distance.get_top()+0.2*UP,
            angle=-PI/2,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            Write(text_metric_space),
        )
        self.wait(1)
        self.play(
            Write(text_metric_space_parts[::2]),
        )
        self.wait(1)
        self.play(
            Write(text_metric_space_parts[1]),
            Create(rect_x),
            Create(arrow_x),
            Create(rect_vec_x),
            Write(text_vector_space),
        )
        self.wait(1)
        self.play(
            Write(text_metric_space_parts[3]),
            Create(rect_d),
            Create(arrow_d),
            Create(rect_distance),
            Write(text_distance),
        )
        self.wait(1)

        fade_out_list = [text_metric_space, text_metric_space_parts, rect_x, 
                         arrow_x, rect_vec_x, text_vector_space,
                         rect_d, arrow_d, rect_distance, text_distance]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

        self.wait(1)

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-6, 7, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=13,
        ).move_to([0, 0, 0]+DOWN)
        self.play(Create(plane))
        self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-6, 7, 1],
            y_length=8,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # dot at tip of vector
        tip_x = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        self.play(FadeIn(tip_x))
        self.wait(1)
        tip_x_text = MathTex("A = (x_1,y_1)",color=BLACK).next_to(tip_x,UP).shift(0.6*RIGHT)
        self.play(
            Write(tip_x_text),
        )
        self.wait(1)

        tip_y = Dot(axes.c2p(2,6), color=dark_green, radius=0.07)
        self.play(FadeIn(tip_y))
        self.wait(1)
        tip_y_text = MathTex("B = (x_2,y_2)",color=BLACK).next_to(tip_y,UP)  #.shift(0.1*RIGHT)
        self.play(
            Write(tip_y_text),
        )
        self.wait(1)

        dot_line_distance =  DashedLine(
            start=axes.c2p(6,4),
            end=axes.c2p(2,6), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_orange,
        )
        text_distance.scale(0.5).next_to(dot_line_distance,DOWN) #.shift(0.4*RIGHT)
        text_dxy = MathTex(r"d(A,B)",color=dark_orange).shift(axes.c2p(0,0)+DOWN+1.5*LEFT).scale(1.5)

        self.play(
            Create(dot_line_distance),
            Write(text_distance),
        )
        self.wait(0.5)
        self.play(
            Write(text_dxy),
        )
        self.wait(0.5)
        self.play(
            FadeOut(text_distance),
        )

        vector_amb = Arrow(
            start=axes.c2p(2,6),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        text_vec_amb = MathTex(r"\vec{BA}",color=dark_orange).move_to(vector_amb.get_center()+0.5*UP)
        text_norm_ab = MathTex(r" = ",r"\|\vec{BA}\|",color=dark_orange).scale(1.5).next_to(text_dxy,RIGHT)

        self.play(
            FadeTransform(dot_line_distance, vector_amb),
        )
        self.wait(0.5)
        self.play(
            Write(text_vec_amb),
            Write(text_norm_ab),
        )
        self.wait(0.5)

        vector_a = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        vector_b = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(2,6),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_vec_b = MathTex(r"\vec{b}",color=dark_green).move_to(vector_b.get_center()+0.5*LEFT)
        text_vec_a = MathTex(r"\vec{a}",color=dark_red).move_to(vector_a.get_center()+0.5*RIGHT)

        self.play(
            GrowArrow(vector_a, run_time=1.2, rate_func=rush_from),
            Write(text_vec_a),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(vector_b, run_time=1.2, rate_func=rush_from),
            Write(text_vec_b),
        )
        self.wait(0.5)

        text_vec_amb_2 = MathTex(r"\vec{BA} = ",r"\vec{a} - \vec{b}",color=dark_pink).move_to(vector_amb.get_center()+0.5*UP+7*LEFT).scale(2)
        text_norm_ab_2 = MathTex(r" = ",r"\|\vec{a} - \vec{b}\|",color=dark_orange).next_to(text_norm_ab,DOWN).scale(1.5)

        self.play(
            TransformFromCopy(text_vec_amb, text_vec_amb_2),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(VGroup(text_vec_amb_2,text_norm_ab), text_norm_ab_2),
        )
        self.wait(0.5)

        fade_out_list = [
            plane, axes, tip_x , tip_x_text , tip_y , tip_y_text , text_dxy , vector_amb,
            text_vec_amb , text_norm_ab , vector_a , vector_b, text_vec_a , text_vec_b, 
            text_vec_amb_2, text_norm_ab_2, 
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

        self.wait(1)

    def scene5_subScene1(self, title, prove_1, distance):
        """prove d is a meter part 1"""

        # proof
        step_1 = MathTex(r"d(x,y) = 0",color=BLACK).scale(1.5).move_to(prove_1.get_center()+2*DOWN)
        step_2 = MathTex(r"\iff",r"\|x-y\| = 0",color=BLACK).scale(1.5).next_to(step_1,RIGHT)
        step_3 = MathTex(r"\iff",r"x-y = 0",color=BLACK).scale(1.5).next_to(step_2,DOWN).shift(0.3*LEFT)
        step_2to3 = MathTex(r"(N1)",color=dark_orange).scale(1.5).next_to(step_3,RIGHT)
        step_4 = MathTex(r"\iff",r"x = y",color=BLACK).scale(1.5).next_to(step_3,DOWN).shift(0.5*LEFT)
        square_for_end_proof = Square(0.3,color=BLACK).scale(1.5).next_to(step_4,RIGHT)
        prove_1_group = VGroup(step_1, step_2, step_3, step_2to3, step_4, square_for_end_proof).shift(3*LEFT+0.7*UP)
        rect_prove_1 = SurroundingRectangle(
            prove_1_group,
            color=dark_orange,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Write(prove_1),
        )
        self.wait(1)

        self.play(
            Create(rect_prove_1),
        )
        self.wait(0.6)
        self.play(
            TransformFromCopy(prove_1[1], step_1),
        )
        self.wait(0.6)
        self.play(
            TransformFromCopy(distance[2],step_2),
        )
        self.wait(0.6)
        self.play(
            Write(step_2to3),
        )
        self.wait(0.3)
        self.play(
            TransformFromCopy(VGroup(step_2to3,step_2),step_3),
        )
        self.wait(0.6)
        self.play(
            Write(step_4),
        )
        self.wait(0.6)
        self.play(
            Create(square_for_end_proof),
        )
        self.wait(0.6)

        # shape

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-2, 5, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=4,
            x_length=13,
        ).move_to([0, 0, 0]+1.5*DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-2, 5, 1],
            y_length=4,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+1.5*DOWN)

        self.play(
            FadeTransform(VGroup(prove_1_group,rect_prove_1),VGroup(plane,axes)),
        )
        self.wait(1)

        tip_x = Dot(axes.c2p(6,4), color=dark_orange, radius=0.09)
        tipx_text = MathTex("x",color=BLACK).next_to(tip_x,DOWN)
        self.play(
            FadeIn(tip_x),
            Write(tipx_text),
        )
        self.wait(0.3)

        tip_y = Dot(axes.c2p(2,1), color=dark_purple, radius=0.09)
        tipy_text = MathTex("y",color=BLACK).next_to(tip_y,UP)
        self.play(
            FadeIn(tip_y),
            Write(tipy_text),
        )
        self.wait(1)

        dot_line_distance =  Arrow(
            start=axes.c2p(2,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            GrowArrow(dot_line_distance),
        )
        self.wait(0.5)

        self.play(
            dot_line_distance.animate.scale(
                0.01,
                about_point=dot_line_distance.get_start()  
            ),
            VGroup(tip_x,tipx_text).animate.move_to(axes.c2p(2,1)),
            tip_y.animate.set_opacity(0),
            FadeOut(dot_line_distance.tip),
            rum_time=3
        )

        self.wait(1)

        fade_out_list = [
            plane, axes, tip_x ,tip_y , tipx_text, tipy_text
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

    def scene5_subScene2(self, title, prove_1, prove_2, distance):
        """prove d is a meter part 2"""

        # proof
        step_1 = MathTex(r"d(x,y)",color=BLACK).scale(1.5).move_to(prove_2.get_center()+2*DOWN)
        step_2 = MathTex(r" = ",r"\|x-y\|",color=BLACK).scale(1.5).next_to(step_1,RIGHT)
        step_3 = MathTex(r" = ",r"\|(-1) \, (y-x)\|",color=BLACK).scale(1.5).next_to(step_2,RIGHT)
        step_4 = MathTex(r" = ",r"|-1| \|(y-x)\|",color=BLACK).scale(1.5).next_to(step_2,DOWN).shift(1*RIGHT)
        step_3to4 = MathTex(r"(N2)",color=dark_orange).scale(1.5).next_to(step_4,RIGHT)
        step_5 = MathTex(r" = ",r"\|(y-x)\|",color=BLACK).scale(1.5).next_to(step_4,DOWN).shift(0.5*LEFT)
        step_6 = MathTex(r" = ",r"d(y,x)",color=BLACK).scale(1.5).next_to(step_5,RIGHT)
        square_for_end_proof = Square(0.3,color=BLACK).scale(1.5).next_to(step_6,RIGHT)
        prove_2_group = VGroup(step_1, step_2, step_3, step_4, step_3to4, step_5, step_6, square_for_end_proof).shift(4*LEFT+0.7*UP)
        rect_prove_2 = SurroundingRectangle(
            prove_2_group,
            color=dark_orange,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            TransformMatchingTex(prove_1, prove_2),
        )
        self.wait(1)

        self.play(
            Create(rect_prove_2),
        )
        self.wait(0.6)
        self.play(
            TransformFromCopy(prove_2[1], step_1),
        )
        self.wait(0.6)
        self.play(
            TransformFromCopy(distance[2],step_2),
        )
        self.wait(0.6)
        self.play(
            Write(step_3),
        )
        self.wait(0.6)
        self.play(
            Write(step_3to4),
        )
        self.wait(0.3)
        self.play(
            TransformFromCopy(VGroup(step_3to4,step_3),step_4),
        )
        self.wait(0.6)
        self.play(
            Write(step_5),
        )
        self.wait(0.6)
        self.play(
            Write(step_6),
        )
        self.wait(0.6)
        self.play(
            Create(square_for_end_proof),
        )
        self.wait(0.6)

        step_1.set_color(dark_red)
        step_6.set_color(dark_red)

        self.wait(0.6)

        # shape

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-2, 5, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=4,
            x_length=13,
        ).move_to([0, 0, 0]+1.5*DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-2, 5, 1],
            y_length=4,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+1.5*DOWN)

        self.play(
            FadeTransform(VGroup(prove_2_group,rect_prove_2),VGroup(plane,axes)),
        )
        self.wait(1)

        tip_x = Dot(axes.c2p(6,4), color=dark_orange, radius=0.09)
        tipx_text = MathTex("x",color=BLACK).next_to(tip_x,DOWN)
        self.play(
            FadeIn(tip_x),
            Write(tipx_text),
        )
        self.wait(0.3)

        tip_y = Dot(axes.c2p(2,1), color=dark_purple, radius=0.09)
        tipy_text = MathTex("y",color=BLACK).next_to(tip_y,UP)
        self.play(
            FadeIn(tip_y),
            Write(tipy_text),
        )
        self.wait(1)

        vector_1 = Arrow(
            start=axes.c2p(2,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        vector_2 = Arrow(
            start=axes.c2p(6,4),
            end=axes.c2p(2,1),
            buff=0,
            stroke_width=6,
            color=dark_terquise,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            GrowArrow(vector_1),
        )
        self.wait(1)

        self.play(
            vector_1.animate.shift(8*LEFT),
            run_time=1
        )
        self.wait(1)

        self.play(
            GrowArrow(vector_2),
        )
        self.wait(1)

        self.play(
            vector_2.animate.shift(7.7*LEFT+0.4*DOWN),
            run_time=1
        )
        self.wait(1)

        comp_line = Line(vector_1.get_start(),vector_1.get_end(),color=dark_red, stroke_width=10)
        self.play(
            Create(comp_line),
        )
        self.wait(0.3)
        self.play(
            comp_line.animate.move_to(vector_2.get_center()),
            run_time=1
        )
        self.wait(1)

        fade_out_list = [
            plane, axes, tip_x ,tip_y , tipx_text, tipy_text, vector_1, vector_2, comp_line
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

    def scene5_subScene3(self, title, prove_2, prove_3, distance):
        """prove d is a meter part 3"""
        normed_space = MathTex("")

    def scene5_subScene4(self, title):
        """definition of normed space"""
        normed_space = MathTex("")


    def scene5(self,title):
        self.play(
            Write(title),
        )
        self.wait(1)
        self.play(
            FadeOut(title),
        )
        self.wait(0.5)

        # constructing metrics with norms
        # self.scene5_subScene0(title)

        # proof needed things
        distance = MathTex(r"d(x,y) ",r" = ",r"\|x-y\|",color=BLACK).scale(2).move_to(title.get_center()+0.2*DOWN)
        rect_distance = SurroundingRectangle(
            distance,
            color=dark_blue,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=5,    
            corner_radius=0.15 
        )

        self.play(
            Create(rect_distance),
            Write(distance),
        )
        self.wait(1)

        text_claim = MathTex(r"\text{Claim : } \\ d \text{ is a } " ,r"\text{metric}",color=BLACK).scale(1.1)
        text_claim.set_color_by_tex(r"\text{metric}",color=dark_blue)

        self.play(
            VGroup(distance,rect_distance).scale(1).animate.to_edge(UL),
            Write(text_claim.move_to(rect_distance.get_right()+0.5*RIGHT+0.2*DOWN)),
        )
        self.wait(1)

        # prove part 1
        prove_1 = MathTex(r"1. \text{  }",r"d(x,y) = 0",r"\iff",r"x = y",color=BLACK).scale(1.5).move_to(title.get_center()+2*DOWN)
        proof_1_needed = [
            prove_1, distance
        ]
        self.scene5_subScene1(title, *proof_1_needed)

        # prove part 2
        prove_2 = MathTex(r"2. \text{  }",r"d(x,y)",r" = ",r"d(y,x)",color=BLACK).scale(1.5).move_to(title.get_center()+2*DOWN)
        proof_2_needed = [
            prove_1, prove_2, distance
        ]
        self.scene5_subScene2(title,*proof_2_needed)

        # prove part 3
        prove_3 = MathTex(r"3. \text{  }",r"d(x,y)",r" \le ",r"d(x,z)",r" + ",r"d(z,y)",color=BLACK).scale(1.5).move_to(title.get_center()+2*DOWN)
        proof_3_needed = [
            prove_2, prove_3, distance
        ]
        self.scene5_subScene3(title, *proof_3_needed)

        # normed space
        # self.scene5_subScene4(title)


    def scene4_subScene0(self,title):
        self.play(
            Write(title),
        )
        self.wait(2)
        self.play(
            FadeOut(title),
        )
        # length

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-6, 7, 0.5],
            x_range=[-8, 8, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=13,
        ).move_to([0, 0, 0]+DOWN)
        self.play(Create(plane))
        self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-6, 7, 0.5],
            y_length=8,
            x_range=[-8, 8, 0.5],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # dot at tip of vector
        tip = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        self.play(FadeIn(tip))
        self.wait(1)
        tip_text = MathTex("(x,y)",color=BLACK).next_to(tip,UP)
        self.play(
            Write(tip_text),
        )
        self.wait(1)

        norm2_2d = MathTex(
            r"\text{length }",r"= ",r"\sqrt{x^2 + y^2}",color=BLACK
        ).move_to(axes.get_center()+1*DOWN)
        # draw vector in (0,0)
        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(
            Write(norm2_2d[0]),
            GrowArrow(vector, run_time=1.2, rate_func=rush_from),
        )
        self.wait(2)

        for _ in range(2):
            self.play(
                tip.animate.scale(1.5).set_color(BLACK),
                rate_func=there_and_back,
            )

        dot_line_1 =  DashedLine(
            start=axes.c2p(6,4),
            end=axes.c2p(6,0), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_red,
        )

        dot_line_1_result = Line(
            start=axes.c2p(0,0),
            end=axes.c2p(6,0), 
            color=dark_pink,
        )

        text_dot_x = MathTex(r"x",color=BLACK).move_to(dot_line_1_result.get_center()+0.3*UP)

        dot_line_2 =  DashedLine(
            start=axes.c2p(6,4),
            end=axes.c2p(0,4), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_not_green,
        )

        dot_line_2_result = Line(
            start=axes.c2p(0,0),
            end=axes.c2p(0,4), 
            color=dark_purple,
        )

        text_dot_y = MathTex(r"y",color=BLACK).move_to(dot_line_2_result.get_center()+0.3*LEFT)

        self.play(
            Create(dot_line_1),
            Create(dot_line_2),
            run_time=1
        )
        self.wait(2)
        self.play(
            Create(dot_line_1_result),
            Write(text_dot_x),
        )
        self.wait(0.5)
        self.play(
            Create(dot_line_2_result),
            Write(text_dot_y),
        )
        self.wait(1)
        self.play(
            FadeOut(dot_line_1),
            FadeOut(dot_line_2),
        )
        dot_line_1_result_group_with_text_x = VGroup(dot_line_1_result,text_dot_x)
        self.play(
            dot_line_1_result_group_with_text_x.animate.move_to(dot_line_2.get_center()+0.19*UP),
            run_time=1
        )
        self.wait(1)

        tip_triangle_1 = Dot(axes.c2p(0,0), color=dark_pink, radius=0.07)
        self.play(FadeIn(tip_triangle_1))
        self.wait(0.5)

        tip_triangle_2 = Dot(axes.c2p(0,4), color=dark_purple, radius=0.07)
        self.play(FadeIn(tip_triangle_2))
        self.wait(1)

        triangle_Euclid = Polygon(
            tip.get_center(),
            tip_triangle_1.get_center(),
            tip_triangle_2.get_center(),
        )

        triangle_Euclid.set_stroke(color=dark_terquise, width=8)
        triangle_Euclid.set_fill(dark_terquise, opacity=0.2)

        self.play(
            DrawBorderThenFill(triangle_Euclid,2),
            run_time=1
        )
        self.wait(3)
        self.play(
            triangle_Euclid.animate.set_fill(WHITE),
            run_time=1
        )

        for _ in range(2):
            self.play(
                vector.animate.set_stroke(width=20).set_color("#9A0000"),
                rate_func=there_and_back,
            )

        self.play(
            Write(norm2_2d[1]),
            Write(norm2_2d[2]),
        )
        self.wait(2)

        # num example 
        text_num_x = MathTex(r"4",color=dark_pink).move_to(text_dot_x.get_center())
        text_num_y = MathTex(r"3",color=dark_pink).move_to(text_dot_y.get_center())
        text_length_vector_1 = MathTex(r"\sqrt{4^2 + 3^2}",color=dark_pink).move_to(vector.get_center()+1.2*RIGHT)
        text_length_vector_2part0 = MathTex(r"\sqrt{16 + 9}",color=dark_pink).move_to(vector.get_center()+1.2*RIGHT)
        text_length_vector_2part1 = MathTex(r"\sqrt{ 25 }",color=dark_pink).move_to(text_length_vector_2part0.get_center())
        text_length_vector_2part2 = MathTex(r"5",color=dark_pink).move_to(text_length_vector_2part1.get_center())
        self.play(
            FadeOut(text_dot_x),
            FadeIn(text_num_x)
        )
        self.wait(0.5)
        self.play(
            FadeOut(text_dot_y),
            FadeIn(text_num_y)
        )
        self.wait(0.5)
        self.play(
            FadeIn(text_length_vector_1),
        )
        self.wait(1)
        self.play(
            FadeTransform(text_length_vector_1,text_length_vector_2part0),
        )
        self.wait(0.7)
        self.play(
            FadeTransform(text_length_vector_2part0,text_length_vector_2part1),
        )
        self.wait(0.7)
        self.play(
            FadeTransform(text_length_vector_2part1,text_length_vector_2part2),
        )
        self.wait(1)
        self.play(
            FadeOut(text_num_x),
            FadeIn(text_dot_x),
            FadeOut(text_num_y),
            FadeIn(text_dot_y),
            FadeOut(text_length_vector_2part2),
        )
        self.wait(1)

        self.play(
            FadeOut(triangle_Euclid),
            FadeOut(dot_line_1_result_group_with_text_x),
            FadeOut(text_dot_y),
            FadeOut(dot_line_1_result),
            FadeOut(dot_line_2_result),
            FadeOut(tip_triangle_1),
            FadeOut(tip_triangle_2),
        )
        self.wait(3)


        # properties of length
        # 1
        text_1 = MathTex(r"\text{Always non-negative}",color=dark_pink
        ).scale(1.3).to_edge(LEFT).shift(0.5*RIGHT+UP)
        self.play(
            Write(text_1),
        )
        self.wait(2)
        text_1_part2 = MathTex(r"\ge 0",color=dark_pink
        ).scale(1.3).next_to(norm2_2d,RIGHT)
        self.play(
            Write(text_1_part2),
        )
        self.wait(2)
        self.play(
            FadeOut(text_1_part2),
        )

        # 2
        text_2 = MathTex(r"\text{vector = }",r"\vec{0}=(0,0)\\",r"\text{length = }",r"0",color=dark_pink
        ).scale(1.3).to_edge(LEFT).shift(RIGHT+UP)
        text_2[2:].shift(1*LEFT)
        arrow_0_0_down = CurvedArrow(
            start_point=text_2.get_corner(UR)+0.2*DOWN+0.3*RIGHT,
            end_point=text_2.get_corner(DR)+0.2*UP+0.3*RIGHT,
            angle=-PI/2,
            color=light_pink,
        )
        self.play(
            FadeTransform(text_1,text_2[0:2]),
        )
        self.play(
            FadeOut(vector),
            tip.animate.move_to(axes.c2p(0,0)),
            run_time=3
        )
        text_2_formula_1 = MathTex(r" \sqrt{0^2 + 0^2}",color=dark_pink
        ).next_to(norm2_2d,DOWN)
        # text_2_formula_1[1].set_color(dark_pink)
        # text_2_formula_1[3].set_color(dark_pink)
        self.play(
            TransformFromCopy(norm2_2d[1:],text_2_formula_1),
        )
        self.wait(1)
        text_2_formula_2 = MathTex(r" = ",r"0",color=dark_pink
        ).next_to(text_2_formula_1,RIGHT).shift(0*DOWN)
        # text_2_formula_2.set_color_by_tex("0", dark_pink)
        self.play(
            Write(text_2_formula_2),
        )
        self.wait(1)
        self.play(
            Write(text_2[2:]),
        )
        self.wait(1)
        self.play(
            Create(arrow_0_0_down),
        )
        self.wait(2)
        arrow_0_0_up = CurvedArrow(
            start_point=text_2.get_corner(DL)+0.2*UP+0.3*LEFT,
            end_point=text_2.get_corner(UL)+0.3*DOWN+0.3*LEFT,
            angle=-PI/2,
            color=light_pink,
        )
        self.play(
            Create(arrow_0_0_up),
        )
        self.wait(3)

        self.play(
            FadeOut(arrow_0_0_up),
            FadeOut(arrow_0_0_down),
            FadeOut(text_2),
            FadeOut(text_2_formula_1),
            FadeOut(text_2_formula_2),
            FadeIn(vector),
            tip.animate.move_to(axes.c2p(6,4)),
            run_time=1
        )
        self.wait(1)

        # 3

        text_3_part1 = MathTex(r"t \cdot ",r"\text{vector}\\",color=dark_pink
        ).scale(1.3).to_edge(LEFT).shift(RIGHT+UP)
        text_3_part2 = MathTex(r"t \cdot ",r"\text{length}",color=dark_pink
        ).scale(1.3).to_edge(LEFT).shift(RIGHT+0.9*DOWN)
        self.play(
            Write(text_3_part1),
        )
        self.wait(2)
        note_text = MathTex(r"t \cdot (x,y) = (t \times x , t \times y )",color=light_purple).move_to(text_3_part1.get_center()+0.6*UP)
        self.play(
            Write(note_text),
            run_time=2.5
        )
        self.wait(2)
        
        # -----------------------------------
        # STEP 0: Original norm
        # -----------------------------------
        norm = MathTex(
            # r"=",
            r"\sqrt{",
            r"(x)^2",
            r"+",
            r"(y)^2",
            r"}",
            color=light_purple
        ).next_to(norm2_2d, DOWN)

        self.play(Write(norm))
        self.wait(2)

        # -----------------------------------
        # STEP 1: x,y  →  tx,ty
        # -----------------------------------
        scaled = MathTex(
            # r"=",
            r"\sqrt{",
            r"(tx)^2",
            r"+",
            r"(ty)^2",
            r"}",
            color=light_purple
        ).move_to(norm)

        self.play(
            TransformMatchingTex(norm, scaled) #, transform_mismatches=True
        )
        self.wait(2)

        # -----------------------------------
        # STEP 2: Expand powers
        # -----------------------------------
        expanded = MathTex(
            # r"=",
            r"\sqrt{ (",
            r"t^2",r"x^2)",
            r"+ (",
            r"t^2",r"y^2)",
            r"}",
            color=light_purple
        ).move_to(scaled)

        self.play(
            TransformMatchingTex(scaled, expanded)
        )
        self.wait(2)

        # -----------------------------------
        # STEP 3: Highlight common factor
        # -----------------------------------
        expanded.set_color_by_tex("t^2", dark_orange)
        self.wait(1)

        # -----------------------------------
        # STEP 4: Factor t^2
        # -----------------------------------
        factored = MathTex(
            # r"=",
            r"\sqrt{",
            r"t^2",
            r"(x^2 + y^2)",
            r"}",
            color=light_purple
        ).move_to(expanded).set_color_by_tex("t^2", dark_orange)

        self.play(
            TransformMatchingTex(expanded, factored)
        )
        self.wait(2)

        # -----------------------------------
        # STEP 5: Move sqrt(x^2+y^2) forward
        # -----------------------------------
        reordered = MathTex(
            # r"=",
            r"\sqrt{t^2}",
            r"\sqrt{x^2 + y^2}",
            color=light_purple
        ).move_to(factored)

        self.play(
            TransformMatchingTex(factored, reordered)
        )
        self.wait(2)

        # -----------------------------------
        # STEP 6: t^2 leaves sqrt and becomes |t|
        # -----------------------------------
        final = MathTex(
            # r"=",
            r"|t|",
            r"\sqrt{x^2 + y^2}",
            color=light_purple
        ).move_to(reordered)

        self.play(
            TransformMatchingTex(reordered, final)
        )
        self.wait(2)
        final[1].set_color(light_orange)
        self.wait(2)
        length_text = MathTex(r"\text{length}",color=light_orange
        ).next_to(final[0],RIGHT)
        self.play(
            ReplacementTransform(final[1],length_text)
        )
        self.wait(1)

        arrow_0_0_up = CurvedArrow(
            start_point=text_3_part1.get_corner(DR)+0.1*UP+0.6*RIGHT,
            end_point=text_3_part2.get_corner(UR)+0.1*DOWN+0.6*RIGHT,
            angle=-PI/2,
            color=light_pink,
        )
        self.play(
            Create(arrow_0_0_up),
        )
        self.play(
            Write(text_3_part2),
        )
        text_3_part2_2 = MathTex(r"|t| \cdot ",r"\text{length}",color=dark_pink
        ).scale(1.3).to_edge(LEFT).shift(RIGHT+0.6*DOWN)
        self.play(
            FadeTransform(text_3_part2,text_3_part2_2),
        )
        self.wait(2)

        self.play(
            FadeOut(final[:2]),
            FadeOut(length_text),
            # FadeOut(text_3_formula_2[0]),
            FadeOut(note_text),
        )

        lambda_text = MathTex("|t| < 1",color=BLACK).scale(1.6).move_to(text_3_part2.get_center()+2*DOWN+LEFT)
        self.play(
            Write(lambda_text)
        )
        vector_lower = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(3,2),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        VECTOR_COPY = vector.copy()

        self.play(
            Transform(vector, vector_lower)
        )

        self.wait(1)

        self.play(
            Transform(vector, VECTOR_COPY)
        )

        self.wait(1)

        # | lambda | > 1

        lambda_text_2 = MathTex("|t| > 1",color=BLACK).scale(1.6).move_to(text_3_part2.get_center()+2*DOWN+LEFT)
        self.play(
            Unwrite(lambda_text),
            Write(lambda_text_2)
        )
        vector_higher = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(7.5,5),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            Transform(vector, vector_higher)
        )

        self.wait(1)

        self.play(
            Transform(vector, VECTOR_COPY)
        )

        self.wait(1)

        # lambda < 0 (negative)

        lambda_text_3 = MathTex("t < 0",color=BLACK).scale(1.6).move_to(text_3_part2.get_center()+2*DOWN+LEFT)
        self.play(
            Unwrite(lambda_text_2),
            Write(lambda_text_3)
        )

        vector_higher = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(-6,-4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            Transform(vector, vector_higher)
        )
        self.wait(1)

        self.play(
            Transform(vector, VECTOR_COPY)
        )

        self.wait(2)

        self.play(
            FadeOut(text_3_part1),
            FadeOut(text_3_part2_2),
            FadeOut(lambda_text_3),
            FadeOut(arrow_0_0_up),
            FadeOut(tip_text),
        )
        
        # 4

        text_4 = MathTex(r"\text{Triangle Inequality}",color=dark_pink
        ).scale(1.3).to_edge(LEFT).shift(RIGHT+1.7*UP)

        self.play(
            Write(text_4),
        )
        self.wait(2)

        vector_rule3_1 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(2,3),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_x = MathTex(r"\vec{a}").set_color(BLACK).move_to(vector_rule3_1.get_center()+0.4*UP)

        vector_rule3_2 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(4,1),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_y = MathTex(r"\vec{b}").set_color(BLACK).move_to(vector_rule3_2.get_center()+0.3*DOWN)

        self.play(
            # ,
            FadeOut(tip),
            FadeOut(vector),
            GrowArrow(vector_rule3_1, run_time=1.0, rate_func=rush_from),
            Write(text_x),
            GrowArrow(vector_rule3_2, run_time=1.0, rate_func=rush_from),
            Write(text_y),
            # run_time=1.0
        )
        self.wait(2)

        dot_arrow_1 =  DashedLine(
            start=axes.c2p(2,3),
            end=axes.c2p(6,4), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_green,
        )

        dot_arrow_2 =  DashedLine(
            start=axes.c2p(4,1),
            end=axes.c2p(6,4), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_red,
        )

        self.play(
            Create(dot_arrow_1),
            Create(dot_arrow_2),
            FadeIn(tip)
        )
        self.wait(2)

        vector_rule3_3 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=BLACK,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        text_x_plus_y = MathTex(r"\vec{a} + \vec{b}").set_color(BLACK).move_to(vector_rule3_3.get_center()+0.47*UP)
        self.play(
            GrowArrow(vector_rule3_3, run_time=1.0, rate_func=rush_from),
            Write(text_x_plus_y),
        )

        self.wait(2)

        self.play(
            # FadeOut(plane),
            FadeOut(axes),
            FadeOut(dot_arrow_1),
            FadeOut(dot_arrow_2),
            # FadeOut(text_x_plus_y),
            # FadeOut(text_x),
            # FadeOut(text_y),
            FadeOut(tip),
        )
        self.wait(4)

        text_x.shift(0.7*RIGHT+0.4*DOWN)
        vector_rule3_1_group = VGroup(vector_rule3_1,text_x)
        self.play(
            vector_rule3_1_group.animate.move_to(dot_arrow_2.get_center()),
            run_time=2
        )
        self.wait(2)

        triangle = Polygon(
            vector_rule3_1.get_end(),
            vector_rule3_2.get_end(),
            vector_rule3_3.get_start(),
        )

        triangle.set_stroke(color=dark_orange, width=7)
        triangle.set_fill(light_orange, opacity=0.3)

        self.play(
            DrawBorderThenFill(triangle,2),
            run_time=1
        )
        self.wait(3)

        self.play(
            triangle.animate.set_opacity(0),
            run_time=0.5
        )

        self.wait(2)

        self.play(
            FadeOut(triangle),
            FadeOut(text_x_plus_y),
            FadeOut(text_x),
            FadeOut(text_y),
        )

        vectors_for_transform = VGroup(vector_rule3_1, vector_rule3_2)
        vector_merged = vector.copy().set_color(dark_red)
        vector_merged.shift(0.5*UP+0.1*LEFT).scale(( vector_rule3_1.get_length() + vector_rule3_2.get_length() )/( vector.get_length() ))

        text_1 = MathTex(r" \text{length } (\vec{a} + \vec{b}) ").set_color(BLACK).move_to(vector.get_center()+0.7*DOWN+0.5*RIGHT)
        text_2 = MathTex(r" \text{length } \vec{a} + \text{length } \vec{b} ").set_color(BLACK).move_to(vector_merged.get_center()+0.7*UP+1.2*LEFT)

        self.wait(3)

        self.play(
            FadeTransform(vectors_for_transform, vector_merged),
            FadeIn(text_1),
            FadeIn(text_2),
        )

        self.wait(3)

        vector.set_color(BLACK)
        self.play(
            # FadeOut(plane),
            FadeOut(text_2),
            FadeOut(text_1),
            FadeOut(vector_rule3_3),
            FadeOut(vector),
            FadeOut(vector_merged),
            FadeOut(text_4),
        )

        return plane,axes,norm2_2d

    def scene4_subScene1(self,title,plane,axes,norm2_def):

        self.play(
            # Create(plane),
            FadeOut(norm2_def),
            Create(axes),
            norm2_def.animate.to_edge(UL).shift(0.8*RIGHT),
            run_time=2
        )

        # norm2_def_Euclidean = MathTex(r"\text{length}_{\text{Euclidean}} \text{  }",color=BLACK
        # ).move_to(norm2_def[0].get_center()+0.2*LEFT)

        # self.play(
        #     ReplacementTransform(norm2_def[0],norm2_def_Euclidean),
        #     run_time=2
        # )
        self.wait(2)

        # 1

        manhatan_arrow = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,6),
            buff=0,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_x = MathTex(r"\vec{x}").set_color(BLACK).move_to(manhatan_arrow.get_center()+0.4*UP)

        self.play(
            GrowArrow(manhatan_arrow, run_time=1.0, rate_func=rush_from),
            Write(text_x),
            run_time=1
        )
        self.wait(2)

        dot_arrow_x =  DashedLine(
            start=axes.c2p(0,0),
            end=axes.c2p(6,0), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_green,
            stroke_width=10,
        )
        text_dot_x = MathTex(r"x_1").set_color(BLACK).move_to(dot_arrow_x.get_center()+0.4*DOWN)

        dot_arrow_y =  DashedLine(
            start=axes.c2p(6,0),
            end=axes.c2p(6,6), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_red,
            stroke_width=10,
        )
        text_dot_y = MathTex(r"x_2").set_color(BLACK).move_to(dot_arrow_y.get_center()+0.4*RIGHT)

        sum_norm_text = MathTex(r"x_1 + x_2",color=BLACK
        ).move_to(text_x.get_center()+0.7*LEFT)

        self.wait(2)
        tip_start = Dot(axes.c2p(0,0), color=dark_red, radius=0.1)
        self.play(FadeIn(tip_start))
        self.wait(1)
        
        tip_end = Dot(axes.c2p(6,6), color=dark_red, radius=0.1)
        self.play(FadeIn(tip_end))
        self.wait(1)


        self.play(
            Create(dot_arrow_x),
            Write(text_dot_x),
        )
        self.wait(1)
        self.play(
            Create(dot_arrow_y),
            Write(text_dot_y),
        )
        self.wait(2)

        self.play(
            TransformMatchingTex(text_x, sum_norm_text),
            run_time=1
        )
        self.wait(1)
        self.play(
            FadeOut(manhatan_arrow),
            FadeOut(dot_arrow_x),
            FadeOut(text_dot_x),
            FadeOut(dot_arrow_y),
            FadeOut(text_dot_y),
            FadeOut(sum_norm_text),
            FadeOut(tip_start),
            FadeOut(tip_end),
        )

        # 2

        manhatan_arrow_2 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(-6,-4),
            buff=0,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_x = MathTex(r"\vec{x}").set_color(BLACK).move_to(manhatan_arrow_2.get_center()+0.4*DOWN)

        self.play(
            GrowArrow(manhatan_arrow_2, run_time=1.0, rate_func=rush_from),
            Write(text_x),
            run_time=1
        )
        self.wait(2)

        dot_arrow_x =  DashedLine(
            start=axes.c2p(0,0),
            end=axes.c2p(-6,0), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_green,
            stroke_width=10,
        )
        text_dot_x = MathTex(r"x_1").set_color(BLACK).move_to(dot_arrow_x.get_center()+0.4*UP)

        dot_arrow_y =  DashedLine(
            start=axes.c2p(-6,0),
            end=axes.c2p(-6,-4), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_red,
            stroke_width=10,
        )
        text_dot_y = MathTex(r"x_2").set_color(BLACK).move_to(dot_arrow_y.get_center()+0.4*LEFT)

        sum_norm_text = MathTex(r"|x_1| + |x_2|",color=BLACK
        ).move_to(text_x.get_center()+0.7*RIGHT)

        self.wait(2)
        tip_start = Dot(axes.c2p(0,0), color=dark_red, radius=0.1)
        self.play(FadeIn(tip_start))
        self.wait(1)
        
        tip_end = Dot(axes.c2p(-6,-4), color=dark_red, radius=0.1)
        self.play(FadeIn(tip_end))
        self.wait(1)


        self.play(
            Create(dot_arrow_x),
            Write(text_dot_x),
        )
        self.wait(1)
        self.play(
            Create(dot_arrow_y),
            Write(text_dot_y),
        )
        self.wait(2)

        self.play(
            TransformMatchingTex(text_x, sum_norm_text),
            run_time=1
        )
        self.wait(1)

        # num example
        text_num_x = MathTex(r"-4",color=dark_pink).move_to(text_dot_x.get_center())
        text_num_y = MathTex(r"-3",color=dark_pink).move_to(text_dot_y.get_center()+0.1*LEFT)
        text_length_vector_1 = MathTex(r"|-4| + |-3|",color=dark_pink).move_to(manhatan_arrow_2.get_center()+1.7*RIGHT)
        text_length_vector_2part0 = MathTex(r"4 + 3",color=dark_pink).move_to(manhatan_arrow_2.get_center()+1*RIGHT)
        text_length_vector_2part1 = MathTex(r"7",color=dark_pink).move_to(text_length_vector_2part0.get_center())
        self.play(
            FadeOut(text_dot_x),
            FadeIn(text_num_x)
        )
        self.wait(0.5)
        self.play(
            FadeOut(text_dot_y),
            FadeIn(text_num_y)
        )
        self.wait(0.5)
        self.play(
            FadeTransform(sum_norm_text,text_length_vector_1),
        )
        self.wait(1)
        self.play(
            FadeTransform(text_length_vector_1,text_length_vector_2part0),
        )
        self.wait(0.7)
        self.play(
            FadeTransform(text_length_vector_2part0,text_length_vector_2part1),
        )
        self.wait(1)
       
        self.play(
            FadeOut(text_num_x),
            FadeIn(text_dot_x),
            FadeOut(text_num_y),
            FadeIn(text_dot_y),
            FadeOut(text_length_vector_2part1),
        )
        self.wait(1)


        norm1_2d = MathTex(
            r"\text{length}_{\text{Manhattan}}",r"= ",r"|x_1| + |x_2|",color=BLACK
        ).next_to(norm2_def,DOWN).shift(0.3*RIGHT)
        self.play(
            Write(norm1_2d),
        )
        self.wait(10)

        self.play(
            FadeOut(tip_start),
            FadeOut(tip_end),
        )

        self.play(
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(manhatan_arrow_2),
            # FadeOut(sum_norm_text),
            FadeOut(dot_arrow_x),
            FadeOut(text_dot_x),
            FadeOut(dot_arrow_y),
            FadeOut(text_dot_y),
            FadeOut(norm1_2d),
            # FadeOut(norm2_def[1:]),
            # FadeOut(norm2_def_Euclidean),
        )
        self.wait(1)

    def scene4_subScene2(self,title):
        "scene4 : subScene2 : norm definition"
        
        question_tex = MathTex("\\text{ What happens if we try to generalize this ? }").set_color(BLACK)
        question_group, question_box, image_1, image_2 = self.ask_question(question_tex,True,True)

        group_GroupBoxQuetion = VGroup(question_group,question_box)
        group_GroupBoxQuetion.shift(1.5*UP)
        image_1.scale(1.2).shift(3.5*DOWN)
        self.add(image_1)
        self.play(
            FadeIn(group_GroupBoxQuetion)
        )
        self.wait(3)

        def_norm_line1 = MathTex(
            r"\text{A norm on } X \text{ is a function }",
            r"\|\cdot\| : X \to \mathbb{R}"
        ).set_color(BLACK)

        def_norm_line2 = MathTex(
            r"\text{satisfying}"
        ).set_color(BLACK)

        # def_norm_line3 = MathTex(
        #     r"\begin{aligned}",
        #     # r"1.& \quad \|x\| \ge 0 \\"
        #     r"1.& \quad \|x\| = 0 \iff x = 0 \\",
        #     r"2.& \quad \|\lambda x\| = |\lambda| \, \|x\| \\",
        #     r"3.& \quad \|x + y\| \le \|x\| + \|y\|",
        #     r"\end{aligned}"
        # ).set_color(BLACK).scale(0.85)

        line1_3 = MathTex(r"1.\quad \|x\| = 0 \iff x = 0")
        line2_3 = MathTex(r"2.\quad \|\lambda x\| = |\lambda| \, \|x\|")
        line3_3 = MathTex(r"3.\quad \|x + y\| \le \|x\| + \|y\|")
        def_norm_line3 = VGroup(line1_3, line2_3, line3_3).arrange(DOWN, aligned_edge=LEFT, buff=0.4).set_color(BLACK).scale(0.9)

        def_norm_line4 = MathTex(r"\quad \text{for all } x,y \in X \text{ and } \lambda \in \mathbb{K}.").set_color(BLACK)

        def_norm = VGroup(def_norm_line1, def_norm_line2, def_norm_line3,def_norm_line4).arrange(DOWN, buff=0.3).scale(0.9)

        def_norm.next_to(title.get_center(), DOWN)

        norm_group, norm_box = self.show_definition(def_norm, title,True)
        norm_group.shift(1.5*UP)
        norm_box.move_to(norm_group.get_center())
        norm_box_and_text_group = VGroup(norm_group,norm_box)
        norm_box_and_text_group.scale(1.2)

        # norm title
        norm_title = MathTex(r"\text{NORM}", color=BLACK, font_size=80).move_to(title.get_center())
        
        self.play(
            TransformMatchingShapes(group_GroupBoxQuetion, norm_box), 
            Write(norm_title),
            FadeOut(image_1),
            # FadeOut(image_2),
            Write(norm_group),
            run_time=1
        )
        image_2.shift(9*LEFT)
        self.add(image_2)

        self.wait(5)
        for line in [line1_3, line2_3, line3_3]:
            rect = SurroundingRectangle(
                line,
                color=dark_red,      
                buff=0.2,  
                fill_opacity=0,
                stroke_width=3,
                corner_radius=0.15,
            )
            self.play(
                Create(rect), 
                run_time=1
            )
            self.wait(5)
            self.play(
                Uncreate(rect), 
                run_time=1
            )

        self.wait(3)
        
        self.play(
            Uncreate(norm_box),
            FadeOut(norm_group),
            FadeOut(image_2),
        )

        return norm_group, norm_box, question_group, question_box, norm_title

    def scene4_subScene1_part2(self,title,):
        point_text = MathTex(r"\vec{x} = (x_1,x_2)",color=BLACK).move_to(title.get_center()+0.5*DOWN)

        norm1 = MathTex(r"\text{length }_{\text{Manhattan} }(\vec{x})",r" = |x_1| + |x_2|",color=dark_orange).scale(1.5).move_to(point_text.get_center()+1*DOWN)
        norm1_2 = MathTex(r"\text{length }_{\text{Manhattan} }(\vec{x})",r" = |x_1|^1 + |x_2|^1",color=dark_orange).scale(1.5).move_to(norm1.get_center())
        norm1_3 = MathTex(r"\text{length }_{\text{Manhattan} }(\vec{x})",r" = (|x_1|^1 + |x_2|^1)^\frac{1}{1} ",color=dark_orange).scale(1.5).move_to(norm1_2.get_center())
        norm1_3_compare = MathTex(
            r"\text{length }_{\text{Manhattan}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^1",
            r"+",
            r"|x_2|", r"^1",
            r")^{", r"\frac{1}{1}", r"}",
            color=dark_orange,
        ).scale(1.5).move_to(norm1_2.get_center())
        common_color = dark_green
        norm1_3_compare.set_color_by_tex("|x_1|", common_color)
        norm1_3_compare.set_color_by_tex("|x_2|", common_color)
        norm1_3_compare.set_color_by_tex("+", common_color)
        norm1_3_compare.set_color_by_tex("(", common_color)
        norm1_3_compare.set_color_by_tex(")", common_color)
        # norm1_3_compare.set_color_by_tex("}", common_color)

        norm2 = MathTex(r"\text{length }_{\text{Euclid} }(\vec{x})",r" = \sqrt{x_1^2 + x_2^2 }",color=dark_pink).scale(1.2).move_to(norm1_3.get_center()+1.2*DOWN)  #Pythagoras
        norm2_2 = MathTex(r"\text{length }_{\text{Euclid} }(\vec{x})",r" = \sqrt{|x_1|^2 + |x_2|^2 }",color=dark_pink).scale(1.5).move_to(norm2.get_center())
        norm2_3 = MathTex(r"\text{length }_{\text{Euclid} }(\vec{x})",r" = (|x_1|^2 + |x_2|^2)^\frac{1}{2} ",color=dark_pink).scale(1.5).move_to(norm2_2.get_center())
        norm2_3_compare = MathTex(
            r"\text{length }_{\text{Euclid}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^2",
            r"+",
            r"|x_2|", r"^2",
            r")^{", r"\frac{1}{2}", r"}",
            color=dark_pink,
        ).scale(1.5).move_to(norm2_2.get_center())
        common_color = dark_green
        norm2_3_compare.set_color_by_tex("|x_1|", common_color)
        norm2_3_compare.set_color_by_tex("|x_2|", common_color)
        norm2_3_compare.set_color_by_tex("+", common_color)
        norm2_3_compare.set_color_by_tex("(", common_color)
        norm2_3_compare.set_color_by_tex(")", common_color)
        # norm2_3_compare.set_color_by_tex("}", common_color)

        norm3 = MathTex(
            r"\text{length }_{\text{?}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^3",
            r"+",
            r"|x_2|", r"^3",
            r")^{", r"\frac{1}{3}", r"}",
            color=dark_red,
        ).scale(1.5).move_to(norm2_3_compare.get_center()+1*DOWN+1*RIGHT)
        common_color = dark_green
        norm3.set_color_by_tex("|x_1|", common_color)
        norm3.set_color_by_tex("|x_2|", common_color)
        norm3.set_color_by_tex("+", common_color)
        norm3.set_color_by_tex("(", common_color)
        norm3.set_color_by_tex(")", common_color)

        norm4 = MathTex(
            r"\text{length }_{\text{?}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^4",
            r"+",
            r"|x_2|", r"^4",
            r")^{", r"\frac{1}{4}", r"}",
            color=dark_red,
        ).scale(1.5).move_to(norm2_3_compare.get_center()+1*DOWN+1*RIGHT)
        common_color = dark_green
        norm4.set_color_by_tex("|x_1|", common_color)
        norm4.set_color_by_tex("|x_2|", common_color)
        norm4.set_color_by_tex("+", common_color)
        norm4.set_color_by_tex("(", common_color)
        norm4.set_color_by_tex(")", common_color)

        # normp = MathTex(r"\text{length }_{\text{p} }(\vec{x})",r" = (|x_1|^p + |x_2|^p)^\frac{1}{p} ",color=dark_red).scale(1.5).move_to(norm2_3.get_center()+1*DOWN)
        normp = MathTex(
            r"\text{length }_{\text{p}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^p",
            r"+",
            r"|x_2|", r"^p",
            r")^{", r"\frac{1}{p}", r"}",
            color=dark_red,
        ).scale(1.5).move_to(norm2_3_compare.get_center()+1*DOWN+1*RIGHT)
        common_color = dark_green
        normp.set_color_by_tex("|x_1|", common_color)
        normp.set_color_by_tex("|x_2|", common_color)
        normp.set_color_by_tex("+", common_color)
        normp.set_color_by_tex("(", common_color)
        normp.set_color_by_tex(")", common_color)
        
        self.play(
            Write(point_text),
        )
        self.wait(2)
        self.play(
            Write(norm1),
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(norm1,norm1_2),
            run_time=0.5
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(norm1_2,norm1_3),
            run_time=0.5
        )
        self.wait(2)

        self.play(
            Write(norm2),
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(norm2,norm2_2),
            run_time=0.5
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(norm2_2,norm2_3),
            run_time=0.5
        )
        self.wait(2)

        self.play(
            TransformMatchingTex(norm1_3,norm1_3_compare),
            TransformMatchingTex(norm2_3,norm2_3_compare),
            run_time=1
        )
        self.wait(2)

        image_think = ImageMobject("images/think_img.png").scale(2).to_edge(DL).shift(3.5*LEFT+1.1*DOWN)
        self.add(image_think)
        self.wait(2)

        self.play(
            Write(norm3),
        )
        self.wait(4)
        self.play(
            TransformMatchingTex(norm3,norm4),
        )
        self.wait(4)

        find_img = ImageMobject("images/find_img.png").scale(2).to_edge(DL).shift(3.5*LEFT+1.3*DOWN)
        self.play(
            FadeOut(image_think),
        )
        self.add(find_img)
        self.wait(1)

        self.play(
            # find_img.animate.scale(0.7).shift(0.5*DOWN),
            TransformMatchingTex(norm4,normp),
            run_time=1
        )
        self.wait(2)

        p_ge_1 = MathTex(r"p \ge 1",color=BLACK)
        text_group,box = self.show_minorPoint(p_ge_1,True)
        text_group.move_to(normp.get_center()+2*DOWN+RIGHT)
        box.move_to(text_group.get_center())
        self.play(
            Create(box),
            Write(text_group),
        )
        self.wait(3)

        self.play(
            FadeOut(text_group),
            FadeOut(box),
            FadeOut(find_img),
            FadeOut(normp),
            FadeOut(norm1_3_compare),
            FadeOut(norm2_3_compare),
            FadeOut(point_text),
            # FadeOut(),
        )
        self.wait(1)

    def scene4_subScene3(self, title):
        # draw number plane as background
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]+DOWN)
        self.play(Create(plane))
        self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 7, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # dot at tip of vector
        tip = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        self.play(FadeIn(tip))

        # draw vector in (0,0)
        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(GrowArrow(vector, run_time=1.2, rate_func=rush_from))
        self.wait(0.5)

        # draw brace
        brace = BraceBetweenPoints(vector.get_start()+ UP*0.2, vector.get_end() + UP*0.2, rotate_vector(vector.get_unit_vector(), PI/2) ).set_color("#000000")
        self.play(GrowFromCenter(brace, run_time=0.8))
        self.wait(0.5)

        # add norm text
        norm_text = brace.get_text("Norm").set_color(BLACK)
        self.play(FadeIn(norm_text, shift=UP*0.2))
        self.wait(0.5)

        # add "= Vector Length" and "= distance to the origin"
        vector_dis_text = MathTex(" \\text{ distance to the origin } = ").set_color(BLACK)
        vector_dis_text.next_to(norm_text, LEFT, buff=0.3)
        self.play(FadeIn(vector_dis_text))  #  norm_text.animate.shift(UP*0.2), 
        self.wait(1)

        vector_length_text = MathTex(" \\text{Vector Length} = ").set_color(BLACK)
        vector_length_text.next_to(norm_text, LEFT, buff=0.3)
        self.play(TransformMatchingTex(vector_dis_text, vector_length_text))
        self.wait(1)

        # group texts
        norm_text_group = VGroup(norm_text, vector_length_text)

        self.play(
            FadeOut(norm_text_group),
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(tip),
            FadeOut(vector),
            FadeOut(brace),
        )
        self.wait(2)

        # blink effect
        # for _ in range(2):
        #     self.play(
        #         norm_text_group.animate.scale(1.5).set_color(dark_red),
        #         brace.animate.set_color(dark_red),
        #         rate_func=there_and_back,
        #         run_time=0.5
        #     )
        # 
        # self.wait(1)
        
        # vecor_name = MathTex("\\text{ x }").set_color(BLACK).move_to(norm_text.get_center())

        # self.play(
        #     TransformMatchingTex(norm_text_group,vecor_name)
        # )
        # self.wait(2)

        # rule1_text = MathTex("\quad \|x\| = 0 \iff x = 0").set_color(BLACK).scale(0.9)
        # rule2_text = MathTex("\quad \|\lambda x\| = |\lambda| \, \|x\|").set_color(BLACK).scale(0.9)
        # rule3_text = MathTex("\quad \|x + y\| \le \|x\| + \|y\|").set_color(BLACK).scale(0.9)

        # rule1_text.move_to(plane.get_edge_center(DOWN) + 1*RIGHT + 1*UP)
        # rule2_text.move_to(plane.get_edge_center(DOWN) + 1*RIGHT + 1*UP)
        # rule3_text.move_to(plane.get_edge_center(DOWN) + 1*RIGHT + 1*UP)

        # RULE 1
        # self.play(
        #     Write(rule1_text),
        #     FadeOut(brace),
        #     FadeOut(vecor_name),
        #     FadeOut(vector),
        #     tip.animate.move_to(axes.c2p(0,0)),
        #     run_time=1.0
        # )

        # self.wait(2)

        # RULE 2
        # self.play(
        #     TransformMatchingTex(rule1_text, rule2_text),
        #     tip.animate.move_to(axes.c2p(6,4)),
        #     GrowArrow(vector, run_time=1.0, rate_func=rush_from),
        #     run_time=1.0
        # )
        # self.wait(1)

        # # | lambda | < 1

        # lambda_text = MathTex("|\lambda| < 1",color=BLACK).scale(2).move_to(axes.get_center()+1*UP+3*LEFT)
        # self.play(
        #     Write(lambda_text)
        # )
        # vector_lower = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(3,2),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # VECTOR_COPY = vector.copy()

        # self.play(
        #     Transform(vector, vector_lower)
        # )

        # self.wait(1)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # # | lambda | > 1

        # lambda_text_2 = MathTex("|\lambda| > 1",color=BLACK).scale(2).move_to(axes.get_center()+1*UP+3*LEFT)
        # self.play(
        #     Unwrite(lambda_text),
        #     Write(lambda_text_2)
        # )
        # vector_higher = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(7.5,5),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Transform(vector, vector_higher)
        # )

        # self.wait(1)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # # lambda < 0 (negative)

        # lambda_text_3 = MathTex("\lambda < 0",color=BLACK).scale(2).move_to(axes.get_center()+1*UP+3*LEFT)
        # self.play(
        #     Unwrite(lambda_text_2),
        #     Write(lambda_text_3)
        # )

        # vector_higher = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(-3,-2),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Transform(vector, vector_higher)
        # )

        # self.wait(1)

        # self.play(
        #     Transform(vector, VECTOR_COPY),
        #     Unwrite(lambda_text_3)
        # )


        # # RULE 3

        # vector_rule3_1 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(2,3),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_red,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_x = MathTex("\\text{ x }").set_color(BLACK).move_to(vector_rule3_1.get_center()+0.4*UP)

        # vector_rule3_2 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(4,1),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_y = MathTex("\\text{ y }").set_color(BLACK).next_to(vector_rule3_2, 0.35*DOWN, 0.1)

        # self.play(
        #     TransformMatchingTex(rule2_text, rule3_text),
        #     FadeOut(tip),
        #     FadeOut(vector),
        #     # FadeOut(vector_lower),
        #     # FadeOut(vector_higher),
        #     GrowArrow(vector_rule3_1, run_time=1.0, rate_func=rush_from),
        #     Write(text_x),
        #     GrowArrow(vector_rule3_2, run_time=1.0, rate_func=rush_from),
        #     Write(text_y),
        #     # run_time=1.0
        # )
        # self.wait(2)

        # dot_arrow_1 =  DashedLine(
        #     start=axes.c2p(2,3),
        #     end=axes.c2p(6,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_green,
        # )

        # dot_arrow_2 =  DashedLine(
        #     start=axes.c2p(4,1),
        #     end=axes.c2p(6,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_red,
        # )

        # self.play(
        #     Create(dot_arrow_1),
        #     Create(dot_arrow_2),
        #     FadeIn(tip)
        # )
        # self.wait(2)

        # vector_rule3_3 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,4),
        #     buff=0,
        #     stroke_width=6,
        #     color=BLACK,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # text_x_plus_y = MathTex("\\text{ x + y }").set_color(BLACK).move_to(vector_rule3_3.get_center()+0.4*UP)
        # self.play(
        #     GrowArrow(vector_rule3_3, run_time=1.0, rate_func=rush_from),
        #     Write(text_x_plus_y),
        # )

        # self.wait(2)

        # self.play(
        #     FadeOut(plane),
        #     FadeOut(axes),
        #     FadeOut(dot_arrow_1),
        #     FadeOut(dot_arrow_2),
        #     FadeOut(text_x_plus_y),
        #     FadeOut(text_x),
        #     FadeOut(text_y),
        #     FadeOut(tip),
        # )

        # vectors_for_transform = VGroup(vector_rule3_1, vector_rule3_2)
        # vector_merged = vector.copy().set_color(dark_red)
        # vector_merged.shift(0.5*UP+0.1*LEFT).scale(( vector_rule3_1.get_length() + vector_rule3_2.get_length() )/( vector.get_length() ))

        # text_1 = MathTex(" \|x + y\| ").set_color(BLACK).move_to(vector.get_center()+0.7*DOWN)
        # text_2 = MathTex(" \|x\| + \|y\| ").set_color(BLACK).move_to(vector_merged.get_center()+0.7*UP)

        # self.wait(0.7)

        # self.play(
        #     FadeTransform(vectors_for_transform, vector_merged),
        #     FadeIn(text_1),
        #     FadeIn(text_2),
        # )

        # self.wait(1)

        # vector.set_color(BLACK)
        # self.play(
        #     FadeOut(rule3_text),
        #     FadeOut(text_2),
        #     FadeOut(text_1),
        #     FadeOut(vector_rule3_3),
        #     FadeOut(vector),
        #     FadeOut(vector_merged),
        # )

    def scene4_subScene4(self,title):
        """scene 4 : sub scene 4 : prove and show ||x|| >= 0 """
        prove_text = MathTex("\|x\| \ge 0",color=BLACK).scale(1.3)
        text_group,box = self.show_conclusion(title, prove_text,True)
        self.play(
            Create(box),
            Write(text_group)
        )
        self.wait(2)

        conclusion_group = VGroup(text_group,box)
        self.play(
            conclusion_group.animate.shift(1.75*UP + 4.5*LEFT),
            run_time=1
        )

        # write proof
        proof_line1 = MathTex("\|x + y\| ","\le \|x\| + ","\|y\|",color=BLACK).scale(1.5).move_to(title.get_center()+0.9*DOWN+2*RIGHT)
        self.play(
            Write(proof_line1),
        )
        self.wait(1)

        variable_replacement = MathTex("y = -x",color=BLACK).scale(1.7).move_to(prove_text.get_center()+2*DOWN)
        self.play(
            Write(variable_replacement),
        )
        self.wait(1)
        proof_line1_variable_changed = MathTex("\|x + -x\| ","\le \|x\| + ","\|-x\|",color=BLACK).scale(1.5).move_to(title.get_center()+0.9*DOWN+2*RIGHT)
        self.play(
            TransformMatchingTex(proof_line1, proof_line1_variable_changed),
        )
        self.wait(1)

        part1_brace = Brace(proof_line1_variable_changed[0],DOWN,color=dark_orange)
        self.play(
            GrowFromCenter(part1_brace, run_time=0.8),
        )
        proof_line2_part1_initial = MathTex("\|0\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[0].get_center()+1.5*DOWN)
        self.play(
            Write(proof_line2_part1_initial),
        )
        self.wait(1)
        proof_line2_part1 = MathTex("0",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[0].get_center()+1.5*DOWN)
        self.play(
            FadeTransform(proof_line2_part1_initial,proof_line2_part1),
        )
        self.wait(1)

        part2_brace = Brace(proof_line1_variable_changed[2],DOWN,color=dark_orange)
        self.play(
            GrowFromCenter(part2_brace, run_time=0.8),
        )
        proof_line2_part2_initial = MathTex("|-1| \, \|x\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[2].get_center()+1.5*DOWN+0.2*RIGHT)
        self.play(
            Write(proof_line2_part2_initial),
        )
        self.wait(1)

        proof_line2_part3 = proof_line1_variable_changed[1].copy()
        self.play(
            proof_line2_part3.animate.shift(1.5*DOWN),
            run_time=1
        )

        proof_line2_part2 = MathTex("\|x\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[2].get_center()+1.5*DOWN)
        self.play(
            FadeTransform(proof_line2_part2_initial, proof_line2_part2),
        )
        proof_line2 = VGroup(proof_line2_part1, proof_line2_part3, proof_line2_part2)

        proof_line3 = MathTex("0 \le 2 \, \|x\|",color=BLACK).scale(1.5).move_to(proof_line2.get_center()+1.5*DOWN)
        self.play( 
            Write(proof_line3),
        )
        self.wait(1)

        proof_line4 = MathTex("0 \le \|x\|",color=BLACK).scale(1.5).move_to(proof_line3.get_center()+1.5*DOWN)
        square_for_end_proof = Square(0.5,color=BLACK).next_to(proof_line4,RIGHT)
        self.play( 
            Write(proof_line4),
        )

        self.wait(1)

        self.play(
            Create(square_for_end_proof),
        )

        self.wait(1)

        self.play(
            FadeOut(proof_line1_variable_changed),
            FadeOut(variable_replacement),
            FadeOut(part1_brace),
            FadeOut(part2_brace),
            FadeOut(proof_line2),
            FadeOut(proof_line3),
            FadeOut(proof_line4),
            FadeOut(square_for_end_proof),
        )

        # create shapes for better understanding
        
        # draw number plane as background
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]+DOWN+RIGHT)
        self.play(Create(plane))
        self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 7, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN+RIGHT)
        self.play(Create(axes))
        self.wait(0.5)

        # dot at tip of vector
        tip = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        self.play(FadeIn(tip))

        # draw vector in (0,0)
        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(GrowArrow(vector, run_time=1.2, rate_func=rush_from))
        self.wait(0.5)

        # draw brace
        brace = BraceBetweenPoints(vector.get_start()+ UP*0.2, vector.get_end() + UP*0.2, rotate_vector(vector.get_unit_vector(), PI/2) ).set_color("#000000")
        self.play(GrowFromCenter(brace, run_time=0.8))
        self.wait(0.5)

        # add norm text
        norm_text = brace.get_text("Norm").set_color(BLACK)
        self.play(FadeIn(norm_text, shift=UP*0.2))
        self.wait(0.5)

        # add "= Vector Length"
        vector_length_text = MathTex(" \\text{Vector Length} = ").set_color(BLACK)
        vector_length_text.next_to(norm_text, LEFT, buff=0.3)
        self.play(FadeIn(vector_length_text))
        self.wait(1)

        vector_group = VGroup(tip,vector,brace,norm_text,vector_length_text)

        vector_group.save_state()

        self.play(
            vector_group.animate.scale(0.01, about_point=axes.c2p(0,0)),
            run_time=3
        )
        self.play(
            Restore(vector_group),
            run_time=3
        )
        
        self.wait(2)

        self.play(
            FadeOut(vector_group),
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(conclusion_group),
            # FadeOut(),
            # FadeOut(),
            # FadeOut(),
            # FadeOut(),
        )

    def scene4_subScene5(self,title):
        """scene 4: sub scene 5 : examples of norm"""

        # unit ball idea
        # nothing for now

        brain_img = ImageMobject("images/graduate_brain_img_mini.png").scale(2).to_corner(DL)
        self.add(brain_img)

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-5, 4, 1],
            x_range=[-4, 7, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]+2*DOWN+2*RIGHT)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-5, 4, 1],
            y_length=6,
            x_range=[-4, 7, 1],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+2*DOWN+2*RIGHT)

        # example of norm

        vector_def = MathTex(
            r"\text{Let } \vec{x} = (x_1, \dots, x_n) \in \mathbb{R}^n.",color=BLACK
        ).to_corner(UL).shift(0.1*RIGHT+0.8*DOWN)

        # norm p
        normp_title = MathTex("p-Norm", color=dark_orange).next_to(vector_def,DOWN).shift(0.7*LEFT)

        normp_full_form = MathTex(
            r"\|\vec{x}\|_", r"p",
            r":=",
            r"(",
            r"|x_1|^", r"p",
            r"+",
            r"|x_2|^", r"p",
            r"+ \dots +",
            r"|x_n|^", r"p",
            r")^{\frac{1}{", r"p", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT).scale(1.2)

        normp_short_form = MathTex(
            r"=",
            r"\left(",
            r"\sum_{i=1}^{n} |x_i|^", r"p",
            r"\right)^{\frac{1}{", r"p", r"}}",
            color=BLACK
        ).next_to(normp_title,DOWN).shift(1.3*RIGHT+0.2*DOWN).scale(1.2)

        normp_full_form.set_color_by_tex("p", dark_pink)
        normp_short_form.set_color_by_tex("p", dark_pink)

        # norm 1
        condition_1 = Text("if p = 1", color=BLACK).move_to(normp_short_form.get_center())
        rect_1 = SurroundingRectangle(
            condition_1,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        norm1_title = MathTex("L1 Norm (Manhattan Norm)", color=dark_orange).move_to(normp_short_form.get_center()+DOWN)
        norm1_full_form = MathTex(
            r"\|\vec{x}\|_", r"\text{1}",
            r":=",
            r"(",
            r"|x_1|^", r"\text{1}",
            r"+",
            r"|x_2|^", r"\text{1}",
            r"+ \dots +",
            r"|x_n|^", r"\text{1}",
            r")^{\frac{1}{", r"\text{1}", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT).scale(1.2)
        norm1_full_form.set_color_by_tex(r"\text{1}", dark_pink)

        # norm 2
        condition_2 = Text("if p = 2", color=BLACK).move_to(normp_short_form.get_center())
        rect_2 = SurroundingRectangle(
            condition_2,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        norm2_title = MathTex("L2 Norm (Euclidean Norm)", color=dark_orange).move_to(norm1_title.get_center())
        norm2_full_form = MathTex(
            r"\|\vec{x}\|_", r"\text{2}",
            r":=",
            r"(",
            r"|x_1|^", r"\text{2}",
            r"+",
            r"|x_2|^", r"\text{2}",
            r"+ \dots +",
            r"|x_n|^", r"\text{2}",
            r")^{\frac{1}{", r"\text{2}", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT).scale(1.2)
        norm2_full_form.set_color_by_tex(r"\text{2}", dark_pink)

        # norm infinity
        condition_oo = MathTex(r"\text{if } p \to \infty", color=BLACK).scale(1.5).move_to(normp_short_form.get_center()+0.3*LEFT)
        rect_oo = SurroundingRectangle(
            condition_oo,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        normoo_title = MathTex(r"L \infty Norm (Maximum Norm)", color=dark_orange).move_to(norm1_title.get_center())
        normoo_limit = MathTex(
            r"\|\vec{x}\|_{\infty}",
            r"=",
            r"\lim_{", r"p", r"\to \infty}",
            r"\left(",
            r"\sum_{i=1}^{n}",
            r"|x_i|^", r"p",
            r"\right)^{\frac{1}{", r"p", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT+0.15*UP).scale(1.2)
        normoo_limit.set_color_by_tex("p", dark_pink)

        norm_oo_short_form = MathTex(
            r"\|\vec{x}\|_{\infty}",
            r"=",
            r"\max_{1 \le i \le n}",
            r"|x_i|",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT+0.3*UP).scale(1.2)

        # vector name 
        self.play(
            Write(vector_def)
        )
        self.wait(1)

        # norm p
        # self.play(
        #     Write(normp_title),
        # )
        # self.wait(0.6)
        self.play(
           Write(normp_full_form),
        )
        self.wait(0.6)
        self.play(
            Write(normp_short_form),
        )
        self.wait(2)
        self.play(
            Unwrite(normp_short_form),
        )
        self.wait(2)

        # norm 1
        self.play(
            Create(rect_1),
            Write(condition_1),
        )
        self.wait(1)
        self.play(
            TransformMatchingShapes(normp_full_form, norm1_full_form)
        )
        self.wait(2)

        # # create grid
        self.play(Create(plane))
        self.wait(0.5)
        self.play(Create(axes))
        self.wait(0.5)

        # norm 1 grid

        points_norm1 = [
            (3, 0),
            (0, 3),
            (-3, 0),
            (0, -3),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ]
        mid_points_norm1 = [
            (1, 0),    
            (0, 1),    
            (-1, 0),   
            (0, -1),   
            (2, 0),
            (1, 0),
            (-1, 0),    
            (-2, 0),
            (-2, 0),
            (-1, 0), 
            (1, 0),  
            (2, 0), 
        ]

        list_tip_2 = []

        for i in range(len(points_norm1)):
            point = points_norm1[i]
            mid_point = mid_points_norm1[i]

            # dot at tip of vector
            tip_2 = Dot(axes.c2p(*point), color=dark_red, radius=0.1)
            list_tip_2.append(tip_2)
            tip_1 = Dot(axes.c2p(*mid_point), color=dark_orange, radius=0.1)

            # draw vector in (0,0)
            vector_1 = Line(
                start=axes.c2p(0,0),
                end=axes.c2p(*mid_point),
                buff=0,
                stroke_width=10,
                color=dark_green,
            )

            vector_2 = Line(
                start=axes.c2p(*mid_point),
                end=axes.c2p(*point),
                buff=0,
                stroke_width=10,
                color=dark_green,
            )

            self.play(Create(vector_1),run_time=0.1) #, run_time=0.1, rate_func=rush_from
            self.play(FadeIn(tip_1),run_time=0.1)
            self.play(Create(vector_2),run_time=0.1)
            self.play(FadeIn(tip_2),run_time=0.1)

            # self.play(
            #     AnimationGroup(
            #         Create(vector_1),
            #         FadeIn(tip_1),
            #         lag_ratio=0.2
            #     )
            # )

            self.play(
                FadeOut(vector_1),
                FadeOut(tip_1),
                FadeOut(vector_2),
            )

        points_polygan = [
            axes.c2p(3, 0),
            axes.c2p(0, 3),
            axes.c2p(-3, 0),
            axes.c2p(0, -3),
        ]

        polygon = Polygon(
            *points_polygan,
            stroke_color=dark_terquise,
            stroke_width=4,
            fill_opacity=0
        )

        self.play(
            Create(polygon),
            rum_time=1
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(*list_tip_2)),
        )
        self.play(
            FadeOut(polygon),
        )

        # norm 2
        self.play(
            TransformMatchingShapes(rect_1, rect_2),
            FadeTransform(condition_1, condition_2),
        )
        self.wait(1)
        self.play(
            TransformMatchingShapes(norm1_full_form, norm2_full_form)
        )
        self.wait(2)

        # norm 2 grid

        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(2,1),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        circle_static = Circle(radius=axes.x_axis.unit_size * np.sqrt(5),color=dark_terquise).move_to(axes.c2p(0,0))

        path = TracedPath(
            vector.get_end,
            stroke_color=dark_terquise,
            stroke_width=4
        )

        self.play(
            Create(vector, run_time=1, rate_func=rush_from),
        )

        self.play(
            Rotate(
                vector,
                angle=TAU,
                about_point=axes.c2p(0,0)
            ),
            Create(path),
            Create(circle_static),
            run_time=3,
            rate_func=linear
        )

        self.wait(2)

        self.play(
            FadeOut(vector),
            FadeOut(path),
            FadeOut(circle_static),
            # FadeOut(),
        )

        self.play(
            FadeOut(vector_def),

        )

        # norm inf

        self.play(
            TransformMatchingShapes(rect_2, rect_oo),
            FadeTransform(condition_2, condition_oo),
        )
        self.wait(1)
        self.play(
            TransformMatchingShapes(norm2_full_form, normoo_limit),
        )
        self.wait(3)
        self.play(
            TransformMatchingShapes(normoo_limit, norm_oo_short_form),
        )
        self.wait(2)

        # norm inf grid

        vector_1 = Line(
            start=axes.c2p(-3,3),
            end=axes.c2p(-3,-3),
            buff=0,
            stroke_width=5,
            color=dark_green,
        )
        vector_2 = Line(
            start=axes.c2p(-3,3),
            end=axes.c2p(3,3),
            buff=0,
            stroke_width=5,
            color=dark_purple,
        )
        vector_3 = Line(
            start=axes.c2p(3,-3),
            end=axes.c2p(3,3),
            buff=0,
            stroke_width=5,
            color=dark_not_green,
        )
        vector_4 = Line(
            start=axes.c2p(3,-3),
            end=axes.c2p(-3,-3),
            buff=0,
            stroke_width=5,
            color=dark_orange,
        )

        self.play(
            Create(vector_1),
        )
        self.wait(0.5)
        self.play(
            Create(vector_2),
        )
        self.wait(0.5)
        self.play(
            Create(vector_3),
        )
        self.wait(0.5)
        self.play(
            Create(vector_4),
        )
        self.wait(1)

        squre = Polygon(
            *[axes.c2p(3,3), axes.c2p(3,-3), axes.c2p(-3,-3), axes.c2p(-3,3)],
            stroke_color=dark_terquise,
            stroke_width=4,
            fill_opacity=0
        )

        self.play(
            Create(squre),
            FadeOut(VGroup(*[vector_1, vector_2, vector_3, vector_4])),
            rum_time=1
        )
        self.wait(1)

        self.play(
            FadeOut(squre),
        )

        self.play(
            FadeOut(rect_oo),
            FadeOut(condition_oo),
            FadeOut(norm_oo_short_form),
        )

        self.wait(1)

        self.play(
            VGroup(plane, axes).animate.shift(1.5*UP+1*LEFT),
            run_time=1
        )

        circle_static = Circle(radius=axes.x_axis.unit_size * 3,color=dark_terquise).move_to(axes.c2p(0,0))

        text_p1 = MathTex(r"p = 1",color=dark_pink).move_to(brain_img.get_top()+2*UP).scale(2)
        rect_p1 = SurroundingRectangle(
            text_p1,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_p2 = MathTex(r"p = 2",color=dark_pink).move_to(brain_img.get_top()+2*UP).scale(2)
        rect_p2 = SurroundingRectangle(
            text_p2,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_pinf = MathTex(r"p \to \infty",color=dark_pink).move_to(brain_img.get_top()+2*UP).scale(2)
        rect_pinf = SurroundingRectangle(
            text_pinf,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        polygon.shift(1.5*UP+1*LEFT)
        self.play(
            Write(text_p1),
            Create(rect_p1),
        )
        self.wait(0.5)
        self.play(
            Create(polygon),
        )
        self.wait(1)

        # circle_static.shift(1.5*UP+1*LEFT)
        self.play(
            TransformMatchingTex(text_p1, text_p2),
            TransformMatchingShapes(rect_p1, rect_p2),
        )
        self.wait(0.5)
        self.play(
            Transform(polygon, circle_static),
        )
        self.wait(1)

        squre.shift(1.5*UP+1*LEFT)
        self.play(
            TransformMatchingTex(text_p2, text_pinf),
            TransformMatchingShapes(rect_p2, rect_pinf),
        )
        self.wait(0.5)
        self.play(
            Transform(polygon, squre),
        )
        self.wait(1)

        self.play(
            FadeOut(rect_pinf),
            FadeOut(text_pinf),
            FadeOut(polygon),
            FadeOut(axes),
            FadeOut(plane),
            FadeOut(brain_img),
        )
        self.wait(1)

    def scene4(self,title):
        """scene 4: what is norm ? """
        # From Intuition to Mathematics
        plane,axes,norm2_def = self.scene4_subScene0(title)

        self.scene4_subScene1(title,plane,axes,norm2_def)

        # self.scene4_subScene1_part2(title)

        # norm definition
        norm_group, norm_box, question_group, question_box, norm_title = self.scene4_subScene2(title)

        # shapes for norm definition
        self.scene4_subScene3(title)

        # prove and show ||x||>=0
        self.scene4_subScene4(title)

        # examples of norm
        self.scene4_subScene5(title)


    def scene3(self,topic_number,first_time=False):
        """scene 3: show topics list"""

        title = Tex(
            "Topics We Will Discuss In this Video ...",
            color=GOLD_A, font_size=60
        ).to_edge(UP)

        if first_time:

            self.camera.background_color = topics_backGround_color

            self.play(
                Write(title),
            )
            self.wait(2)
            
            img = ImageMobject("images/topics.png")
            img.scale(2.65)

            self.play(
                FadeIn(img), 
                run_time=2
            )

            self.camera.frame.save_state()


            rect_1 = Rectangle(width=3, height=5).move_to(img.get_left() + RIGHT * 1.4 +0.6*UP).round_corners(radius=0.3)
            rect_2 = Rectangle(width=3, height=5).move_to(img.get_left() + RIGHT * 4.3 +0.6*UP).round_corners(radius=0.3)
            rect_3 = Rectangle(width=5, height=5).move_to(img.get_left() + RIGHT * 8 +0.6*UP).round_corners(radius=0.3)
            rect_4 = Rectangle(width=4, height=5).move_to(img.get_left() + RIGHT * 12.5 +0.6*UP).round_corners(radius=0.3)

            zoom_rects = [rect_1, rect_2, rect_3, rect_4]

            for rect in zoom_rects:

                rect.set_stroke(GOLD_A, 3)

                self.play(Create(rect), run_time=0.3)

                self.play(
                    self.camera.frame.animate
                    .move_to(rect.get_center())
                    .set(width=rect.width).set(height=rect.height),  
                    run_time=1,
                    rate_func=smooth
                )

                self.wait(5)

                self.play(FadeOut(rect), run_time=1)

            self.play(
                Restore(self.camera.frame),
                run_time=3,
                rate_func=smooth
            )

            self.wait(2)

            self.play(
                FadeOut(img), 
                run_time=2
            )
            self.play(
                Unwrite(title),
            )
            self.camera.background_color = WHITE

        items_list = [  "The Birth of Norms", 
                        "From Norms to Metrics", 
                        "Cauchy Sequences : The Mystery of Nearness", 
                        "Banach Spaces : The Kingdom of Completeness",  ]

        selected_title = Tex(items_list[topic_number], color=BLACK, font_size=80)
        selected_title.move_to(title.get_center())
        
        return selected_title

    def scene2(self,):
        warning_text = MathTex(
            r"X \text{ is a vector space over } \mathbb{K},",
            r"\text{where } \mathbb{K} \text{ is } \mathbb{R} \text{ or } \mathbb{C}.",
            color=BLACK,
        )
        self.show_warning(warning_text,True)
        self.wait(2)

    def scene1_SubScene1(self,):
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]).shift(DOWN*2)
        self.play(Create(plane))
        self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 5, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]).shift(DOWN*2)
        self.play(Create(axes))
        self.wait(0.5)

        # draw vector in (0,0) - a
        vector_a = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(5,3),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(GrowArrow(vector_a, run_time=1.2, rate_func=rush_from))
        self.wait(0.5)

        # draw vector in (0,0) - b
        vector_b = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(-3,5),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(GrowArrow(vector_b, run_time=1.2, rate_func=rush_from))
        self.wait(0.5)

        # add texts
        a_text = MathTex(r"\overrightarrow{a} = (a_1, a_2)",color=BLACK).move_to(vector_a.get_end()+0.5*RIGHT+0.5*UP)
        self.play(FadeIn(a_text, shift=UP*0.2))
        self.wait(0.5)

        b_text = MathTex(r"\overrightarrow{b} = (b_1, b_2)",color=BLACK).move_to(vector_b.get_end()+0.5*LEFT+0.5*UP)
        self.play(FadeIn(b_text, shift=UP*0.2))
        self.wait(0.5)

        inner_product_text = MathTex(" \\langle \\vec{a}, \\vec{b} \\rangle = a_1 b_1 + a_2 b_2 = 0 ",color=BLACK).move_to(plane.get_center() + 0.75*DOWN)
        self.play(FadeIn(inner_product_text, shift=UP*0.2))
        self.wait(0.5)

        self.play(
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(vector_a),
            FadeOut(vector_b),
            FadeOut(a_text),
            FadeOut(b_text),
            FadeOut(inner_product_text),
        )


    def scene1(self,):
        """scene 1: title screen"""

        style = {
            "font_size": 85, "color": BLACK
        }

        title_up = Tex('Kinds of', 'Orthogonality',arg_separator=" ",**style).to_edge(UP)
        title_up[1].set_color(GREEN_E)
        title_down = Tex('in', 'Banach Spaces',arg_separator=" ",**style).move_to(title_up.get_center()+DOWN*0.75)
        title_down[1].set_color(GREEN_E)
        title_part = MathTex('part','\\text{ 1}',color=BLACK, font_size=70).move_to(title_down.get_center() + 0.75*DOWN)
        
        
        # 1-2 : add image

        star1 = ImageMobject("images/star_1_img.png").move_to(title_up.get_center()+ 6*LEFT + 0.5*DOWN )
        self.add(star1)

        star2 = ImageMobject("images/star_1_img.png").move_to(title_down.get_center()+ 5*RIGHT + 1.5*DOWN )
        self.add(star2)

        self.play(
            Write(title_up),
            Write(title_down),
            Write(title_part),
        )

        # 1-3 : add shapes

        # draw axes on top
        self.scene1_SubScene1()

        self.wait(0.5)

        self.play(
            Unwrite(title_up),
            Unwrite(title_down),
            Unwrite(title_part),
        )

        self.remove(star1)
        self.remove(star2)