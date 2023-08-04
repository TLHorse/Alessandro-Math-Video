from manimlib import *

def tx_eq(s, col=BLACK):
    ret = Tex(s, color=col)
    ret.scale(0.85)
    return ret

def t(s):
    return Text(text=s, font='Songti SC', size=15, color=BLACK)

def para_align(mob, to):
    mob.next_to(to, DOWN)
    mob.align_to(to, LEFT)

def middle_point(A, B):
    # coordA = A.get_center()
    # coordB = B.get_center()
    return [(A[0]+B[0])/2, (A[1]+B[1])/2, 0]

class animation(Scene):
    def construct(self):
        t1 = t('解决几何动点问题的关键一步，就是求动点轨迹。')
        t2 = t("本视频介绍up发现的一种方法——速度分析法，\n用以求得所有线性动点的轨迹，进一步解决动点问题。")
        t2.set_color_by_text_to_color_map(text_to_color_map={
            "速度分析法" : BLUE_E
        })
        t2.align_to(t1, LEFT)
        t3 = t("对于例题证明的方法和步骤，欢迎讨论交流。")
        t3.align_to(t1, LEFT)
        t1.shift(UP)
        t3.shift(DOWN*2)

        t1.shift(LEFT)
        t2.shift(LEFT)
        t3.shift(LEFT)
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait(3)
        self.play(Write(t3))
        self.wait(3)
        
        self.play(Uncreate(t3),Uncreate(t2),Uncreate(t1))

        t4 = t("速度分析法类比受力分析。它的底层逻辑是：")
        t5 = t("（1）将题目条件中每个动点的速度大小、运动方向转化为矢量；")
        t6 = t("（2）通过几何关系，由已知矢量推出未知矢量；")
        t7 = t("（3）将推出的矢量作为未知动点的分速度，计算出合速度，")
        t8 = t("找到起点，画出未知动点的轨迹。")

        t5to8 = VGroup(t4, t5, t6, t7, t8)
        t5to8.scale(0.9)
        t5to8.arrange(DOWN, buff=0.5)
        t4.shift(LEFT*2)
        t5.align_to(t4, LEFT)
        t6.align_to(t4, LEFT)
        t7.align_to(t4, LEFT)
        t8.align_to(t4, LEFT)

        self.play(Write(t4))
        self.play(Write(t5))
        self.wait()
        self.play(Write(t6))
        self.wait()
        self.play(Write(t7))
        self.play(Write(t8))
        self.wait(6)

        self.play(Uncreate(t5to8))

        t9 = VGroup(t('先给出如下的引理和基本事实。'), t('若觉得无聊晦涩可以跳过这部分，'), t('这将不会影响后续的理解。'))
        t9.arrange(DOWN, buff=0.2)
        t9.center()
        self.play(FadeIn(t9))
        self.wait(2)
        self.play(FadeOut(t9))

        lemma1(self)
        lemma2(self)

        t12 = t(
"""发现了吗？引理1描述的是运动的位似，引理2则是主从联动（即
瓜豆原理）的矢量描述。这两者都是速度分析中不可或缺的
部分。接下来我们给出一个基本事实，也是速度分析的原则：

若干个动点的速度在同时加上（或减去）一个速度后，这些动点
的相对位置不发生改变，所有动点的轨迹都发生改变。

注：我们所说的“速度”是包含大小、方向的矢量。
""")
        t12.center()
        self.play(ShowCreation(t12))
        self.wait(12)
        self.play(Uncreate(t12))
        
        t13 = t('让我们从例子中学习速度分析吧！\n这里举几个简单的例子：')
        t13.scale(1.2)
        self.play(Write(t13))
        self.wait()
        self.play(Uncreate(t13))

        eg1(self)
        eg2(self)
        eg3(self)
        eg4(self)
        play_end(self)
        

