from manimlib.imports import *
import numpy

class intro1(Scene):
    def construct(self):
        a = TextMobject('In this video I will attempt to explain').shift(UP*0.5)
        b = TextMobject('The effect of changing the parameters in a parabolic graph').shift(DOWN*0.5)
        self.play(Write(a))
        self.wait(0.5)
        self.play(Write(b))
        self.wait(0.5)
        self.play(FadeOut(a),FadeOut(b))
        self.wait(0.5)

class a(Scene):
    def construct(self):
        a = TextMobject('ax').scale(3)
        b = TexMobject('a','x^','2').scale(3)
        b[2].shift(RIGHT*0.3,UP*0.2)
        self.play(Write(a),Write(b[2]))
        self.wait(0.5)
        self.play(FadeOut(a),FadeOut(b[2]))

class ax(GraphScene):

    def xTo2(self, x):
        return x ** 2

    def xTo2a1(self, x):
        return x ** 2 * 1

    def xTo2a2(self, x):
        return x ** 2 * 2

    def xTo2a3(self, x):
        return x ** 2 * 5

    def xTo2a12(self, x):
        return x ** 2 / 2

    def xTo2a13(self, x):
        return x ** 2 / 5

    def nxTo2a(self, x):
        return -x ** 2

    CONFIG = {
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -6,
        "y_max" : 6,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
        "y_labeled_nums": range(-6, 8, 2),
    }


    def construct(self):

        arrowRight = Arrow()
        arrowRight.rotate(2*np.pi)
        arrowRight.scale(0.6)

        arrowLeft = Arrow()
        arrowLeft.rotate(np.pi)
        arrowLeft.scale(0.6)

        arrowDown = Arrow()
        arrowDown.rotate(1.5 * np.pi)
        arrowDown.scale(0.6)

        arrowUp = Arrow()
        arrowUp.rotate(0.5 * np.pi)
        arrowUp.scale(0.6)

        formula1 = TexMobject('ax^2+bx+c')
        formula = TexMobject('ax^2+bx+c')
        formulaNbc = TexMobject('ax^2')

        formula.bg = SurroundingRectangle(formula,color=BLACK,fill_color=BLACK, fill_opacity=1)
        formulaNbc.bg = SurroundingRectangle(formulaNbc,color=YELLOW,fill_color=BLACK,fill_opacity=1)

        canonicalParabulas = TexMobject('For "canonical" Prabulas b = 0, so we can ignore it')
        canonicalParabulas.bg = SurroundingRectangle(canonicalParabulas, color=BLACK, fill_color=BLACK, fill_opacity=1)

        formulaNb = TexMobject('ax^2+c')
        formulaNb.bg = SurroundingRectangle(canonicalParabulas, color=BLACK, fill_color=BLACK, fill_opacity=1)

        formula.scale(1.5)
        formulaNbc.scale(1.5)
        formula.bg.scale(1.5)
        formulaNbc.bg.scale(1.5)

        self.play(FadeIn(formula.bg),Write(formula))
        self.wait(0.25)
        formulaNbc.align_to(formula,LEFT)
        self.wait(0.25)
        self.play(FadeIn(formulaNbc),FadeOut(formula))
        self.wait(0.25)
        temp = TexMobject('ax^2')
        temp.scale(1.5)
        temp.shift(UP,UP,LEFT,LEFT,LEFT,UP,LEFT,LEFT,LEFT)
        self.play(Transform(formulaNbc,temp))
        self.wait(0.25)

        self.setup_axes(animate=True)
        self.wait(0.25)

        Temp = TexMobject('ax^2')
        Temp.scale(1.5)
        Temp.shift(UP, UP, LEFT, LEFT, LEFT, UP, LEFT, LEFT, LEFT)

        a1 = TexMobject('a = 1')
        a1.scale(1.5)
        a1.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT)
        a1.align_to(Temp, LEFT)

        a2 = TexMobject('a = 2')
        a2.scale(1.5)
        a2.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT)
        a2.align_to(Temp, LEFT)

        a3 = TexMobject('a = 5')
        a3.scale(1.5)
        a3.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT)
        a3.align_to(Temp, LEFT)

        a12 = TexMobject('a = \dfrac{1}{2}')
        a12.scale(1.5)
        a12.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT)
        a12.align_to(Temp, LEFT)

        a13 = TexMobject('a = \dfrac{1}{5}')
        a13.scale(1.5)
        a13.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT)
        a13.align_to(Temp, LEFT)

        xto2 = self.get_graph(self.xTo2)
        xto2a1 = self.get_graph(self.xTo2a1)
        xto2a2 = self.get_graph(self.xTo2a2)
        xto2a3 = self.get_graph(self.xTo2a3)
        xto2a12 = self.get_graph(self.xTo2a12)
        xto2a13 = self.get_graph(self.xTo2a13)
        nxto2a = self.get_graph(self.nxTo2a)

        self.play(ShowCreation(xto2), Write(temp))
        self.wait(1)
        self.play(Transform(temp,a1),Transform(xto2,xto2a1))
        self.wait(1)
        self.play(Transform(temp, a2), Transform(xto2, xto2a2))
        self.wait(1)
        self.play(Transform(temp, a3), Transform(xto2, xto2a3))
        self.wait(1)
        self.play(Transform(temp, a12), Transform(xto2, xto2a12))
        self.wait(1)
        self.play(Transform(temp, a13), Transform(xto2, xto2a13))

        aB1 = TexMobject('a \geqslant 1')
        aB1.scale(1.5)
        aS1 = TexMobject('0 \leqslant a \leqslant 1')
        aS1.scale(1.5)

        aB1.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT, LEFT)
        aS1.shift(UP, UP, LEFT, LEFT, LEFT, LEFT, LEFT,LEFT)
        aS1.align_to(temp,LEFT)
        aB1.align_to(temp, LEFT)

        self.wait(1)
        self.play(Transform(temp,aB1))
        arrowLeft.shift(UP,UP,RIGHT)
        arrowRight.shift(UP,UP,LEFT)
        self.play(ShowCreation(arrowRight),ShowCreation(arrowLeft))

        self.play(FadeOut(arrowLeft), FadeOut(arrowRight))

        self.play(Transform(temp,aS1))
        arrowLeft.shift(LEFT,LEFT,LEFT,LEFT)
        arrowRight.shift(RIGHT,RIGHT,RIGHT,RIGHT)
        self.play(ShowCreation(arrowRight),ShowCreation(arrowLeft))
        self.wait(1)
        self.play(FadeOut(arrowRight), FadeOut(arrowLeft))

        aS0 = TexMobject('a < 0')
        aS0.shift(UP, UP)
        aS0.align_to(aB1, RIGHT)
        aS0.scale(1.5)

        self.play(Transform(temp,aS0),Transform(xto2,nxto2a))

        isNegative = TextMobject("a is negative")
        reverse = TextMobject("This makes the function")
        reverse1 = TextMobject("reverse about the x axis")
        reverse.bg = SurroundingRectangle(reverse,color=BLACK,fill_color=BLACK, fill_opacity=1)
        isNegative.shift(UP, UP)
        reverse.bg.shift(UP, UP)
        reverse1.shift(UP, UP)

        formula1.bg = SurroundingRectangle(formula1,color=BLACK,fill_color=BLACK,fill_opacity=1)
        formula1.bg.shift(UP,UP)

        self.play(FadeIn(reverse.bg),Write(isNegative))
        reverse.shift(UP, UP)
        self.wait(0.6)
        self.play(Transform(isNegative,reverse))
        self.wait(0.6)
        self.play(Transform(isNegative, reverse1))
        self.wait(1)
        formula1.shift(UP,UP)
        self.play(FadeOut(reverse.bg),FadeOut(formulaNbc),FadeOut(isNegative))

        temp.bg=SurroundingRectangle(temp,color=BLACK,fill_color=BLACK,fill_opacity=1)
        temp.bg.shift(UP,UP)
        self.wait(1)

        self.play(FadeOut(self.axes),FadeOut(temp.bg),FadeOut(temp),FadeOut(xto2))


