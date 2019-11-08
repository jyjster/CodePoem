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

#NEW
beauty, vibrancy, strength, resiliency = 0, 0, 0, 0

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
        # before the fire, initializing variables
        on, check, yes = 30, 30, 60  
        struggle, fury, flames, burning = 0, 0, 0, 0
        
        # fire begins
        fire = shell
        
         # growth is fire / growth is like fire
        growth = fire
        
         # sometimes it's needed
        import random
        sometimes_is_needed = [True, False][random.randint(0,1)]
        
        # don't fear it or run away
        ['inhibitions', 'doubt', 'fear'].clear()
        
        # go forward into the fire, into the chaos
        fire.forward(chaos)
        
        # clear out any debris
        ['regrets', 'debris'].clear()

        # NEW
        seeds = 0
        
        # you struggle, it burns. it will hurt and there will be pain.
                   # the longer the fire, the more pain
                   # planting the seeds for what's to come / what comes next        
        for moment in range(len('chaos')):
            flames += 1
            struggle *= 2
            fury += 1
            burning *= 2
            
        seeds = chaos * (beauty + vibrancy + strength + resiliency)
        
        # the fire was meant to happen
        fire.right(check)
        
        # the fire dies down, the chaos also
        less_chaos = chaos * 0.7
        
        # life returns to a period of
        life(less_chaos)
        
        # the fire is done for now. it has has gone/left. the fire has ran its course
        fire.left(yes)
        life(less_chaos)
        
        # ashes are remaining
        ashes = fire
        # the ashes have new life
        grow = ashes
        
        # from the ashes/seeds you grow
        grow.right(on)

        # NEW 
        garden = seeds + grow
        
        # you go back to/visit where you were before the chaos/fire
        fire.backward(chaos)
        
        # but return as a garden
            # you emerge from ashes stronger, wiser, older, more resilient than before
            # beauty + vibrancy + strength + resiliency        
        
        # return 
        
        # NEW
        
        return garden
    



garden = shell

garden.left(90)

print(life())

# we look forward to how you grow
you.done()
print("done for now...")

