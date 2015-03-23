function [imgOut, Lw, logAvgLum, A, B ] = reinhard02auto( img, key, phi, whiteLimit );
% reinhard '02 algorithm: auto param setting for tonemapping operator for HDR images
%
% arguments:
%   img:     NxMx3:  high dynamic range (HDR) image in CIE 1931 XYZ -
%            preferably real values, where the Y channel is luminance in cd/m2
%   key:     scalar: ~average reflectance of the scene.  Typical (and
%            default) value is 0.18.  Possible values are 0-1
%   phi:     NOT YET IMPLEMENTED
%   whiteLimit:  scalar: maximum value over which all higher luminances
%            will be mapped to white (burned out)
%
%   imgOut   NxMx3:  tonemapped result image, scaled 0-1
%   Lw       scalar:  maximum luminance of the scene
%   logAvgLum:  scalar: log-average luminance computed
%   A        scalar:  ratio key/logAvgLum (to be used in manual call)
%   B        scalar:  (Lw).^2 (to be used in manual call)
%
% MJMurdoch 28 Aug 2012

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

% log-average luminance: eqn 1 (with correction, N inside the exp)
if isempty( logAvgLum )
    if ch == 1
        % assume image is luminance only
        logAvgLum = 10.^ ( mean(mean( log10( img ))));     
    elseif ch == 3
        % assume XYZ, lum is channel 2
        logAvgLum = 10.^ ( mean(mean( log10( img(:,:,2) ))));
    else
        error('Reinhard:  image must be 1 (luminance only) or 3 channel (XYZ)');
    end
end

% scale the image by key/log avg: eqn 2
A = key /logAvgLum;

% determine scene max - use white limit if smaller
if isempty( Lw )
    if ch == 1
        % assume image is luminance only
        Lw = ( max(max(img)) );
    elseif ch == 3
        % assume XYZ, lum is channel 2
        Lw = ( max(max(img(:,:,2))) );
    else
        error('Reinhard:  image must be 1 (luminance only) or 3 channel (XYZ)');
    end
    
    if Lw > whiteLimit;
        Lw = whiteLimit;
    end
end

% tonemap:  equation 4 in the paper:
B = Lw.^2;

% execute the whole transform:  A=key/logAvgLum;  B = Lw.^2
imgOut = reinhard02calc( img, A, B );
