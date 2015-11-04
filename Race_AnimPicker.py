import maya.cmds as maya
from functools import partial

windowID='RacingEyeCtrl'
nameSpace=['Red:','Blue:','Green:','Yellow:','Purple:']



#unlock to lock
def lockEye(*arg):
	#print 'lock'
	selectobj=maya.ls(sl=True)
	for obj in selectobj:
		if obj == 'cc_l_eyeball01' or obj =='cc_r_eyeball01':
			pos=maya.xform(obj,q=True,t=True,ws=True)
			rot=maya.xform(obj,q=True,ro=True,ws=True)
			maya.setAttr(obj+'.EyepositionLock',1)
			print pos
			print rot
			maya.move(pos[0],pos[1],pos[2],obj,a=True,ws=True)
			maya.rotate(rot[0],rot[1],rot[2],obj,a=True,ws=True)
		else:
			maya.warning('please select "cc_r_eyeball01" or "cc_r_eyeball01" to lock the control')

#lock to unlock			
def UnlockEye(*arg):
	#print 'Unlock'
	selectobj=maya.ls(sl=True)
	for obj in selectobj:
		if obj == 'cc_l_eyeball01' or obj =='cc_r_eyeball01':
			pos=maya.xform(obj,q=True,t=True,ws=True)
			rot=maya.xform(obj,q=True,ro=True,ws=True)
			maya.setAttr(obj+'.EyepositionLock',0)
			print pos
			print rot
			maya.move(pos[0],pos[1],pos[2],obj,a=True,ws=True)
			maya.rotate(rot[0],rot[1],rot[2],obj,a=True,ws=True)
		else:
			maya.warning('please select "cc_r_eyeball01" or "cc_r_eyeball01" to lock the control')


def l_followRoot(*arg):
	#cc_IK_l_stalk_a01
	pos_e01=maya.xform('cc_IK_l_stalk_e01',q=True,rp=True,ws=True)
	rot_e01=maya.xform('cc_IK_l_stalk_e01',q=True,ro=True,ws=True)
	rot_a01=maya.xform('cc_IK_l_stalk_a01',q=True,ro=True,ws=True)
	maya.setAttr('cc_body_rotate01.l_stalk_follow',1)
	maya.rotate(rot_a01[0],rot_a01[1],rot_a01[2],'cc_IK_l_stalk_a01',a=True,ws=True)
	maya.rotate(rot_e01[0],rot_e01[1],rot_e01[2],'cc_IK_l_stalk_e01',a=True,ws=True)
	maya.move(pos_e01[0],pos_e01[1],pos_e01[2],'cc_IK_l_stalk_e01',a=True,ws=True,rpr=True)



def l_followWorld(*arg):
	#cc_IK_r_stalk_a01
	pos_e01=maya.xform('cc_IK_l_stalk_e01',q=True,rp=True,ws=True)
	rot_e01=maya.xform('cc_IK_l_stalk_e01',q=True,ro=True,ws=True)
	rot_a01=maya.xform('cc_IK_l_stalk_a01',q=True,ro=True,ws=True)
	#rot_01=maya.xform('cc_l_eyeball01',q=True,ro=True,ws=True)
	maya.setAttr('cc_body_rotate01.l_stalk_follow',0)
	maya.rotate(rot_a01[0],rot_a01[1],rot_a01[2],'cc_IK_l_stalk_a01',a=True,ws=True)
	maya.rotate(rot_e01[0],rot_e01[1],rot_e01[2],'cc_IK_l_stalk_e01',a=True,ws=True)
	maya.move(pos_e01[0],pos_e01[1],pos_e01[2],'cc_IK_l_stalk_e01',a=True,ws=True,rpr=True)


def r_followRoot(*arg):
	#cc_IK_r_stalk_a01
	pos_e01=maya.xform('cc_IK_r_stalk_e01',q=True,rp=True,ws=True)
	rot_e01=maya.xform('cc_IK_r_stalk_e01',q=True,ro=True,ws=True)
	rot_a01=maya.xform('cc_IK_r_stalk_a01',q=True,ro=True,ws=True)
	maya.setAttr('cc_body_rotate01.r_stalk_follow',1)
	maya.rotate(rot_e01[0],rot_e01[1],rot_e01[2],'cc_IK_r_stalk_e01',a=True,ws=True)
	maya.rotate(rot_a01[0],rot_a01[1],rot_a01[2],'cc_IK_r_stalk_a01',a=True,ws=True)
	maya.move(pos_e01[0],pos_e01[1],pos_e01[2],'cc_IK_r_stalk_e01',a=True,ws=True,rpr=True)


