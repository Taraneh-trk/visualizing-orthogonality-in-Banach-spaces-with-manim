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

        topic_number = 2
        title = self.scene3(topic_number,False)

        self.scene6(title)

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
        ...    

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
        VGroup(n1_proof, n1_proof_box).next_to(line1_n1,DOWN,buff=1)

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
            r" = ( \|x\| + \|y\| )^2",
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