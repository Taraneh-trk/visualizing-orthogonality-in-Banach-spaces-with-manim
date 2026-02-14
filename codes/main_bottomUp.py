from manim import *
import numpy as np

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

    def show_warning(self, body: MathTex):
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

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))

    def ask_question(self,body, return_notShow=False):
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
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))

    def show_minorPoint(self,body,return_notShow):
        """Show message with box to ask a question. """

        title_text = Text("🤏Point", color=dark_blue, font_size=36)

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
    
    def show_example(self,total_title,body,return_notShow=False):
        """Show message with box to show some examples. """

        title_text = Text("Example", color= dark_purple, font_size=36)

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

        self.scene1()

        self.scene2()

        topic_number = 0
        title = self.scene3(topic_number,True)

        # norm
        self.scene4(title)

    def scene4_subScene0(self,title):
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
        self.wait(1)
        self.play(
            Write(norm2_2d[1]),
            Write(norm2_2d[2]),
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
        text_2_formula_1 = MathTex(r"= \sqrt{0^2 + 0^2}",color=dark_pink
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
            r"=",
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
            r"=",
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
            r"=",
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
            r"=",
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
            r"=",
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
            r"=",
            r"|t|",
            r"\sqrt{x^2 + y^2}",
            color=light_purple
        ).move_to(reordered)

        self.play(
            TransformMatchingTex(reordered, final)
        )
        self.wait(2)
        final[2].set_color(light_orange)
        self.wait(2)
        length_text = MathTex(r"\text{length}",color=light_orange
        ).next_to(final[1],RIGHT)
        self.play(
            ReplacementTransform(final[2],length_text)
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
        self.wait(2)

        text_x.shift(0.7*RIGHT+0.4*DOWN)
        vector_rule3_1_group = VGroup(vector_rule3_1,text_x)
        self.play(
            vector_rule3_1_group.animate.move_to(dot_arrow_2.get_center()),
            run_time=1
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
            DrawBorderThenFill(triangle),
            run_time=3
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

        self.wait(1)

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
            Create(axes),
            norm2_def.animate.to_edge(UL).shift(0.8*RIGHT),
            run_time=2
        )

        norm2_def_Euclidean = MathTex(r"\text{length}_{\text{Euclidean}  }",color=BLACK
        ).move_to(norm2_def[0].get_center()+0.2*LEFT)

        self.play(
            ReplacementTransform(norm2_def[0],norm2_def_Euclidean),
            run_time=2
        )
        self.wait(2)

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

        dot_arrow_x =  DashedLine(
            start=axes.c2p(0,0),
            end=axes.c2p(6,0), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_green,
        )
        text_dot_x = MathTex(r"x_1").set_color(BLACK).move_to(dot_arrow_x.get_center()+0.4*DOWN)

        dot_arrow_y =  DashedLine(
            start=axes.c2p(6,0),
            end=axes.c2p(6,6), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_red,
        )
        text_dot_y = MathTex(r"x_2").set_color(BLACK).move_to(dot_arrow_y.get_center()+0.4*RIGHT)

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

        norm1_2d = MathTex(
            r"\text{length}_{\text{Manhattan}}",r"= ",r"|x_1| + |x_2|",color=BLACK
        ).next_to(norm2_def,DOWN).shift(0.3*RIGHT)
        self.play(
            Write(norm1_2d),
        )
        self.wait(6)

        self.play(
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(manhatan_arrow),
            FadeOut(text_x),
            FadeOut(dot_arrow_x),
            FadeOut(text_dot_x),
            FadeOut(dot_arrow_y),
            FadeOut(text_dot_y),
            FadeOut(norm1_2d),
            FadeOut(norm2_def[1:]),
            FadeOut(norm2_def_Euclidean),
        )

    def scene4_subScene2(self,title):
        "scene4 : subScene2 : norm definition"
        
        question_tex = MathTex("\\text{ What happens if we try to generalize this ? }").set_color(BLACK)
        question_group,question_box = self.ask_question(question_tex,True)

        group_GroupBoxQuetion = VGroup(question_group,question_box)
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

        def_norm_line3 = MathTex(
            r"\begin{aligned}"
            # r"1.& \quad \|x\| \ge 0 \\"
            r"1.& \quad \|x\| = 0 \iff x = 0 \\"
            r"2.& \quad \|\lambda x\| = |\lambda| \, \|x\| \\"
            r"3.& \quad \|x + y\| \le \|x\| + \|y\|"
            r"\end{aligned}"
        ).set_color(BLACK).scale(0.85)

        def_norm_line4 = MathTex(r"\quad \text{for all } x,y \in X \text{ and } \lambda \in \mathbb{K}.").set_color(BLACK)

        def_norm = VGroup(def_norm_line1, def_norm_line2, def_norm_line3,def_norm_line4).arrange(DOWN, buff=0.5).scale(0.9)

        def_norm.next_to(title.get_center(), DOWN)

        norm_group, norm_box = self.show_definition(def_norm, title,True)
        norm_group.shift(1.6*UP)
        norm_box.move_to(norm_group.get_center())

        # norm title
        norm_title = MathTex(r"\text{NORM}", color=BLACK, font_size=80).move_to(title.get_center())

        self.play(
            Write(norm_title),
            TransformMatchingShapes(group_GroupBoxQuetion, norm_box), 
            Write(norm_group)
        )
        self.wait(5)
        self.play(
            Uncreate(norm_box),
            FadeOut(norm_group)
        )

        return norm_group, norm_box, question_group, question_box, norm_title

    def scene4_subScene3(self, question_group, question_box, title):
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

    def scene4_subScene4(self,title,norm_title):
        """scene 4 : sub scene 4 : prove and show ||x|| >= 0 """
        prove_text = MathTex("\|x\| \ge 0",color=BLACK).scale(1.3)
        text_group,box = self.show_conclusion(title, prove_text,True)
        self.play(
            Create(box),
            Write(text_group)
        )
        self.wait(0.8)

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

        variable_replacement = MathTex("y = -x",color=BLACK).scale(1.7).move_to(title.get_center()+4*DOWN+4*LEFT)
        self.play(
            Write(variable_replacement),
        )
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
        proof_line2_part2_initial = MathTex("|-1| \, \|x\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[2].get_center()+1.5*DOWN+0.4*RIGHT)
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

        # example of norm

        # norm 1
        vector_def = MathTex(
            r"\text{Let } x = (x_1, \dots, x_n) \in \mathbb{R}^n.",color=BLACK
        ).move_to(title.get_center()+1*DOWN)
        self.play(
            Write(vector_def)
        )
        self.wait(1)
        norm1 = MathTex(
            r"\|x\|_1 := \sum_{i=1}^{n} |x_i|",color=BLACK
        ).move_to(vector_def.get_center()+1*DOWN)
        self.play(
            Write(norm1)
        )
        self.wait(1)



    def scene4(self,title):
        """scene 4: what is norm ? """
        # From Intuition to Mathematics
        plane,axes,norm2_def = self.scene4_subScene0(title)

        self.scene4_subScene1(title,plane,axes,norm2_def)

        # norm definition
        norm_group, norm_box, question_group, question_box, norm_title = self.scene4_subScene2(title)

        # shapes for norm definition
        self.scene4_subScene3(question_group, question_box, title)

        # prove and show ||x||>=0
        self.scene4_subScene4(title,norm_title)

        # examples of norm
        # self.scene4_subScene5(title)


    def scene3(self,topic_number,first_time=False):
        """scene 3: show topics list"""

        if first_time:

            img = ImageMobject("images/topics.png")
            img.scale(2.65)
            self.add(img)
            self.camera.background_color = topics_backGround_color
            self.camera.frame.save_state()


            rect_1 = Rectangle(width=3, height=5).move_to(img.get_left() + RIGHT * 1.4 +0.6*UP)
            rect_2 = Rectangle(width=3, height=5).move_to(img.get_left() + RIGHT * 4.3 +0.6*UP)
            rect_3 = Rectangle(width=5, height=5).move_to(img.get_left() + RIGHT * 8 +0.6*UP)
            rect_4 = Rectangle(width=4, height=5).move_to(img.get_left() + RIGHT * 12.5 +0.6*UP)

            zoom_rects = [rect_1, rect_2, rect_3, rect_4]

            for rect in zoom_rects:

                rect.set_stroke(GOLD_A, 3)

                self.play(Create(rect), run_time=1.2)

                self.play(
                    self.camera.frame.animate
                    .move_to(rect.get_center())
                    .set(width=rect.width).set(height=rect.height),  
                    run_time=3,
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

            self.camera.background_color = WHITE
            self.play(FadeOut(img), run_time=2)

        
        title = Tex(
            "Topics We Will Discuss In this Video ...",
            color=WHITE, font_size=60
        ).to_edge(UP)
        
             
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
        self.show_warning(warning_text)
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