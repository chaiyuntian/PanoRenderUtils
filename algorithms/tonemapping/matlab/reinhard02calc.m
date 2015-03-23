function [imgOut] = reinhard02calc( img, A, B );
% reinhard '02 calculations: calculate tonemapping operator for HDR images
%
% arguments:
%   img:    (any)  high dynamic range (HDR) image in CIE 1931 XYZ -
%            preferably real values, where the Y channel is luminance in cd/m2
%            OR simply Y image or Y values
%   A:       scalar:  key/logAvgLum
%   B:       scalar:  (Lw).^2 
%
%   imgOut   (same as img)  tonemapped result image, scaled 0-1
%
% MJMurdoch 28 Aug 2012

% checks and defaults
if nargin < 3
    help( mfilename );
end

% scale the image by key/log avg: Reinhard'02 eqn 2
img = A .* img;

% tonemap:  equation 4 in the paper:
[r c ch] = size( img );
if ch == 1
    % assume image is luminance only
    imgOut = img .* ( 1 + img/B ) ./ ( 1 + img );
elseif ch == 3
    % assume XYZ, lum is channel 2
    imgOut = img;
    imgOut(:,:,2) = img(:,:,2) .* ( 1 + img(:,:,2)/B ) ./ ( 1 + img(:,:,2) );
    imgOut(:,:,[1 3]) = bsxfun( @times, img(:,:,[1 3]), imgOut(:,:,2)./img(:,:,2) );
else
    error('Reinhard:  image must be 1 (luminance only) or 3 channel (XYZ)');
end
