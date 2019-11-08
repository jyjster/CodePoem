'''

This program is for Arts && Code && Interacitivty's Project 3, Code Poetry 011.

By: Jordan Y. Jackson
Last Modified: 11/08/19, 12AM

REFERENCES

    INSPIRATION
        "All great changes are preceded by chaos" (Deepak Chopra).
    
        "Creation comes from chaos" (Hedda Martina Sola).
    
    CODE
        code for coding a fractal tree graphic in Python via turtle
        https://stackoverflow.com/questions/29154455/making-a-tree-using-turtle-that-is-right-side-up
    POEM
        my poem was inspired by this poem about chaos theory
        https://www.instagram.com/p/BtAQZ-eh_VF/?igshid=1hhj63ed9y5rf
        
    OTHER
        fractals
            https://en.wikipedia.org/wiki/Fractal
        
        chaos theory
            https://en.wikipedia.org/wiki/Chaos_theory
            
            butterfly efffect
                https://en.wikipedia.org/wiki/Butterfly_effect
                
        return statement in Python
              https://guide.freecodecamp.org/python/return-statement/
        
'''

# you are the turtle
import turtle as you

shell = you.Turtle()

# can't separate a turtle from its shell
    # similar to how you can't separate yourself/change/life/progress from chaos
turtle = ('body', 'shell')
try:
    turtle.pop()
except:
    print("can't separate")


# life is defined in terms of chaos
def life(chaos = 100):
    
    if chaos < 10:
        return "no chance for positive change"
      
        
    else: 
        
        on, check, yes = 30, 30, 60  
        struggle, fury, flames, burning = 0, 0, 0, 0
        
        fire = shell
        growth = fire
        import random
    
        sometimes_is_needed = [True, False][random.randint(0,1)]
        
        ['inhibitions', 'doubt', 'fear'].clear()
        
        fire.forward(chaos)
        
        ['regrets', 'debris'].clear()

        for moment in range(len('chaos')):
            flames += 1
            struggle *= 2
            fury += 1
            burning *= 2
        
        
        fire.right(check)
        less_chaos = chaos * 0.7
        

        life(less_chaos)
        
        fire.left(yes)
        life(less_chaos)
        
        ashes = fire
        grow = ashes
        
        grow.right(on)

        
        fire.backward(chaos)
        
        print("garden")
        
        return 
    



garden = shell

garden.left(90)

print(life())

# we look forward to how you grow
you.done()
print("done for now...")

