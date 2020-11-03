%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% Setup %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

aborted=0; % if this parameter is set to one, things will abort. 

% make sure we use different random numbers
rand('twister',sum(1000*clock));

%....................... Saving 
namestring  = ['pruning_' Par.subjn];
if Par.dotraining;
	namestring	= [namestring  '_training'];
end
Par.namestring  = [namestring '_' datestr(now,'_yymmdd_HHMM')]; % detailed name string
Par.savestring = ['data' filesep Par.namestring '.mat'];

if exist('data')~=7; eval(['!mkdir data']); end % make 'data' folder if dosn't exist

if Par.dosave 
	fprintf('............ Data will be saved as                              \n');
	fprintf('............ %s \n', Par.namestring);
	fprintf('............ in the folder ''data''\n');
end

%........................ transition matrix and rewards 

r1 = 20; r2 = 140; r3=70; r4=-20; 
s1='20c'; s2='140c';
s3='5m';s4='1m';
Par.transitionMatrix = [2  4;   3   5;   6   4;  2   5;   1   6;  3   1]; 
Par.rewardMatrix     = [r2 r1; r4 -r3; -r3 r4; r1 r4; -r3 r4; r1 r4];
Par.rewardMatrixStrings = {s2 s1; s4 s3; s3 s4; s1 s4; s3 s4; s1 s4};

%......................... pre-assign some variables 

Data.S = randi(6,Par.Ntrials,1);		% starting states 
Data.Depth = randi(3,Par.Ntrials,1)+2;	% depth from 3 to 5

