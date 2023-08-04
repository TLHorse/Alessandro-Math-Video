from manimlib import *
from math import sqrt

def tx_eq(s, col=BLACK):
    ret = Tex(s, color=col)
    ret.scale(0.85)
    return ret

def t(text, font='LXGW WenKai', size=15, color=BLACK):
    return Text(text=text, font=font, size=size, color=color)

def para_align(mob, to):
    mob.next_to(to, DOWN)
    mob.align_to(to, LEFT)

def middle_point(A, B):
    # coordA = A.get_center()
    # coordB = B.get_center()
    return [(A[0]+B[0])/2, (A[1]+B[1])/2, 0]

def method1(self):
    ttl = t('1. 相邻相交法', size=18)
    ttl.move_to([-6, 3.2, 0], aligned_edge=UL)
    self.play(Write(ttl))
    axes = Axes(
        x_range=[0, 4.5, 1],
        y_range=[0, 4.5, 1],
        width=4.5, 
        height=4.5, 
        axis_config={
            'include_tip': True,
            'graph_origin': [-6, -3, 0]
        }
    )
    axes.set_color(BLACK)
    axes.move_to([-6-0.1, -3-0.1, 0], aligned_edge=DL)
    
    text1 = t('以正方形的左下顶点为原点，两条边\n为坐标轴，建立平面直角坐标系.')
    text1.scale(0.85)
    text1.move_to([-0.5, 2, 0], aligned_edge=UL)
    self.play(Write(axes), Write(text1))
    self.wait()
    text2 = t("设某个时刻A、B分别已经走过路程s，\n两动点又分别走过∆s的路程后，\n所在位置分别为A'、B'")
    text2.scale(0.85)
    para_align(text2, text1)
    a.target.shift(DOWN)
    b.target.shift(RIGHT)
    self.play(Write(text2), MoveToTarget(a), MoveToTarget(b))
    a_ = SmallDot(a.get_center(), color=BLACK)
    A_ = Tex("A'", color=BLACK)
    always(A_.next_to, a_, LEFT)
    b_ = SmallDot(b.get_center(), color=BLACK)
    B_ = Tex("B'", color=BLACK)
    always(B_.next_to, b_, DOWN)
    self.add(a_, b_)
    AB_ = always_redraw(Line, a_.get_center(), b_.get_center(), color=BLACK)
    a_.generate_target()
    b_.generate_target()
    a_.target.shift(DOWN/2)
    b_.target.shift(RIGHT/2)
    self.play(MoveToTarget(a_), MoveToTarget(b_))
    self.play(Write(A_), Write(B_), Write(AB_))
    br1 = BraceLabel(Line(start=a, end=a_), text="ds", brace_direction=RIGHT, color=RED_C)
    br2 = BraceLabel(Line(start=b, end=b_), text="ds", brace_direction=UP, color=RED_C)
    br3 = BraceLabel(Line(start=[-6, 1, 0], end=a), text="s", brace_direction=RIGHT, color=RED_E)
    br4 = BraceLabel(Line(start=[-6, -3, 0], end=b), text="s", brace_direction=UP, color=RED_E)
    self.play(FadeIn(br1, run_time=0.3), FadeIn(br2, run_time=0.3), FadeIn(br3, run_time=0.3), FadeIn(br4, run_time=0.3))
    self.wait(2)

    text3 = t("设AB与A'B'交与点T，易知当∆s→0时\nT的轨迹方程就是曲线的解析式.")
    text3.scale(0.85)
    para_align(text3, text2)
    tdot = SmallDot(axes.coords_to_point(3/8, 15/8), color=BLACK)
    Tdot = Tex('T', color=BLACK)
    Tdot.next_to(tdot, UR)
    self.play(Write(text3), Write(tdot), Write(Tdot))
    self.wait(3)

    # calculation
    bg = FullScreenFadeRectangle(fill_color=WHITE, fill_opacity=0.9)
    self.play(FadeIn(bg))
    tx1 = tx_eq(r"y_{AB}=\frac{s-1}{s}x+1-s,\quad y_{A'B'}=\frac{s+\Delta s-1}{s+\Delta s}x+1-(s+\Delta s)")
    tx1.scale(0.9)
    tx1.move_to([-6, 3, 0], aligned_edge=UL)
    self.play(Write(tx1))
    self.wait(2)
    tx2 = t("联立上述两式，令y相等，得")
    tx2.scale(0.9)
    para_align(tx2, tx1)
    self.play(Write(tx2))
    self.wait(2)
    tx3 = tx_eq(r"\frac{s-1}{s}x+1-s=\frac{s+\Delta s-1}{s+\Delta s}x+1-(s+\Delta s)")
    tx3.scale(0.9)
    para_align(tx3, tx2)
    self.play(Write(tx3))
    self.wait(2)
    tx4 = t("解得")
    tx4.scale(0.9)
    para_align(tx4, tx3)
    self.play(Write(tx4))
    tx5 = tx_eq(r"\left\{\begin{aligned}&x=s^2+t\Delta s \cr &y=s^2+(s-1)\Delta s-2s+1\end{aligned}\right.")
    tx5.scale(0.9)
    para_align(tx5, tx4)
    self.play(Write(tx5))
    self.wait(2)
    tx6 = t("当∆s→0，得到参数方程")
    tx6.scale(0.9)
    tx6.move_to([0,0,0], aligned_edge=LEFT)
    self.play(Write(tx6))
    tx7 = tx_eq(r"\left\{\begin{aligned}&x=s^2 \cr &y=s^2-2s+1\end{aligned}\right.")
    tx7.scale(0.9)
    para_align(tx7, tx6)
    self.play(TransformFromCopy(tx5, tx7))

    tx8 = t("即")
    tx8.move_to([-5, -2.5, 0])
    self.play(Write(tx8))
    
    res = tx_eq(r"y=x-2\sqrt{x}+1 =(\sqrt{x}-1)^2")
    res.next_to(tx8, RIGHT)
    res.shift(RIGHT)
    self.play(TransformFromCopy(tx7, res))
    rect = SurroundingRectangle(res, color=BLUE_E)
    self.play(Write(rect))

    self.wait(5)
    cover = FullScreenRectangle(fill_color=WHITE)
    self.play(FadeIn(cover))
    self.clear()

