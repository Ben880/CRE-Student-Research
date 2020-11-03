fprintf('............. Two step trial %i / %d\n',nt, Z.Ntrials);

for dp=1:2 % two steps 

	%......................... Draw the two stimuli 
	Screen('DrawTexture',wd,stim(S(dp,nt),1),[],box(  lr(dp,nt),:));
	Screen('DrawTexture',wd,stim(S(dp,nt),2),[],box(3-lr(dp,nt),:));
    
	% get last chosen stimulus in 1st step (dp-1) and show faded on upper panel 
	if dp == 2 
		if A(dp-1,nt)==1
			Screen('DrawTexture',wd,stimfa(S(dp-1,nt),1),[],box(3,:));
		else
			Screen('DrawTexture',wd,stimfa(S(dp-1,nt),2),[],box(3,:));
		end
	end
             
	% Show stimulus on screen at next possible display refresh cycle,
	% and record stimulus onset time in 'startrt':
	onset_trial(dp,nt) = Screen('Flip', wd);
	if instr_steps == 1 && dp == 2
		WaitSecs(3-monitorFlipInterval);
		break
	end
	%........................ Get choices 
	valid_choice=0; KeyIsDown=0;redraw=0;
	% while loop to show stimulus until subjects response or until
	% "duration" seconds elapsed.
	if usekbqueue	           % KbQueue is more accurate for USB devices
		KbQueueFlush; KbQueueStart; 
	end
	while (GetSecs - onset_trial(dp,nt)) <= Z.max_choice_time-monitorFlipInterval
		if usekbqueue
			[KeyIsDown,KeyCode] = KbQueueCheck; 
			if KeyIsDown; endrt(dp,nt) = KeyCode(KeyCode~=0);end % get actual time
		else
			[KeyIsDown, endrt(dp,nt), KeyCode] = KbCheck;
		end

		if KeyIsDown; 
			key = KbName(KeyCode);
			if iscell(key); key=key{1}; end
			if     strcmp(key(1),keyleft); 
				a_side(dp,nt) = 1; redraw=1; % left was chosen 
				RT(dp,nt) = endrt(dp,nt)-onset_trial(dp,nt); 
				onset_missing_sign(dp,nt) = NaN; % reaction time, missing onset NaN
				if dp == 1; onset_missing_sign(dp+1,nt) = NaN; end; break;
			elseif strcmp(key(1),keyright); 
				a_side(dp,nt) = 2; redraw=1; % right was chosen 
				RT(dp,nt) = endrt(dp,nt)-onset_trial(dp,nt); 
				onset_missing_sign(dp,nt) = NaN;  % reaction time, missing onset NaN
				if dp == 1; onset_missing_sign(dp+1,nt) = NaN; end; break;
			else KeyIsDown = 0; key='wrong_key';
			end
		else key = 'no_response';
		end
	end

	%......................... no response trials
	if iscell(key); key=key{1};end
	if strcmp(key,'no_response') | strcmp(key,'wrong_key');
		onset_feedback(nt) = NaN; 
		onset_dec(dp,nt) = NaN; 
		onset_dec_mem(dp,nt) = NaN;
		if dp == 1;
			onset_trial(dp+1,nt) = NaN; 
			onset_dec(dp+1,nt) = NaN; 
			onset_dec_mem(dp+1,nt) = NaN;
		end
		DrawFormattedText(wd,'Zu langsam!','center','center',red);
		onset_missing_sign(dp,nt) = Screen('Flip',wd);
		WaitSecs(Z.show_missing_sign-monitorFlipInterval);
		RT(dp,nt) = NaN; 
		A(dp,nt) = NaN;
		a_side(dp,nt) = NaN;
		if dp == 1; 
			RT(dp+1,nt)  = NaN; 
			RT(dp+1,nt)= NaN;
			a_side(dp+1,nt) = NaN;
		end
		break;
	end
    
	% figure out which *stimulus* was chosen
	if   lr(dp,nt)==1; A(dp,nt) = a_side(dp,nt);
	else               A(dp,nt)=3-a_side(dp,nt); 
	end     

	% Show chosen/not chosen stimulus on screen at next possible display 
	% refresh cycle:
	if A(dp,nt)==1
		Screen('DrawTexture',wd,stimch(S(dp,nt),1),[],box(  lr(dp,nt),:));
		Screen('DrawTexture',wd,stim  (S(dp,nt),2),[],box(3-lr(dp,nt),:));
	else
		Screen('DrawTexture',wd,stim  (S(dp,nt),1),[],box(  lr(dp,nt),:));
		Screen('DrawTexture',wd,stimch(S(dp,nt),2),[],box(3-lr(dp,nt),:));
	end
	if dp == 2 %Auswahl vom 1st step bleibt im 2nd step oben (faded)
	   if   A(dp-1,nt)==1
			Screen('DrawTexture',wd,stimfa(S(dp-1,nt),1),[],box(3,:));
	   else
			Screen('DrawTexture',wd,stimfa(S(dp-1,nt),2),[],box(3,:));
	   end
	end
	onset_dec(dp,nt) = Screen('Flip', wd);
	% Choice wir für Rest Choice time in der selben location gezeigt (choicen time - RT)
	WaitSecs(Z.max_choice_time-RT(dp,nt)-monitorFlipInterval);

   % Chosen Stimulus wandert nach oben 
	if A(dp,nt)==1 
		Screen('DrawTexture',wd,stimch(S(dp,nt),1),[],box(3,:));
		Screen('DrawTexture',wd,stimfa(S(dp,nt),2),[],box(3-lr(dp,nt),:));
	else
		Screen('DrawTexture',wd,stimfa(S(dp,nt),1),[],box(  lr(dp,nt),:));
		Screen('DrawTexture',wd,stimch(S(dp,nt),2),[],box(3,:));
	end

	% Show chosen stimulus on upper panel of display (unchosen stimulus remains)
	% at the same location at next possible display refresh cycle:
	onset_dec_mem(dp,nt) = Screen('Flip', wd);
	WaitSecs(Z.display_choice_ontop-monitorFlipInterval);
	if  dp==1 %........................ Determine state 2 
		if trans(nt);	if A(1,nt)==1; S(2,nt) = 2; else S(2,nt)=3; end
		else			   if A(1,nt)==1; S(2,nt) = 3; else S(2,nt)=2; end
		end
	else     %........................ Determine reward output 
		R(nt) = rewprob(S(2,nt)-1,A(2,nt),nt);
	end
    
	% display chosen option and reward
	if dp == 2 
		if A(dp,nt)==1
			Screen('DrawTexture',wd,stimch(S(dp,nt),1),[],box(3,:));
		else
			Screen('DrawTexture',wd,stimch(S(dp,nt),2),[],box(3,:));
		end
		if R(nt);
			Screen('DrawTexture',wd,outcome(1),[],boxo);
		else
			Screen('DrawTexture',wd,outcome(2),[],boxo);
		end

		% write outcome explicitly, too
		if     R(nt)==1
			text1=rew_txt;
			text2=rew_cent;
			ocol=rew_col;
		elseif R(nt)==0
			text1=pun_txt;
			text2=pun_cent;
			ocol=pun_col;
		end
		[wt]=Screen(wd,'TextBounds',text1); ypos1=boxo(2)-(1.5*wt(4));
		[wt]=Screen(wd,'TextBounds',text2); ypos2=boxo(4)+(1.4*wt(4));
		DrawFormattedText(wd,text1,'center',ypos1,ocol);     
		DrawFormattedText(wd,text2,'center',ypos2,ocol);     

		% Show chosen stimulus on upper panel of display and
		% reward/punishment below  at next possible display refresh cycle:
		onset_feedback(nt) = Screen('Flip', wd);
		WaitSecs(Z.display_fb-monitorFlipInterval);
	end
	checkabort;
end

% ....................... Fixation cross + ITI 
Screen('TextSize',wd,txtlarge);
DrawFormattedText(wd,'+','center','center',txtcolor);
Screen('TextSize',wd,txtsize);
onset_cross_var(nt) = Screen('Flip',wd);

if     strcmp(key,'no_response') & dp == 1
	WaitSecs((2*Z.display_choice_ontop)+Z.max_choice_time+Z.display_fb-Z.show_missing_sign-monitorFlipInterval);%ITI
elseif strcmp(key,'no_response') & dp == 2
	WaitSecs(Z.display_choice_ontop+Z.display_fb-Z.show_missing_sign-monitorFlipInterval);%ITI
end

onset_cross_offset_trial(nt) = GetSecs;

if ~dotraining
	WaitSecs(Z.min_display_fix_cross + ITI_final(nt) - monitorFlipInterval);
else 
	WaitSecs(0.6);
end
checkabort;
