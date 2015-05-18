
light_groups=#($a,$b,$c,$d,$e,$f,$g,$h,$j,$k,$l,$'l-1',$'l-2',$m,$n,$o,$sl,$td)--$i,



--"GAPL4T3__28", "Green accent G2 4000lm 3000K MB.ies"

fn disableAllMat mat:meditMaterials[24]=
(
	for i in 1 to mat.names.count do
	(
		mat.mapEnabled[i]=off
	)	

)

------------------------------------------------------------------------------------------------------
------------------------------------------TO DO Color Setting-----------------------------------------
------------------------------------------------------------------------------------------------------
const_color=color 255 184 109 -- corresponding to CCT_Default


fn turnMat mat:meditMaterials[24] mat_Name:"a" state:on =
(

	for i in 1 to mat.names.count do
	(
		if mat.names[i]==mat_Name do
		(
			mat.mapEnabled[i] = state
			if state==on then
			(
				mat.materialList[i].multiplier = 1
				
				)
			else
			(
				mat.materialList[i].multiplier = 0
				)
		)
	)

)

------------------------------------------------------------------------------------------------------
------------------------------------------TO DO Color Setting-----------------------------------------
------------------------------------------------------------------------------------------------------

fn checkMat mat:meditMaterials[24] mat_Name:"a" state:on clr:const_color =
(

	for i in 1 to mat.names.count do
	(
		if mat.names[i]==mat_Name do
		(
			mat.mapEnabled[i] = state
			mat.materialList[i].color = clr
			if state==on then
			(
				mat.materialList[i].multiplier = 1
				)
			else
			(
				mat.materialList[i].multiplier = 0
				)
			
		)
	)

)


fn switch_one lightgroup state:on= 
(
	if lightgroup == undefined then
	(
		print "undefined"
	)
	else
	(
		
		
		turnMat mat:meditMaterials[24] mat_Name:lightgroup.name state:state

		
		for lt in lightgroup.children do
	(
		
		if lt==undefined then
			continue
			
		
		if classof lt == Free_Light then
		(
			lt.on = state
			
		)

			
		if classof lt == VrayIES then
		(
			lt.enabled = state
		)
			
				
		if classof lt == VrayLight then
		(
			lt.on = state
		)
		
		if classof lt == Free_Area then
		(
			
			lt.on = state
			
		)
		
			
	)
		
		)
	

)


fn switch_all lgs:light_groups state:on=
(
	for lightgroup in lgs do
		
	(	
		if lightgroup==undefined then
		(
			
			continue
			
			)
		else
		(
			switch_one lightgroup state: state
		)
	)
)

fn set_one lightgroup state:on cct:5000 ies:""=
(
	if lightgroup==undefined then
	(
		return 0
	)
	else
	(
		division=64
		
		--=====================================================================================================TO CCT 2 COLOR here
		
		checkMat mat:meditMaterials[24] mat_Name:lightgroup.name state:state clr:const_color
		
		for lt in lightgroup.children do
		(
			
			if classof lt == Free_Light then
			(
				lt.on = state
				lt.useKelvin = on
				lt.kelvin = cct
				if ies!="" do
				(
					lt.webfile = ies
				)
				lt.subdivs = division

				continue
			)

				
			if classof lt == VrayIES then
			(
				lt.enabled = state
				if ies!="" do
				(
					lt.ies_file= ies
				)
				
				lt.shape_subdivs = division
				lt.color_mode = 1
				lt.color_temperature = CCT
				continue
			)
				
					
			if classof lt == VrayLight then
			(
				lt.on = state
				lt.subdivs = division

				continue
			)
			
			if classof lt == Free_Area then
			(
				lt.on = state
				lt.useKelvin = on
				lt.kelvin = cct
				if ies!="" do
				(
					lt.webfile = ies
				)
				lt.baseObject.Area_Light_Sampling_Custom_Attribute.mr_NumAreaSamples = division
				continue
				
			)
			
		)
	)

)

