manim -qm -v WARNING integral_scenes.py RiemannRefinement
%%manim -qm -v WARNING RiemannRefinement

from manim import *
import math

class RiemannRefinement(Scene):
    def construct(self):
        # Eixos e função (parábola sempre positiva no intervalo)
        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 0.5],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"include_numbers": True}
        ).to_edge(DOWN)
        self.play(Create(ax), run_time=1.5)

        def f(x):
            return 0.3*(x-2)**2 + 1  # >= 1 no [0,4]

        graph = ax.plot(f, color=BLUE)
        title = Text("Soma de Riemann: refinando Δx", weight=BOLD).to_edge(UP)
        self.play(Write(title), Create(graph), run_time=1.8)

    
        def make_rects(dx):
            rects = ax.get_riemann_rectangles(
                graph,
                x_range=[0, 4],
                dx=dx,
                stroke_color=WHITE,
                stroke_width=1,
                color=YELLOW,
                fill_opacity=0.6,
            )
            return rects

        # Sequência de refinamentos (Δx / 2 a cada passo)
        dx0 = 0.5  # ~8 retângulos
        rects = make_rects(dx0)
        self.play(FadeIn(rects), run_time=1)
        self.wait(2)

        for _ in range(3):  # 0.25, 0.125, 0.0625
            new_rects = make_rects(dx0/2)
            self.play(ReplacementTransform(rects, new_rects), run_time=1.2)
            rects = new_rects
            dx0 /= 2
            self.wait(2)

        # Área "exata" preenchida ao final
        exact_area = ax.get_area(graph, x_range=[0, 4], color=BLUE, opacity=0.5)
        self.play(ReplacementTransform(rects, exact_area), run_time=1.2)
        self.wait(2)
