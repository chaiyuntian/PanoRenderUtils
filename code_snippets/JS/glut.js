
var createGLContext = function(cvs)
{
    var gls = ["web-gl","experimental-webgl"];
    var ctx = null;
    for(var i=0;i<gls.length;i++)
    {
     try{ctx = cvs.getContext(gls[i],{antialias:true});}catch(e){}
     if(ctx){break;}
    }
    if(ctx){ctx.viewportWidth = cvs.width;ctx.viewportHeight = cvs.height;}else{alert("Fail to create webGL context!");}
    return ctx;
};


var getShaderFromDom = function(gl, id)
{
    var shaderScript = document.getElementById(id);
    if (!shaderScript) {return null;}
    var str = "";
    var k = shaderScript.firstChild;
    while (k) {
        if (k.nodeType == 3) {str += k.textContent;}
        k = k.nextSibling;
    }
    var shader;
    if (shaderScript.type == "x-shader/x-fragment") {
        shader = gl.createShader(gl.FRAGMENT_SHADER);
    } else if (shaderScript.type == "x-shader/x-vertex") {
        shader = gl.createShader(gl.VERTEX_SHADER);
    } else {
        alert("dom type invalid")
        return null;
    }
    gl.shaderSource(shader, str);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        alert(gl.getShaderInfoLog(shader));
        return null;
    }
    return shader;
};
