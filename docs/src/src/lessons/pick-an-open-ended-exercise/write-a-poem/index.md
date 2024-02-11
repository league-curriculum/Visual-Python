---
title: Write A Poem

---


Since Tina knows how to write words on the screen, you can teach her to write a poem.  This example provides you with a `line()` function to write lines of poetry and a `by()` function to list yourself as the author!

<iframe width="100%" height="500" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0Atina.penup%28%29%0A%0Adef%20line%28words%2C%20horiz_pos%20%3D%20-50%29%3A%0A%20%20%20%20x%2Cy%20%3D%20tina.pos%28%29%0A%20%20%20%20tina.goto%28max%28horiz_pos%2C%20-190%29%2C%20y%29%0A%20%20%20%20tina.write%28words%29%0A%20%20%20%20x%2Cy%20%3D%20tina.pos%28%29%0A%20%20%20%20tina.goto%28x%2C%20y%20-%2025%29%0A%20%20%20%20%0Adef%20by%28author%29%3A%0A%20%20%20%20x%2Cy%20%3D%20tina.pos%28%29%0A%20%20%20%20tina.goto%28x%20%2B%2070%2C%20max%28%20-190%2C%20y%20-30%29%29%0A%20%20%20%20tina.write%28author%29%0A%20%20%20%20x%2Cy%20%3D%20tina.pos%28%29%0A%20%20%20%20tina.goto%280%2C%20y%29%0A%20%20%20%20%0Atina.goto%28-50%2C%20190%29%0Aline%28%22Snow%20in%20my%20shoe%22%29%0Aline%28%22Abandoned%22%29%0Aline%28%22Sparrow%27s%20nest%22%29%0Aby%28%22Jack%20Kerouac%22%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Keep working at it until the poem looks the way you want it to!  Then click the Share Button ( <i class="fa fa-share-alt"></i> ) to get a link or the Email button ( <i class="fa fa-envelope-o"></i> ) to send it to your friends, teacher, or parents!
 
Hints:
* You can start by replacing the `line()` calls in the existing program.
* If your poem needs more than three lines, add new `line()` function calls with the new lines in them.
* If you want to leave a blank line, use an empty string: `" "`
* If you need your lines to begin further to the left because they're too long, add a comma (`,`) and a negative number down to -200:

```python
line("This line will be far to the left", -190)
```

## Famous poems

Can't think of a poem?  Try putting in some lines from these famous poems and poem fragments.  You can **copy** and **paste** the lines instead of re-typing them.:

#### Emily Dickinson
"Hope" is the thing with feathers—  
That perches in the soul—  
And sings the tune without the words—  
And never stops—at all—  

And sweetest—in the Gale—is heard—  
And sore must be the storm—  
That could abash the little Bird  
That kept so many warm—  

I've heard it in the chillest land—  
And on the strangest Sea—  
Yet, never, in Extremity,  
It asked a crumb—of Me.   

#### Frederick Douglass
When it is finally ours, this freedom, this liberty, this beautiful  
and terrible thing, needful to man as air,     
usable as earth; when it belongs at last to all,   
when it is truly instinct, brain matter, diastole, systole,   
reflex action; when it is finally won; when it is more   
than the gaudy mumbo jumbo of politicians:   
this man, this Douglass, this former slave, this Negro   
beaten to his knees, exiled, visioning a world   
where none is lonely, none hunted, alien,   
this man, superb in love and logic, this man   
shall be remembered. Oh, not with statues’ rhetoric,   
not with legends and poems and wreaths of bronze alone,
but with the lives grown out of his life, the lives   
fleshing his dream of the beautiful, needful thing.


#### e.e. cummings

it may not always be so; and i say  
that if your lips,which i have loved,should touch  
another’s,and your dear strong fingers clutch  
his heart,as mine in time not far away;  
if on another’s face your sweet hair lay  
in such silence as i know,or such  
great writhing words as,uttering overmuch,  
stand helplessly before the spirit at bay;  

if this should be,i say if this should be—  
you of my heart,send me a little word;  
that i may go unto him,and take his hands,  
saying,Accept all happiness from me.  
Then shall i turn my face,and hear one bird  
sing terribly afar in the lost lands  

#### Federico Garcia Lorca

Cirio, candil,  
farol y luciérnaga.  
  
La constelación   
de la saeta.  
  
Ventanitas de oro   
tiemblan,   
y en la aurora se mecen   
cruces superpuestas.
  
Cirio, candil,   
farol y luciérnaga.  
 
