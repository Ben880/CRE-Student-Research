function Data=displayt(t,Data,Par,dV)

fprintf('............. t %i / %d\n',t,Par.Ntrials);

%......................... Draw the six boxes 
for k=1:6; Screen('FillRect',dV.wd,dV.boxcolor,dV.box(k,:));end;  % all boxes 
DrawFormattedText(dV.wd,[num2str(Data.Depth(t)) ' moves'],'center','center',dV.centretextcol);     
Screen('Flip',dV.wd,[],1);
WaitSecs(0.2);

Data.piconset(t) = Screen('Flip',dV.wd,[],1);
WaitSecs(0.3);

Screen('FillRect',dV.wd,dV.boxactive,dV.box(Data.S(t,1),:));	% currently active box 
Data.tOnset(t) = Screen('Flip',dV.wd);

%........................ Get choices 
valid_choice=0; KeyIsDown=0;redraw=0;
% while loop to show stimulus until subjects response or until
% "duration" seconds elapsed.
if Par.usekbqueue	           % KbQueue is more accurate for USB devices
	KbQueueFlush; KbQueueStart; 
end
nKey=1; 
while (GetSecs - Data.tOnset(t)) <= Par.max_choice_time-Par.monitorFlipInterval
	if Par.usekbqueue
		[KeyIsDown,KeyCode] = KbQueueCheck; 
		if KeyIsDown; Data.keypresstime(t,nKey) = KeyCode(KeyCode~=0);end % get actual time
	else
		[KeyIsDown, Data.keypresstime(t,nKey), KeyCode] = KbCheck;
	end

	if KeyIsDown; 
		key = KbName(KeyCode); 
		if iscell(key); key=key{1}; end
		if     strcmp(key(1),Par.keyleft); 
			Data.A(t,nKey) = 1; redraw=1; % left was chosen 
			Data.RT(t,nKey) = Data.keypresstime(t,nKey)-Data.tOnset(t); 
			Data.S(t,nKey+1) = Par.transitionMatrix(Data.S(t,nKey),Data.A(t,nKey));
			Data.R(t,nKey) = Par.rewardMatrix(Data.S(t,nKey),Data.A(t,nKey));
			Data.Rstring{t,nKey} = Par.rewardMatrixStrings{Data.S(t,nKey),Data.A(t,nKey)};
			nKey=nKey+1; 
		elseif strcmp(key(1),Par.keyright); 
			Data.A(t,nKey) = 2; redraw=1; % right was chosen 
			Data.RT(t,nKey) = Data.keypresstime(t,nKey)-Data.tOnset(t); 
			Data.S(t,nKey+1) = Par.transitionMatrix(Data.S(t,nKey),Data.A(t,nKey));
			Data.R(t,nKey) = Par.rewardMatrix(Data.S(t,nKey),Data.A(t,nKey));
			Data.Rstring{t,nKey} = Par.rewardMatrixStrings{Data.S(t,nKey),Data.A(t,nKey)};
			nKey=nKey+1; 
		else KeyIsDown = 0; key='wrong_key';
		end
		if nKey == Data.Depth(t)+1; break;end
	else key = 'no_response';
	end
end

%......................... no response ts
if iscell(key); key=key{1};end
if strcmp(key,'no_response') | strcmp(key,'wrong_key');
	DrawFormattedText(dV.wd,'Too slow!','center','center',dV.warncolor);
	WaitSecs(Par.length_too_slow-Par.monitorFlipInterval);
	Data.A(t,nKey:Data.Depth(t)) = NaN;
	Data.RT(t,nKey:Data.Depth(t)) = NaN; 
	Data.keypresstime(t,nKey:Data.Depth(t)) = NaN;
end
   
save(Par.savestring,'Data','-append');
checkabort;