def lemma1(self):
    t10 = ImageMobject('assets/raster_images/lm1.jpg', height=2)
    t10.align_on_border(UP)
    self.play(FadeIn(t10))
    t10rect = SurroundingRectangle(t10, color=BLUE_E)
    self.play(Write(t10rect))

    a = SmallDot([-1, -3, 0], color=BLACK)
    A = Tex('A', color=BLACK)
    b = SmallDot([-3, 0, 0], color=BLACK)
    B = Tex('B', color=BLACK)
    always(A.next_to, a, LEFT)
    always(B.next_to, b, LEFT)
    self.play(ShowCreation(a), ShowCreation(A))
    self.play(ShowCreation(b), ShowCreation(B))

    p = SmallDot(middle_point(a.get_center(), b.get_center()), color=BLACK)
    P = Tex('P', color=BLACK)
    always(P.next_to, p, LEFT)
    p.add_updater(
        lambda m: m.move_to(
            middle_point(a.get_center(), b.get_center())
        )
    )
    b.generate_target()
    b.target.shift(RIGHT*4)
    AB = always_redraw(Line, a.get_center(), b.get_center(), color=BLACK)
    self.play(Write(AB))
    self.play(ShowCreation(p), ShowCreation(P))
    self.wait(0.2)
    self.play(MoveToTarget(b))

    v = Arrow(start=b.get_center(), end=[3, 0, 0], color=BLUE_E, buff=0)
    vtext = Tex(r'\vec{v}_{B}', color=BLACK)
    vtext.next_to(v, UP)
    self.play(Write(v), Write(vtext))
    kv = Arrow(start=p.get_center(), end=[1.3, -1.5, 0], color=BLUE_E, buff=0)
    kvtext = Tex(r'\vec{v}_{P}=\frac{PA}{BA}\vec{v}_{B}=\frac{\vec{v}_{B}}{2}', color=BLACK)
    kvtext.scale(0.7)
    kvtext.next_to(kv, UR)
    self.play(Write(kv), Write(kvtext))
    self.wait(6)
    self.play(*[Uncreate(i) for i in [t10, t10rect, a, A, b, B, p, P, AB, v, vtext, kv, kvtext]])

def lemma2(self):
    t11 = ImageMobject('assets/raster_images/lm2.jpg', height=3)
    t11.align_on_border(UP)
    self.play(FadeIn(t11))
    t11rect = SurroundingRectangle(t11, color=BLUE_E)
    self.play(Write(t11rect))

    o = SmallDot([-3, -2.5, 0], color=BLACK)
    O = Tex('O', color=BLACK)
    a2 = SmallDot([-3, -0.5, 0], color=BLACK)
    A2 = Tex('A', color=BLACK)
    b2 = SmallDot([-1, -2.5, 0], color=BLACK)
    B2 = Tex('B', color=BLACK)
    O.next_to(o, DL)
    always(A2.next_to, a2, RIGHT)
    always(B2.next_to, b2, DOWN)
    self.play(ShowCreation(o), ShowCreation(O))
    self.play(
        ShowCreation(a2), ShowCreation(A2), 
        ShowCreation(b2), ShowCreation(B2)
    )
    OA2 = always_redraw(Line, o.get_center(), a2.get_center(), color=BLACK)
    OB2 = always_redraw(Line, o.get_center(), b2.get_center(), color=BLACK)
    self.play(Write(OA2), Write(OB2))
    self.wait(0.3)
    a2.generate_target()
    a2.target.shift(LEFT)
    b2.generate_target()
    b2.target.shift(UP)
    self.play(MoveToTarget(a2), MoveToTarget(b2))
    
    va = Arrow(start=a2.get_center(), end=[-5, -0.5, 0], color=BLUE_E, buff=0)
    vatext = Tex(r'\vec{v}_{A}', color=BLACK)
    vatext.next_to(va, UP)
    self.play(Write(va), Write(vatext))
    vb = Arrow(start=b2.get_center(), end=[-1, -0.5, 0], color=BLUE_E, buff=0)
    vbtext = Tex(r'\vec{v}_{B}', color=BLACK)
    vbtext.next_to(vb, LEFT)
    self.play(Write(vb), Write(vbtext))
    self.wait()
    va_eq_vb = Tex(r'\left | \vec{v}_{A} \right |=\left | \vec{v}_{B} \right |', color=BLACK)
    va_eq_vb.move_to([3, -1, 0])
    va_vb_ang = Tex(r'\left \langle \vec{v}_{A}, \vec{v}_{B} \right \rangle =90^{\circ}', color=BLACK)
    va_vb_ang.next_to(va_eq_vb, DOWN)
    va_vb_ang.align_to(va_eq_vb, LEFT)
    self.play(Write(va_eq_vb))
    self.wait()
    self.play(TransformFromCopy(va_eq_vb, va_vb_ang))
    self.wait(6)
    self.play(*[Uncreate(i) for i in [t11, t11rect, a2, A2, b2, B2, o, O, OA2, OB2, va, vatext, vb, vbtext, va_eq_vb, va_vb_ang]])

