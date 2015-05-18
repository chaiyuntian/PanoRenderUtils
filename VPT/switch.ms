--function that turns lights on off
fn Turn lt state = (if lt == undefined then(print "light type undefined")else(if classof lt == Free_Light then (lt.on = state)if classof lt == VRayIES then (lt.enabled = state)if classof lt == VRayLight then (lt.on = state)if classof lt == Free_Area then (lt.on = state)))
fn TurnLG gp state = (if gp == undefined then(print "light group undefined")if classof gp == Dummy then(for l in gp.children do(Turn l state))else(print "input parameter is not group"))
if Turn == undefined or TurnLG == undefined then(false)else(true)
