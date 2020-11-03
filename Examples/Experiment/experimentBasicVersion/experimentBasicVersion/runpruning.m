%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%Main script to run two-step task (modified from Daw et al, 2011) %%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear all; close all;   % Tabula rasa

modifyme;   		% set the subject-specific experimental parameters
expparams;         % experimental parameters *NOT* to be modified between subjects
preps;             % preparations: set up stimulus sequences, left/right etc. 

try    % this is important: if there's an error, psychtoolbox will crash graciously
       % and move on to the 'catch' block at the end, where all screens etc are
       % closed. 

   if Par.debug == 0; HideCursor; end % hide the mouse cursor 
   setup;   % set up the psychtoolbox screen and layout parameters 
            % this includes things like positioning of stimuli and 
            % loading the stimuli into psychtoolbox 

   %---------------------------------------------------------------------------
   fprintf('............. Starting training \n');
   Data.timestamp.training_start= GetSecs;
	%for trial=1:Par.Ntrials
		Data.training=trainingtrial(1,Data,Par,dV);
	%	foo=input('Hit ''n'' to stop training, any other key repeats it','s');
	%	if strfind(foo,'n');break;end
	%end
   Data.timestamp.training_end= GetSecs;
	Screen('Flip',dV.wd,0);

	for k=5:-1:1
		DrawFormattedText(dV.wd,sprintf('Ok - starting... in %is',k),'center','center',col.txtcolor);
		Screen('Flip',dV.wd);
		WaitSecs(1)
	end

   %---------------------------------------------------------------------------
   fprintf('............. Starting experiment \n');


   Data.timestamp.experiment_start = GetSecs;
   for trial = 1:Par.Ntrials
      Data=displaytrial(trial,Data,Par,dV);
		try 
			displayfeedback(trial,Data,Par,dV); 
		end
   end
   Data.timestamp.experiment_end = GetSecs;

   %---------------------------------------------------------------------------
	if Par.dosave; 
		fprintf('saving \n');
		eval(['save data' filesep namestring  '.mat']);
	end
   
   ShowCursor; % show the mouse cursor again 
   Screen('CloseAll');
    
    %----------------------------------------------------------------------
catch % execute this if there's an error, or if we've pressed the escape key

   if aborted==0;    % if there was an error
      fprintf(' ******************************\n')
      fprintf(' **** Something went WRONG ****\n')
      fprintf(' ******************************\n')
      if Par.dosave; eval(['save data/' namestring  '.crashed.mat;']);end
   elseif aborted==1; % if we've abored by pressing the escape key
      fprintf('                               \n')
      fprintf(' ******************************\n')
      fprintf(' **** Experiment aborted ******\n')
      fprintf(' ******************************\n')
      if Par.dosave; eval(['save data/' namestring  '.aborted.mat;']);end
   end
   Screen('CloseAll'); % close psychtoolbox, return screen control to OSX
   rethrow(lasterror)
   psychrethrow(psychlasterror)
   ShowCursor; % show the mouse cursor again 
end