fn set_all lgs:light_groups state:on cct:5000 ies:""= 
(
	for lightgroup in lgs do
	(
		if lightgroup==undefined then
		(
			print "undefined"
		)
		else
		(
		
		set_one lightgroup state: state cct:cct ies:ies
		)
	)
)

--set_all  lgs:light_groups state:on cct:5000 ies:""


fn CreateCameras=
(
	nrange=0
	frange=1000
	tDistance=160
	fov=90

	frontCam=Freecamera fov:fov Name:"_fr" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on 
	rotate frontCam (angleaxis 90.0 [1,0,0])
	rotate frontCam (angleaxis -180 [0,0,1])

	backCam=Freecamera fov:fov Name:"_bk" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on 
	rotate backCam (angleaxis 90.0 [1,0,0])


	leftCam=Freecamera fov:fov Name:"_lf" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on
	rotate leftCam (angleaxis 90.0 [1,0,0])
	rotate leftCam (angleaxis 90.0 [0,0,1])
	rightCam=Freecamera fov:fov Name:"_rt" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on
	rotate rightCam(angleaxis 90.0 [1,0,0])
	rotate rightCam(angleaxis -90.0 [0,0,1])

	upCam=Freecamera fov:fov Name:"_up" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on 
	rotate upCam (angleaxis 180 [1,0,0])

	downCam=Freecamera fov:fov Name:"_dn" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on
	print "Finish creating cameras."

	FaceCamGroup=group #(frontCam,backCam,leftCam,rightCam,upCam,downCam) name:"FaceCameras"
	
	return FaceCamGroup
)

fn RenderAtCam faceCameras:#($Camera001) filePath:"\\\Cnhshaker4dtzzz\\gucci\\result\\" width:1024 height:1024 fmt:".png" gma:1.0 test:0=
(
	--faceCameras.position=cam.position
	if faceCameras==undefined then
	(
		return 0
	)
	for faceCam in faceCameras.children do --SCENE
	(
		if classof faceCam ==Freecamera then
		(
			str="prepare to render, viewpoint:"+faceCameras.name
			fileFull=filePath+"_"+faceCam.name+"_"+(gma as string)+fmt
			print str
			
			if test==0 do
			(
				bmp1=bitmap width height filename:fileFull gamma:gma pixelAspect:1.0
				render camera:faceCam to:bmp1
				save bmp1	
			)
			if test==2 do
			(
				bmp1=bitmap width height filename:fileFull gamma:gma pixelAspect:1.0
				render camera:faceCam to:bmp1
				save bmp1
				exit
			)
			if test==3 do
			(
				s="reder to:"+fileFull
				print s
			)
				--close bmp1
			
			outputStr="saved to file:"+filePath
			print outputStr
			--exit
		)
	)
	
	return 1
)



fn RenderCombination Root:"\\\Cnhshaker4dtzzz\\gucci\\" SceneCam:$Camera001 LG:#($LightGroup) LGIndex:0 ResultFolder:"result\\" IESFolder:"IES\\" IES:"" CCT:3000 Resolution:512 testPrint:0 =
(
	-- set lights parameters and turn all the lights on
	sep="_"
	iesFullPath=Root+IESFolder+IES
	subdiv=32
	print "Turn on light Group"
	
	
	for gr in LG do
	(
		set_one gr state:on cct:CCT ies:IES
	)
	--render 
	--filePrePath=Root+ResultFolder+SceneCam.name+sep+LG.name+sep+IES
	filePrePath=Root+ResultFolder+SceneCam.name+sep+LGIndex as string +sep+IES+sep
	print filePrePath
	RenderAtCam faceCameras:SceneCam filePath:filePrePath width:Resolution height:Resolution fmt:".png" gma:1.0 test:testPrint
	
	print "Turn off light Group"
	
	for gr in LG do
	(
		switch_one gr state:off
	)
	
)


group1=#($c,$d,$f)
group2=#($a)
group3=#($b,$m,$n)
group4=#($k,$g,$j)
group5=#()
group6=#($h)
group7=#($e)
group8=#($l,$'l-1',$'l-2')
group9=#($sl,$td,$o)


groups=#(group1,group2,group3,group4,group5,group6,group7,group8,group9)--group5,group10,group11

