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

def projection_point(arrow1, arrow2):
    # unit vector along arrow1
    v1 = arrow1.get_vector()
    u1 = v1 / np.linalg.norm(v1)

    # projection length
    v2 = arrow2.get_vector()
    proj_len = np.dot(v2, u1)

    return arrow1.get_start() + proj_len * u1

class TitleScene(Scene):

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
        return group, box

    def show_warning(self, body: MathTex,set_image=False,return_not_show=False):
        """Show warning message with box"""

        title_text = Text("❗Note❗", color=dark_red, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_red,
            fill_color=light_red,
            fill_opacity=0.2,
            width=group.width+0.5,
            height=group.height+0.5
        )

        box.move_to(group.get_center())

        VGroup(group, box).shift(1*DOWN)

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
        if return_not_show==False:
            self.play(Create(box), Write(group))
            self.wait(2)
            self.play(FadeOut(group), FadeOut(box))

        if set_image==True:
            self.play(
                # FadeOut(arrow_0_0_down),
                # FadeOut(ex_mark_1),
                FadeOut(ex_mark_2)
            )
        if return_not_show==True:
            return group, box
        
    def show_minorPoint(self,body,return_notShow):
        """Show message with box to ask a question. """

        title_text = Text("Note", color=dark_blue, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_blue,
            fill_color=light_blue,
            fill_opacity=0.2,
            width=group.width + 0.5,
            height=group.height + 0.5
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
        return group, box

    def construct(self):

        # self.scene1()

        # self.scene2()

        topic_number = 0
        title = self.scene3(topic_number,False)

        self.scene4(title)

    def scene4_SubScene1(self,title):
        dot_formula_text = MathTex(
            r"\vec{a} \, \cdot \, \vec{b}",
            r" = ",
            r"\|a\| \,",
            r" \|b\| \, \cos(\theta)",
            color=BLACK,
        ).scale(1.2).move_to(title.get_center()+0.3*DOWN+0.15*LEFT)

        box = SurroundingRectangle(
            dot_formula_text,
            color=dark_pink,        
            buff=0.2,    
            # fill_color=WHITE,      
            fill_opacity=0.2,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        plane = NumberPlane(
            y_range=[-8, 8, 1],
            x_range=[-10, 10, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=9,
            x_length=15,
        ).move_to([0, 0, 0]+DOWN)

        axes = Axes(  # NumberLine
            y_range=[-8, 8, 1],
            y_length=9,
            x_range=[-10, 10, 1],
            x_length=15,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)

        arrow1 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(8,3),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        a_text = MathTex(r"\vec{a}",color=dark_red).scale(1.1).move_to(arrow1.get_center()+0.5*DOWN)

        arrow2 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(1,5),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        b_text = MathTex(r"\vec{b}",color=dark_green).scale(1.1).move_to(arrow2.get_center()+0.6*UP+0.2*LEFT)

        # x = (23*8)/73
        # y = (-8/3)*x + (23/3)
        dashed = always_redraw(
            lambda: DashedLine(
                arrow2.get_end(),
                projection_point(arrow1, arrow2),
                color=dark_orange,
                dash_length=0.15
            )
        )
        # temp_arrow = Arrow(
        #     axes.c2p(x,y), 
        #     arrow2.get_end(),
        # )
        arc_orthagenal = always_redraw(
            lambda: RightAngle(
                arrow1,
                Line(projection_point(arrow1,arrow2), arrow2.get_end()),
                length=0.3,
                color=BLACK
            )
        )

        arrow3 = always_redraw(
            lambda: Arrow(
                start=arrow1.get_start(),
                end=projection_point(arrow1,arrow2),
                buff=0,
                stroke_width=12,
                color=dark_terquise,
                tip_length=0.25,
                tip_shape=StealthTip
            )
        )

        dot_formula_part1 = MathTex(
            r"\|a\|",
            color=dark_red,
        ).scale(1.4).to_corner(UL)

        dot_formula_part2 = MathTex(
            r"\times",
            color=BLACK,
        ).scale(1.4).next_to(dot_formula_part1,RIGHT,buff=0.3)

        dot_formula_part3 = MathTex(
            r"\|b\| \, ",
            r"\cos(\theta)",
            color=dark_terquise,
        ).scale(1.4).next_to(dot_formula_part2,RIGHT,buff=0.3)

        self.play(
            Write(dot_formula_text),
        )
        self.wait(0.5)

        self.play(
            Create(box),
        )

        dot_and_box = VGroup(dot_formula_text, box)
        self.play(
            dot_and_box.animate.scale(0.9).to_edge(DOWN),
        )

        self.play(
            Create(plane),
            Create(axes),
        )
        self.wait(0.5)

        self.play(
            GrowArrow(arrow1),
            Write(a_text),
            GrowArrow(arrow2),
            Write(b_text),
        )

        arc_ab = always_redraw(lambda:
            Angle(
                arrow1,
                arrow2,
                radius=0.7,
                color=BLACK,
                other_angle=False
            )
        )
        tetha_text = always_redraw(lambda:
            MathTex(r"\theta", color=BLACK)
                .scale(1.1)
                .next_to(arc_ab, UP)
                .shift(0.5*RIGHT)
        )

        self.play(
            Create(arc_ab),
            Write(tetha_text),
        )

        self.wait(0.5)
        self.play(
            Create(dashed),
            Create(arc_orthagenal),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(arrow3),
        )
        self.wait(0.5)

        a_copy = arrow1.copy()
        angle_diff = PI/2 - a_copy.get_angle()
        a_copy.rotate(angle_diff, about_point=a_copy.get_start()).scale(0.8).next_to(dot_formula_part1,DOWN,buff=0.5)
        line_a = Line(a_copy.get_start(),a_copy.get_end(),color=dark_red)
        result_copy = arrow3.copy()
        result_copy.rotate(-result_copy.get_angle() + PI/2, about_point=ORIGIN).next_to(dot_formula_part3,DOWN,buff=0.5)
        line_result = Line(result_copy.get_start(),result_copy.get_end(),color=dark_terquise)

        self.play(
            TransformFromCopy(dot_formula_text[2], dot_formula_part1),
            TransformFromCopy(arrow1, line_a),
        )
        self.wait(0.3)
        self.play(
            Write(dot_formula_part2),
        )
        times_copy = dot_formula_part2.copy().shift(2*DOWN)
        self.wait(0.3)
        self.play(
            TransformFromCopy(dot_formula_part2, times_copy),
        )
        self.wait(0.3)
        self.play(
            TransformFromCopy(dot_formula_text[3], dot_formula_part3),
            TransformFromCopy(arrow3, line_result),
        )
        self.wait(1)

        sign_text = MathTex(r"Sign",color=dark_purple).scale(1.2).next_to(line_result,LEFT,buff=0.2).shift(0.2*DOWN)
        pos_text = MathTex(r"+",color=dark_purple).scale(1.2).move_to(sign_text.get_center())
        neg_text = MathTex(r"-",color=dark_purple).scale(1.2).move_to(sign_text.get_center())
        zero_text = MathTex(r"0",color=dark_purple).scale(1.2).move_to(sign_text.get_center())

        theta_lower = MathTex(r"\theta < 90^\circ",color=BLACK).scale(1.5).to_corner(UR)
        theta_equal = MathTex(r"\theta = 90^\circ",color=BLACK).scale(1.5).to_corner(UR)
        theta_upper = MathTex(r"\theta > 90^\circ",color=BLACK).scale(1.5).to_corner(UR)

        self.play(
            line_result.animate.shift(1*RIGHT),
            Write(sign_text),
        )
        self.wait(0.5)
        self.play(
            Write(theta_lower),
        )
        self.play(
            FadeOut(sign_text),
            TransformFromCopy(dot_formula_part3[1] , pos_text),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            FadeTransform(theta_lower, theta_equal),
            Rotate(arrow2, angle = (PI/2 + arrow1.get_angle() - arrow2.get_angle()),
                about_point = axes.c2p(0,0),
                run_time = 3),
            FadeOut(pos_text),
            TransformFromCopy(dot_formula_part3[1] , zero_text),
        )
        self.wait(0.5)
        self.play(
            FadeTransform(theta_equal, theta_upper),
            Rotate(arrow2, angle = (PI/6),
                about_point = axes.c2p(0,0),
                run_time = 3),
            FadeOut(zero_text),
            TransformFromCopy(dot_formula_part3[1] , neg_text),
            run_time=1.5,
        )

        self.wait(1)

        fade_out_list = [
            line_a,
            times_copy,
            line_result,
            neg_text,
            theta_upper,
            dot_formula_part1,
            dot_formula_part2,
            dot_formula_part3,
            dot_formula_text,
            box,
            arrow1,
            a_text,
            arrow2,
            b_text,
            arc_ab,
            tetha_text,
            arrow3,
            dashed,
            arc_orthagenal,
            axes,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )
        self.play(
            FadeOut(plane),
        )
        self.wait(1)

    def scene4_SubScene2(self, title):
        self.wait(1)
        image = ImageMobject("images/graduate_brain_img_mini.png").scale(2.5).to_corner(DL)
        self.add(image)
        a_vector = MathTex(
            r"\vec{a} = ( ",  #0
            r"a_1 ",          #1
            r", ",            #2
            r"a_2 ",          #3
            r", \dots , ",    #4
            r"a_n ",        #5
            r")",             #6
            color=BLACK,
        ).scale(1.3).move_to(title.get_center()+0.5*DOWN)

        a_vector.set_color_by_tex(r"a_1 ",dark_orange)
        a_vector.set_color_by_tex(r"a_2 ",dark_orange)
        a_vector.set_color_by_tex(r"a_n ",dark_orange)

        b_vector = MathTex(
            r"\vec{b} = ( ",    #0
            r"b_1 ",            #1
            r", ",              #2
            r"b_2 ",            #3
            r", \dots , ",      #4
            r"b_n ",            #5
            r")",               #6
            color=BLACK,
        ).scale(1.3).next_to(a_vector,DOWN,buff=0.5)
        b_vector.set_color_by_tex(r"b_1 ",dark_pink)
        b_vector.set_color_by_tex(r"b_2 ",dark_pink)
        b_vector.set_color_by_tex(r"b_n ",dark_pink)

        dot_product_resultpart1 = MathTex(
            r"\vec{a} \, \cdot \vec{b}",
            color=BLACK
        ).scale(1.3).next_to(b_vector,DOWN,buff=1)

        dot_product_resultpart2 = MathTex(
            r" = \sum_{i=1}^{n} a_i b_i",
           color=BLACK,
        ).scale(1.3).next_to(dot_product_resultpart1, RIGHT,buff=0.3)

        VGroup(dot_product_resultpart1, dot_product_resultpart2).shift(1.5*LEFT)

        dot_product_resultpart3 = MathTex(
            r" = ",     #0
            r"a_1 ",    #1
            r"b_1",     #2
            r" + ",     #3
            r"a_2 ",    #4
            r"b_2",     #5
            r" + ",     #6
            r"\dots",   #7
            r" + ",     #8
            r"a_n ",    #9
            r"b_n",     #10
            color=BLACK
        ).scale(1.3).next_to(dot_product_resultpart1,DOWN,buff=1).shift(3*RIGHT)

        dot_product_resultpart3.set_color_by_tex(r"a_1 ", dark_orange)
        dot_product_resultpart3.set_color_by_tex(r"a_2 ", dark_orange)
        dot_product_resultpart3.set_color_by_tex(r"a_n ", dark_orange)

        dot_product_resultpart3.set_color_by_tex(r"b_1", dark_pink)
        dot_product_resultpart3.set_color_by_tex(r"b_2", dark_pink)
        dot_product_resultpart3.set_color_by_tex(r"b_n", dark_pink)


        self.play(
            Write(a_vector),
        )
        self.play(
            Write(b_vector),
        )
        self.wait(0.5)
        self.play(
            Write(dot_product_resultpart1),
        )
        self.wait(0.5)
        self.play(
            Write(dot_product_resultpart2),
        )
        self.wait(0.5)
        self.play(
            Write(dot_product_resultpart3[0]),
        )
        self.play(
            TransformFromCopy(a_vector[1] , dot_product_resultpart3[1]),
            TransformFromCopy(b_vector[1] , dot_product_resultpart3[2]),
            Write(dot_product_resultpart3[3]),
        )
        self.play(
            TransformFromCopy(a_vector[3] , dot_product_resultpart3[4]),
            TransformFromCopy(b_vector[3] , dot_product_resultpart3[5]),
            Write(dot_product_resultpart3[6]),
        )
        self.play(
            TransformFromCopy(VGroup(a_vector[4], b_vector[4]), dot_product_resultpart3[7]),
            Write(dot_product_resultpart3[8]),
        )
        self.play(
            TransformFromCopy(a_vector[5] , dot_product_resultpart3[9]),
            TransformFromCopy(b_vector[5] , dot_product_resultpart3[10]),
        )

        self.wait(1)

        fadeout_list = [
            a_vector,
            b_vector,
            dot_product_resultpart1,
            dot_product_resultpart2,
            dot_product_resultpart3,
        ]
        self.play(
            FadeOut(VGroup(*fadeout_list)),
            FadeOut(image),
        )
        self.wait(1)

    def scene4_SubScene0(self, title):

        self.wait(1)
        dotimage = ImageMobject("images\cute_dot_product.png").scale(1.1).to_edge(DOWN).shift(0.7*DOWN)
        self.add(dotimage)

        recall = Text(" Recall the definition of the dot product ", color=BLACK, font="Palatino Linotype", font_size=50)
        recall_box = SurroundingRectangle(
            recall,
            color=dark_terquise,        
            buff=0.3,    
            # fill_color=WHITE,      
            fill_opacity=0.2,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        VGroup(recall, recall_box).shift(2.8*UP)


        self.play(
            Create(recall_box),
            Write(recall),
        )
        self.wait(0.5)
        self.play(
            FadeOut(VGroup(recall, recall_box)),
            FadeOut(dotimage),
        )
        self.wait(1)

    def scene4_SubScene3(self, title):
        
        function_text = MathTex(r"\text{ Function }", color=BLACK).scale(2).shift(2*UP)
        function_box = RoundedRectangle(
            corner_radius=0.3,
            color= dark_terquise,
            fill_color=dark_terquise,
            fill_opacity=0.2,
            width=function_text.width + 2,
            height=function_text.height + 5
        ).move_to(function_text.get_center()+2*DOWN)

        wheelimage = ImageMobject("images\wheel.png").scale(0.4).move_to(function_box.get_bottom()+2.2*UP)

        a_vec_text = MathTex(r"\vec{a}",color =dark_pink).scale(1.3).to_edge(LEFT).shift(1*RIGHT+1*UP)
        a_vec = Arrow(a_vec_text.get_right(), function_box.get_left()+1*UP, color=dark_pink)
        b_vec_text = MathTex(r"\vec{b}",color=dark_purple).scale(1.3).to_edge(LEFT).shift(1*RIGHT+1*DOWN)
        b_vec = Arrow(b_vec_text.get_right(), function_box.get_left()+1*DOWN, color=dark_purple)
        in_text = MathTex(
            r"c",
            r"\in \mathbb{R}",
            color=BLACK
        ).scale(1.3).to_edge(RIGHT).shift(0.5*LEFT)
        in_vec = Arrow(function_box.get_right(), in_text.get_left(), color=dark_green)
        # brace = BraceBetweenPoints(in_text.get_left(),in_text.get_left(),color=dark_green).shift(0.2*DOWN)
        # scaler_text = MathTex(r"\text{scaler}",color=BLACK).next_to(brace, DOWN, buff=0.5)


        self.play(
            Create(function_box),
        )
        self.add(wheelimage)
        self.play(
            Write(function_text),
        )

        self.play(
            Write(a_vec_text),
            GrowArrow(a_vec),
        )
        self.play(
            Write(b_vec_text),
            GrowArrow(b_vec),
        )
        self.play(
            Write(in_text),
            GrowArrow(in_vec),
        )
        self.wait(1)

        fadeout_list = [
            function_box,
            function_text,
            a_vec,
            a_vec_text,
            b_vec,
            b_vec_text,
            in_text,
            in_vec,
        ]
        self.play(FadeOut(wheelimage))
        self.play(
            FadeOut(VGroup(*fadeout_list)),
        )

        self.wait(1)

    def scene4_subScene4(self,title):
        
        question_tex = MathTex("\\text{ What happens if we try to generalize this ? }").set_color(BLACK)
        question_group, question_box, image_1, image_2 = self.ask_question(question_tex,True,True)

        group_GroupBoxQuetion = VGroup(question_group,question_box)
        group_GroupBoxQuetion.shift(1.5*UP)
        image_1.scale(1.2).shift(3.5*DOWN)
        self.add(image_1)
        self.play(
            FadeIn(group_GroupBoxQuetion)
        )
        self.wait(1)
        self.play(
            FadeOut(group_GroupBoxQuetion),
            FadeOut(image_1),
        )
        self.wait(1)

    def scene4(self,title):
        title.shift(0.5*DOWN)
        # self.play(
        #     Write(title),
        # )
        # self.wait(0.5)
        # self.play(
        #     FadeOut(title),
        # )

        # recall you remember what dor product is ? 
        # self.scene4_SubScene0(title)

        # dot product explanation from shape and a.b=||a|| ||b|| cos(theta)
        # self.scene4_SubScene1(title)

        # dot product calculate formula
        # self.scene4_SubScene2(title)

        # self.scene4_SubScene3(title)

        self.scene4_subScene4(title)


    def scene3(self,topic_number,first_time=False):
        """scene 3: show topics list"""

        title = Tex(
            "Topics We Will Discuss In this Video ...",
            color=GOLD_A, font_size=60
        ).to_edge(UP)

        if first_time:

            bg_rect = Rectangle(
                width=10*config.frame_width, 
                height=10*config.frame_height, 
                stroke_width=0, 
                fill_color=topics_backGround_color, 
                fill_opacity=1
            )
            self.add(bg_rect)
            self.play(
                FadeIn(bg_rect, run_time=0.5),
            )

            self.play(
                Write(title),
            )
            
            img = ImageMobject("images/topics.png")
            img.scale(2.65)

            self.play(
                FadeIn(img), 
                run_time=1
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

                self.play(FadeOut(rect))

            self.play(
                Restore(self.camera.frame),
                run_time=1,
                rate_func=smooth
            )

            self.wait(1)

            self.play(
                FadeOut(img), 
                FadeOut(title),
            )
            self.play(
                FadeOut(bg_rect,run_time=0.5),
            )

        items_list = [  r"Inner Products \\ From Shadows to Structure", 
                        # "From Norms to Metrics", 
                        # r"Cauchy Sequences \\ The Mystery of Nearness", 
                        # "Banach Spaces", 
                     ] # \\ The Kingdom of Completeness

        selected_title = Tex(items_list[topic_number], color=BLACK, font_size=80)
        selected_title.move_to(title.get_center())
        
        return selected_title

    def scene2(self,):
        warning_text = MathTex(
            r"X \text{ is a vector space over } \mathbb{K},",
            r"\text{where } \mathbb{K} \text{ is } \mathbb{R} \text{ or } \mathbb{C}.",
            color=BLACK,
        )
        bg_rect = Rectangle(
            width=config.frame_width, 
            height=config.frame_height, 
            stroke_width=0, 
            fill_color=light_red, 
            fill_opacity=0.2
        )
        self.add(bg_rect)
        self.play(
            FadeIn(bg_rect, run_time=0.5),
        )
        self.show_warning(warning_text,True)
        self.play(
            FadeOut(bg_rect), 
        )
        self.wait(0.5)

    def scene1_SubScene1(self,):
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]).shift(DOWN*2)
        # self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 5, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]).shift(DOWN*2)
        # self.wait(0.5)

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
        # self.wait(0.5)

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
        # self.wait(0.5)

        # add texts
        a_text = MathTex(r"\overrightarrow{a} = (a_1, a_2)",color=BLACK).move_to(vector_a.get_end()+0.5*RIGHT+0.5*UP)
        # self.wait(0.5)

        b_text = MathTex(r"\overrightarrow{b} = (b_1, b_2)",color=BLACK).move_to(vector_b.get_end()+0.5*LEFT+0.5*UP)
        # self.wait(0.5)

        inner_product_text = MathTex(" \\langle \\vec{a}, \\vec{b} \\rangle = a_1 b_1 + a_2 b_2 = 0 ",color=BLACK).move_to(plane.get_center() + 0.75*DOWN)
        # self.wait(0.5)

        self.play(
            Create(plane, run_time=0.2),
            Create(axes, run_time=0.2),
            GrowArrow(vector_a, run_time=0.3, rate_func=rush_from),
            FadeIn(a_text, shift=UP*0.2),
            GrowArrow(vector_b, run_time=0.3, rate_func=rush_from),
            FadeIn(b_text, shift=UP*0.2),
            FadeIn(inner_product_text, shift=UP*0.2),
        )

        self.wait(1)

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
        title_part = MathTex('part','\\text{ 2}',color=BLACK, font_size=70).move_to(title_down.get_center() + 0.75*DOWN)
        
        
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

        self.wait(1)

        self.play(
            Unwrite(title_up),
            Unwrite(title_down),
            Unwrite(title_part),
        )

        self.remove(star1)
        self.remove(star2)

    def scene2(self,):
        warning_text_part1 = MathTex(
            r"X \text{ is a Vector space over } \mathbb{K},",
            r"\text{where } \mathbb{K} \text{ is } \mathbb{R} \text{ or } \mathbb{C}.",
            color=BLACK,
        )
        warning_text_part2 = MathTex(
            r"(X \, , d) \text{ is a Metric space } ",
            # r"\text{where } \mathbb{K} \text{ is } \mathbb{R} \text{ or } \mathbb{C}.",
            color=BLACK,
        )
        warning_text_part3 = MathTex(
            r"(X \, , \|.\|) \text{ is a Normed space } ",
            # r"\text{where } \mathbb{K} \text{ is } \mathbb{R} \text{ or } \mathbb{C}.",
            color=BLACK,
        )
        warning_text = VGroup(warning_text_part1, warning_text_part2, warning_text_part3).arrange(DOWN,buff=0.2)
        bg_rect = Rectangle(
            width=config.frame_width, 
            height=config.frame_height, 
            stroke_width=0, 
            fill_color=light_red, 
            fill_opacity=0.2
        )
        self.add(bg_rect)
        self.play(
            FadeIn(bg_rect, run_time=0.5),
        )
        self.show_warning(warning_text,True)
        self.play(
            FadeOut(bg_rect), 
        )
        self.wait(0.5)