class fa(Scene):
    def construct(self):
        a = TextMobject('Function Addition').scale(2)
        self.play(Write(a))
        self.wait(0.5)
        self.play(FadeOut(a))

class adding(GraphScene):

    val = [3,2.75,2.5,2.25,2,1.75,1.5,1.25,1,0.75,0.5,0.25,-0.25,-0.5,-0.75,-1,-1.25,-1.5,-1.75,-2.25,-2.5,-2.75,-3]

    def lineDr(self,x):
        return self.xSquared(x)+self.twoX(x)

    CONFIG = {
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -6,
        "y_max" : 6,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
        "y_labeled_nums": range(-6, 8, 2),
    }


    def construct(self):

        form = TextMobject('To tackle bx, we must first understand')
        form1 = TextMobject(' what it means to add functions')
        form.bg = SurroundingRectangle(form,color=BLACK,fill_color=BLACK,fill_opacity=1)
        form1.bg = SurroundingRectangle(form1, color=BLACK, fill_color=BLACK, fill_opacity=1)
        form.bg.shift(UP)
        form.shift(UP,UP)

        form_group = VGroup(form,form1)
        form.bg_group = VGroup(form.bg,form1.bg)
        form_bg_group=VGroup(form.bg_group,form_group)
        self.play(Write(form_bg_group))
        self.wait(2)
        self.play(FadeOut(form_bg_group))

        self.setup_axes(animate=True)

        twoX = self.get_graph(self.twoX)
        labTwoX =  self.get_graph_label(twoX,label = 'g_{(x)}=2x')

        xSquared = self.get_graph(self.xSquared)
        labXSquared = self.get_graph_label(xSquared,label = 'f_{(x)}=x^2', x_val=-6,direction=DOWN/2)

        self.play(Write(twoX), Write(xSquared),Write(labTwoX),Write(labXSquared))



        vert_line2x = self.get_vertical_line_to_graph(-2, twoX, color=BLUE)
        vert_lineXsquared = self.get_vertical_line_to_graph(-2, xSquared, color=GREEN)

        xe2 = TextMobject("Let's say x=-2")
        xe2.shift(UP,UP,LEFT,LEFT,LEFT/1.5)
        xe2.bg = SurroundingRectangle(xe2,color=BLACK,fill_color=BLACK,fill_opacity=1)

        tm = TextMobject('This means that the sum of the functions at x=-2 is')
        tm.scale(0.5)
        tm.shift(UP,UP,LEFT,LEFT,LEFT/1.5,UP/1.5,LEFT*1.5)
        ff = TexMobject('f_{(-2)}+g_{(-2)}=h+v')
        ff.shift(UP,UP/2,LEFT,LEFT,LEFT/1.5,UP/1.5,LEFT*1.5)
        ff.scale(0.5)

        f1 = TexMobject('2\\cdot-2+(-2)^2=h+v')
        f1.shift(UP,LEFT,LEFT,LEFT/1.5,UP/1.5,LEFT*1.5)
        f1.scale(0.5)

        f2 = TexMobject('-4+4=h+v')
        f2.shift(UP/2, LEFT, LEFT, LEFT / 1.5, UP / 1.5, LEFT*1.5)
        f2.scale(0.5)

        f3 = TexMobject('0=h+v')
        f3.shift(LEFT, LEFT, LEFT / 1.5, UP / 1.5, LEFT*1.5)
        f3.scale(0.5)

        label = TexMobject('h')
        label.color
        label1 = TexMobject('v')

        label.shift(LEFT*1.25,UP)
        label1.shift(LEFT*1.25,DOWN)

        self.play(Write(xe2.bg), Write(xe2))
        self.wait(1)
        self.play(Transform(xe2,tm))
        self.wait(2)
        self.play(ShowCreation(vert_line2x), ShowCreation(vert_lineXsquared), Write(label), Write(label1))
        self.wait(1)
        self.play(Write(ff))
        self.wait(1)
        self.play(Transform(ff,f1))
        self.wait(1)
        self.play(Transform(ff, f2))
        self.wait(1)
        self.play(Transform(ff, f3))

        circle = Circle(color=YELLOW,color_fll=YELLOW)
        circle.scale(0.03)
        circle.shift(LEFT/5*4.5)

        self.play(Transform(self.get_vertical_line_to_graph(-2, twoX, color=BLUE),circle),Transform(self.get_vertical_line_to_graph(-2, xSquared, color=GREEN),circle))

        self.play(FadeOut(ff))
        self.wait(1)

        dt = TextMobject('Doing this fo every x')
        dt1 = TextMobject('gives you the sum of the functions')

        dt.scale(0.75)
        dt1.scale(0.75)

        dt.shift(LEFT*2,LEFT*2,UP)
        dt1.shift(LEFT*2, LEFT*2, UP)

        self.play(Write(dt))
        self.wait(0.5)
        self.play(Transform(dt,dt1),FadeOut(label))
        self.wait(0.5)
        self.play(FadeOut(label1))

        self.play(FadeOut(dt),FadeOut(xe2),FadeOut(dt1))


        self.play(Write(self.get_vertical_line_to_graph(-3, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-2.75, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-2.5, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-2.25, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-1.75, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-1.5, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-1.25, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-1, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-0.75, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-0.5, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(-0.25, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(0.25, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(0.5, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(0.75, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(1, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(1.25, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(1.5, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(1.75, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(2, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(2.25, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(2.5, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(2.75, twoX, color=BLUE)),
                  Write(self.get_vertical_line_to_graph(3, twoX, color=BLUE)))

        self.wait(1)

        self.play(Write(self.get_vertical_line_to_graph(-3, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-2.75, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-2.5, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-2.25, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-2, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-1.75, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-1.5, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-1.25, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-1, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-0.75, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-0.5, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(-0.25, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(0.25, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(0.5, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(0.75, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(1, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(1.25, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(1.5, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(1.75, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(2, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(2.25, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(2.5, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(2.75, xSquared, color=GREEN)),
                  Write(self.get_vertical_line_to_graph(3, xSquared, color=GREEN)))

     #   for i in range(0, len(self.val)):
     #       a = self.val[i]
     #       vertLine = self.get_vertical_line_to_graph(a,xSquared, color=GREEN)
     #       self.play(ShowCreation(vertLine))

        self.wait(1)

        twoXxSquared = self.get_graph(self.twoXxSquared,color=YELLOW)

        self.play(Transform(self.get_vertical_line_to_graph(-3, twoX, color=BLUE),self.get_vertical_line_to_graph(-3, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-2.75, twoX, color=BLUE),self.get_vertical_line_to_graph(-2.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-2.5, twoX, color=BLUE),self.get_vertical_line_to_graph(-2.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-2.25, twoX, color=BLUE),self.get_vertical_line_to_graph(-2.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1.75, twoX, color=BLUE),self.get_vertical_line_to_graph(-1.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1.5, twoX, color=BLUE),self.get_vertical_line_to_graph(-1.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1.25, twoX, color=BLUE),self.get_vertical_line_to_graph(-1.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1, twoX, color=BLUE),self.get_vertical_line_to_graph(-1, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-0.75, twoX, color=BLUE),self.get_vertical_line_to_graph(-0.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-0.5, twoX, color=BLUE),self.get_vertical_line_to_graph(-0.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-0.25, twoX, color=BLUE),self.get_vertical_line_to_graph(-0.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(0.25, twoX, color=BLUE),self.get_vertical_line_to_graph(0.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(0.5, twoX, color=BLUE),self.get_vertical_line_to_graph(0.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(0.75, twoX, color=BLUE),self.get_vertical_line_to_graph(0.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1, twoX, color=BLUE),self.get_vertical_line_to_graph(1, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1.25, twoX, color=BLUE),self.get_vertical_line_to_graph(1.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1.5, twoX, color=BLUE),self.get_vertical_line_to_graph(1.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1.75, twoX, color=BLUE),self.get_vertical_line_to_graph(1.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2, twoX, color=BLUE),self.get_vertical_line_to_graph(2, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2, twoX, color=BLUE),self.get_vertical_line_to_graph(2.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2.5, twoX, color=BLUE),self.get_vertical_line_to_graph(2.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2.75, twoX, color=BLUE),self.get_vertical_line_to_graph(2.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(3, twoX, color=BLUE),self.get_vertical_line_to_graph(3, twoXxSquared, color=YELLOW)),


                  Transform(self.get_vertical_line_to_graph(-3, xSquared, color=GREEN),self.get_vertical_line_to_graph(-3, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-2.75, xSquared, color=GREEN),self.get_vertical_line_to_graph(-2.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-2.5, xSquared, color=GREEN),self.get_vertical_line_to_graph(-2.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-2.25, xSquared, color=GREEN),self.get_vertical_line_to_graph(-2.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1.75, xSquared, color=GREEN),self.get_vertical_line_to_graph(-1.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1.5, xSquared, color=GREEN),self.get_vertical_line_to_graph(-1.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1.25, xSquared, color=GREEN),self.get_vertical_line_to_graph(-1.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-1, xSquared, color=GREEN),self.get_vertical_line_to_graph(-1, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-0.75, xSquared, color=GREEN),self.get_vertical_line_to_graph(-0.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-0.5, xSquared, color=GREEN),self.get_vertical_line_to_graph(-0.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(-0.25, xSquared, color=GREEN),self.get_vertical_line_to_graph(-0.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(0.25, xSquared, color=GREEN),self.get_vertical_line_to_graph(0.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(0.5, xSquared, color=GREEN),self.get_vertical_line_to_graph(0.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(0.75, xSquared, color=GREEN),self.get_vertical_line_to_graph(0.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1, xSquared, color=GREEN),self.get_vertical_line_to_graph(1, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1.25, xSquared, color=GREEN),self.get_vertical_line_to_graph(1.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1.5, xSquared, color=GREEN),self.get_vertical_line_to_graph(1.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(1.75, xSquared, color=GREEN),self.get_vertical_line_to_graph(1.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2, xSquared, color=GREEN),self.get_vertical_line_to_graph(2, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2, xSquared, color=GREEN),self.get_vertical_line_to_graph(2.25, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2.5, xSquared, color=GREEN),self.get_vertical_line_to_graph(2.5, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(2.75, xSquared, color=GREEN),self.get_vertical_line_to_graph(2.75, twoXxSquared, color=YELLOW)),
                  Transform(self.get_vertical_line_to_graph(3, xSquared, color=GREEN),self.get_vertical_line_to_graph(3, twoXxSquared, color=YELLOW)))




        self.wait(1)

        self.play(ShowCreation(twoXxSquared))

        self.wait(2)

        self.clear()

        self.setup_axes(animate=False)

        self.play(Write(labTwoX),ShowCreation(twoX),Write(labXSquared),ShowCreation(xSquared))

        blf = TextMobject('Because a linear function is negative before 0 and positive after')
        blf.bg = SurroundingRectangle(blf,color=BLACK,color_fill=BLACK,fill_opacity=1)
        blf_group=VGroup(blf.bg,blf)

        blf_group.shift(UP)
        self.play(Write(blf_group))
        self.wait(2)
        self.play(FadeOut(blf_group))

        rectangle = Rectangle(fill_color=RED, fill_opacity=0.5, color=RED, color_opcaity=0.25)
        rectangle.scale(5)
        rectangle.rotate(np.pi/2)
        rectangle.shift(LEFT,LEFT,LEFT,LEFT,LEFT)

        rectangle1 = Rectangle(fill_color=BLUE, fill_opacity=0.5, color=BLUE, color_opcaity=0.25)
        rectangle1.scale(5)
        rectangle1.rotate(np.pi*1.5)
        rectangle1.shift(RIGHT,RIGHT,RIGHT,RIGHT,RIGHT)

        rectangleLab=TexMobject('-')
        rectangleLab.shift(LEFT,LEFT,LEFT/2)
        rectangleLab.scale(4)
        self.play( Write(rectangleLab),Write(rectangle))

        rectangleLab1=TexMobject('+')
        rectangleLab1.shift(RIGHT,RIGHT,RIGHT/2)
        rectangleLab1.scale(4)
        self.play(Write(rectangleLab1),Write(rectangle1))

        self.wait(0.5)

        self.play(FadeOut(rectangleLab),FadeOut(rectangle),FadeOut(rectangle1),FadeOut(rectangleLab1))

        blf1 = TextMobject('it "pulls" the function down before x=0')
        blf1.bg = SurroundingRectangle(blf1,color=BLACK,color_fill=BLACK,fill_opacity=1)
        blf1_group = VGroup(blf1.bg,blf1)

        blf12 = TextMobject('and "pushs" it up after x=0')
        blf12.bg = SurroundingRectangle(blf12,color=BLACK,color_fill=BLACK,fill_opacity=1)
        blf12_group = VGroup(blf12.bg, blf12)

        self.play(Write(blf1_group))
        self.wait(1)
        self.play(Transform(blf1_group,blf12_group))
        self.wait(1.5)
        self.play(FadeOut(blf1_group))

        arrow12=Arrow()
        arrow22=Arrow()
        arrow32=Arrow()
        arrow42=Arrow()
        arrow52=Arrow()
        arrow62=Arrow()
        arrow72=Arrow()
        arrow82=Arrow()

        arrow12.shift(LEFT/10*9*1.5/4,UP/4*3/1.77777777778/1.77777777778,DOWN*0.3,DOWN/2)
        arrow22.shift(LEFT/10*9*1.5/4*2,UP/4*3/0.666666666667,DOWN*0.4,DOWN/2)
        arrow32.shift(LEFT/10*9*1.5/4*3,UP/4*3/0.296296296296,DOWN*0.4,DOWN/2)
        arrow42.shift(LEFT/10*9*1.5,UP/4*3/0.166666666667,DOWN*0.4,DOWN/2)
        arrow52.shift(RIGHT/10*9*1.5/4,UP/4*3/1.77777777778/1.77777777778,UP*0.4,UP/2)
        arrow62.shift(RIGHT/10*9*1.5/4*2,UP/4*3/0.666666666667,UP*0.4,UP/2)
        arrow72.shift(RIGHT/10*9*1.5/4*3,UP/4*3/0.296296296296,UP*0.4,UP/2)
        arrow82.shift(RIGHT/10*9*1.5,UP/4*3/0.166666666667,UP*0.4,UP/2)

        arrow12.rotate(-np.pi/2)
        arrow22.rotate(-np.pi/2)
        arrow32.rotate(-np.pi/2)
        arrow42.rotate(-np.pi/2)
        arrow52.rotate(-np.pi*1.5)
        arrow62.rotate(-np.pi*1.5)
        arrow72.rotate(-np.pi*1.5)
        arrow82.rotate(-np.pi*1.5)





        arrow1 = Arrow()
        arrow2 = Arrow()
        arrow3 = Arrow()
        arrow4 = Arrow()
        arrow5 = Arrow()
        arrow6 = Arrow()
        arrow7 = Arrow()
        arrow8 = Arrow()

        arrow1.shift(LEFT / 10 * 9 * 1.5 / 4, UP / 4 * 3 / 1.77777777778 / 1.77777777778, DOWN * 0.3)
        arrow2.shift(LEFT / 10 * 9 * 1.5 / 4 * 2, UP / 4 * 3 / 0.666666666667, DOWN * 0.4)
        arrow3.shift(LEFT / 10 * 9 * 1.5 / 4 * 3, UP / 4 * 3 / 0.296296296296, DOWN * 0.4)
        arrow4.shift(LEFT / 10 * 9 * 1.5, UP / 4 * 3 / 0.166666666667, DOWN * 0.4)
        arrow5.shift(RIGHT / 10 * 9 * 1.5 / 4, UP / 4 * 3 / 1.77777777778 / 1.77777777778, UP * 0.4)
        arrow6.shift(RIGHT / 10 * 9 * 1.5 / 4 * 2, UP / 4 * 3 / 0.666666666667, UP * 0.4)
        arrow7.shift(RIGHT / 10 * 9 * 1.5 / 4 * 3, UP / 4 * 3 / 0.296296296296, UP * 0.4)
        arrow8.shift(RIGHT / 10 * 9 * 1.5, UP / 4 * 3 / 0.166666666667, UP * 0.4)

        arrow1.rotate(-np.pi / 2)
        arrow2.rotate(-np.pi / 2)
        arrow3.rotate(-np.pi / 2)
        arrow4.rotate(-np.pi / 2)
        arrow5.rotate(-np.pi * 1.5)
        arrow6.rotate(-np.pi * 1.5)
        arrow7.rotate(-np.pi * 1.5)
        arrow8.rotate(-np.pi * 1.5)

        arrow1.scale(0.4)
        arrow2.scale(0.4)
        arrow3.scale(0.4)
        arrow4.scale(0.4)
        arrow5.scale(0.4)
        arrow6.scale(0.4)
        arrow7.scale(0.4)
        arrow8.scale(0.4)





        arrow13 = Arrow()
        arrow23 = Arrow()
        arrow33 = Arrow()
        arrow43 = Arrow()
        arrow53 = Arrow()
        arrow63 = Arrow()
        arrow73 = Arrow()
        arrow83 = Arrow()

        arrow13.shift(LEFT / 10 * 9 * 1.5 / 4, UP / 4 * 3 / 1.77777777778 / 1.77777777778, DOWN * 0.2)
        arrow23.shift(LEFT / 10 * 9 * 1.5 / 4 * 2, UP / 4 * 3 / 0.666666666667, DOWN * 0.2)
        arrow33.shift(LEFT / 10 * 9 * 1.5 / 4 * 3, UP / 4 * 3 / 0.296296296296, DOWN * 0.2)
        arrow43.shift(LEFT / 10 * 9 * 1.5, UP / 4 * 3 / 0.166666666667, DOWN * 0.2)
        arrow53.shift(RIGHT / 10 * 9 * 1.5 / 4, UP / 4 * 3 / 1.77777777778 / 1.77777777778, UP * 0.2)
        arrow63.shift(RIGHT / 10 * 9 * 1.5 / 4 * 2, UP / 4 * 3 / 0.666666666667, UP * 0.2)
        arrow73.shift(RIGHT / 10 * 9 * 1.5 / 4 * 3, UP / 4 * 3 / 0.296296296296, UP * 0.2)
        arrow83.shift(RIGHT / 10 * 9 * 1.5, UP / 4 * 3 / 0.166666666667, UP * 0.2)

        arrow13.rotate(-np.pi / 2)
        arrow23.rotate(-np.pi / 2)
        arrow33.rotate(-np.pi / 2)
        arrow43.rotate(-np.pi / 2)
        arrow53.rotate(-np.pi * 1.5)
        arrow63.rotate(-np.pi * 1.5)
        arrow73.rotate(-np.pi * 1.5)
        arrow83.rotate(-np.pi * 1.5)

        arrow13.scale(0.2)
        arrow23.scale(0.2)
        arrow33.scale(0.2)
        arrow43.scale(0.2)
        arrow53.scale(0.2)
        arrow63.scale(0.2)
        arrow73.scale(0.2)
        arrow83.scale(0.2)

        self.play(Write(arrow1),Write(arrow5))
        self.play(Write(arrow2),Write(arrow6))
        self.play(Write(arrow3),Write(arrow7))
        self.play(Write(arrow4),Write(arrow8))

        slope1 = self.get_graph(self.slope1)
        slope2 = self.get_graph(self.slope2,color=BLUE)
        slope3 = self.get_graph(self.slope3,color=BLUE)

        sum1 = self.get_graph(self.sum1)
        sum2 = self.get_graph(self.sum2)
        sum3 = self.get_graph(self.sum3)

        self.play(ShowCreation(sum1))

        self.play(Transform(sum1,sum2),Transform(twoX, slope2), Transform(arrow1, arrow12), Transform(arrow2, arrow22),
                  Transform(arrow3, arrow32), Transform(arrow4, arrow42), Transform(arrow5, arrow52),
                  Transform(arrow6, arrow62), Transform(arrow7, arrow72), Transform(arrow8, arrow82))

        self.wait(1)

        self.play(Transform(sum1,sum3),Transform(twoX, slope3), Transform(arrow1, arrow13), Transform(arrow2, arrow23),
                  Transform(arrow3, arrow33), Transform(arrow4, arrow43), Transform(arrow5, arrow53),
                  Transform(arrow6, arrow63), Transform(arrow7, arrow73), Transform(arrow8, arrow83))

        self.wait(1)

        self.clear()

        blf2 = TextMobject('The steeper the slope is in the linear function')
        blf21 = TextMobject(' the more it pulls and pushes the function')

        self.wait(1)
        self.play(Write(blf2))
        self.wait(1)
        self.play(Transform(blf2,blf21))
        self.wait(1)
        self.play(FadeOut(blf2))

        self.wait(1)




    def twoX(self,x):
        return 2 * x

    def xSquared(self, x):
        return x ** 2

    def temp(self):
        self.twoX()

    def twoXxSquared(self,x):
        return x * 2 + x ** 2







    def slope1(self,x):
        return x

    def slope2(self,x):
        return 3*x

    def slope3(self,x):
        return 0.5*x

    def sum1(self,x):
        return x**2+2*x

    def sum2(self,x):
        return x**2+x*3

    def sum3(self,x):
        return x**2+x*0.5


class b(Scene):
    def construct(self):
        a = TextMobject('bx').scale(3)
        self.play(Write(a))
        self.wait(0.5)
        self.play(FadeOut(a))

class bx(GraphScene):

    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
        "y_labeled_nums": range(-6, 8, 2),
    }

    def construct(self):
        Ym = TextMobject('You might be wondering what does this has to do with bx')
        Ym1 = TextMobject('Well....')
        Ym2 = TextMobject('Let me dump some visual aids on you')
        Ym31 = TexMobject('y=2x')
        Ym32 = TexMobject('y=3x^2')
        Ym41 = TexMobject('y=bx')
        Ym42 = TexMobject('y=ax^2')
        Ym5 = TexMobject('ax^2+bx')
        Ym6 = TexMobject('ax^2+bx+c')

        Ym7 = TextMobject('Basically, the "bx" refers to a linear function with a b=0')
        Ym8 = TextMobject('that "pulls" and "pushes" the parabula')
        Ym8.shift(DOWN/3*2)

        self.play(Write(Ym))
        self.wait(1)
        self.play(Transform(Ym,Ym1))
        self.wait(1)
        self.play(FadeOut(Ym))
        self.wait(0.5)

        Ym31.shift(RIGHT*2,UP,UP/2)
        Ym32.shift(LEFT*2,UP,UP/2)

        Ym41.shift(RIGHT*2)
        Ym42.shift(LEFT*2)

        Ym5.shift(UP/2)

        self.play(Write(Ym31), Write(Ym32))
        self.wait(2)
        self.play(Transform(Ym31, Ym41), Transform(Ym32, Ym42))
        self.wait(2)
        self.play(Transform(Ym31, Ym5), Transform(Ym32, Ym5))
        self.wait(2)
        self.play(Transform(Ym31, Ym6), Transform(Ym32, Ym6))
        self.wait(2)
        self.play(FadeOut(Ym31),FadeOut(Ym32), Write(Ym7))
        self.wait(2)
        self.play(Write(Ym8))

        self.wait(1)

        self.play(FadeOut(Ym8),FadeOut(Ym7))

        self.setup_axes(animate=True)

        xx1x = self.get_graph(self.xx1xf,color=BLUE)
        xx2x = self.get_graph(self.xx2xf, color=BLUE)
        xx3x = self.get_graph(self.xx3xf, color=BLUE)
        xxhx = self.get_graph(self.xxhxf, color=BLUE)
        xxtx = self.get_graph(self.xxtxf, color=BLUE)
        xxnx = self.get_graph(self.xxnxf, color=BLUE)

        xx1xLab = TexMobject('x^2+x')
        xx2xLab = TexMobject('x^2+2x')
        xx3xLab = TexMobject('x^2+3x')
        xxhxLab = TexMobject('x^2+(-x)')
        xxtxLab = TexMobject('x^2+(-2x)')
        xxnxLab = TexMobject('x^2+(-3x)')

        xx1xLab.bg = SurroundingRectangle(xx1xLab,color=BLACK,color_fill=BLACK,fill_opacity=1)
        xx2xLab.bg = SurroundingRectangle(xx2xLab,color=BLACK,color_fill=BLACK,fill_opacity=1)
        xx3xLab.bg = SurroundingRectangle(xx3xLab,color=BLACK,color_fill=BLACK,fill_opacity=1)
        xxhxLab.bg = SurroundingRectangle(xxhxLab,color=BLACK,color_fill=BLACK,fill_opacity=1)
        xxtxLab.bg = SurroundingRectangle(xxtxLab,color=BLACK,color_fill=BLACK,fill_opacity=1)
        xxnxLab.bg = SurroundingRectangle(xxnxLab,color=BLACK,color_fill=BLACK,fill_opacity=1)

        xx1xLab.bg.shift(UP,UP, UP)
        xx2xLab.bg.shift(UP,UP, UP)
        xx3xLab.bg.shift(UP,UP, UP)
        xxhxLab.bg.shift(UP,UP, UP)
        xxtxLab.bg.shift(UP,UP, UP)
        xxnxLab.bg.shift(UP,UP, UP)

        xx1xLab.shift(UP,UP, UP)
        xx2xLab.shift(UP, UP, UP)
        xx3xLab.shift(UP, UP, UP)
        xxhxLab.shift(UP, UP, UP)
        xxtxLab.shift(UP, UP, UP)
        xxnxLab.shift(UP, UP, UP)

        xx1xGroup = VGroup(xx1xLab.bg,xx1x,xx1xLab)
        xx2xGroup = VGroup(xx2xLab.bg,xx2x,xx2xLab)
        xx3xGroup = VGroup(xx3xLab.bg,xx3x,xx3xLab)
        xxhxGroup = VGroup(xxhxLab.bg,xxhx,xxhxLab)
        xxtxGroup = VGroup(xxtxLab.bg,xxtx,xxtxLab)
        xxnxGroup = VGroup(xxnxLab.bg,xxnx,xxnxLab)

        xx1xGroup.shift(DOWN / 2)
        xx2xGroup.shift(DOWN / 2)
        xx3xGroup.shift(DOWN / 2)
        xxhxGroup.shift(DOWN / 2)
        xxtxGroup.shift(DOWN / 2)
        xxnxGroup.shift(DOWN / 2)


        self.play(Write(xx1xGroup))
        self.wait(1)
        self.play(Transform(xx1xGroup,xx2xGroup))
        self.wait(1)
        self.play(Transform(xx1xGroup, xx3xGroup))
        self.wait(1)
        self.play(Transform(xx1xGroup, xxhxGroup))
        self.wait(1)
        self.play(Transform(xx1xGroup, xxtxGroup))
        self.wait(1)
        self.play(Transform(xx1xGroup, xxnxGroup))
        self.wait(1)



        self.play(FadeOut(self.axes),FadeOut(xx1xGroup))

    def xx1xf(self, x):
        return x ** 2 + 1 * x + 1

    def xx2xf(self, x):
        return x ** 2 + 2 * x + 1

    def xx3xf(self, x):
        return x ** 2 + 3 * x + 1

    def xxhxf(self, x):
        return x ** 2 + -1 * x + 1

    def xxtxf(self, x):
        return x ** 2 + -2 * x + 1

    def xxnxf(self, x):
        return x ** 2 + -3 * x + 1

class c1(Scene):
    def construct(self):
        a = TextMobject('c').scale(3)
        self.play(Write(a))
        self.wait(0.5)
        self.play(FadeOut(a))

class c(GraphScene):

    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
        "y_labeled_nums": range(-6, 8, 2),
    }

    def construct(self):

        self.setup_axes(animate=True)

        xSquared = self.get_graph(self.xSquared,color=BLUE)
        xSquaredLab = TexMobject('x^2+0x')
        xSquaredLab.shift(UP, UP,LEFT,LEFT*2)
        xSquared.bg = SurroundingRectangle(xSquaredLab,color=BLACK,color_fill=BLACK,fill_opacity=1)
        xSquaredGroup = VGroup(xSquared.bg,xSquaredLab,xSquared)

        xSquaredp3 = self.get_graph(self.xSquaredp3, color=BLUE)
        xSquaredp3Lab = TexMobject('x^2+0x+3')
        xSquaredp3Lab.shift(UP, UP,LEFT,LEFT*2)
        xSquaredp3.bg = SurroundingRectangle(xSquaredp3Lab, color=BLACK, color_fill=BLACK,fill_opacity=1)
        xSquaredp3Group = VGroup(xSquaredp3.bg, xSquaredp3Lab, xSquaredp3)

        xSquaredp5 = self.get_graph(self.xSquaredp5, color=BLUE)
        xSquaredp5Lab = TexMobject('x^2+0x+5')
        xSquaredp5Lab.shift(UP, UP,LEFT,LEFT*2)
        xSquaredp5.bg = SurroundingRectangle(xSquaredp5Lab, color=BLACK, color_fill=BLACK,fill_opacity=1)
        xSquaredp5Group = VGroup(xSquaredp5.bg, xSquaredp5Lab, xSquaredp5)

        xSquaredm2 = self.get_graph(self.xSquaredm2, color=BLUE)
        xSquaredm2Lab = TexMobject('x^2+0x-2')
        xSquaredm2Lab.shift(UP, UP,LEFT,LEFT*2)
        xSquaredm2.bg = SurroundingRectangle(xSquaredm2Lab, color=BLACK, color_fill=BLACK,fill_opacity=1)
        xSquaredm2Group = VGroup(xSquaredm2.bg, xSquaredm2Lab, xSquaredm2)

        xSquaredm4 = self.get_graph(self.xSquaredm4, color=BLUE)
        xSquaredm4Lab = TexMobject('x^2+0x-4')
        xSquaredm4Lab.shift(UP, UP,LEFT,LEFT*2)
        xSquaredm4.bg = SurroundingRectangle(xSquaredm4Lab, color=BLACK, color_fill=BLACK,fill_opacity=1)
        xSquaredm4Group = VGroup(xSquaredm4.bg, xSquaredm4Lab, xSquaredm4)

        self.play(Write(xSquaredGroup))
        self.wait(1)
        self.play(Transform(xSquaredGroup,xSquaredp3Group))
        self.wait(1)
        self.play(Transform(xSquaredGroup, xSquaredp5Group))
        self.wait(1)
        self.play(Transform(xSquaredGroup, xSquaredm2Group))
        self.wait(1)
        self.play(Transform(xSquaredGroup, xSquaredm4Group))
        self.wait(1)

        Ay = TextMobject('As you might have guessed')
        Ay.bg=SurroundingRectangle(Ay, color=BLACK, color_fill=BLACK,fill_opacity=1)
        Ay1 = TextMobject('changing c moves the function up and down')
        Ay1.bg = SurroundingRectangle(Ay1, color=BLACK, color_fill=BLACK, fill_opacity=1)
        self.play(Write(Ay.bg),Write(Ay))
        self.wait(1)
        self.play(Transform(Ay.bg,Ay1.bg),Transform(Ay,Ay1))
        self.wait(1)
        self.play(FadeOut(Ay),FadeOut(Ay.bg))
        self.play(Transform(xSquaredGroup,xSquaredp5Group))
        self.play(Transform(xSquaredGroup, xSquaredm4Group))
        self.wait(1)
        self.play(FadeOut(self.axes),FadeOut(xSquared))
    def xSquared(self,x):
        return x**2

    def xSquaredp3(self,x):
        return x**2+3

    def xSquaredp5(self,x):
        return x**2+5

    def xSquaredm2(self,x):
        return x**2-2

    def xSquaredm4(self,x):
        return x**2-4

class toSum(GraphScene):

    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
        "y_labeled_nums": range(-6, 8, 2),
    }

    def construct(self):
        Ts = TextMobject('To sum up')
        a = TextMobject('a widens and narrows the function')
        b = TextMobject('b pulls and pushes the')
        b1 = TextMobject(' function up and down')
        c = TextMobject('c moves the function up and down')

        a.scale(0.6)
        b.scale(0.6)
        b1.scale(0.6)
        c.scale(0.6)

        self.play(Write(Ts))
        self.wait(1)
        self.play(FadeOut(Ts))
        self.setup_axes(animate=True)
        self.wait(1)
        a.shift(UP*2,LEFT*4.5)
        b.shift(UP*2,LEFT*4.5)
        b1.shift(UP*1.5,LEFT*4.5)
        c.shift(UP*1.5,LEFT*4.2)

        xSquared = self.get_graph(self.xSquared)
        xSquared1 = self.get_graph(self.xSquared)
        xx5x = self.get_graph(self.xx5x)
        xfx = self.get_graph(self.xfx)
        x5xx = self.get_graph(self.x5xx)
        xxp5 = self.get_graph(self.xxp5)
        xxn4 = self.get_graph(self.xxn4)
        xn5x = self.get_graph(self.xn5x)
        self.play(Write(a),Write(xSquared),run_time=4)
        self.play(Transform(xSquared,xx5x))
        self.play(Transform(xSquared, xfx))
        self.play(Transform(xSquared, xSquared1))
        self.wait(0.5)
        self.play(Transform(xSquared,x5xx),Transform(a,b),Write(b1))
        self.play(Transform(xSquared, xn5x))
        self.play(Transform(xSquared, xSquared1))
        self.wait(0.5)
        self.play(Transform(a,c),FadeOut(b1))
        self.play(Transform(xSquared,xxp5))
        self.play(Transform(xSquared,xxn4))
        self.wait(1)
        fin = TexMobject('fin').scale(2)
        self.play(FadeOut(xSquared),Transform(a,fin),FadeOut(self.axes))
        self.wait(1)
        self.play(FadeOut(a))
        self.wait(0.5)

    def xSquared(self,x):
        return x**2

    def xx5x(self,x):
        return 5*x**2

    def xfx(self,x):
        return (1/5)*x**2


    def x5xx(self,x):
        return x**2+x*4

    def xn5x(self,x):
        return x**2+x*-4

    def xxp5(self,x):
        return x**2+5

    def xxn4(self,x):
        return x**2-4

class outro(Scene):
    def construct(self):
        a = TextMobject('Thank You For Watching').scale(2)
        b = TextMobject('This video was created using the Manim Python library').shift(UP*0.5)
        c = TextMobject('that was created by Grant Sanderson of 3b1b').shift(DOWN*0.5)
        self.play(Write(b))
        self.wait(0.5)
        self.play(Write(c))
        self.wait(0.5)
        self.play(Transform(b,a),Transform(c,a),run_time=2)
        self.wait(0.5)
