function Q=getQd(dd,s,d,Z);
% 
% Get the Q value of all actions at a a given state looking dd steps ahead. The
% function should be called with d=0, and this increases until d==dd. Z contains
% the transition matrix Z.Tm and the Reward matrix Z.Rm as Ns x Na matrices (Ns
% is number of states, Na number of actions). 


if dd==d							% if it's the end of the tree 
	Q = Z.rewardMatrix(s,:);
else
	dd=dd+1;
	for a=1:2	 				% iterate over actions 
		ss=Z.transitionMatrix(s,a);			% find where this leads us to 
		Q(a)=max(getQb(dd,ss,d,Z)) + Z.rewardMatrix(s,a); 	% Q values from that state 
	end
end