def eg1(self):
    t13 = ImageMobject('assets/raster_images/eg1.jpg')
    t13.move_to([0, 3, 0])
    t13.scale(0.35)

    sq = Square(3, color=BLACK)
    sq.move_to([-4.5, 0, 0])
    self.play(ShowCreation(sq), FadeIn(t13))
    am = SmallDot([-4.5-3/2, 3/2, 0], color=BLACK)
    Am = Tex('A', color=BLACK)
    bm = SmallDot([-4.5-3/2, -3/2, 0], color=BLACK)
    Bm = Tex('B', color=BLACK)
    pm = SmallDot(middle_point(am.get_center(), bm.get_center()), color=BLACK)
    Pm = Tex('P', color=BLACK)
    pm.add_updater(
        lambda m: m.move_to(
            middle_point(am.get_center(), bm.get_center())
        )
    )
    always(Am.next_to, am, LEFT)
    always(Bm.next_to, bm, DOWN)
    always(Pm.next_to, pm, UR)
    self.play(ShowCreation(am), ShowCreation(Am), ShowCreation(bm), ShowCreation(Bm), ShowCreation(pm), ShowCreation(Pm))
    ambm = always_redraw(Line, am.get_center(), bm.get_center(), color=BLACK)
    self.add(ambm)
    
    am.generate_target()
    bm.generate_target()
    am.target.move_to([-4.5-3/2, -3/2, 0])
    bm.target.move_to([-4.5+3/2, -3/2, 0])
    self.play(MoveToTarget(am, run_time=3.5), MoveToTarget(bm, run_time=2.5))
    self.wait()
    am.target.move_to([-4.5-3/2, 3/2, 0])
    bm.target.move_to([-4.5-3/2, -3/2, 0])
    self.play(MoveToTarget(am, run_time=0.5), MoveToTarget(bm, run_time=0.5))

    vam = Arrow(start=am.get_center(), end=[-4.5-3/2, 3/2-1, 0], color=BLUE_E, buff=0)
    vbm = Arrow(start=bm.get_center(), end=[-4.5-3/2+1, -3/2, 0], color=BLUE_E, buff=0)
    t14 = tx_eq(r'\because \vec{v}_{A}=(0, 1), \vec{v}_{B}=(1, 0)')
    t14.move_to([0, 2, 0])
    self.play(Write(vam), Write(vbm), Write(t14))
    self.wait(2)
    vpm1 = Arrow(start=pm.get_center(), end=[-4.5-3/2, 0-0.5, 0], color=BLUE_E, buff=0)
    vpm2 = Arrow(start=pm.get_center(), end=[-4.5-3/2+0.5, 0, 0], color=BLUE_E, buff=0)
    t15 = tx_eq(r'\therefore \vec{v}_{P1}=\frac{\vec{v}_{A}}{2}=(0, \frac{1}{2}), \vec{v}_{P2}=\frac{\vec{v}_{B}}{2}=(\frac{1}{2}, 0)\text{(lem. 1)}')
    para_align(t15, t14)
    self.play(TransformFromCopy(vam, vpm1), TransformFromCopy(vbm, vpm2), TransformFromCopy(t14, t15))
    self.wait(2)
    vpsig = Arrow(start=pm.get_center(), end=[-4.5-3/2+0.5, 0-0.5, 0], color=RED, buff=0)
    t16 = tx_eq(r'\therefore \sum \vec{v}_{P}=\vec{v}_{P1}+\vec{v}_{P2}=\left(\frac{1}{2} , \frac{1}{2}\right)')
    para_align(t16, t15)
    self.play(Write(vpsig), TransformFromCopy(t15, t16))
    self.wait(2)
    t17 = tx_eq(r'\therefore \left | \vec{v}_{P} \right |=\sqrt{\left ( \frac{1}{2}  \right ) ^2+\left ( \frac{1}{2}  \right ) ^2}=\frac{\sqrt{2} }{2} ')
    para_align(t17, t16)
    self.play(TransformFromCopy(t16, t17))
    self.wait(4)
    self.play(Uncreate(t14), Uncreate(t15),Uncreate(t16), Uncreate(t17))
    t18 = t('可见，动点P从正方形一边的\n中点，沿红色箭头方向作直线运动，\n到另一邻边的中点。')
    t18.shift(RIGHT*2.5)
    self.play(Write(t18))
    self.wait(3)
    self.play(*[Uncreate(i) for i in [t13, sq, am, Am, bm, Bm, pm, Pm, ambm, vam, vbm, vpm1, vpm2, vpsig, t18]])