def method2(self):
    ttl = t('2. 界点判别式法', size=18)
    ttl.move_to([-6, 3.2, 0], aligned_edge=UL)
    axes = Axes(
        x_range=[0, 4.5, 1],
        y_range=[0, 4.5, 1],
        width=4.5, 
        height=4.5, 
        axis_config={
            'include_tip': True,
            'graph_origin': [-6, -3, 0]
        }
    )
    axes.set_color(BLACK)
    axes.move_to([-6-0.1, -3-0.1, 0], aligned_edge=DL)
    graph = FunctionGraph(
        function = lambda x: (sqrt(x/4)-1)**2 * 4.3-0.2, 
        x_range = [0.01, 4, 0.001],
        color=RED
    )
    graph.move_to([-6, -3, 0], aligned_edge=DL)
    self.play(Write(ttl), Write(square), Write(a), Write(A), Write(b), Write(B), Write(axes), Write(graph))
    AB1 = always_redraw(Line, a.get_center(), b.get_center(), color=BLACK)
    self.add(AB1)
    def backNforth():
        a.target.shift(DOWN*3)
        b.target.shift(RIGHT*3)
        self.play(MoveToTarget(a, run_time=2), MoveToTarget(b, run_time=2))
        a.target.shift(UP*3)
        b.target.shift(LEFT*3)
        self.play(MoveToTarget(a, run_time=0.2), MoveToTarget(b, run_time=0.2))

    text1 = t('对于正方形内的的任意一点T，\n分类讨论以下三种情况：')
    text1.scale(0.85)
    text1.move_to([-0.5, 2, 0], aligned_edge=UL)
    self.play(Write(text1))
    
    tdot = SmallDot([-5, -2.5, 0], color=BLACK)
    Tdot = Tex("T", color=BLACK)
    always(Tdot.next_to, tdot, UR)
    text2 = t('若T在曲线 下方，\n整个运动过程中AB 两次 经过T，\n关于s的方程有 两个解；')
    text2.set_color_by_text_to_color_map(text_to_color_map={
        "下方": BLUE_E,
        "两次": BLUE_E,
        "两个解": BLUE_E,
    })
    para_align(text2, text1)
    self.play(Write(tdot), Write(Tdot), Write(text2))
    backNforth()
    self.wait(2)

    text3 = t('若T在曲线 上方，\n整个运动过程中AB 不经过 T，\n关于s的方程 无解；')
    text3.set_color_by_text_to_color_map(text_to_color_map={
        "上方": BLUE_E,
        "不经过": BLUE_E,
        "无解": BLUE_E,
    })
    para_align(text3, text1)
    tdot.generate_target()
    tdot.target.move_to([-4, -1, 0])
    self.play(Transform(text2, text3), MoveToTarget(tdot))
    backNforth()
    self.wait(2)

    text4 = t('若T恰好落在在曲线 上，\n整个运动过程中AB 一次 经过T，\n关于s的方程有 唯一解；')
    text4.set_color_by_text_to_color_map(text_to_color_map={
        "上": BLUE_E,
        "一次": BLUE_E,
        "唯一解": BLUE_E,
    })
    para_align(text4, text1)
    tdot.target.move_to([-5, -2, 0])
    self.play(Transform(text2, text4), MoveToTarget(tdot))
    backNforth()
    self.wait()

    text5 = t('——唯一解正是我们想要的.')
    text5.scale(0.85)
    para_align(text5, text4)
    self.play(Write(text5))
    self.wait(3)

    # calculation
    bg = FullScreenFadeRectangle(fill_color=WHITE, fill_opacity=0.9)
    self.play(FadeIn(bg))
    tx1 = tx_eq(r"AB:y=\frac{s-1}{s}x+1-s")
    tx1.scale(0.9)
    tx1.move_to([-6, 3, 0], aligned_edge=UL)
    self.play(Write(tx1))
    self.wait()
    tx2 = t('将直线AB的方程整理为关于s的方程，有')
    tx2.scale(0.9)
    para_align(tx2, tx1)
    self.play(Write(tx2))
    tx3 = tx_eq(r"s^2+(y-x-1)s+x=0")
    tx3.scale(0.9)
    para_align(tx3, tx2)
    self.play(Write(tx3))
    self.wait(2)
    tx4 = t('观察到方程为一元二次方程，令b²-4ac=0，有')
    tx4.scale(0.9)
    para_align(tx4, tx3)
    self.play(Write(tx4))
    tx5 = tx_eq(r"(y-s-1)^2-4x=0")
    tx5.scale(0.9)
    para_align(tx5, tx4)
    self.play(Write(tx5))
    self.wait(2)
    tx6 = t('展开整理，并解出y的值，即边界曲线的解析式.')
    tx6.scale(0.9)
    para_align(tx6, tx5)
    self.play(Write(tx6))
    tx7 = tx_eq(r"y^2-2(x+1)y+(x^2-2x+1)=0")
    tx7.scale(0.9)
    para_align(tx7, tx6)
    self.play(Write(tx7))
    tx8 = tx_eq(r"y_1=(\sqrt{x}-1)^2,\quad y_2=(\sqrt{x}+1)^2>1\text{(abandon)}")
    tx8.scale(0.9)
    para_align(tx8, tx7)
    self.play(TransformFromCopy(tx7, tx8))
    rect = SurroundingRectangle(tx8, color=BLUE_E)
    self.play(Write(rect))
    self.wait(5)

    cover = FullScreenRectangle(fill_color=WHITE)
    self.play(FadeIn(cover))
    self.clear()

