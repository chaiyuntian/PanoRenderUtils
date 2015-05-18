fn CreateCamerasAt pos:[0,0,0]=
(
	if $FaceCameras == undefined then()else(delete $FaceCameras)
	nrange=0
	frange=1000
	tDistance=160
	fov=90

	frontCam=Freecamera fov:fov Name:"CamFront" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on 
	rotate frontCam (angleaxis 90.0 [1,0,0])
	rotate frontCam (angleaxis -180 [0,0,1])

	backCam=Freecamera fov:fov Name:"CamBack" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on 
	rotate backCam (angleaxis 90.0 [1,0,0])


	leftCam=Freecamera fov:fov Name:"CamLeft" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on
	rotate leftCam (angleaxis 90.0 [1,0,0])
	rotate leftCam (angleaxis 90.0 [0,0,1])
	rightCam=Freecamera fov:fov Name:"CamRight" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on
	rotate rightCam(angleaxis 90.0 [1,0,0])
	rotate rightCam(angleaxis -90.0 [0,0,1])

	upCam=Freecamera fov:fov Name:"CamUp" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on 
	rotate upCam (angleaxis 180 [1,0,0])

	downCam=Freecamera fov:fov Name:"CamDown" targetDistance:tDistance nearclip:1 farclip:1000 nearrange:nrange farrange:frange mpassEnabled:off mpassRenderPerPass:off pos:[0,0,0] isSelected:on
	print "Finish creating cameras."

	FaceCamGroup=group #(frontCam,backCam,leftCam,rightCam,upCam,downCam) name:"FaceCameras"
	FaceCamGroup.pos = pos
	return FaceCamGroup
)

