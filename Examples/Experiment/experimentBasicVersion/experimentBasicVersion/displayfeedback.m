function displayfeedback(trial,Data,Par,dV)

fprintf('............. feedback %i / %d\n',trial,Par.Ntrials);

for k=1:6; Screen('FillRect',dV.wd,dV.boxcolor,dV.smallbox(k,:));end;  % all boxes 
Screen('FillRect',dV.wd,dV.boxactive,dV.smallbox(Data.S(trial,1),:));	% currently active box 
Screen('Flip',dV.wd);
WaitSecs(.6);
sn=Data.S(trial,1);

sr=0; 
for nKeyPress=2:Data.Depth(trial)+1
	for k=1:6; Screen('FillRect',dV.wd,dV.boxcolor,dV.smallbox(k,:));end;  % all boxes 
	sp = sn; 
	sn = Data.S(trial,nKeyPress);
	r  = Data.Rstring{trial,nKeyPress-1};
	%sr = sr + r; 
	Screen('FillRect',dV.wd,dV.fbcolor,dV.smallbox(sn,:));	% currently active box 
	Screen('DrawLine',dV.wd,dV.fbcolor,dV.boxcentre(sp,1),dV.boxcentre(sp,2),dV.boxcentre(sn,1),dV.boxcentre(sn,2),3);
	Screen('FillRect',dV.wd,dV.bgcol,dV.fbbox(sn,:,sp));
	DrawFormattedText(dV.wd,r,'center','center',dV.fbcolor,[],[],[],[],[],dV.fbbox(sn,:,sp));
	Screen('Flip',dV.wd);
	WaitSecs(.6);
end

%Screen('Flip',dV.wd,0);
%DrawFormattedText(dV.wd,['Total: ' num2str(sr)],'center','center',dV.fbcolor);
%Screen('Flip',dV.wd);
%WaitSecs(1); 

checkabort;
