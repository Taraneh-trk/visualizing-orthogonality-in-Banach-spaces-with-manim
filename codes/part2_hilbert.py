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

class TitleScene(ThreeDScene):   # Scene

    def show_definition(self, definition: MathTex, total_title, retrun_notShow=False, what_is_defined=""):
        """Show definition with box"""

        title_text = Text(f"⚙️📃Definition {what_is_defined}", color=dark_green, font_size=36)

        group = VGroup(title_text, definition).arrange(DOWN, buff=0.3)
        
        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_green,
            fill_color=light_green,
            fill_opacity=0.15,
            width=group.width + 0.6,
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

        # topic_number = 0
        # title = self.scene3(topic_number,False)

        # self.scene4(title)

        # topic_number = 1
        # title = self.scene3(topic_number,False)

        # self.scene5(title)

        # topic_number = 2
        # title = self.scene3(topic_number,False)

        # self.scene6(title)

        topic_number = 3
        title = self.scene3(topic_number,False)

        # self.scene7(title)

        # self.scene7_1(title)

        self.scene8(title)

    def scene8_SubScene0(self, title):
        self.wait(1)
        image = ImageMobject("images/graduate_brain_img_mini.png").scale(3).to_corner(DL)
        self.add(image)
        or_in_hil_titlepart1 = Tex("Orthogonality in", color=BLACK, font_size=80)
        or_in_hil_titlepart2 = Tex("Normed space", color=BLACK, font_size=80)
        or_in_hil_title = VGroup(or_in_hil_titlepart1, or_in_hil_titlepart2).arrange(DOWN, buff=0.3)
        or_in_hil_title.move_to(title.get_center()+0.5*DOWN)

        self.play(
            Write(or_in_hil_title),
        )
        self.wait(1)
        self.play(
            FadeOut(image),
            FadeOut(or_in_hil_title),
        )
        self.wait(1)

    def scene8_SubScene01(self, title):
        # خاصیت هایی که بین همه تعامد ها در فضاهای نرمدار مشترکن
        title_Summary = Text("Properties That Hold for All Types of Orthogonality",color=BLACK,font_size=40).to_edge(UP) #.shift(0.3*UP)
        self.play(Write(title_Summary))

        headers = [
            (r"\text{NONDEGENERACY}", dark_pink),
            (r"\text{SIMPLIFICATION}", dark_purple),
            (r"\text{CONTINUITY}", dark_terquise),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        
        row_Pythagorean = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]

        row_Isosceles = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]

        row_BJ = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]

        row_Roberts = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]
        
        row_label_roberts = MathTex(r"\text{Roberts}", color=BLACK).scale(0.6)
        row_label_BJ = MathTex(r"\text{BJ}", color=BLACK).scale(0.6)
        row_label_Isosceles = MathTex(r"\text{Isosceles}", color=BLACK).scale(0.6)
        row_label_Pythagorean = MathTex(r"\text{Pythagorean}", color=BLACK).scale(0.6)

        table = MobjectTable(
            [row_Roberts, row_BJ, row_Isosceles, row_Pythagorean],
            row_labels=[row_label_roberts, row_label_BJ, row_label_Isosceles, row_label_Pythagorean],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        ).shift(0.5*DOWN).scale(0.85)

        self.play(
            Create(table),
            run_time = 3,
        )
        self.wait(1)
        self.play(
            FadeOut(table),
            FadeOut(title_Summary),
            # run_time = 3,
        )
        self.wait(1)

    def scene8_SubScene1(self, title):
        title_orth = Tex("Roberts Orthogonality", color=BLACK, font_size=80).to_edge(UP)

        year_text = Tex("1934 - Byron David Roberts",color=BLACK,font_size=65).next_to(title_orth, DOWN,buff=0.5)

        # roberts_image = ImageMobject("")

        robert_def_part1 = MathTex(
            r"\text{Two elements } x \text{ and } y \text{ in a Banach space } X \text{ are said to}",
            color=BLACK,
        )
        robert_def_part2 = MathTex(
            r"\text{be orthogonal in the sense of Roberts if and only if}",
            color=BLACK,
        )
        robert_def_part3 = MathTex(
            r"\|x + ky\| = \|x - ky\| \quad \text{for all } k \in \mathbb{R}",
            color=BLACK,
        )
        robert_def_part4 = MathTex(
            r"\text{and denote it by } x \perp_R y.",
            color=BLACK,
        )
        robert_def = VGroup(robert_def_part1, robert_def_part2, robert_def_part3, robert_def_part4).arrange(DOWN,buff=0.3)
        group, box = self.show_definition(robert_def, title_orth, True)
        VGroup(group, box).scale(1.1).shift(1*UP)

        self.play(
            Write(title_orth),
        )
        self.wait(0.5)
        self.play(
            Write(year_text),
        )
        self.wait(0.5)
        self.play(
            FadeOut(year_text),
        )
        self.play(
            Create(box),
            Write(group),
        )
        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(group),
            FadeOut(box),
        )
        self.wait(1)

    def scene8_SubScene2(self, title):
        self.wait(0.5)
        image = ImageMobject("images/book_brain.png").scale(2).to_corner(DL)
        self.add(image)

        title_orth = Tex("Roberts Orthogonality", color=dark_blue, font_size=60).to_corner(UL)

        plane = NumberPlane(
            y_range=[-1, 11, 1],
            x_range=[-4, 10, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=7,
            x_length=9,
        ).move_to([0, 0, 0] + 0.5 * DOWN)

        axes = Axes(
            y_range=[-1, 11, 1],
            y_length=7,
            x_range=[-4, 10, 1],
            x_length=9,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length": 0.25, "tip_shape": StealthTip}
        ).move_to([0, 0, 0] + 0.5 * DOWN)

        v_x = np.array([7, 2, 0])
        v_y = np.array([-0.6, 3, 0])
        
        k_tracker = ValueTracker(5/3) 

        arrow1 = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*v_x[:2]),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow2 = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*v_y[:2]),
            buff=0,
            stroke_width=6,
            color=dark_purple,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow3 = always_redraw(lambda: Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*(v_y * k_tracker.get_value())[:2]),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        ))

        arc_orthogonal = RightAngle(
            arrow1,
            arrow2,
            length=0.3,
            color=BLACK
        )
        
        # always_redraw(lambda: RightAngle(
        #     arrow1,
        #     arrow3,
        #     length=0.3,
        #     color=BLACK
        # ))

        a_text = MathTex(r"\vec{x}", color=dark_red).scale(1.2).next_to(
            axes.c2p(*v_x[:2]), direction=DOWN + RIGHT, buff=0.15
        )

        b_text = MathTex(r"\vec{y}", color=dark_purple).scale(1.2).next_to(
            axes.c2p(*v_y[:2]), direction=LEFT, buff=0.15
        )

        bk_text = always_redraw(lambda: MathTex(r"k\,\vec{y}", color=dark_green).scale(1.2).next_to(
            axes.c2p(*(v_y * k_tracker.get_value())[:2]), direction=LEFT, buff=0.15
        ))

        side3 = always_redraw(lambda: DashedLine(
            axes.c2p(*v_x[:2]),
            axes.c2p(*(v_x + v_y * k_tracker.get_value())[:2]),
            color=dark_green,
            stroke_width=4,
            dash_length=0.15
        ))

        side4 = always_redraw(lambda: DashedLine(
            axes.c2p(*(v_y * k_tracker.get_value())[:2]),
            axes.c2p(*(v_x + v_y * k_tracker.get_value())[:2]),
            color=dark_red,
            stroke_width=4,
            dash_length=0.15
        ))

        dashed1 = always_redraw(lambda: Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*(v_x + v_y * k_tracker.get_value())[:2]),
            buff=0,
            stroke_width=4,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        ))
        
        dashed2 = always_redraw(lambda: Arrow(
            start=axes.c2p(*(v_y * k_tracker.get_value())[:2]),
            end=axes.c2p(*v_x[:2]),
            buff=0,
            stroke_width=4,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        ))

        diag_text1 = always_redraw(lambda: MathTex(r"\vec{x} + k\,\vec{y}", color=dark_orange).scale(1.1).next_to(
            axes.c2p(*(v_x + v_y * k_tracker.get_value())[:2]), direction=RIGHT, buff=0.15
        ))
        
        diag_text2 = always_redraw(lambda: MathTex(r"\vec{x} - k\,\vec{y}", color=dark_pink).scale(1.1).next_to(
            axes.c2p(*v_x[:2]), direction=RIGHT, buff=0.15
        ).shift(0.2*UP))

        all_shapes = VGroup(*[
            plane,
            axes,
            arrow1,
            arrow2,
            arrow3,
            dashed1,
            dashed2,
            side3,
            side4,
            a_text,
            b_text,
            bk_text,
            diag_text1,
            diag_text2,
            arc_orthogonal
        ]).shift(2*RIGHT)

        roberts = MathTex(
            r"\|x + ky\| ",r"= ",r"\|x - ky\|",
            color = BLACK,
        )
        roberts.set_color_by_tex(r"\|x + ky\| ",dark_orange)
        roberts.set_color_by_tex(r"\|x - ky\|",dark_pink)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        VGroup(roberts, box1).scale(1.2).to_corner(UL).shift(1*DOWN)

        self.play(
            Write(title_orth),
            Create(box1),
            Write(roberts),
        )
        self.play(
            Create(plane),
            Create(axes),
        )
        self.play(
            GrowArrow(arrow1), 
            Write(a_text),
        )
        self.play(
            GrowArrow(arrow2), 
            Write(b_text),
        )
        self.play(
            Create(arc_orthogonal),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(arrow3), 
            Write(bk_text)
        )
        self.play(
            Create(side3), 
            Create(side4)
        )
        self.play(
            GrowArrow(dashed1), 
            Write(diag_text1)
        )
        self.play(
            GrowArrow(dashed2), 
            Write(diag_text2)
        )
        self.wait(1)


        self.play(
            k_tracker.animate.set_value(0.5), run_time=2
        ) 
        self.wait(0.5)
        self.play(
            k_tracker.animate.set_value(2.5), run_time=2
        ) 
        self.wait(0.5)
        self.play(
            k_tracker.animate.set_value(5/3), run_time=1.5
        ) 

        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(all_shapes),
            FadeOut(roberts),
            FadeOut(box1),
            FadeOut(image),
        )
        self.wait(1)

    def scene8_SubScene3(self, title):
        title_orth = Tex("Roberts Orthogonality", color=BLACK, font_size=70).to_edge(UP)

        roberts = MathTex(
            r"\|x + ky\| ",r"= ",r"\|x - ky\|",r"\quad \text{ for all } k \in \mathbb{K}",
            color = BLACK,
        )
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        VGroup(roberts, box1).scale(1.2).next_to(title_orth,DOWN,buff=0.5)
        restrictive = Text("Restrictive",font_size=60,color=dark_red).next_to(box1,DOWN, buff=0.5)
        restrictive2 = Text("In some cases, there may not exist any pair of non-zero \nvectors that are orthogonal in the Roberts sense.",font_size=40,color=dark_green).next_to(restrictive,DOWN, buff=0.3)

        self.play(
            FadeIn(title_orth),
        )
        self.play(
            Create(box1),
            Write(roberts),
        )
        self.wait(0.5)
        self.play(
            Write(restrictive),
        )
        self.wait(0.5)
        self.play(
            Write(restrictive2),
        )
        self.wait(1.5)
        self.play(
            FadeOut(restrictive),
            FadeOut(restrictive2),
        )

        example1_part1 = MathTex(
            r"T = \{\, f : [0,1] \to \mathbb{R} \mid f(x) = ax^2 + bx,\; a,b \in \mathbb{R} \,\}.",
            color=BLACK,
        )
        example1_part2 = MathTex(
            r"\|ax^2 + bx\| = \max_{x \in (0,1)} |ax^2 + bx|.",
            color=BLACK,
        )
        example1_part3 = MathTex(
            r"\text{Two elements of T are orthogonal by Roberts' definition }",
            color=BLACK,
        )
        example1_part4 = MathTex(
            r"\Longleftrightarrow",
            color=BLACK,
        )
        example1_part5 = MathTex(
            r"\text{one of them is zero.}",
            color=BLACK,
        )
        text_example = Text("Example",font_size=40,color=dark_purple)

        example = VGroup(*[
            text_example,
            example1_part1,
            example1_part2,
            example1_part3,
            example1_part4,
            example1_part5,
        ]).arrange(DOWN,buff=0.3).next_to(box1, DOWN, buff=1).shift(0.6*UP)
        
        box2 = SurroundingRectangle(
            example,
            color=dark_purple,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Create(box2),
            Write(text_example),
            Write(example1_part1),
        )
        self.wait(0.5)
        self.play(
            Write(example1_part2),
        )
        self.wait(0.5)
        self.play(
            Write(example1_part3),
        )
        self.play(
            Write(example1_part4),
        )
        self.play(
            Write(example1_part5),
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                example,
                box2,
            ])),
        )
        self.wait(1)

        # proof and counterexample
        # sym
        # 1. Symmetry - Title
        symmetry_title = MathTex(r"\text{Symmetry}",color=dark_pink)
        
        # Symmetry - Statement
        symmetry_statement = MathTex(
            r"\text{If } x \perp_R y \text{, then } y \perp_R x",
            color=BLACK,
        )
        
        # Symmetry - Proof step 1
        symmetry_proof1 = MathTex(
            r"\|x + \lambda y\| = \|x - \lambda y\|",
            r"\Longleftrightarrow",
            r"|\lambda| \left\|\frac{x}{\lambda} + y\right\| = |\lambda| \left\|\frac{x}{\lambda} - y\right\|",
            color=BLACK,
        )
        
        # Symmetry - Proof step 2
        # symmetry_proof2 = MathTex(
        #     r"|\lambda| \left\|\frac{x}{\lambda} + y\right\| = |\lambda| \left\|\frac{x}{\lambda} - y\right\|",
        #     color=BLACK,
        # )
        
        # Symmetry - Proof step 3
        symmetry_proof3 = MathTex(
            r"\Longleftrightarrow",
            r"\left\|y + \frac{1}{\lambda}x\right\| = \left\|y - \frac{1}{\lambda}x\right\|",
            r"\quad \text{Let } \mu = \frac{1}{\lambda}",
            color=BLACK,
        )
        symmetry_proof3.set_color_by_tex(r"\text{Let } \mu = \frac{1}{\lambda}",dark_pink)
        
        # Symmetry - Proof step 4
        # symmetry_proof4 = MathTex(
        #     r"\text{Let } \mu = \frac{1}{\lambda}",
        #     color=dark_pink,
        # )
        
        # Symmetry - Proof step 5
        symmetry_proof5 = MathTex(
            r"\forall \mu \neq 0: \|y + \mu x\| = \|y - \mu x\|",
            # r"\longleftrightarrow",
            r"\quad \therefore y \perp_R x \quad . \blacksquare",
            color=BLACK,
        )
        
        # Symmetry - Conclusion
        # symmetry_conclusion = MathTex(
        #     r"\therefore y \perp_R x \quad . \blacksquare",
        #     color=BLACK,
        # )

        sym = VGroup(*[
            symmetry_title,
            symmetry_statement,
            symmetry_proof1,
            # symmetry_proof2,
            symmetry_proof3,
            # symmetry_proof4,
            symmetry_proof5,
            # symmetry_conclusion,
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        homogeneity_title = MathTex(r"\text{Homogeneity}",color=dark_purple)
        
        # Homogeneity - Statement
        homogeneity_statement = MathTex(
            r"\text{If } x \perp_R y \text{, then } (\alpha x) \perp_R (\beta y) \text{ for } \alpha, \beta \neq 0",
            color=BLACK,
        )
        
        # Homogeneity - Proof step 1
        homogeneity_proof1 = MathTex(
            r"\|\alpha x + \mu(\beta y)\| = \|\alpha x - \mu(\beta y)\|",
            color=BLACK,
        )
        
        # Homogeneity - Proof step 2
        homogeneity_proof2 = MathTex(
            r"|\alpha| \cdot \left\|x + \frac{\mu\beta}{\alpha}y\right\| = |\alpha| \cdot \left\|x - \frac{\mu\beta}{\alpha}y\right\|",
            r"\quad \text{Let } \lambda = \frac{\mu\beta}{\alpha}",
            color=BLACK,
        )
        homogeneity_proof2.set_color_by_tex(r"\quad \text{Let } \lambda = \frac{\mu\beta}{\alpha}",dark_purple)
        
        # Homogeneity - Proof step 3
        # homogeneity_proof3 = MathTex(
        #     r"\|\alpha x - (\mu\beta)y\| = |\alpha| \cdot \left\|x - \frac{\mu\beta}{\alpha}y\right\|"
        # )
        
        # Homogeneity - Proof step 4
        # homogeneity_proof4 = MathTex(
        #     r"\text{Let } \lambda = \frac{\mu\beta}{\alpha}",
        #     color=dark_purple,
        # )
        
        # Homogeneity - Conclusion
        homogeneity_conclusion = MathTex(
            r"\text{Since } x \perp_R y \text{, equality holds} \quad . \blacksquare",
            color=BLACK,
        )

        homo = VGroup(*[
            homogeneity_title,
            homogeneity_statement,
            homogeneity_proof1,
            homogeneity_proof2,
            # homogeneity_proof3,
            # homogeneity_proof4,
            # homogeneity_proof5,
            homogeneity_conclusion,
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(homo),
        )
        self.wait(1)
        self.play(
            FadeOut(homo),
        )

        nonadditivity_title = MathTex(r"\text{Non-Additivity Counterexample}",color=dark_terquise)

        # Non-Additivity - Space
        nonadditivity_space = MathTex(
            r"\text{Space: } \mathbb{R}^3 \text{ with } \ell^\infty \text{ norm: } \|(v_1,v_2,v_3)\|_\infty = \max(|v_1|,|v_2|,|v_3|)",
            color=BLACK,
        )

        # Non-Additivity - Vectors
        nonadditivity_vectors = MathTex(
            r"x = (1,1,1), \quad y = (1,-1,0), \quad z = (1,0,-1)",
            color=BLACK,
        )

        # Check x ⊥_R y - Title
        check_xy_title = MathTex(
            r"\text{Check } x \perp_R y:",
            color=BLACK,
        )

        # Check x ⊥_R y - Step 1
        check_xy_step1 = MathTex(
            r"\|x - \lambda y\|_\infty = \max(|1-\lambda|, |1+\lambda|, |1|)",
            color=BLACK,
        )

        # Check x ⊥_R y - Step 2
        check_xy_step2 = MathTex(
            r"\|x + \lambda y\|_\infty = \max(|1+\lambda|, |1-\lambda|, |1|)",
            color=BLACK,
        )

        # Check x ⊥_R y - Conclusion
        # check_xy_conclusion = MathTex(
        #     r"\text{Equal, so } x \perp_R y"
        # )

        # Check x ⊥_R z - Title
        check_xz_title = MathTex(
            r"\text{Check } x \perp_R z:",
            color=BLACK,
        )

        # Check x ⊥_R z - Step 1
        check_xz_step1 = MathTex(
            r"\|x - \lambda z\|_\infty = \max(|1-\lambda|, |1|, |1+\lambda|)",
            color=BLACK,
        )

        # Check x ⊥_R z - Step 2
        check_xz_step2 = MathTex(
            r"\|x + \lambda z\|_\infty = \max(|1+\lambda|, |1|, |1-\lambda|)",
            color=BLACK,
        )

        # Check x ⊥_R z - Conclusion
        # check_xz_conclusion = MathTex(
        #     r"\therefore x \perp_R z"
        # )

        # Check x ⊥_R (y+z) - Title
        # check_xyz_title = MathTex(r"\text{Check } x \perp_R (y+z):")

        # Sum y+z
        # sum_yz = MathTex(
        #     r"y + z = (2,-1,-1)"
        # )

        # Check for λ=1 - Step 1
        # check_lambda1_step1 = MathTex(
        #     r"x - 1(y+z) = (1-2, 1-(-1), 1-(-1)) = (-1,2,2)"
        # )

        # Check for λ=1 - Norm 1
        check_lambda1_norm1 = MathTex(
            r"\|x - (y+z)\|_\infty = 2",
            r"\quad \|x + (y+z)\|_\infty = 3",
            color=BLACK,
        )

        # Check for λ=1 - Step 2
        # check_lambda1_step2 = MathTex(
        #     r"x + 1(y+z) = (1+2, 1+(-1), 1+(-1)) = (3,0,0)"
        # )

        # Check for λ=1 - Norm 2
        # check_lambda1_norm2 = MathTex(
        #     r"\|x + (y+z)\|_\infty = 3"
        # )

        # Inequality
        inequality = MathTex(
            r"2 \neq 3",
            color=dark_terquise,
        )

        # Final conclusion
        # final_conclusion = MathTex(
        #     r"\therefore x \not\perp_R (y+z) \quad \text{(Additivity fails)}"
        # )

        add = VGroup(*[
            nonadditivity_title,
            nonadditivity_space,
            nonadditivity_vectors,
            VGroup(*[
                VGroup(*[
                    check_xy_title,
                    check_xy_step1,
                    check_xy_step2,
                ]).arrange(DOWN,buff=0.2).scale(0.5).shift(1*LEFT),
                VGroup(*[
                    check_xz_title,
                    check_xz_step1,
                    check_xz_step2,
                ]).arrange(DOWN,buff=0.2).scale(0.5).shift(1*LEFT),
            ]).arrange(RIGHT,buff=0.5),
            check_lambda1_norm1,
            inequality,
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(add),
        )
        self.wait(1)
        self.play(
            FadeOut(add),
        )

        scalar_existence_title = MathTex(r"\text{Scalar Existence Counterexample}", color=dark_green)

        # Scalar Existence - Space
        scalar_existence_space = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with } \ell^\infty \text{ norm: } \|(u,w)\|_\infty = \max(|u|,|w|)",
            color=BLACK,
        )

        # Scalar Existence - Claim
        scalar_existence_claim = MathTex(
            r"\text{Claim: } \forall x,y \, \exists a \in \mathbb{R} \text{ such that } x \perp_R (ax+y)",
            color=BLACK,
        )

        # Scalar Existence - Vectors
        scalar_existence_vectors = MathTex(
            r"x = (1, 0.5), \quad y = (0, 1)",
            color=BLACK,
        )

        # Setup - z definition
        setup_z_title = MathTex(
            r"\text{Assume such } a \text{ exists,} \\ \text{let } z = ax+y = (a,\, 0.5a+1)",
            color=BLACK,
        )

        # Roberts condition
        roberts_condition = MathTex(
            r"\|x+\lambda z\|_\infty = \|x-\lambda z\|_\infty \quad \forall \lambda \in \mathbb{R}",
            color=BLACK,
        )

        # Step 1 - Title
        step1_title = MathTex(
            r"\text{Step 1: Small } \lambda > 0",
            color=BLACK,
        )

        # Step 1 - Reduction
        step1_reduction = MathTex(
            r"|1+\lambda a| = |1-\lambda a| \implies 2\lambda a = 0",
            color=BLACK,
        )

        # Step 1 - Conclusion
        step1_conclusion = MathTex(
            r"\implies a = 0",
            color=BLACK,
        )

        # Step 2 - Title
        step2_title = MathTex(
            r"\text{Step 2: Test } a=0 \text{ with } \lambda = 1",
            color=BLACK,
        )

        # Step 2 - Equation
        step2_equation = MathTex(
            r"\max(|1|,|0.5+\lambda|) = \max(|1|,|0.5-\lambda|)",
            color=BLACK,
        )

        # Step 2 - Evaluation
        step2_evaluation = MathTex(
            r"\max(1, 1.5) = 1.5 \quad , \quad \max(1, 0.5) = 1",
            color=BLACK,
        )

        # Inequality
        inequality = MathTex(
            r"1.5 \neq 1",
            color=dark_green,
        )

        scalar_existence = VGroup(*[
            scalar_existence_title,
            scalar_existence_space,
            scalar_existence_claim,
            VGroup(*[
                VGroup(*[
                    scalar_existence_vectors,
                    setup_z_title,
                    roberts_condition,
                ]).arrange(DOWN, buff=0.2).scale(0.6).shift(1*LEFT),
                VGroup(*[
                    step1_title,
                    step1_reduction,
                    step1_conclusion,
                ]).arrange(DOWN, buff=0.2).scale(0.5).shift(1*LEFT),
                VGroup(*[
                    step2_title,
                    step2_equation,
                    step2_evaluation,
                ]).arrange(DOWN, buff=0.2).scale(0.5).shift(1*LEFT),
            ]).arrange(RIGHT, buff=0.5),
            inequality,
        ]).arrange(DOWN, buff=0.3).next_to(box1, DOWN, buff=0.3)

        self.play(
            Write(scalar_existence),
        )
        self.wait(1)
        self.play(
            FadeOut(scalar_existence),
        )


        headers = [
            (r"\text{Symmetry}", dark_pink),
            (r"\text{Homogeneity}", dark_purple),
            (r"\text{Additivity}", dark_terquise),
            (r"\text{Scalar Existence}", dark_green),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        cross = MathTex(r"\Large \times").set_color(RED)
        check = MathTex(r"\Large \checkmark").set_color(GREEN)
        
        row = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
        ]
        
        row_label = MathTex(r"\text{Roberts}", color=BLACK)

        table = MobjectTable(
            [row],
            row_labels=[row_label],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        )

        table.scale(1).next_to(box1,DOWN,buff=0.5)

        self.play(
            Create(table),
            run_time = 3,
        )
        self.wait(1)

        self.play(
            FadeOut(table),
            FadeOut(VGroup(*[
                box1,
                roberts,
                title_orth,
            ])),
        )

        self.wait(1)


    def define_properties(self, title):
        start = MathTex(
            r"\text{For all } x,y,z \in X \text{ and , For all } \alpha,\beta \in \mathbb{K} ",
            color=BLACK
        ).scale(1.2)
        sym = MathTex(
            r"\text{Symmetry }",r"\text{: If } x \perp y,\ \text{then } y \perp x.",
            color=BLACK,
        ).scale(1.2)
        sym.set_color_by_tex(r"\text{Symmetry }", dark_pink)
        boxsym = SurroundingRectangle(
            sym,
            color=dark_pink,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        homo = MathTex(
            r"\text{Homogeneity }",r"\text{: If } x \perp y,\ \text{then } (\alpha x) \perp (\beta y).",
            color=BLACK,
        ).scale(1.2)
        homo.set_color_by_tex(r"\text{Homogeneity }", dark_purple)
        boxhomo = SurroundingRectangle(
            homo,
            color=dark_purple,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        add = MathTex(
            r"\text{Additivity }",r"\text{: If } x \perp y \ \text{and}\ x \perp z \ \text{, then } x \perp (y+z).",
            color=BLACK,
        ).scale(1.1)
        add.set_color_by_tex(r"\text{Additivity }", dark_terquise)
        boxadd = SurroundingRectangle(
            add,
            color=dark_terquise,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        scaler1 = MathTex(
            r"\text{Scalar Existence Property }",r"\text{: There exists } a \in \mathbb{K} ",
            color=BLACK,
        ).scale(1.1)
        scaler1.set_color_by_tex(r"\text{Scalar Existence Property }", dark_green)
        scaler2 = MathTex(
            r"\text{ such that } x \perp (ax + y).",
            color=BLACK,
        ).scale(1.1)
        boxscaler = SurroundingRectangle(
            VGroup(scaler1, scaler2).arrange(DOWN,buff=0.2),
            color=dark_green,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        all = VGroup(*[
            start,
            VGroup(sym, boxsym),
            VGroup(homo, boxhomo),
            VGroup(add, boxadd),
            VGroup(VGroup(scaler1, scaler2), boxscaler),
        ]).arrange(DOWN,buff=0.5)

        self.play(
            Write(start),
        )
        self.wait(0.5)
        self.play(
            Create(boxsym),
            Write(sym),
        )
        self.wait(0.5)
        self.play(
            Create(boxhomo),
            Write(homo),
        )
        self.wait(0.5)
        self.play(
            Create(boxadd),
            Write(add),
        )
        self.wait(0.5)
        self.play(
            Create(boxscaler),
            Write(VGroup(scaler1, scaler2)),
        )

        self.wait(1)

        self.play(
            FadeOut(all),
        )

    def scene8_SubScene4(self, title):
        title_orth = Tex("Birkhoff-James Orthogonality", color=BLACK, font_size=80).to_edge(UP)

        year_text = Tex("1935 - George David Birkhoff",color=BLACK,font_size=65).next_to(title_orth, DOWN,buff=0.5)
        b_image = ImageMobject("images/George_David_Birkhoff.png").scale(3).next_to(year_text,DOWN,buff=0.5)
        
        """
        wo elements x and y of X are said to be orthogonal in
        the sense of Birkhoff if and only if ‖x‖ ≤ ‖x + λy‖ , ∀λ ∈ R
        """
        robert_def_part1 = MathTex(
            r"\text{Two elements } x \text{ and } y \text{ in a Banach space } X \text{ are said to}",
            color=BLACK,
        )
        robert_def_part2 = MathTex(
            r"\text{be orthogonal in the sense of Birkhoff-James if and only if}",
            color=BLACK,
        )
        robert_def_part3 = MathTex(
            r"\|x\| \le \|x + \lambda y\| \quad \text{for all } \lambda \in \mathbb{R}",
            color=BLACK,
        )
        robert_def_part4 = MathTex(
            r"\text{and denote it by } x \perp_{BJ} y.",
            color=BLACK,
        )
        robert_def = VGroup(robert_def_part1, robert_def_part2, robert_def_part3, robert_def_part4).arrange(DOWN,buff=0.3)
        group, box = self.show_definition(robert_def, title_orth, True)
        VGroup(group, box).scale(1).shift(1*UP)

        self.play(
            Write(title_orth),
        )
        self.wait(0.5)
        self.play(
            Write(year_text),
        )
        self.add(b_image)
        self.wait(0.5)
        self.play(
            FadeOut(year_text),
            FadeOut(b_image),
        )
        self.play(
            Create(box),
            Write(group),
        )
        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(group),
            FadeOut(box),
        )
        self.wait(1)

    def scene8_SubScene5(self, title):
        self.wait(0.5)
        image = ImageMobject("images/book_brain.png").scale(2).to_corner(DL)
        self.add(image)

        title_orth = Tex("Birkhoff-James Orthogonality", color=dark_blue, font_size=60).to_corner(UL).shift(0.15*UP)

        plane = NumberPlane(
            y_range=[-5, 7, 1],
            x_range=[-4, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=7,
            x_length=9,
        ).move_to([0, 0, 0] + 0.5 * DOWN)

        axes = Axes(
            y_range=[-5, 7, 1],
            y_length=7,
            x_range=[-4, 8, 1],
            x_length=9,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length": 0.25, "tip_shape": StealthTip}
        ).move_to([0, 0, 0] + 0.5 * DOWN)

        x_point = np.array([3, 0, 0])  # نقطه ساده روی محور x
        arrow_x = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(3, 0),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        circle = Circle(
            radius=3 * axes.x_axis.unit_size,
            color=dark_orange,
            stroke_width=4
        ).move_to(axes.c2p(0, 0))

        dot_x = Dot(
            axes.c2p(3, 0),
            color=dark_green,
            radius=0.12,
        )

        arrow_y = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(0, 2),
            buff=0,
            stroke_width=3,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        tangent_line = DashedLine(
            start=axes.c2p(3, -7),
            end=axes.c2p(3, 7),
            color=dark_purple,
            stroke_width=3,
            dash_length=0.15
        )

        arc_orthogonal = RightAngle(
            arrow_y,
            arrow_x,
            length=0.3,
            color=BLACK,
            # quadrant=(1,-1)
        )

        x_text = MathTex(r"\vec{x}", color=dark_red).scale(1.2).next_to(
            axes.c2p(1.5, 0), direction=UP, buff=0.1
        )

        y_text = MathTex(r"\vec{y}", color=dark_pink).scale(1.2).next_to(
            axes.c2p(-0.35, 2), direction=UP, buff=0.1
        )

        radius_text = MathTex(r"\|\vec{x}\|", color=dark_red).scale(1.0).next_to(
            axes.c2p(1.5, 0), direction=DOWN, buff=0.1
        )

        tangent_text = MathTex(r"\vec{x} + \lambda \vec{y}", color=dark_purple).scale(1.0).next_to(
            axes.c2p(3, 5), direction=RIGHT, buff=0.15
        )

        # moving_dot = Dot(
        #     # axes.c2p(0, 0),
        #     axes.c2p(3, 6),
        #     color=dark_green,
        #     radius=0.12,
        # )

        all_shapes = VGroup(*[
            plane,
            axes,
            circle,
            arrow_x,
            arrow_y,
            tangent_line,
            # dot_x,
            x_text,
            y_text,
            radius_text,
            tangent_text,
            arc_orthogonal
        ]).shift(2*RIGHT)

        dot_x.shift(2*RIGHT)

        moving_arrow = always_redraw(
            lambda: Arrow(
                start=axes.c2p(0, 0),
                end=dot_x.get_center(),
                buff=0,
                stroke_width=6,
                color=dark_terquise,
                tip_length=0.25,
                tip_shape=StealthTip
            )
        )

        moving_label = always_redraw(
            lambda: MathTex(r"\vec{x} + \lambda \vec{y}", color=dark_terquise).scale(1.0).next_to(
                dot_x.get_center(), direction=RIGHT, buff=0.25
            )
        )

        roberts = MathTex(
            r"\|\vec{x}\| ",r"\le ",r"\|\vec{x} + \lambda \vec{y}\|",
            color = BLACK,
        )
        roberts.set_color_by_tex(r"\|\vec{x}\| ",dark_red)
        roberts.set_color_by_tex(r"\|\vec{x} + \lambda \vec{y}\|",dark_purple)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        VGroup(roberts, box1).scale(1.2).to_corner(UL).shift(1*DOWN)

        self.play(
            Write(title_orth),
            Create(box1),
            Write(roberts),
        )
        self.play(
            Create(plane),
            Create(axes),
        )
        self.play(
            FadeIn(dot_x),
        )
        self.play(
            GrowArrow(arrow_x),
            Write(x_text),
        )
        self.wait(0.3)
        self.play(
            TransformFromCopy(roberts[0], radius_text),
        )
        self.wait(0.3)
        self.play(
            Create(circle),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(arrow_y),
            Write(y_text),
        )
        self.play(
            Create(arc_orthogonal),
        )
        self.wait(0.5)
        self.play(
            Create(tangent_line),
            Write(tangent_text),
        )
        self.wait(0.5)
        self.play(
            FadeIn(moving_arrow),
            Write(moving_label),
        )
        self.wait(0.5)

        self.play(
            dot_x.animate.move_to(axes.c2p(3, 6)),
            run_time=3,
            rate_func=smooth
        )
        self.wait(0.5)

        self.play(
            dot_x.animate.move_to(axes.c2p(3, -5)),
            run_time=3,
            rate_func=smooth
        )
        self.wait(0.5)

        self.play(
            dot_x.animate.move_to(axes.c2p(3, 0)),
            run_time=2,
            rate_func=smooth
        )
        self.wait(1)

        self.play(
            FadeOut(dot_x),
            FadeOut(moving_arrow),
            FadeOut(moving_label),
        )
        self.wait(1.5)
        self.play(
            FadeOut(title_orth),
            FadeOut(all_shapes),
            FadeOut(roberts),
            FadeOut(box1),
            FadeOut(image),
        )
        self.wait(1)

    def scene8_SubScene7(self, title):
        title_orth = Tex("Isosceles Orthogonality", color=BLACK, font_size=80).to_edge(UP)

        year_text = Tex("1945 - Robert C. James",color=BLACK,font_size=65).next_to(title_orth, DOWN,buff=0.5)
        robert_image = ImageMobject("images/Robert_C._James.png").scale(2).shift(1.5*DOWN)

        robert_def_part1 = MathTex(
            r"\text{Two elements } x \text{ and } y \text{ in a Banach space } X \text{ are said to}",
            color=BLACK,
        )
        robert_def_part2 = MathTex(
            r"\text{be orthogonal in the sense of Isosceles if and only if}",
            color=BLACK,
        )
        robert_def_part3 = MathTex(
            r"\|x + y \| = \|x - y\|",
            color=BLACK,
        )
        robert_def_part4 = MathTex(
            r"\text{and denote it by } x \perp_{I} y.",
            color=BLACK,
        )
        robert_def = VGroup(robert_def_part1, robert_def_part2, robert_def_part3, robert_def_part4).arrange(DOWN,buff=0.3)
        group, box = self.show_definition(robert_def, title_orth, True)
        VGroup(group, box).scale(1.1).shift(1*UP)

        self.play(
            Write(title_orth),
        )
        self.wait(0.5)
        self.play(
            Write(year_text),
            FadeIn(robert_image),
        )
        self.wait(0.5)
        self.play(
            FadeOut(year_text),
            FadeOut(robert_image),
        )
        self.play(
            Create(box),
            Write(group),
        )
        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(group),
            FadeOut(box),
        )
        self.wait(1)

    def scene8_SubScene10(self, title):
        title_orth = Tex("Pythagorean Orthogonality", color=BLACK, font_size=80).to_edge(UP)

        year_text = Tex("1945 - Robert C. James",color=BLACK,font_size=65).next_to(title_orth, DOWN,buff=0.5)
        robert_image = ImageMobject("images/Robert_C._James.png").scale(2).shift(1.5*DOWN)

        robert_def_part1 = MathTex(
            r"\text{Two elements } x \text{ and } y \text{ in a Banach space } X \text{ are said to}",
            color=BLACK,
        )
        robert_def_part2 = MathTex(
            r"\text{be orthogonal in the sense of Pythagorean if and only if}",
            color=BLACK,
        )
        robert_def_part3 = MathTex(
            r"\|x + y \|^2 = \|x\|^2 + \|y\|^2",
            color=BLACK,
        )
        robert_def_part4 = MathTex(
            r"\text{and denote it by } x \perp_{P} y.",
            color=BLACK,
        )
        robert_def = VGroup(robert_def_part1, robert_def_part2, robert_def_part3, robert_def_part4).arrange(DOWN,buff=0.3)
        group, box = self.show_definition(robert_def, title_orth, True)
        VGroup(group, box).scale(1.1).shift(1*UP)

        self.play(
            Write(title_orth),
        )
        self.wait(0.5)
        self.play(
            Write(year_text),
            FadeIn(robert_image),
        )
        self.wait(0.5)
        self.play(
            FadeOut(year_text),
            FadeOut(robert_image),
        )
        self.play(
            Create(box),
            Write(group),
        )
        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(group),
            FadeOut(box),
        )
        self.wait(1)

    def scene8_SubScene8(self, title):
        self.wait(0.5)
        image = ImageMobject("images/book_brain.png").scale(2).to_corner(DL)
        self.add(image)

        title_orth = Tex("Isosceles Orthogonality", color=dark_blue, font_size=60).to_corner(UL).shift(0.15*UP)

        plane = NumberPlane(
            y_range=[-5, 7, 1],
            x_range=[-4, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=8,
        ).move_to([0, 0, 0] + 0.5 * DOWN)

        axes = Axes(
            y_range=[-5, 7, 1],
            y_length=8,
            x_range=[-4, 8, 1],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length": 0.25, "tip_shape": StealthTip}
        ).move_to([0, 0, 0] + 0.5 * DOWN)

        x_point = np.array([3, 0, 0])
        arrow_x = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(4, 2),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow_x_inv = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(-4, -2),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow_y = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(-2, 4),
            buff=0,
            stroke_width=3,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        tangent_line1 = Arrow(
            start=arrow_y.get_end(),
            end=arrow_x.get_end(),
            buff=0,
            stroke_width=4,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        tangent_line2 = Arrow(
            start=arrow_x_inv.get_end(),
            end=arrow_y.get_end(),
            buff=0,
            stroke_width=4,
            color=dark_purple,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arc_orthogonal = RightAngle(
            arrow_y,
            arrow_x,
            length=0.3,
            color=BLACK,
            # quadrant=(1,-1)
        )

        x_text = MathTex(r"\vec{x}", color=dark_green).scale(1.0).next_to(
            arrow_x.get_center(), direction=DOWN, buff=0.15
        )

        y_text = MathTex(r"\vec{y}", color=dark_pink).scale(1.0).next_to(
            arrow_y, direction=UP, buff=0.1
        )

        x_inv_text = MathTex(r" - \vec{x}", color=dark_green).scale(1.0).next_to(
            arrow_x_inv.get_center(), direction=DOWN, buff=0.15
        )

        tangent_text1 = MathTex(r"\vec{x} - \vec{y}", color=dark_red).scale(1.0).next_to(
            tangent_line1.get_center(), direction=UR , buff=0.15
        )

        tangent_text2= MathTex(r"\vec{x} + \vec{y}", color=dark_purple).scale(1.0).next_to(
            tangent_line2.get_center(), direction=UL , buff=0.15
        )

        mark1_1 = Line(ORIGIN, 0.2*UP, color=BLACK, stroke_width=5).rotate(
            tangent_line1.get_angle()
        ).move_to(tangent_line1.point_from_proportion(0.5))

        mark2_1 = Line(ORIGIN, 0.2*UP, color=BLACK, stroke_width=5).rotate(
            tangent_line2.get_angle()
        ).scale(1.2).move_to(tangent_line2.point_from_proportion(0.5))

        equality_marks = VGroup(mark1_1, mark2_1)

        all_shapes = VGroup(*[
            plane,
            axes,
            arrow_x,
            arrow_x_inv,
            arrow_y,
            tangent_line1,
            tangent_line2,
            x_text,
            y_text,
            x_inv_text,
            tangent_text1,
            tangent_text2,
            arc_orthogonal,
            equality_marks,
        ]).shift(2*RIGHT)

        roberts = MathTex(
            r"\|\vec{x} - \vec{y}\| ",r"= ",r"\|\vec{x} + \vec{y}\|",
            color = BLACK, 
        )
        roberts.set_color_by_tex(r"\|\vec{x} - \vec{y}\| ",dark_red)
        roberts.set_color_by_tex(r"\|\vec{x} + \vec{y}\|",dark_purple)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        VGroup(roberts, box1).scale(1.2).to_corner(UL).shift(1*DOWN)

        self.play(
            Write(title_orth),
            Create(box1),
            Write(roberts),
        )
        self.play(
            Create(plane),
            Create(axes),
        )
        self.play(
            GrowArrow(arrow_x),
            Write(x_text),
        )
        self.wait(0.3)
        self.play(
            GrowArrow(arrow_y),
            Write(y_text),
        )
        self.play(
            Create(arc_orthogonal),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(arrow_x_inv),
            Write(x_inv_text),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(tangent_line1),
            Write(tangent_text1),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(tangent_line2),
            Write(tangent_text2),
        )
        self.wait(0.5)
        self.play(
            Create(equality_marks),
        )

        self.wait(1.5)
        self.play(
            FadeOut(title_orth),
            FadeOut(all_shapes),
            FadeOut(roberts),
            FadeOut(box1),
            FadeOut(image),
        )
        self.wait(1)

    def scene8_SubScene11(self, title):
        self.wait(0.5)
        image = ImageMobject("images/book_brain.png").scale(2).to_corner(DL)
        self.add(image)

        title_orth = Tex("Pythagorean Orthogonality", color=dark_blue, font_size=60).to_corner(UL).shift(0.15*UP)

        plane = NumberPlane(
            y_range=[-5, 7, 1],
            x_range=[-4, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=8,
        ).move_to([0, 0, 0] + 1.5 * DOWN)

        axes = Axes(
            y_range=[-5, 7, 1],
            y_length=8,
            x_range=[-4, 8, 1],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length": 0.25, "tip_shape": StealthTip}
        ).move_to([0, 0, 0] + 1.5 * DOWN)

        arrow_x = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(4, 0),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow_y = Arrow(
            start=axes.c2p(4, 0),
            end=axes.c2p(4, 3),
            buff=0,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow_sum = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(4, 3),
            buff=0,
            stroke_width=3,
            color=dark_purple,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arc_orthogonal = RightAngle(
            arrow_y,
            arrow_x,
            length=0.3,
            color=BLACK,
            quadrant=(1,-1)
        )

        x_text = MathTex(r"\vec{x}", color=dark_green).scale(1.0).next_to(
            arrow_x.get_center(), direction=DOWN, buff=0.15
        )

        y_text = MathTex(r"\vec{y}", color=dark_pink).scale(1.0).next_to(
            arrow_y, direction=UP, buff=0.1
        )

        x_sum = MathTex(r" \vec{x} + \vec{y}", color=dark_purple).scale(1.0).next_to(
            arrow_sum.get_center()+0.4*LEFT, direction=UP, buff=0.15
        )

        all_shapes = VGroup(*[
            plane,
            axes,
            arrow_x,
            arrow_sum,
            arrow_y,
            x_text,
            y_text,
            x_sum,
            arc_orthogonal,
        ]).shift(2*RIGHT)

        roberts = MathTex(
            r"\|\vec{x} + \vec{y}\|^2 ",r" = ",r"\|\vec{x}\|^2",r" + ",r"\|\vec{y}\|^2",
            color = BLACK, 
        )
        roberts.set_color_by_tex(r"\|\vec{x} + \vec{y}\|^2 ",dark_purple)
        roberts.set_color_by_tex(r"\|\vec{x}\|^2",dark_green)
        roberts.set_color_by_tex(r"\|\vec{y}\|^2",dark_pink)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        VGroup(roberts, box1).scale(1.2).to_corner(UL).shift(1*DOWN)

        self.play(
            Write(title_orth),
            Create(box1),
            Write(roberts),
        )
        self.play(
            Create(plane),
            Create(axes),
        )
        self.play(
            GrowArrow(arrow_x),
            Write(x_text),
        )
        self.wait(0.3)
        self.play(
            GrowArrow(arrow_y),
            Write(y_text),
        )
        self.play(
            Create(arc_orthogonal),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(arrow_sum),
            Write(x_sum),
        )

        self.wait(1.5)
        self.play(
            FadeOut(title_orth),
            FadeOut(all_shapes),
            FadeOut(roberts),
            FadeOut(box1),
            FadeOut(image),
        )
        self.wait(1)

    def han_banakh_shape(self, title):
        axes = ThreeDAxes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-3.5, 3.5, 1],
            z_range=[-2.5, 2.5, 1],
            x_length=9, y_length=9, z_length=6.5,
            color = dark_terquise,
        )
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES, distance=7)
 
        # main_title = Text(
        #     "Hahn-Banach Theorem",
        #     font_size=30,
        #     color=BLACK,
        # ).to_edge(UP)
        # self.add_fixed_in_frame_mobjects(main_title)
        # self.play(Write(main_title))
        # self.wait(0.5)
 
        floor = Surface(
            lambda u, v: axes.c2p(u, v, 0),
            u_range=[-3, 3], v_range=[-3, 3],
            resolution=(1, 1),
            fill_color=dark_blue, fill_opacity=0.25,
            stroke_color=dark_blue, stroke_width=1,
            checkerboard_colors=[dark_blue, dark_blue],
        )
        X_label = MathTex("X", color=dark_blue).move_to(axes.c2p(3.3, 3.3, 0))
        self.add_fixed_orientation_mobjects(X_label)
 
        self.play(Create(floor))
        self.play(Write(X_label))
        self.wait(0.5)
 
        line_M = Line3D(
            start=axes.c2p(-3, 0, 0), end=axes.c2p(3, 0, 0),
            color=dark_red, thickness=0.03,
        )
        M_label = MathTex("M", color=dark_red).move_to(axes.c2p(3.3, -0.4, 0))
        self.add_fixed_orientation_mobjects(M_label)
 
        self.play(Create(line_M))
        self.play(Write(M_label))
        self.wait(1)
 
 
        P_SLOPE = 0.6  # شیب چادر (سوپلینیر/همگن نوع نُرم)
 
        def p(x, y):
            return P_SLOPE * np.sqrt(x ** 2 + y ** 2)
 
        tent = Surface(
            lambda u, v: axes.c2p(u, v, p(u, v)),
            u_range=[-3, 3], v_range=[-3, 3],
            resolution=(28, 28),
            fill_opacity=0.35,
            checkerboard_colors=[GREY_C, GREY_D],
            stroke_color=GREY_D, stroke_width=0.5,
        )
        p_label = MathTex("z = p(x)", color=BLACK).move_to(axes.c2p(0, 3.6, 2.1))
        self.add_fixed_orientation_mobjects(p_label)
 
        self.play(Create(tent), run_time=2.5)
        self.play(Write(p_label))
 
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(0.5)
 
 
        F_SLOPE_ON_M = 0.5  # باید |F_SLOPE_ON_M| <= P_SLOPE باشد تا زیر چادر بماند
 
        def f(x):
            return F_SLOPE_ON_M * x
 
        line_f = Line3D(
            start=axes.c2p(-3, 0, f(-3)), end=axes.c2p(3, 0, f(3)),
            color=dark_green, thickness=0.035,
        )
        f_label = MathTex("f(x)", color=dark_green).move_to(axes.c2p(3.4, 0, f(3) + 0.35))
        self.add_fixed_orientation_mobjects(f_label)
 
        origin_dot = Dot3D(axes.c2p(0, 0, 0), color=BLACK, radius=0.05)
 
        self.play(Create(line_f), FadeIn(origin_dot))
        self.play(Write(f_label))
        self.wait(1)
 
        C_Y = 0.2
        assert np.sqrt(F_SLOPE_ON_M ** 2 + C_Y ** 2) <= P_SLOPE + 1e-9
 
        def F(x, y):
            return F_SLOPE_ON_M * x + C_Y * y
 
        plane_F = Surface(
            lambda u, v: axes.c2p(u, v, F(u, v)),
            u_range=[-3, 3], v_range=[-3, 3],
            resolution=(1, 1),
            fill_color=dark_purple, fill_opacity=0.55,
            stroke_color=light_purple, stroke_width=1.5,
            checkerboard_colors=[dark_purple, dark_purple],
        )
        F_label = MathTex("F(X)", color=dark_purple).move_to(axes.c2p(-3.4, 3.2, F(-3, 3.2)))
        self.add_fixed_orientation_mobjects(F_label)
 
        self.play(Create(plane_F), run_time=2)
        self.play(Write(F_label))
 
        self.play(Indicate(line_f, color=dark_green, scale_factor=1.15))
        self.wait(0.5)
 
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        self.move_camera(
            phi=0,
            theta=-90 * DEGREES,
            gamma=0,
            run_time=2,
        )

        self.wait(1)
        self.clear()
        self.wait(1)

    def han_banakh_def(self, title):
        title_han = MathTex(r" \text{Hahn-Banach Theorem} ", color=BLACK, font_size=70).to_edge(UP)

        hb_part0 = MathTex(
            r"\text{Let } X \text{ be a vector space, and let}",
            color=BLACK,
        )
        hb_part1 = MathTex(
            r"p : X \to \mathbb{R} \text{ be a sublinear function, (i.e., norm)}",
            color=BLACK,
        )
        # hb_part2 = MathTex(
        #     r"p(x+y) \le p(x) + p(y) \quad \text{and} \quad p(\alpha x) = \alpha \, p(x) \; \text{ for } \alpha \ge 0.",
        #     color=BLACK,
        # )
        hb_part3 = MathTex(
            r"\text{Let } M \text{ be a subspace of } X \text{, and let}",
            color=BLACK,
        )
        hb_part4 = MathTex(
            r"f : M \to \mathbb{R} \text{ be a linear functional satisfying}",
            color=BLACK,
        )
        hb_part5 = MathTex(
            r"f(x) \le p(x) \quad \text{for all } x \in M.",
            color=BLACK,
        )
        hb_part6 = MathTex(
            r"\text{Then there exists a linear functional } F : X \to \mathbb{R} \text{ such that}",
            color=BLACK,
        )
        # hb_part7 = MathTex(
        #     r"\text{such that}",
        #     color=BLACK,
        # )
        hb_part8 = MathTex(
            r"(HB1) \quad F(x) = f(x) \quad \text{for all } x \in M,",
            color=BLACK,
        )
        # hb_part9 = MathTex(
        #     r"\text{and}",
        #     color=BLACK,
        # )
        hb_part10 = MathTex(
            r"(HB2) \quad F(x) \le p(x) \quad \text{for all } x \in X.",
            color=BLACK,
        )

        hb_def = VGroup(
            hb_part0, hb_part1, #hb_part2,
            hb_part3, hb_part4, hb_part5,
            hb_part6, #hb_part7,
            hb_part8, hb_part10,
        ).arrange(DOWN)

        group, box = self.show_definition(hb_def, title_han, True)
        def_group = VGroup(group, box).scale(0.9).shift(3*UP)

        self.play(
            Write(title_han),
            Create(box),
            Write(group),
        )
        self.wait(1)

        self.play(
            FadeOut(title_han),
            FadeOut(group),
            FadeOut(box),
        )
        self.wait(1)

    def scene8_SubScene6(self, title):
        title_orth = Tex("Birkhoff-James Orthogonality", color=BLACK, font_size=70).to_edge(UP)

        roberts = MathTex(
            r"\|x\| ",r"\le ",r"\|x + \lambda y\|",r"\quad \text{ for all } \lambda \in \mathbb{K}",
            color = BLACK,
        ).next_to(title_orth,DOWN,buff=0.5)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        
        self.play(
            FadeIn(title_orth),
        )
        self.play(
            Create(box1),
            Write(roberts),
        )
        self.wait(0.5)

        # proof and counterexample
        nonsymmetry_title = MathTex(r"\text{Non-Symmetry Counterexample}",color=dark_pink)

        # Space definition
        nonsymmetry_space = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with } \ell^1 \text{ norm: } \|(u,v)\|_1 = |u| + |v|",
            color=BLACK,
        )

        # Vectors
        nonsymmetry_vectors = MathTex(
            r"x = (1,0), \quad y = (1,1)",
            color=BLACK,
        )

        # Part 1 title
        part1_title = MathTex(
            r"\text{Step 1: Show } x \perp_{BJ} y",
            color=BLACK,
        )

        # Part 1 - norm of x
        part1_norm_x = MathTex(
            r"\|x\|_1 = \|(1,0)\|_1 = |1| + |0| = 1",
            color=BLACK,
        )

        # Part 1 - norm of x + λy
        part1_norm_sum = MathTex(
            r"\|x + \lambda y\|_1 = \|(1+\lambda, \lambda)\|_1 = |1+\lambda| + |\lambda|",
            color=BLACK,
        )

        # Part 1 - inequality
        part1_inequality = MathTex(
            r"1 \leq |1+\lambda| + |\lambda| \quad \forall \lambda \in \mathbb{R}",
            color=BLACK,
        )

        # Part 1 - conclusion
        # part1_conclusion = MathTex(r"\therefore x \perp_{BJ} y")

        # Part 2 title
        part2_title = MathTex(
            r"\text{Step 2: Show } y \not\perp_{BJ} x",
            color=BLACK,
        )

        # Part 2 - norm of y
        part2_norm_y = MathTex(
            r"\|y\|_1 = \|(1,1)\|_1 = |1| + |1| = 2",
            color=BLACK,
        )

        # Part 2 - norm of y + λx
        part2_norm_sum = MathTex(
            r"\|y + \lambda x\|_1 = \|(1+\lambda, 1)\|_1 = |1+\lambda| + 1",
            color=BLACK,
        )

        # Part 2 - required condition
        part2_condition = MathTex(
            r"2 \leq |1+\lambda| + 1 \iff 1 \leq |1+\lambda|",
            color=BLACK,
        )

        # Part 2 - counterexample
        part2_counter = MathTex(
            r"\text{For } \lambda = -1: \quad |1+(-1)| = 0",
            color=dark_pink,
        )

        # Part 2 - inequality fails
        # part2_fails = MathTex(r"1 \leq 0 \quad \text{(False)}")

        # Part 2 - conclusion
        # part2_conclusion = MathTex(r"\therefore y \not\perp_{BJ} x")

        sym = VGroup(*[
            nonsymmetry_title,
            nonsymmetry_space,
            nonsymmetry_vectors,
            VGroup(*[
                VGroup(*[
                    part1_title,
                    part1_norm_x,
                    part1_norm_sum,
                    part1_inequality,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    part2_title,
                    part2_norm_y,
                    part2_norm_sum,
                    part2_condition,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
            ]).arrange(RIGHT,buff=0.5),
            part2_counter,
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        homogeneity_title = MathTex(r"\text{Homogeneity}",color=dark_purple)

        # Statement
        homogeneity_statement = MathTex(
            r"\text{If } x \perp_{BJ} y, \text{ then } (\alpha x) \perp_{BJ} (\beta y) \quad \forall \alpha, \beta \in \mathbb{R}",
            color=BLACK,
        )

        # Assumption
        homogeneity_assumption = MathTex(
            r"\text{Assume } x \perp_{BJ} y: \quad \|x\| \leq \|x + \lambda y\| \quad \forall \lambda \in \mathbb{R}",
            color=BLACK,
        )

        # Goal
        homogeneity_goal = MathTex(
            r"\text{Goal: Show } \|\alpha x\| \leq \|\alpha x + \mu(\beta y)\| \quad \forall \mu \in \mathbb{R}",
            color=BLACK,
        )

        # Case 1 title
        # case1_title = MathTex(
        #     r"\text{Case 1: } \alpha \neq 0",
        #     color=BLACK,
        # )

        # Case 1 - rewrite
        case1_rewrite = MathTex(
            r"\text{Case 1: } \alpha \neq 0",
            r"\quad \|\alpha x + \mu\beta y\| = |\alpha| \cdot \left\|x + \frac{\mu\beta}{\alpha}y\right\|",
            color=BLACK,
        )

        # Case 1 - substitution
        # case1_substitution = MathTex(
        #     r"\text{Let } \lambda_0 = \frac{\mu\beta}{\alpha}",
        #     color=BLACK,
        # )

        # Case 1 - apply assumption
        case1_apply = MathTex(
            r"\|x\| \leq \|x + \lambda_0 y\|",
            r"\quad (\text{Let } \lambda_0 = \frac{\mu\beta}{\alpha})",
            r"\Longleftrightarrow",
            r"|\alpha| \|x\| \leq |\alpha| \|x + \lambda_0 y\|",
            r"\quad \therefore \|\alpha x\| \leq \|\alpha x + \mu\beta y\|",
            color=BLACK,
        )
        case1_apply.set_color_by_tex(r"\quad (\text{Let } \lambda_0 = \frac{\mu\beta}{\alpha})",dark_purple)
        case1_apply.set_color_by_tex(r"quad \therefore \|\alpha x\| \leq \|\alpha x + \mu\beta y\|",dark_purple)

        # Case 1 - multiply
        # case1_multiply = MathTex(
        #     r"|\alpha| \|x\| \leq |\alpha| \|x + \lambda_0 y\|",
        #     color=BLACK,
        # )

        # Case 1 - conclusion
        # case1_conclusion = MathTex(
        #     r"\|\alpha x\| \leq \|\alpha x + \mu\beta y\|",
        #     color=dark_purple,
        # )

        # Case 2 title
        # case2_title = MathTex(
        #     r"\text{Case 2: } \alpha = 0",
        #     color=BLACK,
        # )

        # Case 2 - simplification
        case2_simplification = MathTex(
            r"\text{Case 2: } \alpha = 0",
            r"\quad \|0\| \leq \|0 + \mu(\beta y)\| = \|\mu\beta y\|",
            # r"\quad 0 \leq \|\mu\beta y\| \quad \text{(Always true by norm properties)}",
            color=BLACK,
        )

        # Case 2 - always true
        case2_true = MathTex(
            r"0 \leq \|\mu\beta y\| \quad \text{(Always true by norm properties)} \quad .\blacksquare",
            color=BLACK,
        )

        homo = VGroup(*[
            homogeneity_title,
            homogeneity_statement,
            homogeneity_assumption,
            # homogeneity_goal,
            VGroup(*[
                VGroup(*[
                    # case1_title,
                    case1_rewrite,
                    # case1_substitution,
                    case1_apply,
                    # case1_conclusion,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    # case2_title,
                    case2_simplification,
                    case2_true,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
            ]).arrange(DOWN,buff=0.3),
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(homo),
        )
        self.wait(1)
        self.play(
            FadeOut(homo),
        )

        nonadditivity_title_bj = MathTex(r"\text{Non-Additivity Counterexample}",color=dark_terquise)

        # Space
        nonadditivity_space_bj = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with } \ell^1 \text{ norm},",
            r"\quad x = (1,0), \quad y = (1,1), \quad z = (1,-1)",
            color=BLACK,
        )

        # Vectors
        # nonadditivity_vectors_bj = MathTex(
        #     r"x = (1,0), \quad y = (1,1), \quad z = (1,-1)",
        #     color=BLACK,
        # )

        # Part 1 - x ⊥ y (reference)
        nonadditivity_part1 = MathTex(
            r"\text{Step 1: } x \perp_{BJ} y",
            color=BLACK,
        )
        non_part1_2 = MathTex(
            r"\quad \text{(shown earlier)}",
            color=BLACK,
        )

        # Part 2 title
        nonadditivity_part2_title = MathTex(
            r"\text{Step 2: Show } x \perp_{BJ} z",
            color=BLACK,
        )

        # Part 2 - norm of x
        nonadditivity_part2_norm_x = MathTex(
            r"\|x\|_1 = 1",
            r"\quad , \|x + \lambda z\|_1 = \|(1+\lambda, -\lambda)\|_1 = |1+\lambda| + |\lambda|",
            # r"1 \leq |1+\lambda| + |\lambda| \quad \text{(Always true)}",
            color=BLACK,
        )

        # Part 2 - norm of x + λz
        # nonadditivity_part2_norm_sum = MathTex(
        #     r"\|x + \lambda z\|_1 = \|(1+\lambda, -\lambda)\|_1 = |1+\lambda| + |\lambda|"
        # )

        # Part 2 - inequality
        nonadditivity_part2_inequality = MathTex(
            r"1 \leq |1+\lambda| + |\lambda| \quad \text{(Always true)}",
            color=BLACK,
        )

        # Part 2 - conclusion
        # nonadditivity_part2_conclusion = MathTex(
        #     r"\therefore x \perp_{BJ} z",
        #     color=BLACK,
        # )

        # Part 3 title
        # nonadditivity_part3_title = MathTex(
        #     r"\text{Show } x \not\perp_{BJ} (y+z)",
        #     color=BLACK,
        # )

        # Part 3 - sum
        # nonadditivity_part3_sum = MathTex(
        #     r"y + z = (1,1) + (1,-1) = (2,0)"
        # )

        # Part 3 - norm of x
        # nonadditivity_part3_norm_x = MathTex(r"\|x\|_1 = 1")

        # Part 3 - norm of x + λ(y+z)
        nonadditivity_part3_norm_sum = MathTex(
            r"\text{Show } x \not\perp_{BJ} (y+z) : ",
            r"\quad  \|x + \lambda(y+z)\|_1 = \|(1+2\lambda, 0)\|_1 = |1+2\lambda|",
            # r"\quad (\text{Required: } 1 \leq |1+2\lambda|)",
            color=BLACK,
        )

        # Part 3 - required condition
        # nonadditivity_part3_condition = MathTex(
        #     r"\text{Required: } 1 \leq |1+2\lambda|",
        #     color=BLACK,
        # )

        # Part 3 - counterexample
        nonadditivity_part3_counter = MathTex(
            r"(\text{Required: } 1 \leq |1+2\lambda|)",
            r"\quad  \text{For } \lambda = -\frac{1}{2}: \quad |1+2(-\frac{1}{2})| = 0",
            color=BLACK,
        )

        # Part 3 - inequality fails
        # nonadditivity_part3_fails = MathTex(
        #     r"1 \leq 0 \quad \text{(False)}",
        #     color=BLACK,
        # )

        # Part 3 - conclusion
        # nonadditivity_part3_conclusion = MathTex(
        #     r"\therefore x \not\perp_{BJ} (y+z)",
        #     color=BLACK,
        # )

        add = VGroup(*[
            nonadditivity_title_bj,
            nonadditivity_space_bj,
            # nonadditivity_vectors_bj,
            # homogeneity_goal,
            VGroup(*[
                VGroup(*[
                    nonadditivity_part1,
                    non_part1_2,
                    # case1_rewrite,
                    # case1_substitution,
                    # case1_apply,
                    # case1_conclusion,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    nonadditivity_part2_title,
                    nonadditivity_part2_norm_x,
                    nonadditivity_part2_inequality,
                ]).arrange(DOWN,buff=0.3).scale(0.6).shift(2*LEFT),
            ]).arrange(RIGHT,buff=1),
            VGroup(*[
                # nonadditivity_part3_title,
                nonadditivity_part3_norm_sum,
                nonadditivity_part3_counter,
            ]).arrange(DOWN,buff=0.2).scale(0.8),
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(add),
        )
        self.wait(1)
        self.play(
            FadeOut(add),
        )

        existence_title = MathTex(r"\text{Scaler Existence}", color=dark_green)

        existence_statement = MathTex(
            r"\forall\, x ,\ y \in X,\ \exists\, a \in \mathbb{R}: \quad x \perp_{BJ} (ax + y)",
            color=BLACK,
        )

        trivial_case = MathTex(
            r"\text{If } x = 0: \quad \|0\| \le \|0 + \lambda(a \cdot 0 + y)\| \quad \text{(trivially true)}",
            color=BLACK,
        )

        hb_functional = MathTex(
            r"\text{Assume } x \neq 0. \ \text{By }",
            r"\text{Hahn-Banach}",
            r": \ \exists\, f \text{ s.t. } \|f\| = \|x\|, \ f(x) = \|x\|^2",
            color=BLACK,
        )
        hb_functional.set_color_by_tex(r"\text{Hahn-Banach}", dark_green)

        step1_title = MathTex(r"\text{Step 1: Solve for } a", color=BLACK)

        step1_solve1 = MathTex(
            r"f(ax + y) = 0",
            color=BLACK,
        )
        step1_solve2 = MathTex(
            r"\Longrightarrow\ a\|x\|^2 + f(y) = 0",
            color=BLACK,
        )
        step1_solve3 = MathTex(
            r"\Longrightarrow\ a = -\frac{f(y)}{\|x\|^2}",
            color=BLACK,
        )

        step2_title = MathTex(r"\text{Step 2: Verify } x \perp_{BJ} (ax + y)", color=BLACK)

        step2_body = MathTex(
            r"v = ax + y,\ f(v) = 0 \ \Longrightarrow\ f(x + \lambda v) = f(x) = \|x\|^2",
            color=BLACK,
        )

        step2_ineq = MathTex(
            r"\|x\|^2 = f(x + \lambda v) \le \|f\|\,\|x + \lambda v\| = \|x\|\,\|x + \lambda v\|",
            color=BLACK,
        )

        step2_conclude = MathTex(
            r"\Longrightarrow\ \|x\| \le \|x + \lambda v\| \quad \therefore\ x \perp_{BJ} (ax + y) \quad .\blacksquare",
            color=BLACK,
        )

        existence = VGroup(*[
            existence_title,
            existence_statement,
            trivial_case.scale(0.9),
            hb_functional.scale(0.9),
            VGroup(*[
                VGroup(*[
                    step1_title,
                    step1_solve1,
                    step1_solve2,
                    step1_solve3,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2 * LEFT),
                VGroup(*[
                    step2_title,
                    step2_body,
                    step2_ineq,
                    step2_conclude,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2 * LEFT),
            ]).arrange(RIGHT, buff=0.5),
        ]).arrange(DOWN, buff=0.3).next_to(box1, DOWN, buff=0.3)

        self.play(
            Write(existence[:2]),
        )
        pic_pause = ImageMobject("images/pause.png").scale(1.3).move_to(existence[1].get_center() + 2.5*DOWN)
        self.play(
            FadeIn(pic_pause)
        )
        self.wait(1)
        self.clear()
        self.wait(1)
        self.han_banakh_def(title)
        self.han_banakh_shape(title)
        self.play(
            FadeIn(title_orth),
            FadeIn(box1),
            FadeIn(roberts),
            Write(existence),
        )
        self.wait(1)
        self.play(
            FadeOut(existence),
        )

        headers = [
            (r"\text{Symmetry}", dark_pink),
            (r"\text{Homogeneity}", dark_purple),
            (r"\text{Additivity}", dark_terquise),
            (r"\text{Scalar Existence}", dark_green),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        cross = MathTex(r"\Large \times").set_color(RED)
        check = MathTex(r"\Large \checkmark").set_color(GREEN)
        
        row = [
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]
        
        row_label = MathTex(r"\text{Birkhoff}", color=BLACK)

        table = MobjectTable(
            [row],
            row_labels=[row_label],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        )

        table.scale(1).next_to(box1,DOWN,buff=0.5)

        self.play(
            Create(table),
            run_time = 3,
        )
        self.wait(1)
        self.play(
            FadeOut(table),
            FadeOut(title_orth),
            FadeOut(box1),
            FadeOut(roberts),
        )
        self.wait(1)

    def scene8_SubScene9(self, title):
        title_orth = Tex("Isosceles Orthogonality", color=BLACK, font_size=70).to_edge(UP)

        roberts = MathTex(
            r"\|x + y\| ",r"= ",r"\|x - y\|",
            color = BLACK,
        ).next_to(title_orth,DOWN,buff=0.5)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        
        self.play(
            FadeIn(title_orth),
        )
        self.play(
            Create(box1),
            Write(roberts),
        )
        self.wait(0.5)

        # proof and counterexample

        symmetry_title = MathTex(
            r"\text{Symmetry}",
            color=dark_pink,
        )

        # Statement
        symmetry_statement = MathTex(
            r"\text{If } x \perp_I y, \text{ then } y \perp_I x",
            color=BLACK,
        )

        # Assumption
        symmetry_assumption = MathTex(
            r"\text{Assume } x \perp_I y: \quad \|x + y\| = \|x - y\|",
            color=BLACK,
        )

        # Goal
        symmetry_goal = MathTex(
            r"\text{Goal: Show } \|y + x\| = \|y - x\|",
            color=BLACK,
        )

        # Left side
        symmetry_left = MathTex(
            r"\|y + x\| = \|x + y\| \quad \text{(commutativity of vector addition)}",
            color=BLACK,
        )

        # Right side - step 1
        symmetry_right = MathTex(
            r"\|y - x\| = \|-(x - y)\| = \|x - y\|",
            r"\quad \text{(norm property)}",
            color=BLACK,
        )

        # Right side - step 2
        # symmetry_right_2 = MathTex(
        #     r"\|-(x - y)\| = \|x - y\| \quad \text{(norm property: } \|-v\| = \|v\|\text{)}",
        #     color=BLACK,
        # )

        # Combine
        symmetry_combine = MathTex(
            r"\|y + x\| = \|x + y\| = \|x - y\| = \|y - x\|",
            r"\quad . \blacksquare",
            color=BLACK,
        )

        # Conclusion
        # symmetry_conclusion = MathTex(
        #     r"\therefore y \perp_I x",
        #     color=BLACK,
        # )

        sym = VGroup(*[
            symmetry_title,
            symmetry_statement,
            symmetry_assumption,
            symmetry_goal,
            VGroup(*[
                VGroup(*[
                    symmetry_left,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    symmetry_right,
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
            ]).arrange(DOWN,buff=0.5),
            symmetry_combine,
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        nonhomogeneity_title_iso = MathTex(
            r"\text{Non-Homogeneity Counterexample}",
            color=dark_purple,
        )

        # Space
        nonhomogeneity_space_iso = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with } \ell^1 \text{ norm: } \|(u,v)\|_1 = |u| + |v|",
            color=BLACK,
        )

        # Vectors
        nonhomogeneity_vectors_iso = MathTex(
            r"x = (2,1), \quad y = (-1,2)",
            color=BLACK,
        )

        # Part 1 title
        nonhomogeneity_part1_title = MathTex(
            r"\text{Step 1: Show } x \perp_I y",
            color=BLACK,
        )

        # Part 1 - x+y
        nonhomogeneity_part1_sum = MathTex(
            r"\|x + y\|_1 = 4",
            color=BLACK,
        )

        # Part 1 - x-y
        nonhomogeneity_part1_diff = MathTex(
            r"\|x - y\|_1 = 4",
            color=BLACK,
        )

        # Part 1 - conclusion
        nonhomogeneity_part1_conclusion = MathTex(
            r"4 = 4 \implies x \perp_I y",
            color=BLACK,
        )

        # Part 2 title
        nonhomogeneity_part2_title = MathTex(
            r"\text{Step 2: Show } (2x) \not\perp_I y \text{ for } \alpha = 2, \beta = 1",
            color=BLACK,
        )

        # Part 2 - scaled vector
        # nonhomogeneity_part2_scaled = MathTex(
        #     r"2x = (4,2)",
        #     color=BLACK,
        # )

        # Part 2 - 2x+y
        nonhomogeneity_part2_sum = MathTex(
            r"\|2x + y\|_1 = 7",
            color=BLACK,
        )

        # Part 2 - 2x-y
        nonhomogeneity_part2_diff = MathTex(
            r"\|2x - y\|_1 = 5",
            color=BLACK,
        )

        # Part 2 - conclusion
        nonhomogeneity_part2_conclusion = MathTex(
            r"7 \neq 5 \implies (2x) \not\perp_I y",
            color=BLACK,
        )

        sym = VGroup(*[
            nonhomogeneity_title_iso,
            nonhomogeneity_space_iso,
            nonhomogeneity_vectors_iso,
            VGroup(*[
                VGroup(*[
                    nonhomogeneity_part1_title,
                    nonhomogeneity_part1_sum,
                    nonhomogeneity_part1_diff,
                    nonhomogeneity_part1_conclusion
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    nonhomogeneity_part2_title,
                    nonhomogeneity_part2_sum,
                    nonhomogeneity_part2_diff,
                    nonhomogeneity_part2_conclusion
                ]).arrange(DOWN,buff=0.2).scale(0.8).shift(2*LEFT),
            ]).arrange(RIGHT,buff=1),
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        nonadditivity_title_iso = MathTex(
            r"\text{Non-Additivity Counterexample}",
            color=dark_terquise,
        )

        # Space
        nonadditivity_space_iso = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with } \ell^1 \text{ norm}",
            color=BLACK,
        )

        # Vectors
        nonadditivity_vectors_iso = MathTex(
            r"x = (2,1), \quad y = (1,-1), \quad z = (-1,2)",
            color=BLACK,
        )

        # Part 1 title
        nonadditivity_part1_title_iso = MathTex(
            r"\text{Step 1: Show } x \perp_I y",
            color=BLACK,
        )

        # Part 1 - x+y
        nonadditivity_part1_sum_iso = MathTex(
            r"\|x + y\|_1 = 3",
            color=BLACK,
        )

        # Part 1 - x-y
        nonadditivity_part1_diff_iso = MathTex(
            r"\|x - y\|_1 = 3",
            color=BLACK,
        )

        # Part 1 - conclusion
        nonadditivity_part1_conclusion_iso = MathTex(
            r"3 = 3 \implies x \perp_I y",
            color=BLACK,
        )

        # Part 2 title
        nonadditivity_part2_title_iso = MathTex(
            r"\text{Step 2: Show } x \perp_I z",
            color=BLACK,
        )

        # Part 2 - x+z
        nonadditivity_part2_sum_iso = MathTex(
            r"\|x + z\|_1 = 4",
            color=BLACK,
        )

        # Part 2 - x-z
        nonadditivity_part2_diff_iso = MathTex(
            r"\|x - z\|_1 = 4",
            color=BLACK,
        )

        # Part 2 - conclusion
        nonadditivity_part2_conclusion_iso = MathTex(
            r"4 = 4 \implies x \perp_I z",
            color=BLACK,
        )

        # Part 3 title
        nonadditivity_part3_title_iso = MathTex(
            r"\text{Step 3: Check } x \perp_I (y+z)",
            color=BLACK,
        )

        # Part 3 - sum
        # nonadditivity_part3_sum_iso = MathTex(
        #     r"y + z = (1,-1) + (-1,1) = (0,0) = 0"
        # )

        # Part 3 - x+(y+z)
        nonadditivity_part3_xplus_iso = MathTex(
            r"\|x + (y+z)\|_1 = 4",
            color=BLACK,
        )

        # Part 3 - x-(y+z)
        nonadditivity_part3_xminus_iso = MathTex(
            r"\|x - (y+z)\|_1 = 2",
            color=BLACK,
        )

        # Part 3 - note
        nonadditivity_part3_note = MathTex(
            r"4 \neq 2 \implies x \not\perp_I (y+z)",
            color=BLACK,
        )

        sym = VGroup(*[
            nonadditivity_title_iso,
            nonadditivity_space_iso,
            nonadditivity_vectors_iso,
            VGroup(*[
                VGroup(*[
                    nonadditivity_part1_title_iso,
                    nonadditivity_part1_sum_iso,
                    nonadditivity_part1_diff_iso,
                    nonadditivity_part1_conclusion_iso
                ]).arrange(DOWN,buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    nonadditivity_part2_title_iso,
                    nonadditivity_part2_sum_iso,
                    nonadditivity_part2_diff_iso,
                    nonadditivity_part2_conclusion_iso
                ]).arrange(DOWN,buff=0.2).scale(0.8).shift(2*LEFT),
                VGroup(*[
                nonadditivity_part3_title_iso,
                nonadditivity_part3_xplus_iso,
                nonadditivity_part3_xminus_iso,
                nonadditivity_part3_note,
            ]).arrange(DOWN,buff=0.2).scale(0.8),
            ]).arrange(RIGHT,buff=1),
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        existence_title = MathTex(r"\text{Scalar Existence}", color=dark_green)

        existence_statement = MathTex(
            r"\forall\, x,\ y \in X,\ \exists\, a \in \mathbb{R}: \quad x \perp_I (ax + y)",
            color=BLACK,
        )

        setup_eq = MathTex(
            r"\|x + (ax+y)\| = \|x - (ax+y)\| \ \Longrightarrow\ \|(a+1)x+y\| = \|(a-1)x+y\|",
            color=BLACK,
        )

        trivial_case = MathTex(
            r"\text{If } x = 0,\ \text{choose } a = 0: \quad \|y\| = \|y\| \quad \text{(trivially true)}",
            color=BLACK,
        )

        define_f = MathTex(
            r"\text{Assume } x \neq 0. \ \text{Define } ",
            r"f(a)",
            r" = \|(a+1)x+y\| - \|(a-1)x+y\|",
            color=BLACK,
        )
        define_f.set_color_by_tex(r"f(a)", dark_green)

        step1_title = MathTex(r"\text{Step 1: Continuity}", color=BLACK)

        step1_body1 = MathTex(
            r"\|\cdot\|,\ +,\ \text{scalar mult. continuous} ",
            color=BLACK,
        )
        step1_body2 = MathTex(
            r"\Longrightarrow\ f \text{ continuous on } \mathbb{R}",
            color=BLACK,
        )
        step1_body = VGroup(step1_body1, step1_body2).arrange(DOWN, buff=0.2)

        step2_title = MathTex(r"\text{Step 2: Sign Change at } \pm\infty", color=BLACK)

        step2_pos = MathTex(
            r"\lim_{a \to \infty} f(a) = 2\|x\| > 0", # = (a+1)\|x\| - (a-1)\|x\|
            color=BLACK,
        )

        step2_neg = MathTex(
            r"\lim_{a \to -\infty} f(a) = -2\|x\| < 0",
            color=BLACK,
        )

        conclude = MathTex(
            r"\text{By } ",r"\text{IVT} ",r"\text{ : } \exists\, a \in \mathbb{R},\ f(a) = 0 \ \Longrightarrow\ x \perp_I (ax+y) \quad .\blacksquare",
            color=BLACK,
        )
        conclude.set_color_by_tex(r"\text{IVT}", dark_green)

        existence = VGroup(*[
            existence_title,
            existence_statement,
            setup_eq.scale(0.8),
            trivial_case.scale(0.8),
            define_f.scale(0.8),
            VGroup(
                VGroup(*[
                    step1_title,
                    step1_body,
                ]).arrange(DOWN, buff=0.2).scale(0.7),
                VGroup(*[
                    step2_title,
                    step2_pos,
                    step2_neg,
                ]).arrange(DOWN, buff=0.2).scale(0.7)
            ).arrange(RIGHT, buff=0.5),
            conclude.scale(0.8),
        ]).arrange(DOWN, buff=0.2).next_to(box1, DOWN, buff=0.2)

        self.play(
            Write(existence),
        )
        self.wait(1)
        self.play(
            FadeOut(existence),
        )

        headers = [
            (r"\text{Symmetry}", dark_pink),
            (r"\text{Homogeneity}", dark_purple),
            (r"\text{Additivity}", dark_terquise),
            (r"\text{Scalar Existence}", dark_green),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        cross = MathTex(r"\Large \times").set_color(RED)
        check = MathTex(r"\Large \checkmark").set_color(GREEN)
        
        row = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]
        
        row_label = MathTex(r"\text{Isosceles}", color=BLACK)

        table = MobjectTable(
            [row],
            row_labels=[row_label],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        )

        table.scale(1).next_to(box1,DOWN,buff=0.5)

        self.play(
            Create(table),
            run_time = 3,
        )
        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(box1),
            FadeOut(roberts),
            FadeOut(table),
        )
        self.wait(1)


    def scene8_SubScene12(self, title):
        title_orth = Tex("Pythagorean Orthogonality", color=BLACK, font_size=70).to_edge(UP)

        roberts = MathTex(
            r"\|x + y\|^2 ",r"= ",r"\|x\|^2 + \|y\|^2",
            color = BLACK,
        ).next_to(title_orth,DOWN,buff=0.5)
        box1 = SurroundingRectangle(
            roberts,
            color=dark_blue,        
            buff=0.2,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        
        self.play(
            FadeIn(title_orth),
        )
        self.play(
            Create(box1),
            Write(roberts),
        )
        self.wait(0.5)

        # proof and counterexample

        symmetry_title = MathTex(
            r"\text{Symmetry}",
            color=dark_pink,
        )

        assumption = MathTex(
            r"\text{Assume : } x \perp_P y \implies \|x+y\|^2 = \|x\|^2 + \|y\|^2",
            color=BLACK,
        )

        # Goal
        goal = MathTex(
            r"\text{Goal : } y \perp_P x \implies \|y+x\|^2 = \|y\|^2 + \|x\|^2",
            color=BLACK,
        )

        # Step 1: Commutativity of vector addition
        # step1 = MathTex(r"x + y = y + x")

        # Step 2: Norm equality
        step2 = MathTex(
            r"\|x+y\| = \|y+x\| \implies \|x+y\|^2 = \|y+x\|^2",
            color=BLACK,
        )

        # Step 3: Commutativity of real addition
        step3 = MathTex(
            r"\|x\|^2 + \|y\|^2 = \|y\|^2 + \|x\|^2",
            color=BLACK,
        )

        # Conclusion
        conclusion = MathTex(
            r"\|y+x\|^2 = \|y\|^2 + \|x\|^2",
            color=BLACK,
        )

        # QED
        qed = MathTex(
            r"y \perp_P x \quad . \blacksquare",
            color=BLACK,
        )

        sym = VGroup(*[
            symmetry_title,
            assumption,
            goal,
            VGroup(*[
                step2,
                step3,
                conclusion,
            ]).arrange(DOWN,buff=0.3).scale(0.8),
            qed,
        ]).arrange(DOWN,buff=0.3).next_to(box1,DOWN,buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        nonhomogeneity_title = MathTex(
            r"\text{Non-Homogeneity Counterexample}",
            color=dark_purple,
        )

        # Space definition
        nonhomogeneity_space = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with norm: } \|(u,v)\| = \begin{cases} \sqrt{u^2 + v^2} & \text{if } uv \geq 0 \\ |u| + |v| & \text{if } uv < 0 \end{cases}",
            color=BLACK,
        ).scale(0.8)

        # Vectors
        nonhomogeneity_vectors = MathTex(
            r"x = (1,0), \quad y = (0,1)",
            color=BLACK,
        ).scale(0.8)

        # Part 1 title
        nonhomogeneity_part1_title = MathTex(
            r"\text{Step 1: Show } x \perp_P y",
            color=BLACK,
        )

        # Part 1 - norms
        nonhomogeneity_part1_norms = MathTex(
            r"\|x\| = 1, \quad \|y\| = 1",
            color=BLACK,
        )

        # Part 1 - sum
        nonhomogeneity_part1_sum = MathTex(
            r"\|x+y\|^2 = 2",
            color=BLACK,
        )

        # Part 1 - check
        nonhomogeneity_part1_check = MathTex(
            r"\|x\|^2 + \|y\|^2 = 2",
            color=BLACK,
        )

        # Part 1 - conclusion
        nonhomogeneity_part1_conclusion = MathTex(
            r"2 = 2 \implies x \perp_P y \quad \checkmark",
            color=BLACK,
        )

        # Part 2 title
        nonhomogeneity_part2_title = MathTex(
            r"\text{Step 2: Show } (-x) \not\perp_P y \text{ for } \alpha = -1, \beta = 1",
            color=BLACK,
        )

        # Part 2 - scaled vector
        nonhomogeneity_part2_scaled = MathTex(
            r"\|-x\| = 1",
            color=BLACK,
        )

        # Part 2 - sum
        nonhomogeneity_part2_sum = MathTex(
            r"\|-x+y\| = |-1| + |1| = 2 \quad (uv < 0)",
            color=BLACK,
        )

        # Part 2 - check
        nonhomogeneity_part2_check = MathTex(
            r"\|-x+y\|^2 = 4, \quad \|-x\|^2 + \|y\|^2 = 1 + 1 = 2",
            color=BLACK,
        )

        # Part 2 - conclusion
        nonhomogeneity_part2_conclusion = MathTex(
            r"4 \neq 2 \implies (-x) \not\perp_P y",
            color=BLACK,
        )

        sym = VGroup(*[
            nonhomogeneity_title,
            nonhomogeneity_space,
            nonhomogeneity_vectors,
            VGroup(*[
                VGroup(*[
                    nonhomogeneity_part1_title,
                    nonhomogeneity_part1_norms,
                    nonhomogeneity_part1_sum,
                    nonhomogeneity_part1_check,
                    nonhomogeneity_part1_conclusion,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    nonhomogeneity_part2_title,
                    nonhomogeneity_part2_scaled,
                    nonhomogeneity_part2_sum,
                    nonhomogeneity_part2_check,
                    nonhomogeneity_part2_conclusion,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2*LEFT),
            ]).arrange(RIGHT, buff=1),
        ]).arrange(DOWN, buff=0.2).next_to(box1, DOWN, buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )


        nonadditivity_title = MathTex(
            r"\text{Non-Additivity Counterexample}",
            color=dark_terquise,
        )

        # General statement
        # nonadditivity_statement = MathTex(
        #     r"x \perp_P y \text{ and } x \perp_P z \not\Rightarrow x \perp_P (y+z)",
        #     color=BLACK,
        # )

        nonadditivity_inner_assumption = MathTex(
            r"\text{Space: } \mathbb{R}^2 \text{ with norm: } \ell_\infty \, , \|(u,v)\|_\infty = \max{(|u|,|v|)}",
            color=BLACK,
        )

        nonadditivity_inner_linearity = MathTex(
            r"x = (1,0), \quad y = (\sqrt{2}-1, \, 1), \quad z = (\sqrt{2}-1, \, -1)",
            color=BLACK,
        )

        nonadditivity_part1_1 = MathTex(
            r"\text{Step } 1 : x \perp_P y",
            color=BLACK,
        )

        nonadditivity_part1_2 = MathTex(
            r"\|x\|_\infty = 1, \quad \|y\|_\infty = 1",
            color=BLACK,
        )
        nonadditivity_part1_3 = MathTex(
            r"\|x + y\|_\infty = \sqrt{2}",
            color=BLACK,
        )
        nonadditivity_part1_4 = MathTex(
            r"1 + 1 = 2",
            color=BLACK,
        )

        nonadditivity_part2_1 = MathTex(
            r"\text{Step } 2 : x \perp_P z",
            color=BLACK,
        )

        nonadditivity_part2_2 = MathTex(
            r"\|x\|_\infty = 1, \quad \|z\|_\infty = 1",
            color=BLACK,
        )
        nonadditivity_part2_3 = MathTex(
            r"\|x + z\|_\infty = \sqrt{2}",
            color=BLACK,
        )
        nonadditivity_part2_4 = MathTex(
            r"1 + 1 = 2",
            color=BLACK,
        )

        nonadditivity_part3_1 = MathTex(
            r"\text{Step } 3 : x \not\perp_P (y+z)",
            color=BLACK,
        )

        nonadditivity_part3_2 = MathTex(
            r"\|x\|_\infty = 1, \quad \|y+z\|_\infty = 2\sqrt{2}-2",
            color=BLACK,
        )
        nonadditivity_part3_3 = MathTex(
            r"\|x + (y+z)\|_\infty = 2\sqrt{2}-1",
            color=BLACK,
        )
        nonadditivity_part3_4 = MathTex(
            r"(2\sqrt{2}-2)^2 + 1 = 13-8\sqrt{2} \approx 1.686 \ne (2\sqrt{2}-1)^2 \approx 3.343",
            color=dark_terquise,
        )


        sym = VGroup(*[
            nonadditivity_title,
            nonadditivity_inner_assumption,
            nonadditivity_inner_linearity,
            VGroup(*[
                VGroup(*[
                    nonadditivity_part1_1,
                    nonadditivity_part1_2,
                    nonadditivity_part1_3,
                    nonadditivity_part1_4,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    nonadditivity_part2_1,
                    nonadditivity_part2_2,
                    nonadditivity_part2_3,
                    nonadditivity_part2_4,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2*LEFT),
                VGroup(*[
                    nonadditivity_part3_1,
                    nonadditivity_part3_2,
                    nonadditivity_part3_3,
                ]).arrange(DOWN, buff=0.2).scale(0.7).shift(2*LEFT),
            ]).arrange(RIGHT, buff=1),
            nonadditivity_part3_4,
        ]).arrange(DOWN, buff=0.3).next_to(box1, DOWN, buff=0.3)

        self.play(
            Write(sym),
        )
        self.wait(1)
        self.play(
            FadeOut(sym),
        )

        existence_title = MathTex(r"\text{Scalar Existence}", color=dark_green)

        existence_statement = MathTex(
            r"\forall\, x,\ y \in X,\ x \neq 0,\ \exists\, a \in \mathbb{R}: \quad x \perp_P (ax + y)",
            color=BLACK,
        )

        setup_eq = MathTex(
            r"\|x+(ax+y)\|^2 = \|x\|^2 + \|ax+y\|^2 \ \Longrightarrow\ \|(a+1)x+y\|^2 - \|ax+y\|^2 - \|x\|^2 = 0",
            color=BLACK,
        )

        define_f = MathTex(
            r"\text{Define } ",
            r"f(a)",
            r" = \|(a+1)x+y\|^2 - \|ax+y\|^2 - \|x\|^2",
            color=BLACK,
        )
        define_f.set_color_by_tex(r"f(a)", dark_green)

        step1_title = MathTex(r"\text{Step 1: Continuity}", color=BLACK)

        step1_body1 = MathTex(
            r"\|\cdot\|^2,\ +,\ \text{scalar mult. continuous} ",
            color=BLACK,
        )
        step1_body2 = MathTex(
            r"\Longrightarrow\ f \text{ continuous on } \mathbb{R}",
            color=BLACK,
        )
        step1_body = VGroup(step1_body1, step1_body2).arrange(DOWN, buff=0.2)

        step2_title = MathTex(r"\text{Step 2: Asymptotic Behavior}", color=BLACK)

        step2_approx = MathTex(
            r"\|ax+y\| \approx |a|\,\|x\| \ \Longrightarrow\ f(a) \approx 2a\|x\|^2",
            color=BLACK,
        )

        step2_pos = MathTex(
            r"a \to +\infty \ \Longrightarrow\ f(a) \to +\infty",
            color=BLACK,
        )

        step2_neg = MathTex(
            r"a \to -\infty \ \Longrightarrow\ f(a) \to -\infty",
            color=BLACK,
        )

        conclude = MathTex(
            r"\text{By } ",r"\text{IVT} ",r"\text{ : } \exists\, a \in \mathbb{R},\ f(a) = 0 \ \Longrightarrow\ x \perp_P (ax+y) \quad .\blacksquare",
            color=BLACK,
        )
        conclude.set_color_by_tex(r"\text{IVT}", dark_green)

        existence = VGroup(*[
            existence_title,
            existence_statement,
            setup_eq.scale(0.75),
            define_f.scale(0.8),
            VGroup(
                VGroup(*[
                    step1_title,
                    step1_body,
                ]).arrange(DOWN, buff=0.2).scale(0.7),
                VGroup(*[
                    step2_title,
                    step2_approx,
                    step2_pos,
                    step2_neg,
                ]).arrange(DOWN, buff=0.2).scale(0.7)
            ).arrange(RIGHT, buff=0.5),
            conclude.scale(0.8),
        ]).arrange(DOWN, buff=0.2).next_to(box1, DOWN, buff=0.2)

        self.play(
            Write(existence),
        )
        self.wait(1)
        self.play(
            FadeOut(existence),
        )

        headers = [
            (r"\text{Symmetry}", dark_pink),
            (r"\text{Homogeneity}", dark_purple),
            (r"\text{Additivity}", dark_terquise),
            (r"\text{Scalar Existence}", dark_green),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        cross = MathTex(r"\Large \times").set_color(RED)
        check = MathTex(r"\Large \checkmark").set_color(GREEN)
        
        row = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
           MathTex(r"\Large \checkmark").set_color(GREEN),
        ]
        
        row_label = MathTex(r"\text{Pythagorean}", color=BLACK).scale(0.6)

        table = MobjectTable(
            [row],
            row_labels=[row_label],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        )

        table.scale(1).next_to(box1,DOWN,buff=0.5)

        self.play(
            Create(table),
            run_time = 3,
        )
        self.wait(1)
        self.play(
            FadeOut(title_orth),
            FadeOut(box1),
            FadeOut(roberts),
            FadeOut(table),
        )
        self.wait(1)

    def scene8_SubScene13(self, title):
        metric_circle = Ellipse(
            width=14, height=8,
            color=dark_pink,
            stroke_width=4,
            # fill_opacity = 0.01,
        )
        
        norm_circle = Ellipse(
            width=12, height=6,
            color=dark_purple,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(DOWN * 0.3)
        
        banach_circle = Ellipse(
            width=7, height=4,
            color=dark_terquise,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(RIGHT * 1.8+0.8*DOWN)
        
        inner_circle = Ellipse(
            width=7, height=4,
            color=dark_orange,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(LEFT * 1.8+0.8*DOWN)
        
        metric_text = Text(" Metric space ", font_size=60, color=dark_pink).move_to(UP * 3.2)
        
        norm_text = Text(" Normed space ", font_size=48, color=dark_purple).move_to(UP * 1.8)
        
        banach_text = Text(" Banach space ", font_size=36, color=dark_terquise).move_to(RIGHT * 3.5 + 0.8*DOWN)
        
        inner_text = Text(" Inner product\n       space ", font_size=36, color=dark_orange, line_spacing=0.8).move_to(LEFT * 3.5 + 0.8*DOWN)
        
        hilbert_text = Text(" Hilbert space ", font_size=36, color=dark_green).move_to(DOWN * 0.5)

        intersection = Intersection(banach_circle, inner_circle, color=dark_green, fill_opacity=0.1)

        diff_banach = Difference(banach_circle, inner_circle, color=dark_terquise, fill_opacity=0.1)
        
        diff_inner = Difference(inner_circle, banach_circle, color=dark_orange, fill_opacity=0.1)

        all_shapes = VGroup(*[
            metric_circle,
            norm_circle,
            banach_circle,
            inner_circle,
            metric_text,
            norm_text,
            banach_text,
            inner_text,
            hilbert_text,
            intersection,
        ]).scale(0.7).to_corner(DR)

        self.wait(0.5)
        self.play(
            FadeIn(all_shapes),
        )
        self.wait(1)

        talk_circle = Ellipse(
            width=7, height=4,
            color=dark_red,
            stroke_width=6,
            fill_opacity = 0.1,
        ).scale(0.7).move_to(inner_circle.get_center())

        text1 = MathTex(
            r"x \perp_{P} y \Longleftrightarrow x \perp_{I} y \Longleftrightarrow x \perp_{BJ} y \Longleftrightarrow x \perp_{R} y \Longleftrightarrow \langle x , y \rangle = 0",
            color=dark_orange,
        ).next_to(all_shapes,UP,buff=0.4).shift(2*LEFT)
        
        self.play(
            Create(talk_circle),
            Write(text1),
        )

        self.wait(1)

        text2 = MathTex(
            r"x \perp_{R} y \Longrightarrow x \perp_{I} y",
            color=dark_purple,
        ).next_to(all_shapes,UP,buff=0.4).shift(2*LEFT)

        talk_circle2 = Ellipse(
            width=12, height=6,
            color=dark_red,
            stroke_width=4,
            fill_opacity = 0.1,
        ).scale(0.7).move_to(norm_circle.get_center())

        self.play(
            Transform(talk_circle, talk_circle2),
            FadeTransform(text1, text2),
        )
        
        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                all_shapes,
                talk_circle,
                text2,
            ]))
        )

        self.wait(1)

    def scene8_SubScene14(self, title):
        title_Summary = Text("Summary",color=BLACK,font_size=50).to_edge(UP).shift(0.3*UP)
        self.play(Write(title_Summary))

        headers = [
            (r"\text{Symmetry}", dark_pink),
            (r"\text{Homogeneity}", dark_purple),
            (r"\text{Additivity}", dark_terquise),
            (r"\text{Scalar Existence}", dark_green),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        
        row_Pythagorean = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
           MathTex(r"\Large \checkmark").set_color(GREEN),
        ]

        row_Isosceles = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
           MathTex(r"\Large \checkmark").set_color(GREEN),
        ]

        row_BJ = [
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \checkmark").set_color(GREEN),
        ]

        row_Roberts = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
        ]
        
        row_label_roberts = MathTex(r"\text{Roberts}", color=BLACK).scale(0.6)
        row_label_BJ = MathTex(r"\text{BJ}", color=BLACK).scale(0.6)
        row_label_Isosceles = MathTex(r"\text{Isosceles}", color=BLACK).scale(0.6)
        row_label_Pythagorean = MathTex(r"\text{Pythagorean}", color=BLACK).scale(0.6)

        table = MobjectTable(
            [row_Roberts, row_BJ, row_Isosceles, row_Pythagorean],
            row_labels=[row_label_roberts, row_label_BJ, row_label_Isosceles, row_label_Pythagorean],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        ).shift(0.5*DOWN)

        self.play(
            Create(table),
            run_time = 3,
        )
        self.wait(1)
        self.play(
            FadeOut(table),
            FadeOut(title_Summary),
            # run_time = 3,
        )
        self.wait(1)

    def scene8_SubScene3_2(self, title):
        title_dictator = Text("The Geometric Dictatorship of Roberts", color=BLACK).move_to(title.get_center())
        self.play(
            Write(title_dictator),
        )
        self.wait(0.5)

        # ---------- تنظیمات کلی: بزرگ‌نمایی و جابجایی به پایین ----------
        SCALE = 1.5
        SHIFT = DOWN * 1.0

        def P(vec):
            return vec * SCALE + SHIFT

        points = [
            P(RIGHT * 3),                      # نقطه راست
            P(RIGHT * 1 + UP * 2.0),           # قله سمت راست
            P(LEFT * 1.5 + UP * 1.5),          # قله سمت چپ
            P(LEFT * 3),                       # نقطه چپ
            P(LEFT * 1.5 + DOWN * 1.5),        # دره سمت چپ
            P(RIGHT * 1 + DOWN * 2.0)          # دره سمت راست
        ]

        # ---------- کره واحد با گرادیان رنگی زیباتر ----------
        unit_ball = Polygon(
            *points,
            color=BLUE_D,
            fill_color=[BLUE_E, BLUE_D, TEAL_E],
            fill_opacity=0.25,
            stroke_width=4,
        )
        ball_label = MathTex(r"\text{Unit Ball}", color=BLUE_E).scale(1.1)
        ball_label.next_to(unit_ball, UP + RIGHT).shift(DOWN * 0.6 + LEFT * 0.3)

        self.play(Create(unit_ball), Write(ball_label), run_time=2)
        self.wait(1)

        # ---------- محور span(x) و بردارها ----------
        span_x = DashedLine(
            P(LEFT * 4), P(RIGHT * 4),
            color=RED_E, dash_length=0.15, stroke_width=3,
        )
        span_label = MathTex(r"\text{span}(x)", color=RED_E).scale(1.0).next_to(span_x, RIGHT).shift(0.6*DOWN + 1*LEFT)

        x_vec = Vector(RIGHT * 2 * SCALE, color=RED_D).shift(SHIFT)
        x_label = MathTex(r"\vec{x}", color=RED_D).scale(1.1).next_to(x_vec, DOWN).shift(0.3 * RIGHT)

        y_vec = Vector(UP * 1.5 * SCALE, color=GREEN_D).shift(SHIFT)
        y_label = MathTex(r"\vec{y}", color=GREEN_D).scale(1.1).next_to(y_vec, LEFT)

        self.play(Create(span_x), Write(span_label))
        self.play(GrowArrow(x_vec), Write(x_label))
        self.play(GrowArrow(y_vec), Write(y_label))
        self.wait(1)

        # ---------- وترها (chords) ----------
        chords = VGroup()
        chord_data = [
            (-1.5, 1.5),
            (0.0, 1.8),
            (1.0, 2.0),
        ]

        chord_midpoint_coords = []
        for x_val, y_val in chord_data:
            top = P(np.array([x_val, y_val, 0]))
            bottom = P(np.array([x_val, -y_val, 0]))
            mid = P(np.array([x_val, 0, 0]))
            chord_midpoint_coords.append(mid)

            chord = Line(top, bottom, color=ORANGE, stroke_width=3.5)
            chords.add(chord)

        self.play(Create(chords), run_time=2, lag_ratio=0.3)
        self.wait(0.5)

        # ---------- افکت درخشان قرمز روی نقاط میانی  ----------
        def glow_dot(point, color=PINK, max_radius=0.30, num_circles=5, core_radius=0.07):
            glow = VGroup()
            for i in range(num_circles, 0, -1):
                r = max_radius * i / num_circles
                op = 0.5 * (1 - i / num_circles) + 0.05
                circ = Circle(
                    radius=r, color=color, fill_color=color,
                    fill_opacity=op, stroke_opacity=0,
                )
                circ.move_to(point)
                glow.add(circ)
            core = Dot(point, radius=core_radius, color=color, z_index=2)
            glow.add(core)
            return glow

        glow_groups = VGroup()
        for pt in chord_midpoint_coords:
            g = glow_dot(pt)
            glow_groups.add(g)
            self.play(
                Flash(pt, color=PINK, line_length=0.25, num_lines=10, flash_radius=0.35),
                FadeIn(g, scale=1.3),
                run_time=0.5,
            )

        # افکت تپش ملایم برای جلب توجه بیشتر
        self.play(
            *[g[-1].animate.scale(1.4) for g in glow_groups],
            rate_func=there_and_back,
            run_time=0.8,
        )
        self.wait(1)

        # ---------- نیمه‌ی بالایی چندضلعی ----------
        top_points = points[:4]
        top_half = Polygon(
            *top_points,
            color=YELLOW_E,
            fill_color=[YELLOW_D, YELLOW_E],
            fill_opacity=0.6,
            stroke_width=3,
        )

        self.play(FadeIn(top_half, shift=UP * 0.2))
        self.wait(0.5)

        self.play(
            Rotate(
                top_half,
                angle=PI,
                axis=RIGHT,
                about_point=SHIFT,   # چرخش حول مرکز جدید شکل (به‌جای ORIGIN)
            ),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(1)
        self.clear()
        self.wait(1)

    def scene8_SubScene3_1(self, title):
        x_y = MathTex(
            r"x = (x_1, x_2, \dots , x_n),",
            r"\quad y = (y_1, y_2, \dots , y_n)",
            r" \, \in \mathbb{R}^n",
            color=BLACK,
        ).move_to(title.get_center()) #+0.5*DOWN

        x_p_y = MathTex(
            r"x \perp_R y \Longrightarrow \|x + \lambda y\| = \|x - \lambda y\| , \quad \forall \lambda \in \mathbb{R}",
            color=dark_blue,
        ).next_to(x_y,DOWN,buff=0.5)
        condition = MathTex(
            r"\text{Lets use }", r"\| \cdot \|_\infty", r" \text{ as the norm. }",
            color=dark_orange,
        ).next_to(x_p_y,DOWN,buff=0.6)
        condition_box = SurroundingRectangle(
            condition,
            color=dark_orange,
            fill_opacity=0.1,
            buff=0.25,
            corner_radius=0.1,
        )
        use_l_inf = MathTex(
            r"\max_{1 \leq i \leq n} |x_i - \lambda y_i| = \max_{1 \leq i \leq n} |x_i + \lambda y_i|, \quad ",r"\forall \lambda \in \mathbb{R}",
            color=dark_blue,
        ).next_to(condition,DOWN,buff=0.6)
        lambda_box = SurroundingRectangle(
            use_l_inf[1],
            color=dark_pink,
            fill_opacity=0.1,
            buff=0.2,
            corner_radius=0.1,
        )
        pic1 = ImageMobject("images/computer.png").scale(2).to_corner(DL).shift(0.2*DOWN)
        pic2 = ImageMobject("images/loop.png").scale(2).next_to(pic1, RIGHT, buff=1.25)
        pic3 = ImageMobject("images/crash.png").scale(2).next_to(pic2, RIGHT, buff=1.25)
        vector_1 = Arrow(
            start=pic1.get_right(),
            end=pic2.get_left(),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        vector_2 = Arrow(
            start=pic2.get_right(),
            end=pic3.get_left(),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        
        self.play(
            Write(x_y),
            # Write(x_p_y),
        )
        self.wait(0.5)
        self.play(
            # Write(x_y),
            Write(x_p_y),
        )
        self.wait(0.5)
        self.play(
            Create(condition_box),
            Write(condition),
        )
        self.wait(0.5)
        self.play(
            # Create(lambda_box),
            Write(use_l_inf),
        )
        self.wait(0.5)
        self.play(
            Create(lambda_box),
        )
        self.wait(0.5)
        self.play(
            FadeIn(pic1),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(vector_1),
        )
        self.wait(0.5)
        self.play(
            FadeIn(pic2),
        )
        self.wait(0.5)
        self.play(
            GrowArrow(vector_2),
        )
        self.wait(0.5)
        self.play(
            FadeIn(pic3),
        )
        self.wait(0.5)
        self.play(
            FadeOut(pic1),
            FadeOut(pic2),
            FadeOut(pic3),
            FadeOut(VGroup(*[
                x_y,
                condition,
                condition_box,
                use_l_inf,
                lambda_box,
                vector_1,
                vector_2,
            ])),
            x_p_y.animate.move_to(x_y.get_center()),
        )

        f_lambda = MathTex(
            r"f(\lambda) = \| x + \lambda y \|",
            color=dark_pink,
        ).next_to(x_p_y,DOWN,buff=0.3).shift(2*LEFT)

        self.play(
            Write(f_lambda),
        )
        self.wait(0.5)

        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 7.5, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}
        )
        axes.to_edge(DOWN, buff=0.6).shift(RIGHT)
        plane = NumberPlane(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 7.5, 1],
            x_length=9,
            y_length=5.5,
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
        ).to_edge(DOWN, buff=0.6).shift(RIGHT)

        x_label = MathTex(r"\lambda", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex(r"f(\lambda)", color=BLACK).scale(0.8)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.15)

        self.play(Create(plane), Create(axes), run_time=1.5)
        self.play(Write(x_label), Write(y_label))
        self.wait(0.5)

        raw_points = [
            (-3, 5),
            (-2, 3),
            (-1, 2),
            (0, 2.5),
            (1, 3.5),
            (2, 5),
            (3, 7),
        ]

        dots_coords = [axes.c2p(x, y) for x, y in raw_points]

        segments = VGroup()
        for i in range(len(dots_coords) - 1):
            seg = Line(
                dots_coords[i], dots_coords[i + 1],
                color=dark_green, stroke_width=5,
            )
            segments.add(seg)

        for seg in segments:
            self.play(Create(seg), run_time=0.6)

        self.wait(0.5)

        breakpoint_coords = dots_coords[1:-1]

        def glow_dot(point, color=RED, max_radius=0.28, num_circles=5):
            glow = VGroup()
            for i in range(num_circles, 0, -1):
                r = max_radius * i / num_circles
                op = 0.5 * (1 - i / num_circles) + 0.05
                circ = Circle(radius=r, color=color, fill_color=color,
                               fill_opacity=op, stroke_opacity=0)
                circ.move_to(point)
                glow.add(circ)
            core = Dot(point, radius=0.07, color=color, z_index=2)
            glow.add(core)
            return glow

        glow_groups = VGroup()
        for pt in breakpoint_coords:
            g = glow_dot(pt)
            glow_groups.add(g)
            self.play(
                Flash(pt, color=RED, line_length=0.25, num_lines=10, flash_radius=0.35),
                FadeIn(g, scale=1.3),
                run_time=0.6,
            )

        self.wait(0.3)

        self.play(
            *[
                g[-1].animate.scale(1.4)
                for g in glow_groups
            ],
            rate_func=there_and_back,
            run_time=0.8,
        )
        self.wait(0.3)

        label_pos = axes.c2p(-0.5, 6.6)
        breakpoints_text = Text("Breakpoints", color=RED, weight=BOLD).scale(0.7)
        breakpoints_text.move_to(label_pos).shift(1*LEFT)

        arrows = VGroup()
        for pt in [breakpoint_coords[1], breakpoint_coords[2], breakpoint_coords[3]]:
            arrow = Arrow(
                start=breakpoints_text.get_bottom() + 0.1 * DOWN,
                end=pt,
                color=RED,
                stroke_width=2.5,
                max_tip_length_to_length_ratio=0.15,
                buff=0.15,
            )
            arrows.add(arrow)

        self.play(Write(breakpoints_text))
        self.play(*[GrowArrow(a) for a in arrows], run_time=1)

        self.wait(1)
        self.clear()
        self.wait(1)

    def scene8_SubScene3_0(self, title):
        headers = [
            (r"\text{Symmetry}", dark_pink),
            (r"\text{Homogeneity}", dark_purple),
            (r"\text{Additivity}", dark_terquise),
            (r"\text{Scalar Existence}", dark_green),
        ]

        col_labels = [MathTex(h).set_color(color) for h, color in headers]

        cross = MathTex(r"\Large \times").set_color(RED)
        check = MathTex(r"\Large \checkmark").set_color(GREEN)
        
        row = [
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \checkmark").set_color(GREEN),
            MathTex(r"\Large \times").set_color(RED),
            MathTex(r"\Large \times").set_color(RED),
        ]
        
        row_label = MathTex(r"\text{Roberts}", color=BLACK)

        table = MobjectTable(
            [row],
            row_labels=[row_label],
            col_labels=col_labels,
            include_outer_lines=True,
            line_config={"stroke_width": 3, "color": GRAY},
            h_buff=0.3,
        )

        table.scale(0.9).move_to(title.get_center()+0.5*DOWN)

        self.play(
            FadeIn(table),
        )
        self.wait(1)

        col_index = 2  # 0: Symmetry, 1: Homogeneity, 2: Additivity, 3: Scalar Existence

        highlight_group = VGroup(
            col_labels[col_index],
            row[col_index],
        )

        col_box = SurroundingRectangle(
            highlight_group,
            color=dark_red,
            fill_opacity=0.1,
            buff=0.25,
            corner_radius=0.1,
        )
        detecter_text = Text("Detector", font_size=30, color=dark_red).next_to(col_box, DOWN, buff=0.5)
        theoream_title = Text("Characterization of Inner Product Spaces", font_size=40, color=dark_blue)
        theoream_text1 = MathTex(r"\text{Let } X \text{ be a normed space with } \dim(X) \ge 2. ",color=BLACK)
        theoream_text2 = MathTex(r"\text{The space } X \text{ is an inner product space } ",r"\text{if and only if }",color=BLACK)
        theoream_text2.set_color_by_tex(r"\text{if and only if }", dark_red)
        theoream_text3 = MathTex(r"\text{Roberts orthogonality is additive}",color=BLACK)
        theoream_text4 = MathTex(r"\text{with respect to the second variable. }",color=BLACK)
        theoream_text = VGroup(theoream_text1, theoream_text2, theoream_text3, theoream_text4).arrange(DOWN, buff=0.2)
        theoream_text_final1 = MathTex(
            r"X \text{ is an inner product space}",
            color=BLACK,
        )
        theoream_text_final2 = MathTex(
            r"\iff",
            color=BLACK,
        )
        theoream_text_final3 = MathTex(
            r"\forall x,y,z \in X, \, x \perp_R y, \, x \perp_R z \implies x \perp_R (y + z)",
            color=BLACK,
        )
        theoream_text_final = VGroup(theoream_text_final1, theoream_text_final2, theoream_text_final3).arrange(DOWN, buff=0.2)
        
        box_theoream = SurroundingRectangle(
            VGroup(theoream_title, theoream_text).arrange(DOWN, buff=0.2).next_to(table, DOWN, buff=0.6),
            color=dark_blue,
            fill_opacity=0.1,
            buff=0.2,
            corner_radius=0.1,
        )

        box_theoream_final = SurroundingRectangle(
            VGroup(theoream_title, theoream_text_final).arrange(DOWN, buff=0.2).next_to(table, DOWN, buff=0.6),
            color=dark_blue,
            fill_opacity=0.1,
            buff=0.2,
            corner_radius=0.1,
        )
        self.play(
            Create(col_box),
            # Write(detecter_text),
        )
        self.wait(0.5)
        self.play(
            Write(detecter_text),
        )
        self.wait(0.5)
        self.play(
            FadeOut(detecter_text),
        )
        self.wait(0.5)
        self.play(
            Create(box_theoream),
            Write(theoream_title),
            Write(theoream_text),
        )
        self.wait(1)
        self.play(
            TransformMatchingShapes(VGroup(box_theoream, theoream_title, theoream_text), VGroup(box_theoream_final, theoream_title, theoream_text_final)),
        )
        self.wait(1)
        self.clear()
        self.wait(1)

    def scene8(self, title):

        ########## roberts

        # self.scene8_SubScene0(title)

        # self.scene8_SubScene01(title)

        # self.scene8_SubScene1(title)

        # self.scene8_SubScene2(title)

        # self.define_properties(title)    # این رو لازم ندارم دیگه 

        # self.scene8_SubScene3(title)

        # self.scene8_SubScene3_0(title)
        # self.scene8_SubScene3_1(title)  # این یک طرفه هست و اون طرفش درست نیست مثل اینکه  ->  درستش کردم :)
        self.scene8_SubScene3_2(title)

        ########## birkhof

        # self.scene8_SubScene4(title)

        # self.scene8_SubScene5(title)

        # self.han_banakh_def(title)  # این رو برای تست اینجا گذاشتم
        # self.han_banakh_shape(title)  # این رو برای تست اینجا گذاشتم

        # self.scene8_SubScene6(title)

        ########## isosceles

        # self.scene8_SubScene7(title)

        # self.scene8_SubScene8(title)

        # self.scene8_SubScene9(title)

        ########## pythagorean

        # self.scene8_SubScene10(title)

        # self.scene8_SubScene11(title)

        # self.scene8_SubScene12(title)

        # self.scene8_SubScene13(title)

        # self.scene8_SubScene14(title)

    def scene7_SubScene0(self, title):
        self.wait(1)
        image = ImageMobject("images/graduate_brain_img_mini.png").scale(3).to_corner(DL)
        self.add(image)
        or_in_hil_titlepart1 = Tex("Orthogonality in", color=BLACK, font_size=80)
        or_in_hil_titlepart2 = Tex("an inner product space", color=BLACK, font_size=80)
        or_in_hil_title = VGroup(or_in_hil_titlepart1, or_in_hil_titlepart2).arrange(DOWN, buff=0.3)
        or_in_hil_title.move_to(title.get_center()+0.5*DOWN)

        self.play(
            Write(or_in_hil_title),
        )
        self.wait(1)
        self.play(
            FadeOut(image),
            FadeOut(or_in_hil_title),
        )
        self.wait(1)

    def scene7_SubScene1(self, title):
        self.play(
            Write(title),
        )

        orth_part0 = MathTex(
            r"\text{An element }x \text{ of an inner product space } X",
            color=BLACK,
        )
        orth_part1 = MathTex(
            r"\text{ is said to be orthogonal to an element } y \in X \text{ if}",
            color=BLACK,
        )
        orth_part2 = MathTex(
            r"\langle x , y \rangle = 0",
            color=BLACK,
        )
        orth_part3 = MathTex(
            r"\text{We also say that } x \text{ and } y \text{ are orthogonal, and we write }",
            color=BLACK,
        )
        orth_part4 = MathTex(
            r"x \perp y .",
            color=BLACK,
        )
        orth_def = VGroup(orth_part0, orth_part1, orth_part2, orth_part3, orth_part4).arrange(DOWN)

        group, box = self.show_definition(orth_def,title ,True)
        def_group = VGroup(group, box).scale(1.1).shift(1*UP)

        self.play(
            Create(box),
            Write(group),
        )
        self.wait(1)

        self.play(
            # FadeOut(title),
            FadeOut(group),
            FadeOut(box),
        )
        self.wait(1)

    def scene7_SubScene2(self, title):

        self.add(title)

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

        all_shapes = VGroup(*[
            plane,
            axes,
            vector_a,
            a_text,
            vector_b,
            b_text,
            inner_product_text,
        ]).scale(1.3).shift(0.5*UP)

        angle_ab = RightAngle(
            vector_a,
            vector_b,
            length=0.3,
            color=BLACK
        )

        self.play(
            Create(plane),
            Create(axes),
        )
        self.play(
            GrowArrow(vector_a, rate_func=rush_from),
            FadeIn(a_text, shift=UP*0.2),
            GrowArrow(vector_b, rate_func=rush_from),
            FadeIn(b_text, shift=UP*0.2),
            Create(angle_ab),
        )
        self.play(
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
            FadeOut(angle_ab),
        )

        self.wait(1)

    def scene7_SubScene3(self, title):
        metric_circle = Ellipse(
            width=14, height=8,
            color=dark_pink,
            stroke_width=4,
            # fill_opacity = 0.01,
        )
        
        norm_circle = Ellipse(
            width=12, height=6,
            color=dark_purple,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(DOWN * 0.3)
        
        banach_circle = Ellipse(
            width=7, height=4,
            color=dark_terquise,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(RIGHT * 1.8+0.8*DOWN)
        
        inner_circle = Ellipse(
            width=7, height=4,
            color=dark_orange,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(LEFT * 1.8+0.8*DOWN)
        
        metric_text = Text(" Metric space ", font_size=60, color=dark_pink).move_to(UP * 3.2)
        
        norm_text = Text(" Normed space ", font_size=48, color=dark_purple).move_to(UP * 1.8)
        
        banach_text = Text(" Banach space ", font_size=36, color=dark_terquise).move_to(RIGHT * 3.5 + 0.8*DOWN)
        
        inner_text = Text(" Inner product\n       space ", font_size=36, color=dark_orange, line_spacing=0.8).move_to(LEFT * 3.5 + 0.8*DOWN)
        
        hilbert_text = Text(" Hilbert space ", font_size=36, color=dark_green).move_to(DOWN * 0.5)

        intersection = Intersection(banach_circle, inner_circle, color=dark_green, fill_opacity=0.1)

        diff_banach = Difference(banach_circle, inner_circle, color=dark_terquise, fill_opacity=0.1)
        
        diff_inner = Difference(inner_circle, banach_circle, color=dark_orange, fill_opacity=0.1)

        all_shapes = VGroup(*[
            metric_circle,
            norm_circle,
            banach_circle,
            inner_circle,
            metric_text,
            norm_text,
            banach_text,
            inner_text,
            hilbert_text,
            intersection,
        ])

        self.wait(0.5)
        self.play(
            FadeIn(all_shapes),
        )
        self.wait(1)

        talk_circle = Ellipse(
            width=7, height=4,
            color=dark_red,
            stroke_width=6,
            fill_opacity = 0.1,
        ).shift(LEFT * 1.8+0.8*DOWN)

        self.wait(0.5)
        inner_text[0:12].set_color(dark_red)
        self.wait(1)
        self.play(
            Create(talk_circle),
        )
        self.wait(1)

        talk_circle2 = Ellipse(
            width=12, height=6,
            color=dark_red,
            stroke_width=6,
            fill_opacity = 0.1,
        ).shift(DOWN * 0.3)

        self.wait(0.5)
        inner_text[0:12].set_color(dark_orange)
        self.wait(0.5)
        norm_text[0:4].set_color(dark_red)
        self.wait(1)
        self.play(
            Transform(talk_circle, talk_circle2),
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                all_shapes,
                talk_circle,
            ]))
        )

        self.wait(1)

    def scene7_SubScene2_1(self, title):
        self.show_nondegeneracy()
        self.show_simplification()
        self.show_continuity()
        self.show_homogeneity()
        self.show_symmetry()
        self.show_additivity()
        self.show_existence()
        # self.show_uniqueness()   #این رو به قبلی اضافه کردم
        # self.show_unique_diagonals()
        self.show_scalar_existence()

    def create_title_and_box_custom(self, title_text, math_formula):
        title = Text(title_text, font_size=60, color=BLACK).to_edge(UP) #.shift(0.3*DOWN)
        formula = MathTex(math_formula, color=BLACK, font_size=45)
        box = SurroundingRectangle(
            formula,
            color=dark_blue,
            buff=0.3,
            fill_opacity=0.1,
            stroke_width=3,
            corner_radius=0.15
        )
        group = VGroup(formula, box).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Create(box), Write(formula))
        self.wait(1)
        return title, group, box

    def show_nondegeneracy(self):
        title, group, box = self.create_title_and_box_custom(
            "Nondegeneracy", 
            r"\forall \lambda , \mu \in \mathbb{K} \quad \lambda x \perp \mu x \iff \lambda x = 0 \lor \mu x = 0"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        
        # val = ValueTracker(2.5)
        
        vec_x = always_redraw(lambda: Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(2.5, 0),
            buff=0, stroke_width=6, color=dark_purple,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_x = always_redraw(
            lambda : MathTex(r"\vec{x}",color=dark_purple).move_to(vec_x.get_center()+0.4*DOWN)
        )

        val1 = ValueTracker(4.5)
        vec_x1 = always_redraw(lambda: Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(val1.get_value(), 0),
            buff=0, stroke_width=6, color=dark_pink,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_x1 = always_redraw(
            lambda : MathTex(r"\lambda \vec{x}",color=dark_pink).move_to(vec_x1.get_center()+0.4*UP)
        )

        val2 = ValueTracker(-3.5)
        vec_x2 = always_redraw(lambda: Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(val2.get_value(), 0),
            buff=0, stroke_width=6, color=dark_red,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_x2 = always_redraw(
            lambda : MathTex(r"\mu \vec{x}",color=dark_red).move_to(vec_x2.get_center()+0.4*DOWN)
        )
        
        dot = Dot(axes.c2p(0,0), color=dark_green, radius=0.15)
        
        self.play(Create(plane))
        self.play(Create(axes))
        self.play(GrowArrow(vec_x), Write(text_x))
        self.play(GrowArrow(vec_x1), Write(text_x1))
        self.play(GrowArrow(vec_x2), Write(text_x2))
        self.wait(0.5)
        self.play(val1.animate.set_value(0.01), run_time=2)
        self.play(Create(dot), Flash(dot, color=dark_green))
        self.wait(1)
        
        # self.play(FadeOut(VGroup(*[
        #     axes,
        #     vec_x,
        #     text_x,
        #     dot,
        #     title,
        #     group,
        #     box,
        #     vec_x1,
        #     text_x1,
        #     vec_x2,
        #     text_x2,
        # ])),
        # FadeOut(plane),
        # )
        
        self.clear()
        self.wait(1)

    def show_simplification(self):
        title, group, box = self.create_title_and_box_custom(
            "Simplification", 
            r"x \perp y \implies \lambda x \perp \lambda y \quad \forall \lambda \in \mathbb{K}"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        lam = ValueTracker(1)
        
        vec_x = always_redraw(lambda: Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(lam.get_value() * 4, 0),
            buff=0, stroke_width=6, color=dark_orange,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_x1 = always_redraw( lambda : 
                MathTex(
                r"\vec{x}",
                color=dark_orange,
            ).move_to(vec_x.get_center()+ 0.4*DOWN)
        )
        text_x2 = always_redraw( lambda : 
                MathTex(
                r"\lambda \vec{x}",
                color=dark_orange,
            ).move_to(vec_x.get_center()+ 0.4*DOWN)
        )
        
        vec_y = always_redraw(lambda: Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(0, lam.get_value() * 2),
            buff=0, stroke_width=6, color=dark_purple,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_y1 = always_redraw( lambda : 
                MathTex(
                r"\vec{y}",
                color=dark_purple,
            ).move_to(vec_y.get_center()+ 0.4*LEFT)
        )
        text_y2 = always_redraw( lambda : 
                MathTex(
                r"\lambda \vec{y}",
                color=dark_purple,
            ).move_to(vec_y.get_center()+ 0.4*LEFT)
        )
        
        angle = always_redraw(lambda: RightAngle(vec_x, vec_y, length=0.3, color=BLACK))
        
        self.play(Create(plane), Create(axes))
        self.play(GrowArrow(vec_x), Write(text_x1), GrowArrow(vec_y), Write(text_y1))
        self.play(Create(angle))

        self.play(
            TransformMatchingTex(text_x1, text_x2),
            TransformMatchingTex(text_y1, text_y2),
            lam.animate.set_value(1.8), run_time=1
        )
        self.play(lam.animate.set_value(0.5), run_time=1)
        self.play(lam.animate.set_value(-1.5), run_time=1.5)
        self.wait(1)
        
        # self.play(FadeOut(VGroup(*self.mobjects)))
        self.clear()
        self.wait(1)

    def get_right_angle_mark(self, vec1, vec2, size=0.3, color=BLACK):
        start = vec1.get_start()
        
        d1 = normalize(vec1.get_end() - vec1.get_start())
        d2 = normalize(vec2.get_end() - vec2.get_start())
        
        p1 = start + d1 * size
        p2 = start + d1 * size + d2 * size
        p3 = start + d2 * size
        
        return Polygon(start, p1, p2, p3,
                    stroke_color=color,
                    stroke_width=2,
                    fill_opacity=0)

    def show_continuity(self):
        title, group, box = self.create_title_and_box_custom(
            "Continuity", 
            r"x_n \perp y_n, \text{ } x_n \to x, \text{ } y_n \to y \implies x \perp y"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip},
        ).next_to(box, DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box, DOWN, buff=0.5)

        self.play(Create(plane), Create(axes))

        # تعداد مراحل چرخش (مرحله آخر = x_n, y_n)
        n_steps = 4
        angles = np.linspace(0, PI/4, n_steps)

        def make_vec_x(angle):
            return Arrow(
                start=axes.c2p(0, 0),
                end=axes.c2p(4 * np.cos(angle), 4 * np.sin(angle)),
                buff=0, stroke_width=5, color=dark_terquise,
                tip_length=0.25, tip_shape=StealthTip
            )

        def make_vec_y(angle):
            return Arrow(
                start=axes.c2p(0, 0),
                end=axes.c2p(-4 * np.sin(angle + 0.01), 4 * np.cos(angle + 0.01)),
                buff=0, stroke_width=5, color=dark_pink,
                tip_length=0.25, tip_shape=StealthTip
            )

        last_text_x = None
        last_text_y = None
        last_angle_mark = None

        for i, ang in enumerate(angles):
            is_last = (i == n_steps - 1)

            vec_x = make_vec_x(ang)
            vec_y = make_vec_y(ang)

            if is_last:
                ang*=1.5
                vec_x = make_vec_x(ang)
                vec_y = make_vec_y(ang)

                label_x = r"\vec{x_n}"
                label_y = r"\vec{y_n}"
            else:
                label_x = rf"\vec{{x_{i+1}}}"
                label_y = rf"\vec{{y_{i+1}}}"

            text_x = MathTex(label_x, color=dark_terquise).move_to(axes.c2p(4 * np.cos(ang), 4 * np.sin(ang)) +0.5*RIGHT)
            text_y = MathTex(label_y, color=dark_pink).move_to(axes.c2p(-4 * np.sin(ang + 0.01), 4 * np.cos(ang + 0.01)) +0.5*UP)

            angle_mark = self.get_right_angle_mark(vec_x, vec_y, size=0.3, color=BLACK)

            if i == 0:
                # مرحله اول: نمایش کامل بردارها با رشد از مبدا
                self.play(
                    GrowArrow(vec_x), Write(text_x),
                    GrowArrow(vec_y), Write(text_y),
                    Create(angle_mark)
                )
            else:
                # مراحل بعد: بدون پاک کردن قبلی‌ها، فقط اضافه می‌شوند
                self.play(
                    ReplacementTransform(prev_vec_x.copy(), vec_x),
                    ReplacementTransform(prev_vec_y.copy(), vec_y),
                    FadeIn(text_x), FadeIn(text_y),
                    FadeIn(angle_mark),
                    run_time=0.8
                )

            prev_vec_x, prev_vec_y = vec_x, vec_y
            last_text_x, last_text_y = text_x, text_y
            last_angle_mark = angle_mark
            self.wait(0.3)

        self.wait(1)

        # حالا x_n, y_n به x, y تبدیل می‌شوند (بدون پاک شدن بقیه چیزها)
        final_text_x = MathTex(r"\vec{x}", color=dark_terquise).move_to(last_text_x.get_center())
        final_text_y = MathTex(r"\vec{y}", color=dark_pink).move_to(last_text_y.get_center())

        self.play(
            Transform(last_text_x, final_text_x),
            Transform(last_text_y, final_text_y),
            run_time=1.5
        )

        self.wait(1)
        self.clear()
        self.wait(1)

    def show_homogeneity(self):
        title, group, box = self.create_title_and_box_custom(
            "Homogeneity", 
            r"x \perp y \implies \lambda x \perp \mu y \quad \forall \lambda, \text{ } \mu \in \mathbb{R}"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)

        lam = ValueTracker(1)
        mu = ValueTracker(1)
        
        vec_x = always_redraw(lambda: Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(lam.get_value() * 3, 0),
            buff=0, stroke_width=6, color=dark_green,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_x1 = always_redraw( lambda : 
                MathTex(
                r"\vec{x}",
                color=dark_green,
            ).move_to(vec_x.get_center()+ 0.4*DOWN)
        )
        text_x2 = always_redraw( lambda : 
                MathTex(
                r"\lambda \vec{x}",
                color=dark_green,
            ).move_to(vec_x.get_center()+ 0.4*DOWN)
        )
        
        vec_y = always_redraw(lambda: Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(0, mu.get_value() * 3),
            buff=0, stroke_width=6, color=dark_blue,
            tip_length=0.25, tip_shape=StealthTip
        ))
        text_y1 = always_redraw( lambda : 
                MathTex(
                r"\vec{y}",
                color=dark_blue,
            ).move_to(vec_y.get_center()+ 0.4*LEFT)
        )
        text_y2 = always_redraw( lambda : 
                MathTex(
                r"\mu \vec{y}",
                color=dark_blue,
            ).move_to(vec_y.get_center()+ 0.4*LEFT)
        )
        
        angle = always_redraw(lambda: self.get_right_angle_mark(vec_x, vec_y, size=0.3, color=BLACK))
        
        self.play(Create(plane), Create(axes))
        self.play(GrowArrow(vec_x), Write(text_x1), GrowArrow(vec_y), Write(text_y1), Create(angle))
        self.play(
            TransformMatchingTex(text_x1, text_x2),
            TransformMatchingTex(text_y1, text_y2),
        )
        self.play(lam.animate.set_value(1.8), run_time=1)
        self.play(mu.animate.set_value(-0.5), run_time=1)
        self.play(lam.animate.set_value(-1), mu.animate.set_value(1.2), run_time=1)
        self.wait(1)
        
        # self.play(FadeOut(VGroup(*self.mobjects)))
        self.clear()
        self.wait(1)

    def show_symmetry(self):
        title, group, box = self.create_title_and_box_custom(
            "Symmetry", 
            r"x \perp y \implies y \perp x"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        
        vec_x = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(4, 0),
            buff=0, stroke_width=5, color=dark_red,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_x = MathTex(
            r"\vec{x}",
            color=dark_red,
        ).move_to(vec_x.get_center()+0.4*DOWN)
        
        vec_y = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(0, 4),
            buff=0, stroke_width=5, color=dark_orange,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_y = MathTex(
            r"\vec{y}",
            color=dark_orange,
        ).move_to(vec_y.get_center()+0.4*LEFT)
        
        arc1 = RightAngle(vec_x, vec_y, length=0.3, color=BLACK)
        arc2 = RightAngle(vec_y, vec_x, length=0.3, color=BLACK)
        
        self.play(Create(plane), Create(axes))
        self.play(GrowArrow(vec_x), Write(text_x), GrowArrow(vec_y), Write(text_y))
        self.play(Create(arc1))
        self.wait(0.5)
        self.play(ReplacementTransform(arc1, arc2))
        self.wait(1)
        
        # self.play(FadeOut(VGroup(*self.mobjects)))
        self.clear()
        self.wait(1)

    def show_additivity(self):
        title, group, box = self.create_title_and_box_custom(
            "Additivity", 
            r"x \perp y \land x \perp z \implies x \perp (y+z)"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        
        vec_x = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(0, 5),
            buff=0, stroke_width=6, color=dark_pink,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_x = MathTex(
            r"\vec{x}",
            color=dark_pink,
        ).move_to(vec_x.get_center()+0.4*LEFT)

        vec_y = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(3, 0),
            buff=0, stroke_width=6, color=dark_green,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_y = MathTex(
            r"\vec{y}",
            color=dark_green,
        ).move_to(vec_y.get_center()+0.4*DOWN)

        vec_z = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(-6, 0),
            buff=0, stroke_width=6, color=dark_orange,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_z = MathTex(
            r"\vec{z}",
            color=dark_orange,
        ).move_to(vec_z.get_center()+0.4*UP)

        vec_sum = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(-3, 0),
            buff=0, stroke_width=6, color=dark_purple,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_sum = MathTex(
            r"\vec{y} + \vec{z}",
            color=dark_purple,
        ).move_to(vec_sum.get_center()+0.4*DOWN)
        
        self.play(Create(plane), Create(axes))
        self.play(GrowArrow(vec_x), Write(text_x), GrowArrow(vec_y), Write(text_y), GrowArrow(vec_z), Write(text_z))
        self.wait(0.5)
        self.play(GrowArrow(vec_sum), Write(text_sum))
        self.play(Create(RightAngle(vec_x, vec_sum, length=0.3, color=BLACK)))
        self.wait(1)
        
        # self.play(FadeOut(VGroup(*self.mobjects)))
        self.clear()
        self.wait(1)

    def show_existence(self):
        title, group, box = self.create_title_and_box_custom(
            "Existence", 
            r"\exists y \in P : \|y\| = \rho \land x \perp y"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        
        vec_x = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(2.5, 1.5),
            buff=0, stroke_width=6, color=dark_purple,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_x = MathTex(
            r"\vec{x}",
            color=dark_purple,
        ).move_to(vec_x.get_center()+0.4*LEFT+0.2*UP)

        circle = Circle(radius=2 * (6/8), color=BLACK).shift(axes.c2p(0,0))
        
        line = Line(axes.c2p(-2.5, 4.16), axes.c2p(2.5, -4.16), color=GRAY).set_opacity(0.5)
        
        vec_y1 = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(-1.03, 1.71),
            buff=0, stroke_width=6, color=dark_terquise,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_y1 = MathTex(
            r"\vec{y_1}",
            color=dark_terquise,
        ).move_to(vec_y1.get_center()+0.4*LEFT+0.1*DOWN)

        vec_y2 = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(1.03, -1.71),
            buff=0, stroke_width=6, color=dark_pink,
            tip_length=0.25, tip_shape=StealthTip
        )
        text_y2 = MathTex(
            r"\vec{y_2}",
            color=dark_pink,
        ).move_to(vec_y2.get_center()+0.4*LEFT+0.1*DOWN)
        
        self.play(Create(plane), Create(axes), GrowArrow(vec_x), Write(text_x))
        self.play(Create(circle))
        self.play(Create(line))
        self.play(GrowArrow(vec_y1), Write(text_y1), GrowArrow(vec_y2), Write(text_y2))
        self.wait(1)
        
        self.play(FadeOut(VGroup(*[
            title, group, box
        ])))

        title, group, box = self.create_title_and_box_custom(
            "Uniqueness", 
            r"\text{The vector } y \text{ is unique given an orientation.}"
        )
        self.wait(1)

        self.clear()
        self.wait(1)

    def show_uniqueness(self):
        title, group, box = self.create_title_and_box_custom(
            "Uniqueness", 
            r"\text{The vector } y \text{ is unique given an orientation.}"
        )
        
        # axes = Axes(
        #     y_range=[-6, 6, 1],
        #     x_range=[-10, 10, 1], 
        #     y_length=6,
        #     x_length=9,
        #     axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip}, # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        # ).next_to(box,DOWN, buff=0.5)
        # plane = NumberPlane(
        #     y_range=[-6, 6, 1],
        #     x_range=[-10, 10, 1],
        #     background_line_style={
        #         "stroke_color": GRAY,
        #         "stroke_opacity": 0.5
        #     },
        #     y_length=6,
        #     x_length=9,
        # ).next_to(box,DOWN, buff=0.5)
        
        # vec_x = Arrow(
        #     start=axes.c2p(0,0), end=axes.c2p(2.5, 1.5),
        #     buff=0, stroke_width=6, color=dark_purple,
        #     tip_length=0.25, tip_shape=StealthTip
        # )
        # circle = Circle(radius=2 * (6/8), color=BLACK).shift(axes.c2p(0,0))
        
        # vec_y1 = Arrow(
        #     start=axes.c2p(0,0), end=axes.c2p(-1.03, 1.71),
        #     buff=0, stroke_width=6, color=dark_terquise,
        #     tip_length=0.25, tip_shape=StealthTip
        # )
        # vec_y2 = Arrow(
        #     start=axes.c2p(0,0), end=axes.c2p(1.03, -1.71),
        #     buff=0, stroke_width=6, color=dark_pink,
        #     tip_length=0.25, tip_shape=StealthTip
        # )
        
        # orientation = Arc(radius=0.7, angle=PI/2, color=dark_orange).add_tip()
        
        # self.play(Create(axes), GrowArrow(vec_x), Create(circle), GrowArrow(vec_y1), GrowArrow(vec_y2))
        # self.play(Create(orientation))
        # self.play(FadeOut(vec_y2), vec_y1.animate.set_color(dark_orange))
        # self.wait(1)
        
        # self.play(FadeOut(VGroup(*self.mobjects)))
        self.clear()
        self.wait(1)

    def show_unique_diagonals(self):
        title, group, box = self.create_title_and_box_custom(
            "Unique Diagonals", 
            r"\exists ! \rho > 0 : (x + \rho y) \perp (x - \rho y)"
        )
        
        rho = ValueTracker(0.4)
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip},
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        
        def get_verts():
            v_x = np.array([8, 0, 0])
            v_y = np.array([2, 6, 0]) * rho.get_value()
            return (
                axes.c2p(0, 0),
                axes.c2p(*v_x),
                axes.c2p(*(v_x + v_y)),
                axes.c2p(*v_y),
            )

        def get_poly():
            p0, p1, p2, p3 = get_verts()
            return Polygon(p0, p1, p2, p3, color=dark_orange, fill_opacity=0.1)

        def get_poly_labels():
            p0, p1, p2, p3 = get_verts()
            mid_bottom = (np.array(p0) + np.array(p1)) / 2
            mid_left   = (np.array(p3) + np.array(p0)) / 2
            label_x = MathTex(r"\vec{x}",        color=dark_orange, font_size=36).move_to(mid_bottom + np.array([0,    -0.35, 0]))
            label_y = MathTex(r"\rho \vec{y}",   color=dark_orange, font_size=36).move_to(mid_left   + np.array([-0.5,  0,   0]))
            return VGroup(label_x, label_y)

        def get_diag1():
            p0, p1, p2, p3 = get_verts()
            d1 = DashedLine(p0, p2, color=dark_red)
            mid = (np.array(p0) + np.array(p2)) / 2
            label = MathTex(r"x + \rho y", color=dark_red, font_size=34).move_to(mid + np.array([-0.8, 0.35, 0])).shift(0.3*DOWN+0.2*LEFT)
            return VGroup(d1, label)

        def get_diag2():
            p0, p1, p2, p3 = get_verts()
            d2 = DashedLine(p1, p3, color=dark_pink)
            mid = (np.array(p1) + np.array(p3)) / 2
            label = MathTex(r"x - \rho y", color=dark_pink, font_size=34).move_to(mid + np.array([0.8, 0.35, 0])).shift(0.3*DOWN+0.3*RIGHT)
            return VGroup(d2, label)

        poly        = always_redraw(get_poly)
        poly_labels = always_redraw(get_poly_labels)
        diag1       = always_redraw(get_diag1)
        diag2       = always_redraw(get_diag2)

        self.play(Create(plane), Create(axes))
        self.play(Create(poly))
        self.play(FadeIn(poly_labels))
        self.play(Create(diag1))
        self.play(Create(diag2))
        self.play(rho.animate.set_value(1.114), run_time=3, rate_func=smooth)
        self.wait(1)
        
        self.clear()
        self.wait(1)

    def show_scalar_existence(self):
        title, group, box = self.create_title_and_box_custom(
            "Scalar Existence", 
            r"\exists a \in \mathbb{K} : x \perp (ax + y)"
        )
        
        axes = Axes(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1], 
            y_length=6,
            x_length=9,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip},
        ).next_to(box,DOWN, buff=0.5)
        plane = NumberPlane(
            y_range=[-6, 6, 1],
            x_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            },
            y_length=6,
            x_length=9,
        ).next_to(box,DOWN, buff=0.5)
        
        vec_x = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(3, 0),
            buff=0, stroke_width=6, color=dark_blue,
            tip_length=0.25, tip_shape=StealthTip
        )
        label_x = MathTex(r"x", color=dark_blue, font_size=36)\
            .next_to(vec_x, DOWN, buff=0.2)

        vec_y = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(2, 2.5),
            buff=0, stroke_width=6, color=dark_green,
            tip_length=0.25, tip_shape=StealthTip
        )
        label_y = MathTex(r"y", color=dark_green, font_size=36)\
            .next_to(vec_y.get_end(), UR, buff=0.15)
        
        dashed = DashedLine(axes.c2p(2, 2.5), axes.c2p(2, 0), color=GRAY)
        
        vec_ax = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(-2, 0),
            buff=0, stroke_width=6, color=dark_red,
            tip_length=0.25, tip_shape=StealthTip
        )
        label_ax = MathTex(r"ax", color=dark_red, font_size=36)\
            .next_to(vec_ax, DOWN, buff=0.2)
        
        vec_sum = Arrow(
            start=axes.c2p(0,0), end=axes.c2p(0, 2.5),
            buff=0, stroke_width=6, color=dark_orange,
            tip_length=0.25, tip_shape=StealthTip
        )
        label_sum = MathTex(r"ax + y", color=dark_orange, font_size=36)\
            .next_to(vec_sum.get_end(), UL, buff=0.15)
        
        right_angle = RightAngle(vec_x, vec_sum, length=0.3, color=BLACK)

        self.play(Create(plane), Create(axes))
        self.play(GrowArrow(vec_x), FadeIn(label_x),
                  GrowArrow(vec_y), FadeIn(label_y))
        self.play(Create(dashed))
        self.play(GrowArrow(vec_ax), FadeIn(label_ax))
        self.play(GrowArrow(vec_sum), FadeIn(label_sum),
                  Create(right_angle))
        self.wait(1)
        
        self.clear()
        self.wait(1)

    def scene7_1(self, title):
        title_property_line1 = Text("Properties of Orthogonality",color=BLACK).scale(1.5)
        title_property_line2 = Text("in Inner Product Spaces",color=BLACK).scale(1.5)
        title_property = VGroup(title_property_line1, title_property_line2).arrange(DOWN, buff=0.2)
        
        pic1 = ImageMobject(r"images/property1.png").scale(1.3).move_to(title_property.get_center()+2.5*UL)
        pic2 = ImageMobject(r"images/property2.png").scale(1.3).move_to(title_property.get_center()+2.5*DR)

        self.play(
            Write(title_property),
            FadeIn(pic1),
            FadeIn(pic2),
        )
        self.wait(1)
        self.play(
            FadeOut(title_property),
            FadeOut(pic1),
            FadeOut(pic2),
        )

    def scene7(self, title):

        # title.shift(0.5*DOWN)
        # self.play(
        #     Write(title),
        # )
        # self.wait(0.5)
        # self.play(
        #     FadeOut(title),
        # )
        
        # self.scene7_SubScene0(title)

        # self.scene7_SubScene1(title)

        # self.scene7_SubScene2(title)

        self.scene7_SubScene2_1(title)

        # self.scene7_SubScene3(title)

    def scene6_SubScene0(self, title):

        # inner_product_text = MathTex(
        #     r"\text{Inner product}",
        #     color=BLACK
        # ).scale(1.2).to_edge(LEFT).shift(0.2*RIGHT)
        # box1 = SurroundingRectangle(
        #     inner_product_text,
        #     color=dark_orange,        
        #     buff=0.3,    
        #     fill_opacity=0.1,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )

        # norm_text = MathTex(
        #     r"\text{Norm}",
        #     color=BLACK
        # ).scale(1.2)
        # box2 = SurroundingRectangle(
        #     norm_text,
        #     color=dark_green,        
        #     buff=0.3,    
        #     fill_opacity=0.1,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )
        # arrow1 = Arrow(
        #     start=box1.get_right()+0.1*RIGHT,
        #     end=box2.get_left()+0.1*LEFT,
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_red,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # inner_to_norm_text = MathTex(
        #     r"\|x\| = \sqrt{\langle x , x \rangle}",
        #     color=BLACK
        # ).scale(1.6).move_to(arrow1.get_center()+2.5*UP)
        # box4 = SurroundingRectangle(
        #     inner_to_norm_text,
        #     color=dark_red,        
        #     buff=0.3,    
        #     fill_opacity=0.1,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )

        # metric_text = MathTex(
        #     r"\text{Metric}",
        #     color=BLACK
        # ).scale(1.2).to_edge(RIGHT).shift(0.4*LEFT)
        # box3 = SurroundingRectangle(
        #     metric_text,
        #     color=dark_pink,        
        #     buff=0.3,    
        #     fill_opacity=0.1,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )
        # arrow2 = Arrow(
        #     start=box2.get_right()+0.1*RIGHT,
        #     end=box3.get_left()+0.1*LEFT,
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_terquise,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # norm_to_metric_text = MathTex(
        #     r"d(x,y) = \|x-y\|",
        #     color=BLACK
        # ).scale(1.6).move_to(arrow2.get_center()+2.5*DOWN)
        # box5 = SurroundingRectangle(
        #     norm_to_metric_text,
        #     color=dark_terquise,        
        #     buff=0.3,    
        #     fill_opacity=0.1,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )

        # self.play(
        #     Create(box1),
        #     Write(inner_product_text),
        # )
        # self.play(
        #     GrowArrow(arrow1),
        # )
        # self.play(
        #     Create(box2),
        #     Write(norm_text),
        # )
        # self.play(
        #     Create(box4),
        #     Write(inner_to_norm_text),
        # )
        # self.play(
        #     GrowArrow(arrow2),
        # )
        # self.play(
        #     Create(box3),
        #     Write(metric_text),
        # )
        # self.play(
        #     Create(box5),
        #     Write(norm_to_metric_text),
        # )

        # self.wait(1)

        # self.play(
        #     FadeOut(VGroup(*[
        #         box3,
        #         metric_text,
        #         box2,
        #         norm_text,
        #         box1,
        #         inner_product_text,
        #         arrow1,
        #         arrow2,
        #         box4,
        #         inner_to_norm_text,
        #         box5,
        #         norm_to_metric_text,
        #     ]))
        # )

        # self.wait(1)

        title_hilbert = Tex("Hilbert space", color=BLACK, font_size=80)
        title_hilbert.move_to(title.get_center())
        self.play(Write(title_hilbert))

        part1 = MathTex(
            r"\text{A Hilbert space is an inner product space } (X,\langle . ,. \rangle) ",
            # r"d(x,y)=\|x-y\|.",
            color=BLACK
        )
        part2 = MathTex(
            r"\text{ which is complete with respect to the metric}",
            # r"d(x,y)=\|x-y\|.",
            color=BLACK
        )
        part3 = MathTex(
            r"\text{induced by its inner product .}",
            # r"d(x,y)=\|x-y\|.",
            color=BLACK
        )
        banach_definition = VGroup(part1, part2, part3).arrange(DOWN,buff=0.2)

        group, box = self.show_definition(banach_definition,title,True)
        banach_group = VGroup(group, box).scale(1.15)

        self.play(
            Create(box),
            Write(group),
        )

        self.wait(1)

        self.play(
            FadeOut(banach_group),
        )

    def scene6_SubScene1(self, title):
        book_image = ImageMobject("images/book_brain.png").scale(2).to_corner(DL).shift(0.4*LEFT+0.5*DOWN)
        self.add(book_image)

        norm_space = MathTex(r"(X\, , \langle . , . \rangle)",r"+",r"\text{Complete}",r"\text{ w.r.t }",r"\text{inner product induced metric}",color=BLACK).scale(1.1).move_to(title.get_center()+2*DOWN)
        norm_space.set_color_by_tex(r"(X\, , \langle . , . \rangle)",color=dark_pink)
        norm_space.set_color_by_tex(r"\text{Complete}",color=dark_pink)
        brace = BraceBetweenPoints(norm_space.get_left()+0.5*DOWN, norm_space.get_right()+0.5*DOWN).set_color(dark_orange)
        banach_space = MathTex(r"\text{Hilbert space}",color=dark_pink).scale(2).next_to(brace,DOWN)

        self.play(
            Write(norm_space[0]),
        )
        self.play(
            Write(norm_space[1:]),
        )
        self.play(
            GrowFromCenter(brace, run_time=0.8),
        )
        self.play(
            Write(banach_space),
        )
        self.wait(1)
        fade_out_list = [
            norm_space,
            banach_space,
            brace,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
            FadeOut(book_image),
        )

    def scene6_SubScene2(self, title):

        metric_circle = Ellipse(
            width=14, height=8,
            color=dark_pink,
            stroke_width=4,
            # fill_opacity = 0.01,
        )
        
        norm_circle = Ellipse(
            width=12, height=6,
            color=dark_purple,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(DOWN * 0.3)
        
        banach_circle = Ellipse(
            width=7, height=4,
            color=dark_terquise,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(RIGHT * 1.8+0.8*DOWN)
        
        inner_circle = Ellipse(
            width=7, height=4,
            color=dark_orange,
            stroke_width=4,
            # fill_opacity = 0.01,
        ).shift(LEFT * 1.8+0.8*DOWN)
        
        # hilbert_circle = Circle(
        #     radius=1.5,
        #     color=dark_green,
        #     stroke_width=3
        # ).shift(UP * 0.2)
        
        # متن‌ها
        metric_text = Text(" Metric space ", font_size=60, color=dark_pink).move_to(UP * 3.2)
        
        norm_text = Text(" Normed space ", font_size=48, color=dark_purple).move_to(UP * 1.8)
        
        banach_text = Text(" Banach space ", font_size=36, color=dark_terquise).move_to(RIGHT * 3.5 + 0.8*DOWN)
        
        inner_text = Text(" Inner product\n      space ", font_size=36, color=dark_orange, line_spacing=0.8).move_to(LEFT * 3.5 + 0.8*DOWN)
        
        hilbert_text = Text(" Hilbert space ", font_size=36, color=dark_green).move_to(DOWN * 0.5)

        intersection = Intersection(banach_circle, inner_circle, color=dark_green, fill_opacity=0.1)

        diff_banach = Difference(banach_circle, inner_circle, color=dark_terquise, fill_opacity=0.1)
        
        diff_inner = Difference(inner_circle, banach_circle, color=dark_orange, fill_opacity=0.1)

        self.play(
            Create(metric_circle),
            Write(metric_text),
        )
        self.wait(0.5)
        self.play(
            Create(norm_circle),
            Write(norm_text),
        )
        self.wait(0.5)
        self.play(
            Create(inner_circle),
            Write(inner_text),
        )
        self.wait(0.5)
        self.play(
            Create(banach_circle),
            Write(banach_text),
        )
        self.wait(0.5)
        self.play(
            Create(intersection),
            Write(hilbert_text),
        )
        self.wait(1)
        
        self.play(
            FadeOut(VGroup(*[
                metric_circle,
                norm_circle,
                banach_circle,
                inner_circle,
                metric_text,
                norm_text,
                banach_text,
                inner_text,
                hilbert_text,
                intersection,
            ]))
        )
        self.wait(1)

    def scene6_SubScene3(self, title):
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
        self.play(Create(plane))

        title_example1 = Tex(
            "Example",
            color=dark_green, font_size=80
        ).to_edge(UP)
        self.play(
            Write(title_example1),
        )

        space_c_1_1 = MathTex(r"\text{Space } C( [-1, 1] )",color=dark_pink).scale(1.5).move_to(title.get_center()+3*LEFT+1*DOWN)
        definition_text = MathTex(r"g,",r"f : [-1, 1] \to \mathbb{R}",color=BLACK).scale(1.3).next_to(space_c_1_1,DOWN)
        
        banach_space = MathTex(r"\text{Banach space}",color=BLACK).scale(1.2).next_to(definition_text,DOWN,buff=0.5)
        image_cross = ImageMobject("images/red_cross.png").scale(1.2).move_to(banach_space.get_center())

        box1 = SurroundingRectangle(
            banach_space,
            color=dark_red,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        hilbert_space = MathTex(r"\text{Hilbert space}",color=BLACK).scale(1.2).next_to(banach_space,RIGHT,buff=3)
        image_cross2 = ImageMobject("images/red_cross.png").scale(1.2).move_to(hilbert_space.get_center())
        box2 = SurroundingRectangle(
            hilbert_space,
            color=dark_red,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow1 = Arrow(
            start=box1.get_right()+0.1*RIGHT,
            end=box2.get_left()+0.1*LEFT,
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            Write(space_c_1_1),
            Write(definition_text),
        )
        self.wait(0.5)
        self.play(
            Create(box1),
            Write(banach_space),
        )
        self.wait(0.5)
        self.add(image_cross)
        self.wait(0.5)
        self.play(
            GrowArrow(arrow1),
            Create(box2),
            Write(hilbert_space),
        )
        self.wait(0.5)
        self.add(image_cross2)
        self.wait(0.5)

        space_l_2_1 = MathTex(r"\text{Space } L^2( [-1, 1] )",color=dark_pink).scale(1.5).move_to(box1.get_center()+1.5*DOWN)
        l2_norm = MathTex(
            r"\|f\| = (\int_{-1}^{1} |f(x)|^2 \, dx)^{\frac{1}{2}}",
            color=dark_orange,
        ).next_to(space_l_2_1, RIGHT,buff=1.5)

        hil2_space = MathTex(r"\text{Hilbert space}",color=BLACK).scale(1.2).next_to(space_l_2_1,DOWN,buff=0.5)
        box3 = SurroundingRectangle(
            hil2_space,
            color=dark_green,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        image_check = ImageMobject("images/tik .png").scale(0.1).next_to(hil2_space,RIGHT).shift(0.2*UP)
        self.play(
            Write(space_l_2_1),
        )
        self.wait(0.5)
        self.play(
            Write(l2_norm),
        )
        self.wait(0.5)
        self.play(
            Create(box3),
            Write(hil2_space),
        )
        self.wait(0.5)
        self.add(image_check)
        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                title_example1,
                space_c_1_1,
                space_l_2_1,
                definition_text,
                banach_space,
                hil2_space,
                hilbert_space,
                box1,
                box2,
                box3,
                arrow1,
                l2_norm,
            ])),
            FadeOut(image_check),
            FadeOut(image_cross),
            FadeOut(image_cross2),
        )
        self.play(
            FadeOut(plane),
        )
        self.wait(1)

    def hilbert_animation(self, title):
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

        image = ImageMobject("images/david_hilbert.png").scale(0.35)

        name_text = Text("David Hilbert",color=BLACK,font="mistral",font_size=75).next_to(image,UP,buff=0.3)
        date_text = Text("1862 – 1943",color=BLACK,font="mistral",font_size=75).next_to(image,DOWN,buff=0.3)
        text2 = Text("Hilbert’s \n23 Problems",color=dark_orange,font="mistral",font_size=65).next_to(image,RIGHT,buff=0.3).shift(1*UP)
        text4 = Text("We must know\nwe will know",color=dark_red,font="mistral",font_size=65).next_to(image,RIGHT,buff=0.1).shift(1.7*DOWN)
        text1 = Text("Hilbert spaces",color=dark_pink,font="mistral",font_size=65).next_to(image,LEFT,buff=0.3).shift(1*UP)
        text3 = Text("Quantum \nmechanics",color=dark_terquise,font="mistral",font_size=65).next_to(image,LEFT,buff=0.3).shift(1*DOWN)


        self.play(
            Create(plane),
        )
        self.wait(0.5)
        self.add(image)
        self.wait(1)
        self.play(
            Write(name_text),
            Write(date_text),
        )
        self.wait(1)
        self.play(
            Write(text1),
        )
        self.wait(1)
        self.play(
            Write(text2),
        )
        self.wait(1)
        self.play(
            Write(text3),
        )
        self.wait(1)
        self.play(
            Write(text4),
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                name_text,
                date_text,
                text1,
                text2,
                text3,
                text4,
            ])),
            FadeOut(image),
        )
        self.play(
            FadeOut(plane),
        )
        self.wait(1)


    def scene6(self, title):
        title.shift(0.5*DOWN)
        # self.play(
        #     Write(title),
        # )
        # self.wait(0.5)
        # self.play(
        #     FadeOut(title),
        # )

        self.hilbert_animation(title)

        # self.scene6_SubScene0(title)

        # self.scene6_SubScene1(title)

        # self.scene6_SubScene2(title)

        # self.scene6_SubScene3(title)

    def scene5_SubScene0(self, title):

        book_image = ImageMobject("images/book_brain.png").scale(1.6).to_corner(DL).shift(0.4*LEFT)
        self.add(book_image)

        x_def = MathTex(
            r"y \in X",
            color=BLACK
        ).scale(1.2).to_corner(UL)
        norm_def_from_inner_product = MathTex(
            r"\|y\|",
            r" = ",
            r"\sqrt{\langle y , y \rangle}",
            color=BLACK
        ).scale(1.2).next_to(x_def,RIGHT,buff=1).shift(0.1*UP)

        norm_def_box = SurroundingRectangle(
            norm_def_from_inner_product,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Write(x_def),
        )
        self.play(
            Create(norm_def_box),
            Write(norm_def_from_inner_product),
        )
        self.wait(0.5)
        self.play(
            FadeOut(x_def),
            VGroup(norm_def_box, norm_def_from_inner_product).animate.scale(1.2).to_corner(UL),
        )
        self.wait(0.5)

        line1_n1 = MathTex(
            r"\| y \| = 0 ",r"\;\Leftrightarrow\;",r" y = 0",
            color=dark_green,
        ).scale(1.6)
        line2_n1 = MathTex(
            r"\| y \| = 0",
            r"\;\Leftrightarrow\;",
            r" \sqrt{\langle y , y \rangle} = 0",
            color=BLACK
        )
        line3_n1 = MathTex(
            r"\;\Leftrightarrow\; \langle y , y \rangle = 0",
            color=BLACK
        )
        line4_n1 = MathTex(
            r"\;\Leftrightarrow\; y = 0",
            r"\quad (IP4) ",
            r"\quad .\blacksquare", #find me
            color=BLACK
        )

        n1_proof = VGroup(line2_n1, line3_n1, line4_n1).arrange(DOWN,buff=0.4,aligned_edge=LEFT).scale(1.5)
        line3_n1.shift(2.5*RIGHT)
        line4_n1.shift(2.5*RIGHT)
        n1_proof_box = SurroundingRectangle(
            n1_proof,
            color=dark_green,        
            buff=0.5,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        line1_n1.next_to(norm_def_box,RIGHT,buff=1)
        VGroup(n1_proof, n1_proof_box).next_to(line1_n1,DOWN,buff=1).shift(1*LEFT)

        self.play(
            Create(n1_proof_box),
            Write(line1_n1),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(line1_n1[0], line2_n1[0]),
        )
        self.play(
            Write(line2_n1[1]),
            TransformFromCopy(norm_def_from_inner_product, line2_n1[2]),
        )
        self.wait(0.5)
        self.play(
            Write(line3_n1),
        )
        self.wait(0.5)
        self.play(
            Write(line4_n1[1]),
        )
        self.play(
            Write(line4_n1[0]),
        )
        self.play(
            Write(line4_n1[2]),
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(line1_n1, n1_proof, n1_proof_box)),
        )

        self.wait(1)

        line1_n2 = MathTex(
            r"\| \alpha \, y \| ",
            r"= | \alpha | \| y \| ",
            color=dark_green,
        ).scale(1.6)
        
        line2_n2 = MathTex(
            r"\| \alpha \, y \|",
            r" = \sqrt{\langle \alpha \, y , \alpha \, y \rangle}",
            color=BLACK,
        )
        line3_n2 = MathTex(
            r" = \sqrt{\alpha \langle y , \alpha \, y \rangle}",
            r"\quad (IP2)",
            color=BLACK,
        )
        line4_n2 = MathTex(
            r" = \sqrt{\alpha \overline{\alpha} \langle y , y \rangle}",
            r"\quad \text{(Point 1-2)}",
            color=BLACK,
        )
        line5_n2 = MathTex(
            r" = \sqrt{| \alpha |^2 \langle y , y \rangle}",
            r" = | \alpha | \, \| y \|",
            r"\quad .\blacksquare",
            color=BLACK,
        )

        n2_proof = VGroup(line2_n2, line3_n2, line4_n2, line5_n2).arrange(DOWN,buff=0.4,aligned_edge=LEFT).scale(1.2)
        line3_n2.shift(2*RIGHT)
        line4_n2.shift(2*RIGHT)
        line5_n2.shift(2*RIGHT)
        n2_proof_box = SurroundingRectangle(
            n2_proof,
            color=dark_green,        
            buff=0.5,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        line1_n2.next_to(norm_def_box,RIGHT,buff=1)
        VGroup(n2_proof, n2_proof_box).next_to(line1_n2, DOWN,buff=1)

        self.play(
            Write(line1_n2),
        )
        self.wait(0.5)
        self.play(
            Create(n2_proof_box),
            TransformFromCopy(line1_n2[0], line2_n2[0]),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(norm_def_from_inner_product, line2_n2[1]),
        )
        self.wait(0.5)
        self.play(
            Write(line3_n2[1]),
        )
        self.play(
            Write(line3_n2[0]),
        )
        self.wait(0.5)
        self.play(
            Write(line4_n2[1]),
        )
        self.play(
            Write(line4_n2[0]),
        )
        self.wait(0.5)
        self.play(
            Write(line5_n2[0]),
        )
        self.play(
            Write(line5_n2[1]),
        )
        self.play(
            Write(line5_n2[2]),
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(line1_n2, n2_proof, n2_proof_box)),
        )

        self.wait(1)

        line1_n3 = MathTex(
            r"\| x + y \| ",
            r"\le \| x \| +  \| y \| ",
            color=dark_green,
        ).scale(1.6)

        line2_n3 = MathTex(
            r"\| x + y \|^2 ",
            color=BLACK,
        )

        line3_n3 = MathTex(
            r" = \|x\|^2 + ",
            r"\langle x ,y \rangle + \langle y , x \rangle ",
            r"+ \|y\|^2",
            r"\quad \text{(Point 1-2)}",
            color=BLACK,
        )

        line4_n3_0 = MathTex(
            r"\quad  \text{Triangle inequality for numbers}",
            color=dark_red,
        )

        line4_n3 = MathTex(
            r"\le \|x\|^2 + 2 \, | \langle x ,y \rangle | + \|y\|^2",
            color=BLACK,
        )

        line5_n3 = MathTex(
            r"\le \|x\|^2 + 2 \, \|x\| \, \|y\| + \|y\|^2",
            r"\quad \text{Schwarz inequality}",
            color=BLACK,
        )

        line6_n3 = MathTex(
            r" = ( \|x\| + \|y\| )^2 \quad .\blacksquare",
            color=BLACK,
        )

        n3_proof = VGroup(line2_n3, line3_n3, line4_n3_0, line4_n3, line5_n3, line6_n3).arrange(DOWN,buff=0.4,aligned_edge=LEFT) #.scale(1.2)
        # line3_n3.shift(2*RIGHT)
        # line4_n3.shift(2*RIGHT)
        # line5_n3.shift(2*RIGHT)
        n3_proof_box = SurroundingRectangle(
            n3_proof,
            color=dark_green,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        line1_n3.next_to(norm_def_box,RIGHT,buff=1)
        VGroup(n3_proof, n3_proof_box).next_to(line1_n3, DOWN,buff=0.5).shift(1.5*LEFT)

        self.play(
            Write(line1_n3),
        )
        self.wait(0.5)
        self.play(
            Create(n3_proof_box),
            TransformFromCopy(line1_n3[0], line2_n3[0]),
        )
        self.wait(0.5)
        self.play(
            Write(line3_n3[3]),
        )
        self.play(
            Write(line3_n3[:3]),
        )
        self.wait(0.5)
        line3_n3[1].set_color(dark_red)
        self.play(
            Write(line4_n3_0),
        )
        self.play(
            Write(line4_n3),
        )
        self.wait(0.5)
        self.play(
            Write(line5_n3[1]),
        )
        self.play(
            Write(line5_n3[0]),
        )
        self.wait(0.5)
        self.play(
            Write(line6_n3),
        )
        
        self.wait(1)

        self.play(
            FadeOut(VGroup(line1_n3, n3_proof, n3_proof_box,norm_def_box , norm_def_from_inner_product)),
            FadeOut(book_image),
        )

        self.wait(1)

    def scene5_SubScene1(self, title):
        inner_text = MathTex(
            r"\text{Inner product }",
            r" \Longrightarrow ",
            r"\text{ Norm}",
            color=BLACK
        )
        back_text = MathTex(
            r" \Longleftarrow ",
            color=BLACK
        ).move_to(inner_text[1].get_center()+0.5*DOWN)

        title_example_group = VGroup(inner_text, back_text).move_to(title.get_center()) #aligned_edge=
        
        cross_image = ImageMobject("images/red_cross.png").scale(0.7).move_to(back_text.get_center())

        back_box = SurroundingRectangle(
            back_text,
            color=dark_red,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        exmaple1_part1 = MathTex(
            r"\text{Euclidean inner product  } ",
            color=dark_blue
        )
        ep3 = MathTex(
            r"\langle (w_1, \ldots, w_n), (z_1, \ldots, z_n) \rangle = w_1\overline{z_1} + \cdots + w_n\overline{z_n}.",
            color=dark_blue,
        )
        exmaple1_part2 = MathTex(
            r"\text{Euclidean Norm  }",
            color=dark_green
        )
        ep4 = MathTex(
            r"\|x\| = (\xi_1 \overline{\xi_1} + \cdots + \xi_n \overline{\xi_n})^{1/2} = (|\xi_1|^2 + \cdots + |\xi_n|^2)^{1/2}",
            color=dark_green,
        )
        exmaple1_group = VGroup(exmaple1_part1, ep3, exmaple1_part2, ep4).arrange(DOWN,buff=0.5).scale(1).next_to(title_example_group,DOWN,buff=1.5)

        box1 = SurroundingRectangle(
            exmaple1_group,
            color=dark_pink,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Write(inner_text),
        )
        self.wait(0.5)
        self.play(
            Create(box1),
            Write(exmaple1_part1),
            Write(ep3),
        )
        self.wait(0.5)
        self.play(
            Write(exmaple1_part2),
            Write(ep4),
        )
        self.wait(0.5)
        self.play(
            FadeOut(exmaple1_group),
            FadeOut(box1),
        )
        self.wait(0.5)
        self.play(
            Write(back_text),
        )
        self.wait(0.5)
        self.add(cross_image)
        self.wait(0.5)

        exmaple1_part1 = MathTex(
            r"\text{The } L^1 \text{ Norm is not induced by an inner product.  } ",
            color=dark_blue
        )
        ep3 = MathTex(
            r"\text{The } L^{\infty} \text{ Norm is not induced by an inner product.  } ",
            color=dark_blue,
        )
        exmaple1_part2 = MathTex(
            r"\text{The } L^{P} \text{ Norm (where } P \ne 2 \text{ ) } ",
            color=dark_red
        ).scale(1.3)
        ep4 = MathTex(
            r"\text{is not induced by an inner product. }",
            color=dark_red
        ).scale(1.3)
        
        exmaple1_group = VGroup(exmaple1_part1, ep3, exmaple1_part2, ep4).arrange(DOWN,buff=0.5).scale(1).next_to(title_example_group,DOWN,buff=1.5)

        box1 = SurroundingRectangle(
            exmaple1_group,
            color=dark_pink,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Create(box1),
            Write(exmaple1_group),
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                box1,
                exmaple1_group,
                inner_text,
                back_text,
            ])),
            FadeOut(cross_image),
        )

        self.wait(1)

    def scene5_SubScene2(self, title):
        question_tex = MathTex(r"\text{ Which norms come from an inner product ? }").set_color(BLACK)
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

    def scene5_SubScene3(self, title):
        paralle_text_part2 = MathTex(
            r"\|x + y\|^2 + \|x - y\|^2 = 2(\|x\|^2 + \|y\|^2)",
            color=BLACK
        ).scale(1.3)
        paralle_text_part1 = MathTex(
            r"\text{Parallelogram Equality}",
            color=dark_terquise
        ).scale(1.4)

        p_group = VGroup(paralle_text_part1, paralle_text_part2).arrange(DOWN,buff=0.5)

        box1 = SurroundingRectangle(
            p_group,
            color=dark_terquise,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        p_group_all = VGroup(p_group, box1)
        p_group_all.to_edge(UP)

        self.play(
            Create(box1),
            Write(p_group),
        )
        self.wait(1)

        line1 = MathTex(
            r"\|x + y\|^2 + \|x - y\|^2 ",
            r"= \langle x + y, x + y \rangle + \langle x - y, x - y \rangle",
            color=BLACK
        )

        line2 = MathTex(
            r"= \|x\|^2 + \|y\|^2 + \langle x, y \rangle + \langle y, x \rangle",
            color=BLACK
        )

        line3 = MathTex(
            r"+ \|x\|^2 + \|y\|^2 - \langle x, y \rangle - \langle y, x \rangle",
            color=BLACK
        )

        line4 = MathTex(
            r"= 2(\|x\|^2 + \|y\|^2) \, . ",
            color=BLACK
        )

        proof_text = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT)
        line2.shift(3.5*RIGHT)
        line3.shift(4*RIGHT)
        line4.shift(3.5*RIGHT)

        square = Square(side_length=0.3, color=BLACK, fill_opacity=0).move_to(line4.get_center()+2.2*RIGHT+1.1*DOWN)

        box2 = SurroundingRectangle(
            proof_text,
            color=dark_purple,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        VGroup(proof_text, box2).shift(1*DOWN)

        self.play(
            Create(box2),
            Write(line1[0]),
        )
        self.wait(0.5)
        self.play(
            Write(line1[1]),
        )
        self.wait(0.5)
        self.play(
            Write(line2),
        )
        self.play(
            Write(line3),
        )
        self.wait(0.5)
        self.play(
            Write(line4),
            Create(square),
        )

        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                proof_text,
                box2,
                square,
            ])),
        )

        self.wait(1)

        plane = NumberPlane(
            y_range=[-6, 7, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=13,
        ).move_to([0, 0, 0]+3*DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-6, 7, 1],
            y_length=8,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+3*DOWN)
        self.play(
            p_group_all.animate.shift(0.2*UP),
            Create(plane),
            Create(axes)
        )
        self.wait(0.5)

        arrow1 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,1),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow_1_top = Arrow(
            start=axes.c2p(1,3),
            end=axes.c2p(7,4),
            buff=0,
            stroke_width=4,
            color=dark_red,
            tip_length=0.15,
            tip_shape=StealthTip
        )

        a_text = MathTex(r"\vec{x}",color=dark_red).scale(1.1).move_to(arrow1.get_center()+0.5*DOWN)

        arrow2 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(1,3),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        arrow_2_right = Arrow(
            start=axes.c2p(6,1),
            end=axes.c2p(7,4),
            buff=0,
            stroke_width=4,
            color=dark_green,
            tip_length=0.15,
            tip_shape=StealthTip
        )

        b_text = MathTex(r"\vec{y}",color=dark_green).scale(1.1).move_to(arrow2.get_center()+0.6*UP+0.2*LEFT)

        arrow_sum = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(7,4),
            buff=0,
            stroke_width=4,
            color=dark_purple,
            tip_length=0.15,
            tip_shape=StealthTip
        )
        sum_text = MathTex(r"\vec{x} + \vec{y}",color=dark_purple).scale(1.0).move_to(arrow_sum.get_center()+0.5*DOWN+0.3*RIGHT)

        arrow_diff = Arrow(
            start=axes.c2p(1,3),
            end=axes.c2p(6,1),
            buff=0,
            stroke_width=4,
            color=dark_orange,
            tip_length=0.15,
            tip_shape=StealthTip
        )
        diff_text = MathTex(r"\vec{x} - \vec{y}",color=dark_orange).scale(1.0).move_to(arrow_diff.get_center()+0.5*UP+0.3*LEFT)

        self.play(
            GrowArrow(arrow1),
            Write(a_text),
        )
        # self.wait(0.5)
        self.play(
            GrowArrow(arrow2),
            Write(b_text),
        )

        self.play(
            GrowArrow(arrow_1_top),
        )
        self.play(
            GrowArrow(arrow_2_right),
        )
        self.wait(0.5)

        self.play(
            GrowArrow(arrow_sum),
            Write(sum_text),
        )
        self.play(
            Create(arrow_diff),
            Write(diff_text),
        )

        self.wait(1)

        self.play(
            FadeOut(VGroup(*[
                plane, 
                axes,
                arrow1,
                arrow2,
                arrow_1_top,
                arrow_2_right,
                arrow_diff,
                arrow_sum,
                sum_text,
                diff_text,
                a_text,
                b_text,
                p_group_all,
            ])),
        )

        self.wait(1)

    def scene5_SubScene4(self, title):
        circle_metric = Circle(4,dark_pink,fill_color=dark_pink,fill_opacity=0.1)
        text_metric_space = MathTex(r"\text{Metric space}",color=dark_pink).scale(2).move_to(circle_metric.get_center()+2.3*UP)

        circle_norm = Circle(2.8,dark_purple,fill_color=dark_purple,fill_opacity=0.1).shift(1*DOWN)
        text_norm_space = MathTex(r"\text{Normed space}",color=dark_purple).scale(1.5).move_to(circle_norm.get_center()+1.3*UP)

        circle_banach = Circle(1.8,dark_orange,fill_color=dark_orange,fill_opacity=0.1).shift(1.8*DOWN)
        text_banach_space_part1 = MathTex(r"\text{Inner product} ",color=dark_orange)
        text_banach_space_part2 = MathTex(r"\text{space} ",color=dark_orange)
        text_banach_space = VGroup(text_banach_space_part1, text_banach_space_part2).arrange(DOWN,buff=0.2).move_to(circle_banach.get_center()+0.2*UP)

        
        self.play(
            Write(text_norm_space),
            Create(circle_norm),
        )
        self.wait(0.5)
        self.play(
            Write(text_banach_space),
            TransformFromCopy(circle_norm, circle_banach),
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

    def scene5(self, title):
        title.shift(0.5*DOWN)
        # self.play(
        #     Write(title),
        # )
        # self.wait(0.5)
        # self.play(
        #     FadeOut(title),
        # )

        # self.scene5_SubScene0(title)

        # self.scene5_SubScene1(title)

        # self.scene5_SubScene2(title)

        # self.scene5_SubScene3(title)

        self.scene5_SubScene4(title)

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

    def scene4_SubScene5(self,title):
        title_inner_product = Tex("Inner product", color=BLACK, font_size=80).to_edge(UP)
        self.play(
            Write(title_inner_product),
        )
        def_inner_product_line1 = MathTex(
            r"\text{An inner product on } X \text{ is a function(mapping) }",
            r"\langle \cdot , \cdot \rangle : X \times X \to \mathbb{K}"
        ).set_color(BLACK)

        def_inner_product_line2 = MathTex(
            r"\text{satisfying}"
        ).set_color(BLACK)

        # def_inner_product_line3 = MathTex(
        #     r"\begin{aligned}",
        #     # r"1.& \quad \|x\| \ge 0 \\"
        #     r"1.& \quad \|x\| = 0 \iff x = 0 \\",
        #     r"2.& \quad \|\lambda x\| = |\lambda| \, \|x\| \\",
        #     r"3.& \quad \|x + y\| \le \|x\| + \|y\|",
        #     r"\end{aligned}"
        # ).set_color(BLACK).scale(0.85)

        line1 = MathTex(r"IP1.\quad \langle x + y , z \rangle = \langle x , z \rangle + \langle y , z \rangle",color=BLACK)
        line2 = MathTex(r"IP2.\quad \langle \lambda x , y \rangle = \lambda \langle x , y \rangle",color=BLACK)
        line3 = MathTex(r"IP3.\quad \langle x , y \rangle = \overline{\langle y , x \rangle}",color=BLACK)
        line4 = MathTex(r"IP4.\quad \langle x , x \rangle \ge 0",color=BLACK)
        line5 = MathTex(r"\phantom{IP4.}\quad \langle x , x \rangle = 0 \iff x = 0",color=BLACK)

        def_inner_product_line3 = VGroup(line1, line2, line3, line4, line5).arrange(DOWN, aligned_edge=LEFT, buff=0.4).set_color(BLACK).scale(0.9)

        def_inner_product_line4 = MathTex(
            r"\quad \text{for all vectors }",
            r"x, y, z \in X \text{ and all scalars } \lambda \in \mathbb{K} ."
            ).set_color(BLACK)

        def_inner_product = VGroup(def_inner_product_line1, def_inner_product_line2, def_inner_product_line3,def_inner_product_line4).arrange(DOWN, buff=0.3).scale(0.9)

        def_inner_product.next_to(title.get_center(), DOWN)

        inner_product_group, inner_product_box = self.show_definition(def_inner_product, title,True)
        inner_product_group.shift(3.5*UP)
        inner_product_box.move_to(inner_product_group.get_center())
        inner_product_box_and_text_group = VGroup(inner_product_group,inner_product_box)
        inner_product_box_and_text_group.scale(0.9)

        self.play(
            Create(inner_product_box),
            Write(inner_product_group),
        )
        self.wait(1)
        for line in [line1, line2, line3,line4, line5]:
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
            )
            self.wait(1)
            self.play(
                Uncreate(rect), 
            )

        self.wait(1)
        self.play(
            FadeOut(VGroup(*[
                inner_product_group,
                inner_product_box,
                title_inner_product,
            ]))
        )
        self.wait(1)


    def scene4_SubScene6(self, title):
        title_inner_product = Tex("Point 1", color=dark_blue, font_size=80).to_edge(UP)
        self.play(
            Write(title_inner_product),
        )

        ip3 = MathTex(
            r"IP3.\quad \langle x , y \rangle = ",
            r"\overline{\langle y , x \rangle}",
            color=BLACK
        ).scale(1.4).next_to(title_inner_product, DOWN,buff=1)
        bar_part = ip3[1][0]
        box1 = SurroundingRectangle(
            bar_part,
            color=dark_pink,        
            buff=0.1,    
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        ip3_text = MathTex(r"\text{Complex conjugation}",color=dark_pink).scale(1.4).next_to(ip3, DOWN,buff=1)
        box2 = SurroundingRectangle(
            ip3_text,
            color=dark_pink,        
            buff=0.2,    
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        note_text = MathTex(
            r"\text{If } \mathbb{K} = \mathbb{R} \text{ ,then } \langle x , y \rangle = \langle y , x \rangle" , 
            color=dark_green,
        ).scale(1.4).next_to(ip3_text, DOWN,buff=1)

        self.play(
            Write(ip3),
        )
        self.play(
            Create(box1),
        )
        self.play(
            Create(box2),
            Write(ip3_text),
        )
        self.wait(1)
        self.play(
            Write(note_text),
        )
        self.wait(1)
        fadeout_list = [
            ip3,
            box1,
            box2,
            ip3_text,
            note_text,
        ]
        self.play(
            FadeOut(VGroup(*fadeout_list)),
        )
        self.wait(1)

        title_inner_product2 = Tex("Point 2", color=dark_blue, font_size=80).to_edge(UP)
        self.play(
            TransformMatchingTex(title_inner_product, title_inner_product2),
        )
        self.wait(0.2)

        ip1 = MathTex(r"IP1.\quad \langle x + y , z \rangle = \langle x , z \rangle + \langle y , z \rangle",color=BLACK).scale(1.4)
        ip2 = MathTex(r"IP2.\quad \langle \lambda x , y \rangle = \lambda \langle x , y \rangle",color=BLACK).scale(1.4)

        ip_group = VGroup(ip1,ip2).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.9).next_to(title_inner_product2, DOWN,buff=0.6)

        line1 = MathTex(
            r"\quad \langle \alpha x + \beta y , z \rangle ",
            r" = \langle \alpha x , z \rangle + \langle \beta y , z \rangle ",
            r"\quad (IP1)",
            color=dark_green,
        )
        # line2 = MathTex(
        #     r" = \quad \langle \alpha x , z \rangle + \langle \beta y , z \rangle ",
        #     r"\quad IP1.",
        #     color=dark_green,
        # )
        line3 = MathTex(
            r" = \alpha \langle x , z \rangle + \beta \langle y , z \rangle ",
            r"\quad (IP2)",
            color=dark_green,
        )

        line_group = VGroup(line1,line3).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.9).next_to(ip2, DOWN,buff=0.6)
        line3.shift(2.5*RIGHT)

        conclusion = MathTex(
            r"\text{Inner product is }",
            r"\text{linear}",
            r"\text{ in the }",
            r"\text{first factor}",
            r"\text{.}",
            color=BLACK
        ).scale(1.5).to_edge(DOWN)
        conclusion.set_color_by_tex(r"\text{linear}", dark_red)
        conclusion.set_color_by_tex(r"\text{first factor}", dark_red)

        self.play(
            Write(ip_group),
        )
        self.play(
            Write(line1[0]),
        )
        self.play(
            Write(line1[2]),
        )
        self.play(
            Write(line1[1]),
        )
        self.play(
            Write(line3[1]),
        )
        self.play(
            Write(line3[0]),
        )
        self.wait(0.5)
        self.play(
            Write(conclusion),
        )

        fadeout_list = [
            ip_group,
            line1,
            line3,
            conclusion,
        ]
        self.play(
            FadeOut(VGroup(*fadeout_list)),
        )
        self.wait(1)

        title_inner_product3 = Tex("Point 3", color=dark_blue, font_size=80).to_edge(UP)
        self.play(
            TransformMatchingTex(title_inner_product2, title_inner_product3),
        )
        self.wait(0.2)

        line1 = MathTex(
            r"\langle  x , \alpha y + \beta z \rangle ",
            r" = \overline{ \langle  \alpha y + \beta z , x \rangle } ",
            r"\quad (IP3)",
            color=dark_green,
        )
        line2 = MathTex(
            r" = \overline{ \alpha \langle y , x \rangle + \beta \langle z , x \rangle } ",
            r"\quad (IP1 - IP2)",
            color=dark_green,
        )
        line3 = MathTex(
            r" = \overline{ \alpha } \overline{ \langle y , x \rangle } + \overline{ \beta } \overline{ \langle z , x \rangle } ",
            color=dark_green,
        )
        line4 = MathTex(
            r" = \overline{ \alpha } \langle x , y \rangle + \overline{ \beta } \, \langle x , z \rangle",
            r"\quad (IP3)",
            color=dark_green,
        )
        line_group = VGroup(line1,line2,line3,line4).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(1.2).next_to(title_inner_product3, DOWN,buff=0.6)
        line2.shift(2.8*RIGHT)
        line3.shift(3*RIGHT)
        line4.shift(3*RIGHT)

        conclusion2_part1 = MathTex(
            r"\text{Inner product is }",
            r"\text{conjugate linear}",
            r"\text{ in the }",
            r"\text{second factor}",
            r"\text{.}",
            color=BLACK
        ).scale(1.1).to_edge(DOWN)
        conclusion2_part1.set_color_by_tex(r"\text{conjugate linear}", dark_red)
        conclusion2_part1.set_color_by_tex(r"\text{second factor}", dark_red)

        conclusion2_part2 = MathTex(
            r"\text{Inner product is }",
            r"\text{semi-linear}",
            r"\text{ in the }",
            r"\text{second factor}",
            r"\text{.}",
            color=BLACK
        ).scale(1.1).to_edge(DOWN)
        conclusion2_part2.set_color_by_tex(r"\text{semi-linear}", dark_red)
        conclusion2_part2.set_color_by_tex(r"\text{second factor}", dark_red)

        conclusion2 = MathTex(
            r"\text{Inner product is }",
            r"\text{half-linear}",
            r"\text{ in the }",
            r"\text{second factor}",
            r"\text{.}",
            color=BLACK
        ).scale(1.1).to_edge(DOWN)
        conclusion2.set_color_by_tex(r"\text{half-linear}", dark_red)
        conclusion2.set_color_by_tex(r"\text{second factor}", dark_red)

        self.play(
            Write(line1[0]),
        )
        self.play(
            Write(line1[2]),
        )
        self.play(
            Write(line1[1]),
        )
        self.play(
            Write(line2[1]),
        )
        self.play(
            Write(line2[0]),
        )
        self.play(
            Write(line3),
        )
        self.play(
            Write(line4[1]),
        )
        self.play(
            Write(line4[0]),
        )
        self.wait(1)
        self.play(
            Write(conclusion2_part1),
        )
        self.wait(0.5)
        self.play(
            TransformMatchingTex(conclusion2_part1, conclusion2_part2),
        )
        self.wait(0.5)
        self.play(
            TransformMatchingTex(conclusion2_part2, conclusion2),
        )
        self.wait(0.5)
        fadeout_list = [
            line_group,
            conclusion2,
        ]
        self.play(
            FadeOut(VGroup(*fadeout_list)),
        )
        self.wait(1)

        title_inner_product4 = Tex("Conclusion", color=dark_blue, font_size=80).to_edge(UP)
        self.play(
            TransformMatchingTex(title_inner_product3, title_inner_product4),
        )
        self.wait(0.2)
        conclusion.scale(0.8).next_to(title_inner_product4,DOWN,buff=0.8)
        conclusion2.next_to(conclusion,DOWN,buff=0.5)
        result_part1 = MathTex(
            r"1 \text{ times linear }",
            color=dark_orange,
        ).next_to(conclusion2,DOWN,buff=0.5)
        result_part2 = MathTex(
            r"\frac{1}{2} \text{ times linear }",
            color=dark_orange,
        ).next_to(result_part1,DOWN,buff=0.5)
        result_part3 = MathTex(
            r"1 \, \frac{1}{2} \text{ times linear }",
            color=dark_orange,
        ).next_to(conclusion2,DOWN,buff=0.5)
        result_part4 = MathTex(
            r"\text{Sesquilinear}",
            color=dark_red,
        ).scale(2).next_to(conclusion2,DOWN,buff=0.5)

        self.play(
            Write(conclusion),
        )
        self.play(
            Write(conclusion2),
        )
        self.wait(0.5)
        self.play(
           TransformFromCopy(conclusion[1], result_part1),
        )
        self.wait(0.5)
        self.play(
           TransformFromCopy(conclusion2[1], result_part2),
        )
        self.wait(0.5)
        self.play(
           TransformMatchingTex(VGroup(result_part1, result_part2), result_part3),
        )
        self.wait(0.5)
        self.play(
           TransformMatchingTex(result_part3, result_part4),
        )
        self.wait(0.5)
        
        fadeout_list = [
            title_inner_product4,
            conclusion,
            conclusion2,
            # result_part1,
            # result_part2,
            # result_part3,
            result_part4,

        ]
        self.play(
            FadeOut(VGroup(*fadeout_list)),
        )
        self.wait(1)

    def scene4_SubScene7(self, title):
        title_example = Tex("Example", color=dark_purple, font_size=80).to_edge(UP)
        self.play(
            Write(title_example),
        )

        exmaple1_part1 = MathTex(
            r"\text{Euclidean inner product : } \langle \cdot, \cdot \rangle : \mathbb{K}^n \times \mathbb{K}^n \to \mathbb{K}",
            color=dark_blue
        )
        exmaple1_part2 = MathTex(
            r"\langle (w_1, \ldots, w_n), (z_1, \ldots, z_n) \rangle = w_1\overline{z_1} + \cdots + w_n\overline{z_n}.",
            color=dark_blue
        )
        exmaple1_group = VGroup(exmaple1_part1, exmaple1_part2).arrange(DOWN,buff=0.5).scale(1.2).next_to(title_example,DOWN,buff=0.9)

        box1 = SurroundingRectangle(
            exmaple1_group,
            color=dark_purple,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        exmaple2_part1 = MathTex(
            r"\langle \cdot, \cdot \rangle : C([-1,1]) \times C([-1,1]) \to \mathbb{R}",
            color=dark_green
        )
        exmaple2_part2 = MathTex(
            r"\langle f, g \rangle = \int_{-1}^{1} f(x)g(x) \, dx.",
            color=dark_green
        )
        exmaple2_group = VGroup(exmaple2_part1, exmaple2_part2).arrange(DOWN,buff=0.5).scale(1.2).next_to(exmaple1_group,DOWN,buff=0.9)

        box2 = SurroundingRectangle(
            exmaple2_group,
            color=dark_purple,        
            buff=0.3,    
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Create(box1),
            Write(exmaple1_group),
        )
        self.wait(1)
        self.play(
            Create(box2),
            Write(exmaple2_group),
        )
        self.wait(1)
        self.play(
            FadeOut(VGroup(*[
                title_example,
                exmaple1_group,
                box1,
                exmaple2_group,
                box2,
            ]))
        )
        self.wait(1)

    def scene4_SubScene8(self, title):
        text_normed_space = MathTex(r"\text{Inner product space}",color=dark_green).move_to(title.get_center()+DOWN).scale(2)
        text_normed_space_parts = MathTex(r"( \, ",r"X",r" \, \, , \, \, ",r"\langle . , . \rangle",r" \, )",color=dark_blue,arg_separator="  ").move_to(text_normed_space.get_center()+1.6*DOWN).scale(2)
        rect_x = SurroundingRectangle(
            text_normed_space_parts[1],
            color=dark_pink,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_vector_space = MathTex(r"\text{Vector space}",color=dark_pink).move_to(text_normed_space_parts.get_center()+2.6*DOWN+3*LEFT).scale(2)
        rect_vec_x = SurroundingRectangle(
            text_vector_space,
            color=dark_pink,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        VGroup(text_vector_space, rect_vec_x).shift(0.3*LEFT)
        arrow_x = CurvedArrow(
            start_point=text_normed_space_parts[1].get_left()+0.2*LEFT,
            end_point=rect_vec_x.get_top()+0.2*UP,
            angle=PI/2,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        rect_d = SurroundingRectangle(
            text_normed_space_parts[3],
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_distance = MathTex(r"\text{Inner product}",color=dark_orange).move_to(text_normed_space_parts.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        rect_distance = SurroundingRectangle(
            text_distance,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_d = CurvedArrow(
            start_point=text_normed_space_parts[3].get_right()+0.2*RIGHT,
            end_point=rect_distance.get_top()+0.2*UP,
            angle=-PI/2,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            Write(text_normed_space),
        )
        self.wait(1)
        self.play(
            Write(text_normed_space_parts[::2]),
        )
        self.wait(1)
        self.play(
            Write(text_normed_space_parts[1]),
            Create(rect_x),
            Create(arrow_x),
            Create(rect_vec_x),
            Write(text_vector_space),
        )
        self.wait(1)
        self.play(
            Write(text_normed_space_parts[3]),
            Create(rect_d),
            Create(arrow_d),
            Create(rect_distance),
            Write(text_distance),
        )
        self.wait(1)

        fade_out_list = [text_normed_space, text_normed_space_parts, rect_x, 
                         arrow_x, rect_vec_x, text_vector_space,
                         rect_d, arrow_d, rect_distance, text_distance]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
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

        # self.scene4_subScene4(title)

        # self.scene4_SubScene5(title)

        # self.scene4_SubScene6(title)

        # self.scene4_SubScene7(title)

        self.scene4_SubScene8(title)


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
                        "From Inner product to Norm", 
                        r"Hilbert spaces \\ The Kingdom of Completeness", 
                        "Orthogonality", 
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