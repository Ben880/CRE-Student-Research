[foo, foo, key ] = KbCheck;
if strcmpi(KbName(key),'ESCAPE')
	aborted=1; 
	Screen('Fillrect',dV.wd,ones(1,3)*100);
	text='Aborting experiment';
	col=[200 30 0];
	Screen('TextSize',dV.wd,60);
	DrawFormattedText(dV.wd,text,'center','center',col,60);
	error('Pressed ESC --- aborting experiment')
end
