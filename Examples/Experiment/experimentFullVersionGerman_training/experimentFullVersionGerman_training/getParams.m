function params = getParams(params)

    % debug mode runs in a window and expects keyboard input. normal mode
    % (params.debugmode = 0) runs fullscreen and expects inputs from a
    % response box over a com port specified in params.boxport in file
    % getParams.m
    params.debugmode = 0;
    
    params.freeTrainingDuration1 = 60; % 1 minute
    params.maxTrainingDuration1 = 15*60; % max 15 minutes
    params.freeTrainingDuration2 = 60; % 1 minute
    params.maxTrainingDuration2 = 15*60; % max 15 minutes
    
    % Specify task params
    params.boxport = 4; % response box port
    
    % this is the byte that the scanner sends to indicate a new slice
    if strcmp(params.loc,'Z')
        params.sliceSignalNum = 53;
    else
        params.sliceSignalNum = 32;
    end

    % the second parameter to config_display specifies the screen
    % resolution. 1=640x480, 3=1024x768, 6=1600x1200
    if params.scannermode
        if strcmp(params.loc,'Z')
            config_display(2,3) % run fullscreen on second monitor
            config_serial(4,19200);
            params.keyone = 49;
            params.keytwo = 50;
        else
           config_display(1,3) % run fullscreen on first monitor
           params.keyone = 28;
           params.keytwo = 29;
        end
    elseif params.debugmode
        % run in window and use keyboard
        config_display(0,3) 
        params.keyone = 10; % [j]
        params.keytwo = 11; % [k]
        dbstop if error;
    else
        % run fullscreen and use responsebox
        config_display(1,3) % run fullscreen
        if strcmp(params.loc,'Z')
            config_serial (4, 115200);
            params.keyone = 1;
            params.keytwo = 2;
        else
            params.keyone = 28;
            params.keytwo = 29;
        end
    end
    
    % timings in ms
    params.planningTime = 9000;
    params.timePerFeedbackArrow = 800;
    params.timeInputBase = 1500;
    params.timeInputPerChoice = 300;
    params.getPostTrialBreakDuration = @() 1500;
    params.getPreFeedbackBreakDuration = @() rand(1)*1000;
    
    % use the following to scale the task
    params.scaling = 1.6; 
    ps = params.scaling;
    params.fontFamily = 'Arial';
    params.fontSizeHuge = 28*ps;
    params.fontSizeLarge = 24*ps;
    params.fontSizeMedium = 22*ps;
    
    % -------------------------------------------------------------------
    % the params below should better not be changed
    params.coords.x = [80*ps -80*ps -160*ps -80*ps 80*ps 160*ps];
    params.coords.y = [139*ps 139*ps 0*ps -139*ps -139*ps 0*ps];
    params.coords.w = ones(6,1)*40*ps; 
    params.coords.h = ones(6,1)*40*ps;
    
    params.arrowCoords{1,2}=[50*ps, 139*ps, -50*ps, 139*ps];
    params.arrowCoords{1,4}=[50*ps, 99*ps, -50*ps, -99*ps];
    params.arrowCoords{2,3}=[-110*ps, 99*ps, -140*ps, 40*ps];
    params.arrowCoords{2,5}=[-50*ps, 99*ps, 50*ps, -99*ps];
    params.arrowCoords{3,4}=[-140*ps, -40*ps, -110*ps, -99*ps];
    params.arrowCoords{3,6}=[-120*ps, 10*ps, 120*ps, 10*ps];
    params.arrowCoords{4,5}=[-50*ps, -139*ps, 50*ps, -139*ps];
    params.arrowCoords{4,2}=[-80*ps, -99*ps, -80*ps, 99*ps];
    params.arrowCoords{5,6}=[110*ps, -99*ps, 140*ps, -40*ps];
    params.arrowCoords{5,1}=[80*ps, -99*ps, 80*ps, 99*ps];
    params.arrowCoords{6,1}=[140*ps, 40*ps, 110*ps, 99*ps];
    params.arrowCoords{6,3}=[120*ps, -10*ps, -120*ps, -10*ps];

    % Sizes of rewards and punishments
    params.tMatrix = [2 4; 3 5; 6 4; 2 5; 1 6; 3 1];
    params.r1 = 20; params.r2 = 140; params.r3 = 70; 
    params.rMatrix = [params.r2 params.r1; ...
                      -params.r1 -params.r3; ...
                      -params.r3 -params.r1; ...
                      params.r1 -params.r1; ...
                      -params.r3 -params.r1; ...
                      params.r1 -params.r1];

    params.movecode={'Zug' 'Züge'};
    
    % now we define plenty of trials. In total, we have 12 repetitions for
    % each combination of each possible starting state and depths 3-6,
    % so 12*4*6=288
    
    params.startingStates = [4,2,4,4,5,2,6,5,3,3,6,5,6,3,1,2,3,1,4,2,1,6,1,5,...
        2,6,2,4,2,5,4,6,1,4,4,6,5,3,3,3,1,1,6,5,2,1,5,3,...
        3,2,6,6,5,1,4,2,1,3,5,3,3,6,2,1,6,2,1,4,4,5,5,4,...
        3,2,6,6,5,3,1,2,3,1,3,4,4,5,6,2,1,6,2,1,4,5,5,4,...
        1,6,6,1,2,3,4,4,2,5,4,6,6,3,5,2,3,3,5,1,4,1,5,2,...
        4,6,1,5,1,1,4,4,3,3,1,5,5,6,3,6,4,5,3,2,2,6,2,2,...
        4,2,4,4,5,2,6,5,3,3,6,5,6,3,1,2,3,1,4,2,1,6,1,5,...
        2,6,2,4,2,5,4,6,1,4,4,6,5,3,3,3,1,1,6,5,2,1,5,3,...
        3,2,6,6,5,1,4,2,1,3,5,3,3,6,2,1,6,2,1,4,4,5,5,4,...
        3,2,6,6,5,3,1,2,3,1,3,4,4,5,6,2,1,6,2,1,4,5,5,4,...
        1,6,6,1,2,3,4,4,2,5,4,6,6,3,5,2,3,3,5,1,4,1,5,2,...
        4,6,1,5,1,1,4,4,3,3,1,5,5,6,3,6,4,5,3,2,2,6,2,2];
    params.planningDepths = [3,4,6,4,5,5,5,3,6,3,6,4,3,5,4,6,4,6,5,3,3,4,5,6,...
        3,6,6,5,5,4,4,3,4,3,6,5,3,6,3,5,5,3,4,5,4,6,6,4,...
        4,3,3,6,5,5,4,5,4,3,4,5,6,5,6,3,4,4,6,5,3,3,6,6,...
        4,3,3,6,5,6,5,5,5,4,3,4,3,4,5,6,3,4,4,6,5,3,6,6,...
        3,6,3,6,3,3,3,6,5,6,5,4,5,6,4,4,4,5,3,5,4,4,5,6,...
        4,3,6,5,5,3,6,3,3,6,4,3,4,4,4,6,5,6,5,4,6,5,3,5,...
        3,4,6,4,5,5,5,3,6,3,6,4,3,5,4,6,4,6,5,3,3,4,5,6,...
        3,6,6,5,5,4,4,3,4,3,6,5,3,6,3,5,5,3,4,5,4,6,6,4,...
        4,3,3,6,5,5,4,5,4,3,4,5,6,5,6,3,4,4,6,5,3,3,6,6,...
        4,3,3,6,5,6,5,5,5,4,3,4,3,4,5,6,3,4,4,6,5,3,6,6,...
        3,6,3,6,3,3,3,6,5,6,5,4,5,6,4,4,4,5,3,5,4,4,5,6,...
        4,3,6,5,5,3,6,3,3,6,4,3,4,4,4,6,5,6,5,4,6,5,3,5];

end




