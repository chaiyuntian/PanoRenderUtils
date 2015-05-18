include "switch.ms"
include "camera.ms"

--CreateCamerasAt pos:[100,100,1000]
--Turn $i1_001 on
--TurnLG $LGI1 on
global root_path = "F:\\PythonScripts\\"
global image_path_default = root_path + "test.png"
global image_width = 256
global image_height = 256
global image_format = ".png"
global image_default_gamma = 1.0


fn RenderAtCam Cam fullpath:image_path_default w:image_width h:image_height fmt:image_format gma:image_default_gamma =
(
	if Cam==undefined then(return 0)if classof Cam ==Freecamera or classof Cam == Targetcamera then
	(str="prepare to render, viewpoint:"+Cam.name;bmp1=bitmap w h filename:fullpath gamma:gma pixelAspect:1.0;render camera:Cam to:bmp1;save bmp1;s="reder to:"+fullpath)
	return 1
)

RenderAtCam $Camera001

