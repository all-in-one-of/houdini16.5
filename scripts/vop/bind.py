import hou
bind=[]
for i in kwargs['node'].parent().children():
	if i.type().description() == 'Bind':
		if i.parm('parmname').eval() == 'parm':
			bind.append(i)
if len(bind)<2:
	kwargs['node'].parm('overridetype').set(1)
	kwargs['node'].parm('useasparmdefiner').set(1)
	kwargs['node'].parm('exportparm').set(1)
	baby = kwargs['node'].createOutputNode('bind')
	baby.parm('parmname').set("`chs('../{0}/parmname')`".format(kwargs['node'].name()))
	baby.parm('overridetype').set(1)
	baby.parm('useasparmdefiner').set(1)
	baby.parm('exportparm').set(1)
	baby.moveToGoodPosition()