def eg2(self):
    t19 = ImageMobject('assets/raster_images/eg2.jpg')
    t19.move_to([0, 2.7, 0])
    t19.scale(0.51)

    sq = Square(3, color=BLACK)
    sq.move_to([-4.5, 0, 0])
    self.play(ShowCreation(sq), FadeIn(t19))
    am2 = SmallDot([-4.5-3/2, 3/2, 0], color=BLACK)
    Am2 = Tex('A', color=BLACK)
    om = SmallDot([-4.5-3/2, -3/2, 0], color=BLACK)
    Om = Tex('O', color=BLACK)
    bm2 = SmallDot([-4.5+3/2, -3/2, 0], color=BLACK)
    Bm2 = Tex('B', color=BLACK)
    Am2.next_to(am2, LEFT)
    always(Om.next_to, om, DOWN)
    always(Bm2.next_to, bm2, DR)
    self.play(ShowCreation(am2), ShowCreation(Am2), ShowCreation(om), ShowCreation(Om), ShowCreation(bm2), ShowCreation(Bm2))

    am2om = always_redraw(Line, start=am2.get_center(), end=om.get_center(), color=BLACK)
    self.add(am2om)
    bm2om = always_redraw(Line, start=bm2.get_center(), end=om.get_center(), color=BLACK)
    self.add(bm2om)

    om.generate_target()
    bm2.generate_target()
    om.target.shift(RIGHT*3)
    bm2.target.shift(UR*3)
    self.play(MoveToTarget(om, run_time=3), MoveToTarget(bm2, run_time=3))
    self.wait()
    om.target.shift(LEFT*3)
    bm2.target.shift(DL*3)
    self.play(MoveToTarget(om, run_time=0.5), MoveToTarget(bm2, run_time=0.5))

    vom = Arrow(start=om.get_center(), end=[-4.5-3/2+0.8, -3/2, 0], color=BLUE_E, buff=0)
    t20 = tx_eq(r'\because \vec{v}_{A}=(0,0), \vec{v}_{O}=(0,1)')
    t20.move_to([1,1.5,0])
    self.play(Write(t20), Write(vom))
    self.wait()
    vomd = Arrow(start=om.get_center(), end=[-4.5-3/2-0.8, -3/2, 0], color=GREEN_E, buff=0)
    vam2d = Arrow(start=am2.get_center(), end=[-4.5-3/2-0.8, 3/2, 0], color=GREEN_E, buff=0)
    t21 = tx_eq(r"& \therefore \vec{v}_{A}'=\vec{v}_{A}-\vec{v}_{O}=(0,-1),\\ & \vec{v}_{O}'=\vec{v}_{O}-\vec{v}_{O}=(0,0)\quad\text{(basic fact)}")
    para_align(t21, t20)
    self.play(Write(vomd), Write(vam2d), TransformFromCopy(t20,t21))
    
    ding = t('（定）')
    ding.move_to(om.get_center())
    ding.shift(DR*0.6)
    dong = t('（动）')
    dong.move_to(am2.get_center())
    dong.shift(DR*0.6)
    self.play(Write(ding), Write(dong))
    self.wait()
    self.play(FadeOut(vomd), FadeOut(vom))
    self.wait(2)

    vam2dr = Arrow(start=am2.get_center(), end=[-4.5-3/2-0.8, 3/2, 0], color=GREEN_E, buff=0)
    self.add(vam2dr)

    t22 = tx_eq(r"\therefore \vec{v}_{B1}'=(0, 1)\quad\text{(lem. 2)}")
    para_align(t22, t21)
    self.play(Rotate(vam2dr,PI/2,run_time=1,axis=IN,about_point=om.get_center()), TransformFromCopy(t21,t22))

    vomdd = Arrow(start=om.get_center(), end=[-4.5-3/2+0.8, -3/2, 0], color=RED, buff=0)
    vam2dd = Arrow(start=am2.get_center(), end=[-4.5-3/2+0.8, 3/2, 0], color=RED, buff=0)
    vb = Arrow(start=bm2.get_center(), end=[-4.5+3/2+0.8, -3/2, 0], color=RED, buff=0)
    vbsig = Arrow(start=bm2.get_center(), end=[-4.5+3/2+0.8, -3/2+0.8, 0], color=RED_E, buff=0)

    t23 = tx_eq(r"& \therefore \vec{v}_{A}=\vec{v}_{A}'+\vec{v}_{O}=(0,-1), \\ & \vec{v}_{O}=\vec{v}_{O}'+\vec{v}_{O}=(0,0),\\ & \sum\vec{v}_{B}=\vec{v}_{B1}'+\vec{v}_{O}=(1,1)")
    para_align(t23, t22)
    self.play(Write(vomdd), Write(vam2dd), Write(vb), Swap(ding,dong))
    self.play(Uncreate(vam2d), Uncreate(vam2dd))
    self.wait(2)
    self.play(Write(vbsig), TransformFromCopy(t22,t23))
    self.wait(4)
    self.play(FadeOut(t19), *[Uncreate(i) for i in [t20, t21, ding, dong, t22, t23]])

    t24 = t(
'''不同于例1，这道题稍有复杂。画出O的
速度矢量后，我们发现无法直接使用引理2即瓜
豆原理，因此将A、O同时赋予一个向左的速度
vO，使得O为定点（可理解为切换O为参照物），
然后使用瓜豆原理画出O为定点时B的速度矢
量，再将所有点加上一个向右的速度，把向左的
速度vO抵消掉。这个向右的速度与瓜豆原理得出
的那个速度进行合成，所得即B的速度大小、方向，
从而得到B的轨迹，即深红色箭头方向的线段。

当然了，本题也可以连接AB，直接用瓜豆原理。''')
    t24.shift(RIGHT*2.5)
    t24.scale(0.8)
    self.play(Write(t24))
    self.wait(12)
    self.play(*[Uncreate(i) for i in [sq, am2, Am2, om, Om, bm2, Bm2, am2om, bm2om, vomd, vom, vam2d, vam2dr, vomdd, vam2dd, vb, vbsig, t24]])