def method3(self):
    ttl = t('3. 偏导数法', size=18)
    ttl.move_to([-6, 3.2, 0], aligned_edge=UL)
    axes = Axes(
        x_range=[0, 4.5, 1],
        y_range=[0, 4.5, 1],
        width=4.5, 
        height=4.5, 
        axis_config={
            'include_tip': True,
            'graph_origin': [-6, -3, 0]
        }
    )
    axes.set_color(BLACK)
    axes.move_to([-6-0.1, -3-0.1, 0], aligned_edge=DL)
    graph = FunctionGraph(
        function = lambda x: (sqrt(x/4)-1)**2 * 4.3-0.2, 
        x_range = [0.01, 4, 0.001],
        color=RED
    )
    graph.move_to([-6, -3, 0], aligned_edge=DL)
    self.play(Write(ttl), Write(square), Write(a), Write(A), Write(b), Write(B), Write(axes), Write(graph))
    AB1 = always_redraw(Line, a.get_center(), b.get_center(), color=BLACK)
    self.add(AB1)

    text1 = t('当x为某个定值x0，\n改变s的大小，\n若此时对应的y的最大值为y0，\n不难发现(x0, y0)在边界曲线上.')
    # text1.scale(0.85)
    text1.move_to([-0.5, 0, 0], aligned_edge=UL)
    l = Line([-4.5, -3, 0], [-4.5, 1, 0], color=BLUE_E)
    x0label = Tex(r"x_0", color=BLUE)
    x0label.next_to(l.get_start(), DOWN)
    self.play(Write(text1), Write(l), Write(x0label))

    a.target.shift(DOWN*3)
    b.target.shift(RIGHT*3)
    self.play(MoveToTarget(a, run_time=2), MoveToTarget(b, run_time=2))
    a.target.shift(UP*3)
    b.target.shift(LEFT*3)
    self.play(MoveToTarget(a, run_time=2), MoveToTarget(b, run_time=2))
    self.wait(3)

    # calculation
    bg = FullScreenFadeRectangle(fill_color=WHITE, fill_opacity=0.9)
    self.play(FadeIn(bg))
    tx1 = tx_eq(r"AB:y=\frac{s-1}{s}x+1-s")
    tx1.scale(0.9)
    tx1.move_to([-6, 2, 0], aligned_edge=UL)
    self.play(Write(tx1))
    self.wait()
    tx2 = t('将直线AB的函数解析式对s求偏导，并令其为0，解得')
    tx2.scale(0.9)
    para_align(tx2, tx1)
    tx2.shift(DOWN*0.2)
    self.play(Write(tx2))
    tx3 = tx_eq(r"\frac{\partial y}{\partial s} = \frac{x}{s^2}-1=0\Rightarrow  s=\sqrt{x}")
    tx3.scale(0.9)
    para_align(tx3, tx2)
    tx3.shift(DOWN*0.2)
    self.play(Write(tx3))
    self.wait(2)
    tx4 = t('将s=√x往回带入原解析式，整理得')
    tx4.scale(0.9)
    para_align(tx4, tx3)
    tx4.shift(DOWN*0.2)
    self.play(Write(tx4))
    tx5 = tx_eq(r"y=\frac{\sqrt{x}-1}{\sqrt{x}}x+1-\sqrt{x}=(\sqrt{x}-1)^2 ")
    tx5.scale(0.9)
    para_align(tx5, tx4)
    tx5.shift(DOWN*0.2)
    self.play(Write(tx5))
    self.wait()
    rect = SurroundingRectangle(tx5, color=BLUE_E)
    self.play(Write(rect))
    self.wait(5)

    cover = FullScreenRectangle(fill_color=WHITE)
    self.play(FadeIn(cover))
    self.clear()

