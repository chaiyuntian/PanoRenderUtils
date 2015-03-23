function [imgOut, Lw, logAvgLum] = reinhard02( img, key, phi, whiteLimit, Lw, logAvgLum );
% reinhard '02 algorithm: tonemapping operator for HDR images
%
% arguments:
%   img:     NxMx3:  high dynamic range (HDR) image in CIE 1931 XYZ -
%            preferably real values, where the Y channel is luminance in cd/m2
%   key:     scalar: ~average reflectance of the scene.  Typical (and
%            default) value is 0.18.  Possible values are 0-1
%   phi:     NOT YET IMPLEMENTED
%   whiteLimit:  scalar: maximum value over which all higher luminances
%            will be mapped to white (burned out)
%   Lw       scalar:  value to be used in place of actual scene max
%            luminance, for example to make the "auto-exposure" of one 
%            image match another
%   logAvgLum:  scalar: value to be used in place of actual log-average
%            luminance, for example to make the "auto-exposure" of one 
%            image match another
%
%   imgOut   NxMx3:  tonemapped result image, scaled 0-1
%   Lw       scalar:  maximum luminance of the scene (or specified)
%   logAvgLum:  scalar: log-average luminance computed (or specified)
%
% MJMurdoch 25 Jan 2012
%  log-avg override added 23 July 2012

% checks and defaults
if nargin < 1
    help( mfilename );
end
if nargin < 4
    whiteLimit = 1E20;
end
if nargin < 3
    phi = 8;
end
if nargin < 2
    key = 0.18;
end
if nargin < 5
    Lw = [];
end
if nargin < 6
    logAvgLum = [];
end


% image check
[r,c,ch] = size( img );
if ch < 3
    % assume image is luminance only
    img = repmat( img, [1 1 3]);
    ch = 3;
end


% input image is XYZ:  convert to xyY and work on Y channel only
img = reshape( xyz2xyY( reshape( img, r*c, ch) ), [r c ch] );

% log-average luminance: eqn 1 (with correction, N inside the exp)
% compute only if not specified as input
if isempty( logAvgLum )
    logAvgLum = 10.^ ( mean(mean( log10( img(:,:,3) ))));
end

% scale the image by key/log avg: eqn 2
img(:,:,3) = key /logAvgLum .* img(:,:,3);

% determine scene max - use white limit if smaller
% compute only if not specified as input
if isempty( Lw )
    Lw = ( max(max(img(:,:,3))) );
    if Lw > whiteLimit;
        Lw = whiteLimit;
    end
end

% tonemap:  equation 4 in the paper:
img(:,:,3) = img(:,:,3) .* ( 1 + img(:,:,3)/Lw.^2 ) ./ ( 1 + img(:,:,3) );

% return from xyY to XYZ
imgOut = reshape( xyY2xyz( reshape( img, r*c, ch) ), [r c ch] );


