from manim import * 
import numpy as np

def StyleSetter_BasedOnTextType(text_type:str):
        if text_type == "title":
            return {"font_size": 48, "color": WHITE, "weight": BOLD, "should_center": True, "font": "Arial"}
        elif text_type == "subtitle":
            return {"font_size": 40, "color": WHITE}
        else:
            return {"font_size": 24, "color": WHITE}

config.background_color = WHITE

class TitleScene(Scene):

    topics = {
        0 : "Banach Spaces",
        1 : "others",
    }
    
    def construct(self):

        self.scene1()

        current_topic = self.topics[0]
        title = self.scene2(current_topic)
        self.play(FadeOut(title))

        current_topic = self.topics[1]
        title = self.scene2(current_topic)


    
    def scene2(self,current_topic):
        #  scene 2
        # ------------------------------ 
        # 2-1 : show items

        title = Tex("Topics We Discussed In this Video ...", arg_separator=" ", should_center=True, color=BLACK).to_edge(UP).set_font_size(60)
        
        self.play(Write(title))

        self.wait(0.1)

        items_list = ["Banach Spaces","others"]
        blist = BulletedList(*items_list).set_color(BLACK).scale(1.25).to_edge(LEFT).shift(1.75*UP)

        self.play(Write(blist))

        self.wait(1)

        current_item_mob = blist[items_list.index(current_topic)]
        target_scale = 1.5
        target_shift = 1.5 * RIGHT

        self.play(
            current_item_mob.animate.set_color(GREEN_E).scale(target_scale).shift(target_shift),
            run_time=1.0 
        )
        
        self.wait(1)

        selected_title = Tex(current_topic, arg_separator=" ").set_color(BLACK).set_font_size(80).move_to(title.get_center())
        self.play(
            Transform(title, selected_title),
            FadeOut(blist)
        )

        self.wait(1)

        return title

    def scene1(self):
        # add scence 1
        # ------------------------------ 
        # 1-1 : title

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

        graph1 = ImageMobject("images/graph_2_img.png").scale(0.8).move_to(axes.get_center() + 3*RIGHT + 0.25*UP)
        graph2 = ImageMobject("images/graph_3_img.png").scale(1.2).move_to(axes.get_center() + 3*LEFT + 0.4*UP)

        self.play(
            Write(title_up),
            Write(title_down),
        )

        self.wait(0.1)  

        self.play(
            FadeIn(axes),
            FadeIn(graph1),
            FadeIn(graph2)
        )

        self.wait(1)

        self.play(
            FadeOut(axes),
            FadeOut(graph1),
            FadeOut(graph2)
        )

        self.wait(0.1)  

        self.play(
            Unwrite(title_up),
            Unwrite(title_down),
        )
        self.remove(star1)
        self.remove(star2)
