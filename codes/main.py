from manim import *
import numpy as np

def style_setter_based_on_text_type(text_type: str):
    if text_type == "title":
        return {"font_size": 48, "color": WHITE, "weight": BOLD, 
                "should_center": True, "font": "Arial"}
    elif text_type == "subtitle":
        return {"font_size": 40, "color": WHITE}
    else:
        return {"font_size": 24, "color": WHITE}

class TitleScene(Scene):
    topics = {
        0: "Banach Spaces",
        1: "others",
    }
    
    def construct(self):

        self.scene1()

        current_topic = self.topics[0]
        title = self.scene2(current_topic)

        self.play(title.animate.set_opacity(0.02).scale(1.02))
        self.wait(0.5)
        
        warning_text = MathTex(
            'X', '\\text{ is a }', '\\text{ vector space }', 
            '\\text{ over } k, \\quad k \\in \\{\\mathbb{R}, \\mathbb{C}\\}',
            color="#9A0000",
            tex_to_color_map={
                'X': BLACK, 
                '\\text{ vector space }': BLACK,
            }
        ).scale(1.35)
        self.show_warning(warning_text)
        self.wait(0.5)
        
        self.play(title.animate.set_opacity(1).scale(1/1.02))
        def_banach = self.scene3(title)

        self.scene4(def_banach, title)

        self.wait(1)
        
        self.play(FadeOut(title))
        
        # current_topic = self.topics[1]
        # title = self.scene2(current_topic)

    def scene4(self, def_banach, title):
        """scene 4: definition of complete"""

        # 4-1 : definition
        line1 = MathTex("X", "\\text{ is complete }").set_color(BLACK)
        line2 = MathTex(
            "\\text{if every }", 
            "\\textbf{Cauchy sequence }", 
            "(x_n) \\subset X"
        ).set_color(BLACK)
        line2.set_color_by_tex("\\textbf{Cauchy sequence }","#9A0000")
        line3 = MathTex(
            "\\textbf{converges }", 
            "\\text{in } X."
        ).set_color(BLACK)
        line3.set_color_by_tex("\\textbf{converges }","#9A0000")

        def_complete = VGroup(line1, line2, line3).arrange(DOWN, buff=0.5)
        
        def_complete.next_to(title.get_center() + DOWN * 2, DOWN)
        
        # 4-2 : shape
        group,box = self.show_definition(def_complete, title)
        
        zoom = 2

        shape_center = box.get_center() + DOWN*0.25 + RIGHT*1.5
        group_box_group = VGroup(box, group)

        circle = Circle(
            radius=3.3,
            color="#5E913B",
            fill_color="#5D913B66",
            fill_opacity=0.2
        ).move_to(shape_center)

        self.play(FadeTransform(group_box_group, circle))
        self.wait(0.5)

        angles = np.linspace(0, 2*PI, 8, endpoint=False)
        radii = [1.72, 1.7, 1.0, 1.6, 1.9, 1.85, 1.2, 1.8]
        radii = [r * zoom for r in radii]

        points = [
            shape_center + np.array([
                radii[i] * np.cos(angles[i]),
                radii[i] * np.sin(angles[i]),
                0
            ])
            for i in range(len(angles))
        ]

        smooth_shape = VMobject(color="#5E913B", fill_color="#5D913B66", fill_opacity=0.2)
        smooth_shape.set_points_smoothly(points + [points[0]])
        smooth_shape.close_path()

        self.play(FadeTransform(circle, smooth_shape), run_time=2)
        self.wait(1)

        num_points = 5
        distances = [11.0, 6.0, 3.0, 0.65, 0]
        # distances = [d * zoom for d in distances]

        # start_pos = shape_center + np.array([0.5, 0.7, 0]) * zoom
        # end_pos   = shape_center + np.array([-0.7, -0.5, 0]) * zoom

        start_pos = shape_center + np.array([0.8, -0.4, 0])
        end_pos   = shape_center + np.array([-1.7, -1.5, 0])

        all_positions = []
        for i in range(num_points):
            t = i / (num_points - 1)
            base_pos = start_pos + t * (end_pos - start_pos)

            direction = end_pos - start_pos
            perpendicular = np.array([-direction[1], direction[0], 0])
            if np.linalg.norm(perpendicular) > 0:
                perpendicular /= np.linalg.norm(perpendicular)

            offset = perpendicular * distances[i] * 0.5
            position = base_pos + offset
            all_positions.append(position)

        colors = [
            "#7A3D7B12", "#7A3D7B2B", "#7A3D7B40", "#7A3D7B55",
            "#7A3D7B6A", "#7A3D7B7F", "#7A3D7B94", "#7A3D7BA9",
            "#7A3D7BBE", "#7A3D7BD3"
        ]

        dots = []
        all_position = []
        for i, pos in enumerate(all_positions):
            dot = Dot(
                point=pos,
                color=colors[i],
                radius=0.1,
                fill_opacity=0.9 - (0.7 * i/(num_points-1))
            ).shift(3*UP).shift(LEFT)
            dots.append(dot)
            all_position.append(dot.get_center())
            self.play(FadeIn(dot), run_time=0.1)
            self.wait(0.1)
        all_positions = all_position.copy()
        
        self.wait(1)

        lines = VGroup()
        for i in range(num_points-1):
            line = Line(
                start=all_positions[i],
                end=all_positions[i+1],
                color="#7597BE",
                stroke_width=1,
            )
            lines.add(line)

        self.play(Create(lines), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(lines), run_time=0.5)

        arrow_start = title.get_center() + 3*DOWN + 2*LEFT
        arrow_end = all_positions[-1]

        arrow = Arrow(
            start=arrow_start,
            end=arrow_end,
            color=BLACK,
            stroke_width=6,
            tip_length=0.3,
            max_tip_length_to_length_ratio=0.25,
            buff=0.1
        )

        limit_text = Text("limit", font_size=24, color=BLACK, weight=BOLD)
        limit_text.next_to(arrow, UP, buff=0.3)

        final_dot = Dot(
            point=arrow_end,
            color=BLACK,
            radius=0.12,
            fill_opacity=1
        )

        self.play(
            GrowArrow(arrow),
            Write(limit_text),
            Transform(dots[-1], final_dot),
        )

        for _ in range(2):
            self.play(
                final_dot.animate.scale(1.5).set_color("#9A0000"),
                rate_func=there_and_back,
            )

        self.wait(2)

        # 4-3 : fade out every thing
        self.play(
            FadeOut(arrow),
            FadeOut(limit_text),
            FadeOut(final_dot),
        )
        for dot in dots+[smooth_shape]:
            self.play(
                FadeOut(dot)
            )

        self.wait(0.5)
        
        # 4-4 : set changes to start with normed space definition
        self.play(
            def_banach[1].animate.set_color(BLACK).scale(1/1.4),
            def_banach[2].animate.set_opacity(1).scale(1/0.8),
            run_time=1.0
        )

        self.wait(0.5)

        self.play(
            def_banach[2].animate.set_color("#7597BE").scale(1.4),
            def_banach[1].animate.set_opacity(0.03).scale(0.8),
            run_time=1.0
        )

    def show_warning(self, body: MathTex):
        """Show warning message with box"""

        title_text = Text("Note", color="#9A0000", font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color="#9A0000",
            fill_color="#9A000045",
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
    
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

    def show_definition(self, definition: MathTex, total_title):
        """Show definition with box"""

        title_text = Text("Definition", color="#5E913B", font_size=36)

        group = VGroup(title_text, definition).arrange(DOWN, buff=0.3)
        
        box = RoundedRectangle(
            corner_radius=0.3,
            color="#5E913B",
            fill_color="#5D913B66",
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
        

        self.play(Create(box), Write(group))
        self.wait(2)
        return group, box

    def scene3(self, title):
        """scene 3: definition of Banach space"""

        def_banach = Tex(
            'A', ' Complete ', ' Normed Space',
            color=BLACK, font_size=60
        ).move_to(title.get_center() + DOWN)
        
        text_group, box = self.show_definition(def_banach, title)
        
        self.wait(1)
        
        self.play(FadeOut(text_group[0]), FadeOut(box))
        self.wait(0.1)

        self.play(Unwrite(def_banach[0]))
        self.wait(0.5)

        self.play(
            def_banach[1].animate.shift(UP * 1.5 + LEFT * 1.5),
            def_banach[2].animate.shift(UP * 1.5 + RIGHT * 1.5),
            run_time=1.0
        )
        
        self.wait(0.5)
        
        self.play(
            def_banach[1].animate.set_color("#7597BE").scale(1.4),
            def_banach[2].animate.set_opacity(0.03).scale(0.8),
            run_time=1.0
        )
        
        self.wait(1)
        return def_banach

    def scene2(self, current_topic):
        """scene 2: show topics list"""

        title = Tex(
            "Topics We Will Discuss In this Video ...",
            color=BLACK, font_size=60
        ).to_edge(UP)
        
        self.play(Write(title))
        self.wait(0.5)

        items_list = ["Banach Spaces", "others"]
        blist = BulletedList(*items_list).set_color(BLACK).scale(1.25).to_edge(LEFT).shift(1.75*UP)

        self.play(Create(blist))
        self.wait(1)

        current_item_index = items_list.index(current_topic)

        current_item_mob = blist[current_item_index]
        
        target_scale = 1.5
        target_shift = RIGHT * 1.5

        self.play(
            current_item_mob.animate.set_color(GREEN_E).scale(target_scale).shift(target_shift),
            run_time=1.0
        )
        
        self.wait(1)

        selected_title = Tex(current_topic, color=BLACK, font_size=80)
        selected_title.move_to(title.get_center())
        
        self.play(
            Transform(title, selected_title),
            FadeOut(blist)
        )
        
        self.wait(1)
        return title

    def scene1(self):
        """scene 1: title screen"""

        style = {
            "font_size": 85, "color": BLACK
        }

        title_up = Tex('Kinds of', 'Orthogonality',arg_separator=" ",**style).to_edge(UP)
        title_up[1].set_color(GREEN_E)
        title_down = Tex('in', 'Banach Spaces',arg_separator=" ",**style).move_to(title_up.get_center()+DOWN*0.75)
        title_down[1].set_color(GREEN_E)
        
        
        # 1-2 : add image

        star1 = ImageMobject("images/star_1_img.png").move_to(title_up.get_center()+ 6*LEFT + 0.5*DOWN )
        self.add(star1)

        star2 = ImageMobject("images/star_1_img.png").move_to(title_down.get_center()+ 5*RIGHT + 1.5*DOWN )
        self.add(star2)

        # 1-3 : add shapes
        # NumberLine
        axes = Axes(x_range=[0,5], y_range=[0,5], y_length=4, x_axis_config={"color":BLACK, "include_ticks":False, "tip_width":0.25},y_axis_config={"color":BLACK, "include_ticks":False, "tip_width":0.25}).to_corner(DL)
        self.add(axes)
        
        graph1 = ImageMobject("images/graph_2_img.png").scale(0.8).move_to(axes.get_center() + 3*RIGHT + 0.25*UP)
        self.add(graph1)
        
        graph2 = ImageMobject("images/graph_3_img.png").scale(1.2).move_to(axes.get_center() + 3*LEFT + 0.4*UP)
        self.add(graph2)

        self.play(
            Write(title_up),
            Write(title_down),
        )

        # self.wait(0.1)  

        # self.play(
        #     FadeIn(axes),
        #     FadeIn(graph1),
        #     FadeIn(graph2)
        # )

        self.wait(1)

        # self.play(
        #     FadeOut(axes),
        #     FadeOut(graph1),
        #     FadeOut(graph2)
        # )

        # self.wait(0.1)  

        self.play(
            Unwrite(title_up),
            Unwrite(title_down),
        )

        self.remove(star1)
        self.remove(star2)
        self.remove(axes)
        self.remove(graph1)
        self.remove(graph2)


config.background_color = WHITE