def eg3(self):
    t25 = ImageMobject('assets/raster_images/eg3.jpg')
    t25.move_to([0, 2.45, 0])
    t25.scale(0.6)

    k_an = [-4, -3, 0]
    k_cn = [-4+3*0.9, -3, 0]
    k_bn = [-4, -3+4*0.9, 0]
    pl = Polygon(k_an, k_bn, k_cn)
    pl.set_color(BLACK)
    an = SmallDot(k_an, color=BLACK)
    An = Tex('A', color=BLACK)
    always(An.next_to, an, DOWN)
    bn = SmallDot(k_bn, color=BLACK)
    Bn = Tex('B', color=BLACK)
    always(Bn.next_to, bn, LEFT)
    cn = SmallDot(k_cn, color=BLACK)
    Cn = Tex('C', color=BLACK)
    always(Cn.next_to, cn, UR)
    dn = SmallDot([k_cn[0], k_bn[1], 0], color=BLACK)
    Dn = Tex('D', color=BLACK)
    always(Dn.next_to, dn, UP)
    an.generate_target()
    bn.generate_target()
    cn.generate_target()
    dn.generate_target()
    an.target.move_to(k_cn)
    bn.target.move_to(k_an)
    cn.target.move_to(k_bn)
    dn.target.move_to([k_cn[0]-6*0.9, k_bn[1], 0])

    self.play(FadeIn(t25),Write(pl), Write(an), Write(An), Write(bn), Write(Bn), Write(cn), Write(Cn), Write(dn), Write(Dn))
    l_anbn = always_redraw(Line, start=an.get_center(), end=bn.get_center(), color=BLACK)
    l_ancn = always_redraw(Line, start=an.get_center(), end=cn.get_center(), color=BLACK)
    l_cndn = always_redraw(Line, start=cn.get_center(), end=dn.get_center(), color=BLACK)
    l_dnbn = always_redraw(Line, start=dn.get_center(), end=bn.get_center(), color=BLACK)
    self.play(Write(l_anbn), Write(l_ancn), Write(l_cndn), Write(l_dnbn))
    self.wait()
    self.play(MoveToTarget(an, run_time=4), MoveToTarget(bn, run_time=4), MoveToTarget(cn, run_time=4), MoveToTarget(dn, run_time=4))
    self.wait()
    an.target.move_to(k_an)
    bn.target.move_to(k_bn)
    cn.target.move_to(k_cn)
    dn.target.move_to([k_cn[0], k_bn[1], 0])
    self.play(MoveToTarget(an, run_time=0.5), MoveToTarget(bn, run_time=0.5), MoveToTarget(cn, run_time=0.5), MoveToTarget(dn, run_time=0.5))

    k_dn = [k_cn[0], k_bn[1], 0]
    van = Arrow(start=k_an, end=middle_point(k_an, k_cn), buff=0, color=BLUE_E)
    vbn = Arrow(start=k_bn, end=middle_point(k_bn, k_an), buff=0, color=BLUE_E)
    vcn = Arrow(start=k_cn, end=middle_point(k_bn, k_cn), buff=0, color=BLUE_E)
    vdan = Arrow(start=k_dn, end=middle_point(k_dn, k_bn), buff=0, color=GREEN_E)
    vdcn = Arrow(start=k_dn, end=middle_point(k_dn, [-4, -3+8*0.9, 0]), buff=0, color=GREEN_E)
    vdbn = Arrow(start=k_dn, end=middle_point(k_dn, k_cn), buff=0, color=GREEN_E)
    t26 = tx_eq(r'\because \vec{v}_{A}=(3,0) \therefore \vec{v}_{D1}=-\vec{v}_{A}=(-3,0)')
    vdsig = Arrow(start=k_dn, end=k_bn, buff=0, color=RED)

    self.play(Write(van), Write(vbn), Write(vcn))
    self.wait(0.5)
    t26 = tx_eq(r'\because \vec{v}_{A}=(3,0) \therefore \vec{v}_{D1}=-\vec{v}_{A}=(-3,0)')
    t26.move_to([2.7, 0.8, 0])
    self.play(Write(t26), TransformFromCopy(van, vdan))
    self.wait(2)
    t27 = tx_eq(r'\because \vec{v}_{B}=(-4,0) \therefore \vec{v}_{D2}=\vec{v}_{B}=(0, -4)')
    para_align(t27, t26)
    self.play(TransformFromCopy(t26, t27), TransformFromCopy(vbn, vdbn))
    self.wait(2)
    t28 = tx_eq(r'\because \vec{v}_{C}=(-3,4) \therefore \vec{v}_{D3}=\vec{v}_{C}=(-3, 4)')
    para_align(t28, t27)
    self.play(TransformFromCopy(t27, t28), TransformFromCopy(vcn, vdcn))
    self.wait(2)

    t29 = tx_eq(r'\therefore \sum \vec{v}_{D}=(-3, 0)+(0, -4)+(-3,4) \\ =(-6,0)')
    para_align(t29, t28)
    self.play(TransformFromCopy(t28, t29), Write(vdsig))
    self.wait(4)

    self.play(*[Uncreate(i) for i in [t26, t27, t28, t29]])

    t30 = t(
'''可见D的轨迹是过B平行于AC的
直线，轨迹长为图中红箭头长的两倍。
值得注意的是，在本题中速度的推导
用到了平行四边形的性质。A、D在对
角顶点上，因此D的一个分速度与A的
速度大小相等、方向相反；C和D、B
和D在同一条边上，因此D的一个分速
度和C的速度相同，一个和B相同。
''')
    t30.shift(RIGHT*3.2+DOWN)
    t30.scale(0.85)
    self.play(Write(t30))
    self.wait(10)
    self.play(FadeOut(t25), *[Uncreate(i) for i in [an, bn, cn, dn, An, Bn, Cn, Dn, l_anbn, l_cndn, l_ancn, l_dnbn, van, vbn, vcn, vdan, vdbn, vdcn, vdsig, t30, pl]])

