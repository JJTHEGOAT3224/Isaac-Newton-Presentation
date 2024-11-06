from manim import * 

class IssacNewtonPresentation(Scene):
    def construct(self):
        
        #c = NumberPlane().add_coordinates()
        #self.play(Write(c))


        # Intro To Presentation

        s1 = Square(5,
                    color = "#003049",
                    fill_opacity = 1,
                    )
        s2 = Square(4,
                    color = "#d62828",
                    fill_opacity = 1).shift(DOWN*.5)
        s3 = Square(3,
                    color = "#f77f00",
                    fill_opacity = 1).shift(DOWN*1)
        s4 = Square(2,
                    color = "#fcbf49",
                    fill_opacity = 1).shift(DOWN*1.5)
        s5 = Square(1,
                    color = "#eae2b7",
                    fill_opacity = 1).shift(DOWN*2)
        sb = Square(5,
                    color = LOGO_WHITE,)
        introt = Text("Isaac Newton ").shift(DOWN*2)


        self.play(GrowFromEdge(s1,
                               DOWN))
        self.play(GrowFromEdge(s2,
                               DOWN))
        self.play(GrowFromEdge(s3,
                               DOWN))
        self.play(GrowFromEdge(s4,
                               DOWN))
        self.play(GrowFromEdge(s5,
                               DOWN))
        self.play(Create(sb))
        
        self.play(s1.animate.shift(UP*1),
                  s2.animate.shift(UP*1),
                  s3.animate.shift(UP*1),
                  s4.animate.shift(UP*1),
                  s5.animate.shift(UP*1),
                  sb.animate.shift(UP*1),
                  )
        self.play(Write(introt))


        # Fade Out Unneeded Mobjects 

        self.play(Transform(s1,
                            s2,),
                            FadeOut(s1),
                            Transform(s2,
                                      s3),
                                      FadeOut(s2),
                                      Transform(s3,
                                                s4),
                                                FadeOut(s3),
                                                Transform(s4,
                                                          s5),
                                                          FadeOut(s4),
                                                          FadeOut(s5))
        
        # Transform Into Title 

        l1_start = (-6.1,
                    2.9,
                    0)
        l1_end = (6.1,
                  2.9,
                  0)
        line = Line(l1_start,l1_end)


        title = Title("Isaac Newton",
                      include_underline = False)
                      
        self.play(Transform(introt,
                            title),
                            ReplacementTransform(sb,
                                                 line))

        # Early Life

        # Title Text

        p1text = Text("Early Life").scale(3)

        self.play(Write(p1text))

        # Transform Into Info 

        bdatetext = Text("Birth Date: 2/2/34",
                                            ).shift(UP*1.5, LEFT*3)
        ddatetext = Text("Death Date: 2/3/34").next_to(bdatetext,DOWN)
        edutextl1 = Text("Education: Trinity College (1668").next_to(ddatetext,DOWN)

        self.play(Transform(p1text[0:3],
                            bdatetext),
                            Transform(p1text[3:6],
                            ddatetext),
                            Transform(p1text[6:9],
                            edutextl1))


        self.play
        
        
        self.wait(30)



        
    
        

