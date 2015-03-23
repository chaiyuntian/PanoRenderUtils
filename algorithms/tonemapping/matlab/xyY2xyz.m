function xyz = xyY2xyz(xyY);

% XYY2XYZ  convert CIE xyY (chromaticity coordinates plus Y) to CIE XYZ
%
% MJMurdoch 19 Jan 2009

x = xyY(:,3) ./ xyY(:,2) .* xyY(:,1);
z = xyY(:,3) ./ xyY(:,2) .* (1 - sum( xyY(:,1:2),2) );

xyz = [ x xyY(:,3) z ];
