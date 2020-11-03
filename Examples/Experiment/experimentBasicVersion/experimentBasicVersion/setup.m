fprintf('............ Setting up the screen   \n');

%................... colours (in RBG)
col.white 		= [200 200 200];
col.hard_white  = [255 255 255];
col.black 		= [0 0 0]; 
col.gray1  		= [70 70 70];
col.red 			= [255 50 50]; 
col.blue 		= [120 120 255]; 
col.green 		= [30 255 30]; 
col.purple		= [148 0 211];
col.brown		= [205 133 63];
col.chartreuse = [127 255 0];
col.yellow		= [250 250 50]; 
col.purple		= [150 0 150];
col.txtcolor 	= col.hard_white;
dV.bgcol 		= col.black;	% this is just in grayscale (each value separately)

dV.boxcolor		  = col.gray1; 
dV.boxactive     = col.white; 
dV.centretextcol = col.blue; 
dV.fbcolor       = col.blue; 
dV.warncolor	  = col.red; 


%................... open a screen
addpath(genpath('/Applications/Psychtoolbox/'));

AssertOpenGL;
Screen('Preference','Verbosity',0);

screenNumber = 0;

if Par.debug; 
	Screen('Preference','SkipSyncTests',2); % ONLY do this for quick debugging;
	dV.wd=Screen('OpenWindow',0,dV.bgcol(2),[0 0 600 400],[],2,[],[]); % Make small PTB screen on my large screen
else
   Screen('Preference','SkipSyncTests',2)
	dV.wd=Screen('OpenWindow', screenNumber,dV.bgcol(2),[],[],2,[],[],[]);			% Get Screen. This is always size of the display. 
end 

%................... keyboard setup
KbName('UnifyKeyNames');        % need this for KbName to behave
% start queue for KbQueueCheck 
if Par.usekbqueue; 
	KbQueueCreate; 
	KbQueueStart; 
end

%---------------------------------------------------------------------------
%                    SCREEN LAYOUT
%---------------------------------------------------------------------------
[wdw, wdh]=Screen('WindowSize', dV.wd);	% Get screen size 

boxwidth = wdw/6; 
boxheight = wdh/6; 

TotalCharacterWrap = 55; % The total number of characters allowed per line
% General text/stimulus settings for experiment
txtsizefrac = 0.06;                     % text size as fraction of screen height!
blw         = .35;                      % width of stimulus as fraction of **xfrac**
blh         = .35;                      % height of stimulus as fraction of **xfrac**
dV.txtsize = ceil(wdh * txtsizefrac);
dV.txtlarge = ceil(1.5*dV.txtsize);
Screen('TextSize',dV.wd,dV.txtsize);	% Set size of text

% six squares in hectagonal grid 

dV.boxcentre(1,:) = [5/8*wdw 1/4*wdh]; 
dV.boxcentre(2,:) = [3/8*wdw 1/4*wdh]; 
dV.boxcentre(3,:) = [1/6*wdw 1/2*wdh]; 
dV.boxcentre(4,:) = [3/8*wdw 3/4*wdh]; 
dV.boxcentre(5,:) = [5/8*wdw 3/4*wdh]; 
dV.boxcentre(6,:) = [5/6*wdw 1/2*wdh]; 

for k=1:6
	dV.box(k,1) = dV.boxcentre(k,1)-boxwidth/2;
	dV.box(k,2) = dV.boxcentre(k,2)-boxheight/2;
	dV.box(k,3) = dV.boxcentre(k,1)+boxwidth/2;
	dV.box(k,4) = dV.boxcentre(k,2)+boxheight/2;
	dV.smallbox(k,1) = dV.boxcentre(k,1)-boxwidth/2/2;
	dV.smallbox(k,2) = dV.boxcentre(k,2)-boxheight/2/2;
	dV.smallbox(k,3) = dV.boxcentre(k,1)+boxwidth/2/2;
	dV.smallbox(k,4) = dV.boxcentre(k,2)+boxheight/2/2;
end

% 12 boxes for reward feedback 

for s=1:6
	for a=1:2
		sn = Par.transitionMatrix(s,a);
		dV.fbboxcentre(sn,s,:) = (dV.boxcentre(s,:) + dV.boxcentre(sn,:))/2; 
		dV.fbbox(sn,1,s) = dV.fbboxcentre(sn,s,1)-boxwidth/2;
		dV.fbbox(sn,2,s) = dV.fbboxcentre(sn,s,2)-boxheight/2/2;
		dV.fbbox(sn,3,s) = dV.fbboxcentre(sn,s,1)+boxwidth/2;
		dV.fbbox(sn,4,s) = dV.fbboxcentre(sn,s,2)+boxheight/2/2;
	end
end

% monitor frame rate
[Par.monitorFlipInterval nrValidSamples stddev] = Screen('GetFlipInterval', dV.wd);

save(Par.savestring,'Data','Par');
