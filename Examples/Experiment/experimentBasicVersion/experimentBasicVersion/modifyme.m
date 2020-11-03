%----------------------------------------------------------------------------
%        MAIN FILE TO EDIT
%        This is the only file that should demand any changes!!!
%----------------------------------------------------------------------------
fprintf('............ Setting basic parameters according to \n')
fprintf('............            MODIFYME.M\n'); 
fprintf('............ \n')

% set this to zero to go fullscreen 
Par.debug       = 1;

%----------------------------------------------------------------------------
%        Do training? 
%----------------------------------------------------------------------------
Par.dotraining   = 0;   % 0: main experimental session
                    % 1: training session 

%----------------------------------------------------------------------------
%        To save or not to save
%        This should ALWAYS be set to 1 when doing experiments obviously
%----------------------------------------------------------------------------
Par.dosave   = 1;      % save output? 

%----------------------------------------------------------------------------
%        Patient Information 
%--------------------------------------------------------------------------
Par.subjn    = '0000';  % Subject Number *** has to be in single quotes ***

%----------------------------------------------------------------------------
%        EXPERIMENT VERSION 
%        PLEASE check this is correct! 
%----------------------------------------------------------------------------
Par.expversion = 'pruningbasic-0.1-170508';