def eg4(self):
    img = ImageMobject('assets/raster_images/eg4.jpg')
    img.move_to([0, 3, 0])
    img.scale(0.35)
    k_b = [-3.5, -2.5, 0]
    k_c = [-3.5+2, -2.5, 0]
    k_a = [-3.5, -2.5+4, 0]
    pl = Polygon(k_a, k_b, k_c)
    pl.set_color(BLACK)

    a = SmallDot(k_a, color=BLACK)
    A = Tex('A', color=BLACK)
    always(A.next_to, a, LEFT)
    b = SmallDot(k_b, color=BLACK)
    B = Tex('B', color=BLACK)
    always(B.next_to, b, DOWN)
    self.play(Write(pl), Write(a), Write(A), Write(b), Write(B), FadeIn(img))
    self.wait()

    l_ab = always_redraw(Line, start=a.get_center(), end=b.get_center(), color=BLACK)
    self.add(l_ab)
    a.generate_target()
    b.generate_target()
    a.target.move_to(k_b)
    b.target.move_to(k_c)
    self.play(MoveToTarget(a, run_time=3), MoveToTarget(b, run_time=3))
    self.wait()
    a.target.move_to(k_a)
    b.target.move_to(k_b)
    self.play(MoveToTarget(a, run_time=0.5), MoveToTarget(b, run_time=0.5))
    
    va = Arrow(start=a.get_center(), end=middle_point(k_a, k_b), buff=0, color=BLUE_E)
    vb = Arrow(start=b.get_center(), end=middle_point(k_b, k_c), buff=0, color=BLUE_E)
    eq1 = tx_eq(r'\because \vec{v}_{A}=(0,-2), \vec{v}_{B}=(1, 0)')
    eq1.move_to([2.2, 1.2, 0])
    self.play(Write(eq1), Write(va), Write(vb))
    self.wait(2)

    vad = Arrow(start=k_a, end=[-3.5-1, -2.5+4, 0], buff=0, color=GREEN_E)
    vbd = Arrow(start=k_b, end=[-3.5-1, -2.5, 0], buff=0, color=GREEN_E)
    eq2 = tx_eq(r"&\therefore \vec{v}_{A}'=\vec{v}_{A}-\vec{v}_{B}=(-1, -2)\\&\vec{v}_{B}'=\vec{v}_{B}-\vec{v}_{B}=(0,0)")
    para_align(eq2, eq1)
    self.play(TransformFromCopy(eq1, eq2), Write(vad), Write(vbd))
    ding = t('（定）')
    ding.move_to(k_b)
    ding.shift(DR*0.6)
    dong = t('（动）')
    dong.move_to(k_a)
    dong.shift(UR*0.6)
    self.play(Write(ding), Write(dong))
    self.wait(2)
    vasig = Arrow(start=k_a, end=[-3.5-1, -2.5+4-2, 0], buff=0, color=RED)
    self.play(Uncreate(vb), Uncreate(vbd), Write(vasig))
    self.wait()
    traj = DashedLine(start=k_a, end=[-3.5-2, -2.5, 0], color=RED_E)
    la_label = tx_eq("l_{A'}", col=RED_E)
    la_label.move_to(traj.get_end())
    la_label.shift(UP)
    self.play(Write(traj), Write(la_label))

    eq3 = tx_eq(r"&\therefore A'B'=AB, \text{when}\ A'B'_{min}, AB_{min}")
    para_align(eq3, eq2)
    self.play(TransformFromCopy(eq2, eq3))

    perpline = DashedLine(start=k_b, end=[-3.5-8/5, -2.5+4/5, 0], color=RED_E)
    eq4 = tx_eq(r"\text{when}\ AB\perp l_{A'}, A'B'_{min}")
    para_align(eq4, eq3)
    self.play(TransformFromCopy(eq3, eq4), Write(perpline))
    eq5 = tx_eq(r"\therefore  AB_{min}=A'B'_{min}=\frac{4}{\sqrt{5} }=\frac{4\sqrt{5} }{5}")
    para_align(eq5, eq4)
    self.play(TransformFromCopy(eq4, eq5))
    self.wait(5)

    self.play(*[Uncreate(i) for i in [eq1, eq2, eq3, eq4, eq5]])
    
    explanation = t(
'''在本题中，通过赋予全局一个向
左的速度，巧妙将两动点之间距离
最短转化为定点到直线间垂线段最
短，可以理解为改变参照物，用三
角函数一除即得答案。常规方法则
须设动点路程构造二次函数求最值。''')
    explanation.shift(RIGHT*3.2)
    explanation.scale(0.85)
    self.play(Write(explanation))
    self.wait(8)
    self.play(FadeOut(img), *[Uncreate(i) for i in [pl, a, b, A, B, va, vad, vb, vbd, vasig, ding, dong, la_label, traj, perpline, explanation, l_ab]])

def play_end(self):
    ask = t(
"""思考：为什么上面这些例子中，
动点的轨迹都是直线呢？""")
    ask.center()
    self.play(ShowCreation(ask))
    self.wait(2)
    ans = t(
"""直线不是偶然。题设中每个动点的速度是一个
不变的向量，而经过几何旋转平移，这些向量
加上一个另一个不变的向量，或乘以一个系数，
仍然是一个不变的向量，因此未知的动点轨迹
一定是匀速直线运动。""")
    ans2 = t(
"""因此，如果在题目中，已知动点作线性运
动，经过了平移、旋转这样的线性变换，得
到未知动点，那么未知动点的轨迹一定是直
线——我称之为「动点线性定理」。
""")
    ans3 = t(
"""再碰到这类的题，就找到动点的起止位
置，大胆去连，轨迹就是它啦！""")
    end = Tex('END', color=BLACK)
    end.scale(2)
    end.center()
    ans3.center()
    ans2.center()
    ans.center()

    self.play(Transform(ask, ans))
    self.wait(10)
    self.play(Transform(ask, ans2))
    self.wait(9)
    self.play(Transform(ask, ans3))
    self.wait(3)
    self.play(Transform(ask, end))
    self.wait(3)