def r_followWorld(*arg):
	#cc_IK_r_stalk_a01
	pos_e01=maya.xform('cc_IK_r_stalk_e01',q=True,rp=True,ws=True)
	rot_e01=maya.xform('cc_IK_r_stalk_e01',q=True,ro=True,ws=True)
	rot_a01=maya.xform('cc_IK_r_stalk_a01',q=True,ro=True,ws=True)
	maya.setAttr('cc_body_rotate01.r_stalk_follow',0)
	maya.rotate(rot_e01[0],rot_e01[1],rot_e01[2],'cc_IK_r_stalk_e01',a=True,ws=True)
	maya.rotate(rot_a01[0],rot_a01[1],rot_a01[2],'cc_IK_r_stalk_a01',a=True,ws=True)
	maya.move(pos_e01[0],pos_e01[1],pos_e01[2],'cc_IK_r_stalk_e01',a=True,ws=True,rpr=True)


def quickselection(controller,*arg):
	global nameSpace
	row1=cmds.radioButtonGrp('row1',q=True,sl=True)
	row2= cmds.radioButtonGrp('row2',q=True,sl=True)
	if (row2==3):
		loadednamespace=''
		if(maya.objExists(loadednamespace+controller)):
			maya.select(loadednamespace+controller)
		else:
			maya.warning('Object '+loadednamespace+controller+'does not exist');
		return
	if (row1==0):
		loadednamespace=nameSpace[row2+2]
		print loadednamespace
		if(maya.objExists('loadednamespace+controller')):
			maya.select(loadednamespace+controller)
		else:
			maya.warning('Object '+loadednamespace+controller+'does not exist');
		return
	else:
		loadednamespace=nameSpace[row1-1]
		print loadednamespace
		if(maya.objExists('loadednamespace+controller')):
			maya.select(loadednamespace+controller)
		else:
			maya.warning('Object '+loadednamespace+controller+'does not exist');
		return

