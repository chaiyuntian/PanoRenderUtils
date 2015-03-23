function xyY = xyz2xyY(xyz);

% XYZ2XYY  convert CIE XYZ to CIE xyY (chromaticity coordinates plus Y)
%
% MJMurdoch 19 Jan 2009


xy = xyz(:,1:2) ./ repmat( sum( xyz, 2 ), 1, 2 );

xyY = [xy xyz(:,2)];