def explore(self):
    ttl = t('事实上……', size=22)
    ttl.move_to([-6, 3.2, 0], aligned_edge=UL)
    text1 = t('一个轨迹恰好为所求曲线的动\n点，是可以被几何构造出来的！\n *不是证明而是验证')
    text1.set_color_by_text_to_color_map(text_to_color_map={
        "*不是证明而是验证": GREY
    })
    para_align(text1, ttl)
    self.wait(3)
    text2 = t('正如右图所示，不难发现\nJE长等于J到直线y=x的距离，')
    para_align(text2, text1)
    text3 = t('也就是说，J的轨迹是一个\n被顺/逆时针旋转45°的 抛物线.')
    text3.set_color_by_text_to_color_map(text_to_color_map={
        "抛物线": BLUE_E
    })
    para_align(text3, text2)
    text4 = t('现在我们尝试利用这条\n性质，求出J的轨迹.')
    para_align(text4, text3)
    self.play(Write(ttl))
    self.wait()
    self.play(Write(text1))
    self.wait()
    self.play(Write(text2))
    self.wait(3)
    self.play(Write(text3))
    self.wait(3)
    self.play(Write(text4))
    self.wait(2)

    #calculation
    bg = FullScreenFadeRectangle(fill_color=WHITE, fill_opacity=0.9)
    self.play(FadeIn(bg))
    tx1 = t("旋转前的解析式为")
    tx1.scale(0.9)
    tx1.move_to([-6, 3, 0], aligned_edge=UL)
    self.play(Write(tx1))
    tx2 = tx_eq(r"x^2=2py=\sqrt{2}\left ( y-\frac{\sqrt{2}}{4}\right )")
    tx2.scale(0.9)
    para_align(tx2, tx1)
    self.play(Write(tx2))
    self.wait(2)
    tx3 = tx_eq(r"\Rightarrow y=\frac{\sqrt{2}}{2}x^2 +\frac{\sqrt{2}}{4}")
    tx3.scale(0.9)
    tx3.next_to(tx2, RIGHT)
    self.play(TransformFromCopy(tx2, tx3))
    self.wait(2)
    tx4 = t("对此抛物线上的任意一点应用旋转矩阵变换，其中θ=45°")
    tx4.scale(0.9)
    para_align(tx4, tx2)
    self.play(Write(tx4))
    tx5 = tx_eq(r"\begin{bmatrix}\cos \theta   & -\sin \theta\\\sin \theta  &\cos \theta\end{bmatrix}\begin{bmatrix}t \\\frac{\sqrt{2}}{2}t^2 +\frac{\sqrt{2}}{4}\end{bmatrix}=\begin{bmatrix}-\frac{1}{2}\left ( t-\frac{\sqrt{2}}{2} \right ) ^2 \\\frac{1}{2}\left ( t+\frac{\sqrt{2}}{2} \right )  ^2\end{bmatrix}")
    tx5.scale(0.8)
    para_align(tx5, tx4)
    self.play(Write(tx5))
    self.wait()
    tx6 = tx_eq(r"\Rightarrow\left\{    \begin{aligned}        &x=-\frac{1}{2}\left ( t-\frac{\sqrt{2}}{2} \right ) ^2 \\        &y=\frac{1}{2}\left ( t+\frac{\sqrt{2}}{2} \right )  ^2     \end{aligned}\right.")
    tx6.scale(0.63)
    tx6.next_to(tx5, RIGHT)
    self.play(Write(tx6))

    tx7 = t("解出t并舍去y>1的曲线部分，将参数方程化为函数解析式，")
    tx7.scale(0.9)
    para_align(tx7, tx5)
    self.play(Write(tx7))
    tx8 = tx_eq(r"y=(\sqrt{x}-1)^2")
    para_align(tx8, tx7)
    self.play(Write(tx8))
    self.wait()
    rect = SurroundingRectangle(tx8, color=BLUE_E)
    self.play(Write(rect))
    self.wait(5)
    cover = FullScreenRectangle(fill_color=WHITE)
    self.play(FadeIn(cover))
    self.clear()

