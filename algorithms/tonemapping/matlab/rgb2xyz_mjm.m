function xyz = rgb2xyz(rgb, M, gamma);

% RGB2XYZ  convert RGB to CIE XYZ with transformationmatrix M
% and gamma
%
%	ref: Bruce Lindbloom
%	http://www.brucelindbloom.com
%

xyz = (rgb .^ gamma) * M;