def Racing_pannel():

    maya.window(windowID, widthHeight=(420, 900), title='Racing Character Helper',s=True,rtf=True)
    maya.columnLayout(h=890)
    maya.text(l='Racing Character quickselection',w=420,al='center',fn='boldLabelFont')
    maya.setParent('..')
    maya.columnLayout(h=10)
    maya.setParent('..')
    windowform=maya.formLayout('windowform')
    mytab=maya.tabLayout(innerMarginWidth=10, innerMarginHeight=10)
    maya.formLayout(windowform,e=True,af=[(mytab,'left',10),(mytab,'right',10)])
    maya.columnLayout('Rig_Body',w=400,h=650)
    tabform=maya.formLayout()
    prefpath=maya.internalVar(upd=True)
    print prefpath
    maya.image(image=prefpath+'icons/CharacterRig_Background.png')
    #Control buttons
    cc_IK_r_stalk_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_IK_r_stalk_a01',c=partial(quickselection,'cc_IK_r_stalk_a01'))
    cc_r_pos_stalk01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_pos_stalk01',c=partial(quickselection,'cc_r_pos_stalk01'))
    cc_r_stalkbend01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkbend01',c=partial(quickselection,'cc_r_stalkbend01'))
    cc_IK_r_stalk_e01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_IK_r_stalk_e01',c=partial(quickselection,'cc_IK_r_stalk_e01'))
    cc_r_stalkhand_Rotate01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand_Rotate01',c=partial(quickselection,'cc_r_stalkhand_Rotate01'))
    cc_r_eyeball01=maya.button(l='', w=60, h=60, al='center',bgc=(1,1,0),ann='cc_r_eyeball01',c=partial(quickselection,'cc_r_eyeball01'))
    cc_IK_l_stalk_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_IK_l_stalk_a01',c=partial(quickselection,'cc_IK_l_stalk_a01'))
    cc_l_pos_stalk01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_pos_stalk01',c=partial(quickselection,'cc_l_pos_stalk01'))
    cc_l_stalkbend01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkbend01',c=partial(quickselection,'cc_l_stalkbend01'))
    cc_IK_l_stalk_e01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_IK_l_stalk_e01',c=partial(quickselection,'cc_IK_l_stalk_e01'))
    cc_l_stalkhand_Rotate01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand_Rotate01',c=partial(quickselection,'cc_l_stalkhand_Rotate01'))
    cc_l_eyeball01=maya.button(l='', w=60, h=60, al='center',bgc=(0,0,1),ann='cc_l_eyeball01',c=partial(quickselection,'cc_l_eyeball01'))
    cc_body_rotate01=maya.button(l='', w=120, h=120, al='center',bgc=(1,0,0),ann='cc_body_rotate01',c=partial(quickselection,'cc_body_rotate01'))
    globalmove01=maya.button(l='', w=150, h=15, al='center',bgc=(1,0,0),ann='globalmove01',c=partial(quickselection,'globalmove01'))
    cc_l_eyeIris01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_eyeIris01',c=partial(quickselection,'cc_l_eyeIris01'))
    cc_r_eyeIris01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_eyeIris01',c=partial(quickselection,'cc_r_eyeIris01'))
    cc_IKFK01=maya.button(l='', w=20, h=20, al='center',bgc=(1,0,0),ann='cc_IKFK01',c=partial(quickselection,'cc_IKFK01'))

    cc_tail_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,0,0),ann='cc_tail_a01',c=partial(quickselection,'cc_tail_a01'))
    cc_tail_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,0,0),ann='cc_tail_b01',c=partial(quickselection,'cc_tail_b01'))
    cc_tail_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,0,0),ann='cc_tail_c01',c=partial(quickselection,'cc_tail_c01'))
    cc_autotail01=maya.button(l='', w=20, h=20, al='center',bgc=(1,0,0),ann='cc_autotail01',c=partial(quickselection,'cc_autotail01'))

    #FKcontrol
    cc_FK_l_stalk_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_FK_l_stalk_a01',c=partial(quickselection,'cc_FK_l_stalk_a01'))
    cc_FK_l_stalk_b01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_FK_l_stalk_b01',c=partial(quickselection,'cc_FK_l_stalk_b01'))
    cc_FK_l_stalk_c01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_FK_l_stalk_c01',c=partial(quickselection,'cc_FK_l_stalk_c01'))
    cc_FK_l_stalk_d01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_FK_l_stalk_d01',c=partial(quickselection,'cc_FK_l_stalk_d01'))
    cc_FK_l_stalk_e01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_FK_l_stalk_e01',c=partial(quickselection,'cc_FK_l_stalk_e01'))

    cc_FK_r_stalk_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_FK_r_stalk_a01',c=partial(quickselection,'cc_FK_r_stalk_a01'))
    cc_FK_r_stalk_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_FK_r_stalk_b01',c=partial(quickselection,'cc_FK_r_stalk_b01'))
    cc_FK_r_stalk_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_FK_r_stalk_c01',c=partial(quickselection,'cc_FK_r_stalk_c01'))
    cc_FK_r_stalk_d01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_FK_r_stalk_d01',c=partial(quickselection,'cc_FK_r_stalk_d01'))
    cc_FK_r_stalk_e01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_FK_r_stalk_a01',c=partial(quickselection,'cc_FK_r_stalk_e01'))


    #End
    #Positioning the button
    maya.formLayout(tabform,e=True,ap=[(cc_IK_l_stalk_a01,'left',-20,50),(cc_IK_l_stalk_a01,'top',0,52)])
    maya.formLayout(tabform,e=True,ap=[(cc_l_pos_stalk01,'left',-25,50),(cc_l_pos_stalk01,'top',0,55)])
    maya.formLayout(tabform,e=True,ap=[(cc_IK_r_stalk_a01,'right',-5,31),(cc_IK_r_stalk_a01,'top',0,52)])
    maya.formLayout(tabform,e=True,ap=[(cc_r_pos_stalk01,'right',-6,31),(cc_r_pos_stalk01,'top',0,55)])
    maya.formLayout(tabform,e=True,ap=[(cc_body_rotate01,'left',0,28),(cc_body_rotate01,'top',0,65)])
    maya.formLayout(tabform,e=True,ap=[(globalmove01,'left',5,24),(globalmove01,'top',0,95)])
    maya.formLayout(tabform,e=True,ap=[(cc_l_stalkbend01,'left',2,50),(cc_l_stalkbend01,'top',0,40)])
    maya.formLayout(tabform,e=True,ap=[(cc_IK_l_stalk_e01,'left',20,52),(cc_IK_l_stalk_e01,'top',0,27)])
    maya.formLayout(tabform,e=True,ap=[(cc_r_stalkbend01,'right',-2,28),(cc_r_stalkbend01,'top',0,40)])
    maya.formLayout(tabform,e=True,ap=[(cc_IK_r_stalk_e01,'right',137,50),(cc_IK_r_stalk_e01,'top',0,26)])
    maya.formLayout(tabform,e=True,ap=[(cc_l_stalkhand_Rotate01,'left',17,51),(cc_l_stalkhand_Rotate01,'top',2,30)])
    maya.formLayout(tabform,e=True,ap=[(cc_r_stalkhand_Rotate01,'left',0,21),(cc_r_stalkhand_Rotate01,'top',2,29)])

    maya.formLayout(tabform,e=True,ap=[(cc_l_eyeball01,'left',10,50),(cc_l_eyeball01,'top',0,11)])
    maya.formLayout(tabform,e=True,ap=[(cc_r_eyeball01,'right',120,50),(cc_r_eyeball01,'top',0,11)])

    maya.formLayout(tabform,e=True,ap=[(cc_l_eyeIris01,'left',0,56),(cc_l_eyeIris01,'top',1,5)])
    maya.formLayout(tabform,e=True,ap=[(cc_r_eyeIris01,'left',0,19),(cc_r_eyeIris01,'top',1,5)])

    maya.formLayout(tabform,e=True,ap=[(cc_IKFK01,'left',0,37),(cc_IKFK01,'top',0,90)])
    maya.formLayout(tabform,e=True,ap=[(cc_tail_a01,'left',0,56),(cc_tail_a01,'top',0,90)])
    maya.formLayout(tabform,e=True,ap=[(cc_tail_b01,'left',0,62),(cc_tail_b01,'top',0,90)])
    maya.formLayout(tabform,e=True,ap=[(cc_tail_c01,'left',0,68),(cc_tail_c01,'top',0,90)])
    maya.formLayout(tabform,e=True,ap=[(cc_autotail01,'left',0,62),(cc_autotail01,'top',0,85)])

    maya.formLayout(tabform,e=True,ap=[(cc_FK_l_stalk_a01,'left',0,65),(cc_FK_l_stalk_a01,'top',0,28)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_l_stalk_b01,'left',0,65),(cc_FK_l_stalk_b01,'top',0,34)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_l_stalk_c01,'left',0,65),(cc_FK_l_stalk_c01,'top',0,40)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_l_stalk_d01,'left',0,65),(cc_FK_l_stalk_d01,'top',0,46)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_l_stalk_e01,'left',0,65),(cc_FK_l_stalk_e01,'top',0,52)])

    maya.formLayout(tabform,e=True,ap=[(cc_FK_r_stalk_a01,'left',0,10),(cc_FK_r_stalk_a01,'top',0,28)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_r_stalk_b01,'left',0,10),(cc_FK_r_stalk_b01,'top',0,34)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_r_stalk_c01,'left',0,10),(cc_FK_r_stalk_c01,'top',0,40)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_r_stalk_d01,'left',0,10),(cc_FK_r_stalk_d01,'top',0,46)])
    maya.formLayout(tabform,e=True,ap=[(cc_FK_r_stalk_e01,'left',0,10),(cc_FK_r_stalk_e01,'top',0,52)])
    #End
    maya.setParent('..')
    maya.setParent('..')
    righand=maya.columnLayout('Rig_Hand',w=400,h=650)
    tabform01=maya.formLayout()
   	#prefpath=maya.internalVar(upd=True)
    maya.image(image=prefpath+'icons/CharacterHand_Background.png')
    cc_l_stalkhand01_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand01_a01',c=partial(quickselection,'cc_l_stalkhand01_a01'))
    cc_l_stalkhand01_b01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand01_b01',c=partial(quickselection,'cc_l_stalkhand01_b01'))
    cc_l_stalkhand01_c01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand01_c01',c=partial(quickselection,'cc_l_stalkhand01_c01'))

    cc_l_stalkhand02_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand02_a01',c=partial(quickselection,'cc_l_stalkhand02_a01'))
    cc_l_stalkhand02_b01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand02_b01',c=partial(quickselection,'cc_l_stalkhand02_b01'))
    cc_l_stalkhand02_c01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand02_c01',c=partial(quickselection,'cc_l_stalkhand02_c01'))

    cc_l_stalkhand03_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand03_a01',c=partial(quickselection,'cc_l_stalkhand03_a01'))
    cc_l_stalkhand03_b01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand03_b01',c=partial(quickselection,'cc_l_stalkhand03_b01'))
    cc_l_stalkhand03_c01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand03_c01',c=partial(quickselection,'cc_l_stalkhand03_c01'))

    cc_l_stalkhand04_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand04_a01',c=partial(quickselection,'cc_l_stalkhand04_a01'))
    cc_l_stalkhand04_b01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand04_b01',c=partial(quickselection,'cc_l_stalkhand04_b01'))
    cc_l_stalkhand04_c01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand04_c01',c=partial(quickselection,'cc_l_stalkhand04_c01'))

    cc_l_stalkhand05_a01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand05_a01',c=partial(quickselection,'cc_l_stalkhand05_a01'))
    cc_l_stalkhand05_b01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand05_b01',c=partial(quickselection,'cc_l_stalkhand05_b01'))
    cc_l_stalkhand05_c01=maya.button(l='', w=20, h=20, al='center',bgc=(0,0,1),ann='cc_l_stalkhand05_c01',c=partial(quickselection,'cc_l_stalkhand05_c01'))


    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand01_a01,'left',0,48),(cc_l_stalkhand01_a01,'top',0,24)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand01_b01,'left',0,48),(cc_l_stalkhand01_b01,'top',0,19)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand01_c01,'left',0,48),(cc_l_stalkhand01_c01,'top',0,13)])

    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand02_a01,'left',5,53),(cc_l_stalkhand02_a01,'top',2,26)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand02_b01,'left',0,62),(cc_l_stalkhand02_b01,'top',5,24)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand02_c01,'left',0,70),(cc_l_stalkhand02_c01,'top',2,23)])

    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand03_a01,'left',0,52),(cc_l_stalkhand03_a01,'top',0,31)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand03_b01,'left',0,57),(cc_l_stalkhand03_b01,'top',0,35)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand03_c01,'left',2,61),(cc_l_stalkhand03_c01,'top',0,39)])

    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand04_a01,'left',0,44),(cc_l_stalkhand04_a01,'top',0,31)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand04_b01,'left',0,39),(cc_l_stalkhand04_b01,'top',0,35)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand04_c01,'left',0,35),(cc_l_stalkhand04_c01,'top',0,39)])

    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand05_a01,'left',0,42),(cc_l_stalkhand05_a01,'top',2,26)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand05_b01,'left',0,34),(cc_l_stalkhand05_b01,'top',6,24)])
    maya.formLayout(tabform01,e=True,ap=[(cc_l_stalkhand05_c01,'left',0,26),(cc_l_stalkhand05_c01,'top',2,23)])



    cc_r_stalkhand01_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand01_a01',c=partial(quickselection,'cc_r_stalkhand01_a01'))
    cc_r_stalkhand01_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand01_b01',c=partial(quickselection,'cc_r_stalkhand01_b01'))
    cc_r_stalkhand01_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand01_c01',c=partial(quickselection,'cc_r_stalkhand01_c01'))

    cc_r_stalkhand02_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand02_a01',c=partial(quickselection,'cc_r_stalkhand02_a01'))
    cc_r_stalkhand02_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand02_b01',c=partial(quickselection,'cc_r_stalkhand02_b01'))
    cc_r_stalkhand02_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand02_c01',c=partial(quickselection,'cc_r_stalkhand02_c01'))

    cc_r_stalkhand03_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand03_a01',c=partial(quickselection,'cc_r_stalkhand03_a01'))
    cc_r_stalkhand03_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand03_b01',c=partial(quickselection,'cc_r_stalkhand03_b01'))
    cc_r_stalkhand03_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand03_c01',c=partial(quickselection,'cc_r_stalkhand03_c01'))

    cc_r_stalkhand04_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand04_a01',c=partial(quickselection,'cc_r_stalkhand04_a01'))
    cc_r_stalkhand04_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand04_b01',c=partial(quickselection,'cc_r_stalkhand04_b01'))
    cc_r_stalkhand04_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand04_c01',c=partial(quickselection,'cc_r_stalkhand04_c01'))

    cc_r_stalkhand05_a01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand05_a01',c=partial(quickselection,'cc_r_stalkhand05_a01'))
    cc_r_stalkhand05_b01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand05_b01',c=partial(quickselection,'cc_r_stalkhand05_b01'))
    cc_r_stalkhand05_c01=maya.button(l='', w=20, h=20, al='center',bgc=(1,1,0),ann='cc_r_stalkhand05_c01',c=partial(quickselection,'cc_r_stalkhand05_c01'))


    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand01_a01,'left',0,48),(cc_r_stalkhand01_a01,'top',0,64)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand01_b01,'left',0,48),(cc_r_stalkhand01_b01,'top',0,59)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand01_c01,'left',0,48),(cc_r_stalkhand01_c01,'top',0,53)])

    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand02_a01,'left',5,53),(cc_r_stalkhand02_a01,'top',2,66)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand02_b01,'left',0,62),(cc_r_stalkhand02_b01,'top',5,64)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand02_c01,'left',0,70),(cc_r_stalkhand02_c01,'top',2,63)])

    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand03_a01,'left',0,52),(cc_r_stalkhand03_a01,'top',0,71)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand03_b01,'left',0,57),(cc_r_stalkhand03_b01,'top',0,75)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand03_c01,'left',2,61),(cc_r_stalkhand03_c01,'top',0,79)])

    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand04_a01,'left',0,44),(cc_r_stalkhand04_a01,'top',0,71)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand04_b01,'left',0,39),(cc_r_stalkhand04_b01,'top',0,75)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand04_c01,'left',0,35),(cc_r_stalkhand04_c01,'top',0,79)])

    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand05_a01,'left',0,42),(cc_r_stalkhand05_a01,'top',2,66)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand05_b01,'left',0,34),(cc_r_stalkhand05_b01,'top',6,64)])
    maya.formLayout(tabform01,e=True,ap=[(cc_r_stalkhand05_c01,'left',0,26),(cc_r_stalkhand05_c01,'top',2,63)])

    maya.setParent('..')
    maya.setParent('..')
    maya.setParent('..')
    maya.setParent('..')
    maya.columnLayout(h=5)
    maya.setParent('..')
    #maya.setParent('..')
    #back to the root layout
    maya.separator(w=420,st='in')
    windowlayout=maya.columnLayout('secondblock',w=420,h=700,rs=5)
    maya.text(l='Character Selection and NameSpace Management',w=420,al='center',fn='boldLabelFont')
    maya.columnLayout(w=400,cat=('left',60))
    grp_radioButton01 = cmds.radioButtonGrp('row1',numberOfRadioButtons=3,labelArray3=['Red', 'Blue', 'Green'],cal=[1,'center'])
    grp_radioButton02 = cmds.radioButtonGrp('row2',numberOfRadioButtons=3, shareCollection=grp_radioButton01,labelArray3=['Yellow', 'Purple', 'None'],sl=3)
    maya.setParent('..')
    maya.separator(w=420,st='in')
    maya.text(l='Extra Control',w=420,al='center',fn='boldLabelFont')
    form=maya.formLayout()
    layout1=maya.columnLayout(w=200, h=100, cat=('left', 20),rs=5)
    maya.text(l='Eye Lock/Unlock',al='center',w=200,fn='boldLabelFont') 
    maya.button(l='Lock', w=160, h=30, al='center',c=lockEye)
    maya.button(l='Unlock', w=160, h=30, al='center',c=UnlockEye)
    maya.setParent('..')
    layout2=maya.columnLayout(w=200,h=100,rs=10)
    maya.text(l='Body Root/World',al='center',w=200,fn='boldLabelFont')
    maya.rowColumnLayout(w=200, h=25, nr=1,cs=[1,5],cat=[1,'left',20])
    maya.text(l='left stalk:',al='left',w=50,fn='boldLabelFont')
    maya.button(l='Root', w=50, h=20, al='center',c=l_followRoot)
    maya.button(l='World', w=50, h=20, al='center',c=l_followWorld)
    maya.setParent('..')
    maya.rowColumnLayout(w=200, h=20, nr=1,cs=[1,5],cat=[1,'left',15])
    maya.text(l='right stalk:',al='left',w=55,fn='boldLabelFont')
    maya.button(l='Root', w=50, h=20, al='center',c=r_followRoot)
    maya.button(l='World', w=50, h=20, al='center',c=r_followWorld)
    maya.setParent('..')
    maya.formLayout(form,e=True,ac=[layout2,'left',5,layout1])
    maya.showWindow(windowID)



def controlgui():
    if (maya.window(windowID, ex=True)):
        maya.deleteUI(windowID, wnd=True)
    Racing_pannel()

controlgui()