# class test(Scene):
#     def construct(self):
#         self.add_sound(sound_file='assets/sounds/widmung.mp4')
#         explore(self)

def ending(self):
    text1 = t('包络线的本质是一个点集，')
    text2 = t('而这个集合里的所有点都来自于运动的线段.')
    text3 = t('只要搞清楚哪个点在包络线上，')
    text4 = t('求解析式便易如反掌了.')
    text1.move_to([0,1,0])
    text2.next_to(text1, DOWN)
    text3.next_to(text2, DOWN)
    text4.next_to(text3, DOWN)
    self.play(Write(text1))
    self.wait()
    self.play(Write(text2))
    self.wait()
    self.play(Write(text3))
    self.wait()
    self.play(Write(text4))
    self.wait(2)
    self.play(Uncreate(text1), Uncreate(text2), Uncreate(text3), Uncreate(text4))
    
    end = Tex('END', color=BLACK)
    end.scale(3)
    end.center()
    self.play(Write(end, run_time=2))

class animation(Scene):
    def construct(self):
        que = t('在边长为1的正方形顶点上，动点A、B以相同速度出发并运动：')
        que.move_to([0,3.2,0])
        self.play(Write(que))
        global square, a, A, b, B, AB
        square = Square(4, color=BLACK)
        square.center()
        a = SmallDot([-2, 2, 0], color=BLACK)
        A = Tex('A', color=BLACK)
        always(A.next_to, a, LEFT)
        b = SmallDot([-2, -2, 0], color=BLACK)
        B = Tex('B', color=BLACK)
        always(B.next_to, b, DOWN)
        self.play(FadeIn(a), FadeIn(A), FadeIn(b), FadeIn(B), ShowCreation(square))
        self.wait()

        # match AB
        AB = always_redraw(Line, a.get_center(), b.get_center(), color=BLACK)
        self.add(AB)

        # animate forth
        a.generate_target()
        a.target.move_to(b.get_center())
        b.generate_target()
        b.target.move_to([2, -2, 0])
        self.play(MoveToTarget(a, run_time=2), MoveToTarget(b, run_time=2))
        self.wait()
        a.target.move_to([-2, 2, 0])
        b.target.move_to([-2, -2, 0])
        lines = []
        colors = color_gradient([BLACK, BLUE_E], 50)
        for i in range(50):
            start = [2-4/50*i, -2, 0]
            end = [-2, -2+4/50*i, 0]
            lines.append(Line(start, end, color=colors[i]))

        que_ = t('则AB扫过的图形的边缘的解析式是什么呢？')
        que_.move_to([0,3.2,0])
        self.play(ReplacementTransform(que, que_), MoveToTarget(a, run_time=0.5), MoveToTarget(b, run_time=0.5))
        for l in lines:
            self.play(FadeIn(l, run_time=0.05))
            self.wait(0.02)
        graph = FunctionGraph(
            function = lambda x: (sqrt(x/4)-1)**2 * 4.3-0.2, 
            x_range = [0.01, 4, 0.001],
            color=RED
        )
        graph.center()
        self.play(Write(graph))
        self.wait(5)

        self.play(*[Uncreate(i) for i in [que, que_, graph]+lines])
        a.target.shift(LEFT*4+DOWN)
        b.target.shift(LEFT*4+DOWN)
        square.generate_target()
        square.target.shift(LEFT*4+DOWN)
        for i in [a.target, b.target, square.target]:
            i.set_color(GREY_A)
        self.play(MoveToTarget(a), MoveToTarget(b), MoveToTarget(square), FadeOut(AB), FadeOut(A), FadeOut(B))

        text1 = t("这里我们介绍求此曲线解析式的 三种方法：")
        text1.set_color_by_text_to_color_map(text_to_color_map={
            "三种": RED
        })
        text1.move_to([-0.6, 2, 0])
        text2 = t("①相邻相交法：求某个时刻与下个时刻的AB的交点")
        text2.set_color_by_text_to_color_map(text_to_color_map={
            "求某个时刻与下个时刻的AB的交点": GREY
        })
        para_align(text2, text1)
        text2.shift(DOWN*0.2)
        text3 = t("②界点判别式法：对曲线上的点应用判别式")
        text3.set_color_by_text_to_color_map(text_to_color_map={
            "对曲线上的点应用判别式": GREY
        })
        para_align(text3, text2)
        text3.shift(DOWN*0.2)
        text4 = t("③偏导数法：对于某个x，求整个运动中y的最大值")
        text4.set_color_by_text_to_color_map(text_to_color_map={
            "对于某个x，求整个运动中y的最大值": GREY
        })
        para_align(text4, text3)
        text4.shift(DOWN*0.2)
        self.play(Write(text1))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(Write(text4))
        self.wait(5)
        self.play(Uncreate(text1), Uncreate(text2), Uncreate(text3), Uncreate(text4))
        for i in [a.target, b.target, square.target]:
            i.set_color(BLACK)
        self.play(MoveToTarget(a), MoveToTarget(b), MoveToTarget(square), FadeIn(AB), FadeIn(A), FadeIn(B))
        del text1, text2, text3, text4, que, que_
        
        method1(self)
        method2(self)
        method3(self)
        explore(self)
        ending(self)