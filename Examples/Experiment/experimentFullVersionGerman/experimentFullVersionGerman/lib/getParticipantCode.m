function params = getParticipantCode(params)

params.num=[];
while isempty(params.num) || ~isnumeric(params.num)
    params.num = input('Bitte Teilnehmer Nummer eingeben (Ber Pat 1000+, Ber Ctr 2000+, ZH Pat 3000+, ZH Ctr 4000+) ');
end
    
params.loc=[];
while isempty(params.loc) || ~(strcmp(params.loc,'B')|strcmp(params.loc,'Z'))
    params.loc = input('Bitte Ort eingeben (B oder Z) ','s');
end

params.task = 'Pruning'; 
params.tasknumber = '1';

params.session=[];
while 1; 
    params.session= input('Bitte Session eingeben (main1 oder main2?) ','s');
	 if strcmp(params.session,'main1'); break; end
	 if strcmp(params.session,'main2'); break; end
end

params.datatype='behaviour';

params.datetime=datestr(now,'YYYYmmdd_HHMM');
   
savestr = ['AIDAZ_' num2str(params.num) '_' params.loc '_' params.task '_' params.session '_' params.datatype '_' params.datetime];
savedir = ['../results_AIDA_fMRI_' params.session '/' params.tasknumber '_' params.task];
params.savestr=savestr;
params.savedir=savedir;

% make save folder
if ~exist(params.savedir, 'dir')
   mkdir(params.savedir);
else
	fprintf('************************\n')
	fprintf('************************\n')
   fprintf('       WATCH OUT!!      \n')
	fprintf('directory already exists\n Make sure this isn''t the previous subject''s data!!!\n')
	fprintf('************************\n')
	fprintf('************************\n')
	foo=[];
	while ~(strcmp(foo,'yes') | strcmp(foo,'no'))
		 foo = input('Are you sure you want to continue? [yes/no]','s');
	end
	if strcmp(foo,'no'); error('Ok - you don''t want to continue');end
end

if params.scannermode==0; 
	fprintf('Task in behavioural mode (affects screen settings)\n');
elseif params.scannermode==1; 
	fprintf('Task in scanner mode (affects screen settings)\n');
end
