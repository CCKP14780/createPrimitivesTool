import maya.cmds as cmds

def primsTool():
    if cmds.window('primsTool',q=True,ex=True):
        cmds.deleteUI('primsTool',window=True)
        
    cmds.window('primsTool',title='Primitive Tool')
########################################################
    cmds.frameLayout(label='Primitives')
    
    cmds.columnLayout(adj=True)
    cmds.iconTextRadioCollection('prims_radioCollection')
    cmds.iconTextRadioButton('cube_radioButton',label='cube',i = 'cube.png')
    cmds.iconTextRadioButton('sphere_radioButton',label='sphere',i = 'sphere.png')
    cmds.iconTextRadioButton('cone_radioButton',label='cone',i = 'cone.png')
    
    cmds.button(l = 'Create', h = 30,c=createPrims)
########################################################
    cmds.showWindow('primsTool')
    cmds.window('primsTool',e=True,wh=[300,300])
########################################################    

def createPrims(*args):
    primCol = cmds.iconTextRadioCollection('prims_radioCollection',q=True,sl=True)#eg. cube_radioButton
    prim = primCol.split('_')[0]#(from eg.)you will get prim =['cube','radiobutton']
    # ==>prim[0] = 'cube'
    
    if prim =='cube':
        cmds.polyCube()

    elif prim =='sphere':
        cmds.polySphere()    

    elif prim =='cone':
        cmds.polyCone()

primsTool()