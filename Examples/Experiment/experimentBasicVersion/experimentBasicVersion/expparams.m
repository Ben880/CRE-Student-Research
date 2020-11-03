%----------------------------------------------------------------------------
%        Experimental Parameters
%        DO NOT MODIFY between subjects within one experiment
%----------------------------------------------------------------------------
% Daw's timing: choice time 2s (2x), stimulus faded on top: 3s (2x), feedback: 1.5s,
% mean jittered ITI (fMRI), one trial: 13.5s

% General parameters of the experiment
Par.Ntrials = 50;         % number of trials  & actual start trial
if Par.debug;      Par.Ntrials = 100;end

Par.max_choice_time = 5; 			% maximum choice time in seconds 
Par.length_too_slow = 1; 			% time to display that they were too slow 

%----------------------------------------------------------------------------
%        Keyboard / input device settings 
%----------------------------------------------------------------------------

Par.devicetype='keyboard';

if     strcmpi(Par.devicetype,'keyboard'); % if using keyboard
	Par.keyleft			= 'f';			% left key
	Par.keyright	   = 'j';			% right key
	Par.keystop	   	= '1';			% right key
	%Par.instrforward	= 'RightArrow';
	%Par.instrbackward	= 'LeftArrow';
	Par.usekbqueue    = 1;
else
	error('Unknown device type')
end