scene0=#(1,2,3,4,8)
scene1=#(1,2,3,4,9)
--scene1=#(3,4,9)
scene2=#(1,2,3,4,9)
scene3=#(1,2,3,4,7,9)
scene4=#(1,2,3,4,7,9)
scene5=#(6,7)

--scenes =#(scene0,scene1,scene2,scene3,scene4,scene5)
--scenes =#(scene2,scene3)
scenes =#(scene1)

viewPoints=#($FaceCameras001)
--viewPoints=#($FaceCameras,$FaceCameras001,$FaceCameras002,$FaceCameras003,$FaceCameras004,$FaceCameras005)

--viewPoints=#($FaceCameras001)

irreplace=#(3,4,6,7,8,9)
spotlight=#(1,2)
covelight=#(4)



fn hasObject arr item=
(
	for v in arr do
	(
		if item == v do
		(
			return true
			
			)
		
		)
	
	return false
)
	
--define const varialbes-----------------------------------------------------------------------------------------------------------------------------------------


--viewPoints=#($FaceCameras004,$FaceCameras005)

Root0="\\\Cnhshaker4dtzzz\\gucci\\"

result_folder="result\\"

ies_folder="IES\\"



product_names=#("GAPL4T3__18","GAPL4T3__38" ,"LSHPL3T3_" )
iesfiles=#("Green accent G2 4000lm 3000K NB.ies","Green accent G2 4000lm 3000K WB.ies","DN497 1xDLED830 UGR19 1xLGIT7030.ies")

sep="_"-- filepath seperator

outputSize=2048

CCT_Default=3000

--light Locations

fileFormat=".png"

--we dont create cameras anymore, the designer has done it for us now.
--faceCams=CreateCameras() 

switch_all state:off

disableAllMat mat:meditMaterials[24]


isTest=0
messagebox "Start Rendering?"

renderOnce=false

count=0
for s in 1 to scenes.count do
(
	print scenes[s]
	cam=viewPoints[s]
	if cam==undefined do
	(
		continue
	)
	print cam.name
	print cam.position
	
	for index in scenes[s] do
	(
		gpgp=groups[index]

		if hasObject irreplace index do
		(
			print "Irreplaceable"
			RenderCombination Root:Root0 SceneCam:cam LG:gpgp LGIndex:index ResultFolder:result_folder IESFolder:ies_folder IES:"" CCT:CCT_Default testPrint:isTest Resolution:outputSize
			
			count =count+6
			if renderOnce==true then
			(
				exit
			)
			continue
		)
		
		if hasObject spotlight index do
		(
			print "spot light"
			--get ies file here
			for i in 1 to iesfiles.count do
			(
				
				
				RenderCombination Root:Root0 SceneCam:cam LG:gpgp LGIndex:index ResultFolder:result_folder IESFolder:ies_folder IES:iesfiles[i] CCT:CCT_Default testPrint:isTest Resolution:outputSize
				
				
			)
			
			
			count =count+6
			if renderOnce==true then
			(
				exit
			)
			continue
		)
			
		if hasObject covelight index do
		(
			print "Cove Light"
			--get ies file here
			RenderCombination Root:Root0 SceneCam:cam LG:gpgp LGIndex:index ResultFolder:result_folder IESFolder:ies_folder IES:"" CCT:CCT_Default testPrint:isTest Resolution:outputSize
			count =count+6
			if renderOnce==true then
			(
				exit
			)
			continue
			
		)
		
	)
	if renderOnce==true then
	(
		exit
	)
)

s="count:"+count as string

print s
--k=RenderCombination Root:Root0 SceneCam:viewPoints[1] LG:lightGroups_one[1] LGPair:lightGroups_pair[1] ResultFolder:result_folder IESFolder:ies_folder IES:iesFiles[1] CCT:3000 faces:faceCams testPrint:2

print "Rendering Complete!"

--delete the box after rendering
--delete(Bx)
--		File Path and File name should be ShopName//SceneName_CameraID_LightGroupID_up/dn/LF/RT/.jpg
--=========
