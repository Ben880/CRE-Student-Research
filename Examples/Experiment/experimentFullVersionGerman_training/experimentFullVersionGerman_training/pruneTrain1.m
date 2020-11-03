%{
Markov decision-making task, originally used in Tanaka et al. (2006),
then adopted by Neir Eshel and Niall Lally.
This was rewritten, extended and translated to German in March 2015 
by Daniel Renz, renz@biomed.ee.ethz.ch.
The task consists of three parts. This is the first part (transition
training). The structure of the transition training is as follows
1) A free training phase lets the participant explore the maze. It's 
   duration can be specified by params.freeTrainingDuration1.
2) A goal training phase presents the participant with many tasks to be
   solved (You start at X, your goal is Y, you have Z moves). A task is
   repeated until solved successfully. 
3) A test phase checks if the participant has correctly learned all 12
   transitions. With one error or less, we finish the training. If more
   than one error, the training repeats from the first phase until 
   params.maxTrainingDuration1 is reached.
%}


function pruneTrain1()
    % init and setup ----------------------------------------------------
    clear all
    addpath('Cogent2000v1.32/Toolbox', 'lib');
    params.scannermode = 0;
    params = getParticipantCode(params);
    params = getParams(params);
    
    % enter subject details
    params.savestr = [params.savestr, '_train1'];
    
    % init and start cogent
    initStartCogent(params);
    makeCogentSprites(params);
    
    % start timer
    tic;
    results.startDateTime = datestr(now,0);

    % instructions ------------------------------------------------------
    cgpencol(1,1,1)
    cgfont(params.fontFamily, params.fontSizeHuge)
    cgtext('Psychochess', 0, 100*params.scaling)
    cgfont(params.fontFamily, params.fontSizeMedium)
    cgtext('Willkommen zum ersten Teil des Trainings,', 0, 30*params.scaling)
    cgtext('bitte drücken Sie eine Taste zum Fortfahren.', 0, 0)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    cgfont(params.fontFamily, params.fontSizeMedium)
    cgtext('Sie werden 6 Rechtecke auf dem Bildschirm sehen. Sie können sich',0,100*params.scaling)
    cgtext('zwischen den Rechtecken hin und her bewegen, indem Sie die',0,75*params.scaling)
    if params.debugmode
        cgtext('Tasten ''J'' oder ''K'' drücken. Sie können sich von jedem',0,50*params.scaling)
    else
		 if strcmp(params.loc,'Z');
           cgtext('Tasten ''1'' oder ''2'' drücken. Sie können sich von jedem',0,50*params.scaling)
		 elseif strcmp(params.loc,'B');
			  cgtext('blaue oder gelbe Taste drücken. Sie können sich von jedem',0,50*params.scaling)
		 end
    end
	 cgtext('Rechteck zu einem von zwei anderen Rechtecken bewegen.',0,25*params.scaling);
	 cgtext('Eine Taste geht jeweils durch die Mitte, die andere um den Kreis. ',0,0*params.scaling);
	 cgtext('Sie haben jetzt etwas Zeit, um dies auszuprobieren. Prägen Sie sich ganz gut',0,-50*params.scaling);
	 cgtext('ein, welche Taste sie jeweils drücken müssen, um sich von jedem',0,-75*params.scaling);
	 cgtext('Rechteck durch die Mitte oder im Kreis zu bewegen. ',0,-100*params.scaling);
    cgtext('Bitte drücken Sie irgendeine Taste zum Fortfahren.',0,-150*params.scaling)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    % main game loop ----------------------------------------------------
    % they are allowed to quit this training only if they have made no more
    % than one error in doTesting(), or if time is up.
    results.freeTrain = {};
    results.goalTrain = {};
    results.test = {};
    while 1
        [timeOut, choices, keyTimes] = doFreeTraining(params);
        results.freeTrain{end+1} = struct('choices', choices, 'keyTimes', keyTimes);
        if timeOut, break, end;
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
        
        [timeOut, stats] = doGoalTraining(params);
        results.goalTrain{end+1} = stats;
       
        if timeOut, break, end;
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
        
        [doContinue, stats] = doTesting(params);
        results.test{end+1} = stats;
        if doContinue, break, end;
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
    end

    % save and clean up -------------------------------------------------
    if ~exist('results', 'dir')
      mkdir('results');
    end
    results.type = 'train1';
    eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
    cgtext('Gut gemacht! Der erste Teil des Trainings ist nun vorbei.', 0, 50*params.scaling)
    cgtext('Bitte SPACE betätigen, um das Training zu beenden!', 0, -100*params.scaling)
    cgflip(0,0,0)
    waitkeydown(inf,71);
    cgshut; 
    stop_cogent; 
    clear all
end

% -----------------------------------------------------------------------

function [timeOut, choices, keyTimes] = doFreeTraining(params)
    cgfont(params.fontFamily, params.fontSizeMedium)
    cgtext('Sie sind das WEISSE Rechteck! Bitte bewegen Sie sich',0,100*params.scaling)
    cgtext('eine Weile umher, damit Sie ein  Gefühl dafür bekommen,',0,75*params.scaling)
    cgtext('wie Sie sich bewegen können.',0,50*params.scaling)
    cgtext('Bitte drücken Sie eine Taste, um das Training zu starten.',0,-150*params.scaling)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    state = 1;
    tFreeTrain = toc;
    timeOut = 0;
    choices = [];
    keyTimes = [];
    clearkeys();
    while toc - tFreeTrain < params.freeTrainingDuration1
        drawGame(state, params, params.freeTrainingDuration1 - (toc - tFreeTrain));
        cgflip(0,0,0);
        [ks, kt] = waitAndCheckKey(time()+100, params);
        ch = getChoicesFromKeys(params, ks);
        state = updateState(params, state, ch);
        keyTimes = [keyTimes; kt];
        choices = [choices; ch];
        timeOut = timeIsUp(params, params.maxTrainingDuration1);
        if timeOut, return, end;
    end
end % doFreeTraining()

% -----------------------------------------------------------------------
function [timeOut, stats] = doGoalTraining(params)
    timeOut = 0;
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgtext('Sie sind das WEISSE Rechteck! Ihr Ziel ist es, das rote Ziel',0,100*params.scaling)
    cgtext('mit dem LETZTEN Zug zu erreichen. Sie können das rote Ziel',0,75*params.scaling)
    cgtext('schon vor dem letzten Zug betreten, aber Sie müssen',0,50*params.scaling)
    cgtext('dort die Zugabfolge mit dem letzten Zug beenden.',0,25*params.scaling)
    cgtext('Bitte drücken Sie eine Taste, um das Training zu starten.',0,-150*params.scaling)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    % train all transitions of depth 1. Then 6 x depth 2, 2 x depth 3.
    % in the following matrices, the first column indicates the
    % starting state and the second column the goal state
    % all transitions of depth 1
    trialsCheckTrans = [1, 2; 1, 4; 2, 3; 2, 5; 3, 6; 3, 4; ...
                        4, 5; 4, 2; 5, 6; 5, 1; 6, 3; 6, 1];
    trialsCheckIdx = randperm(size(trialsCheckTrans,1));
    % some transitions of depth 2
    trialsCheck2 = [1, 3; 2, 4; 3, 5; 4, 6; 5, 1; 6, 2; 1, 5; ...
                    2, 1; 3, 2; 4, 3; 5, 2; 6, 4];
    trialsCheck2Idx = randperm(size(trialsCheck2,1));
    % some transitions of depth 3
    trialsCheck3 = [1, 4; 2, 5; 3, 6; 4, 1; 5, 2; 6, 3; 1, 6; ...
                    2, 1; 3, 5; 4, 6; 5, 3; 6, 5];
    trialsCheck3Idx = randperm(size(trialsCheck3,1));
    maxdep = 3;

    trials = [trialsCheckTrans(trialsCheckIdx,:); ...
              trialsCheck2(trialsCheck2Idx(1:6),:); ...
              trialsCheck3(trialsCheck3Idx(1:2),:)];
    trialDepths = [ones(length(trialsCheckTrans(trialsCheckIdx,:)),1); ...
              2*ones(length(trialsCheck2(trialsCheck2Idx(1:6),:)),1); ...
              3*ones(length(trialsCheck3(trialsCheck3Idx(1:2),:)),1)];
    stats = struct('trialTimes', [], 'choiceTimes', [], 'choices', [], ...
                    'success', [], 'states', []);
    counter = 1;
    trial = 1;
    clearkeys();
    while counter <= size(trials,1)
        tstates = zeros(1,maxdep+1);
        tstates(1) = trials(counter,1);
        tchoices = zeros(1,maxdep);
        tchoiceTimes = zeros(1,maxdep);
        stats.trialTimes(trial) = time();

        target = trials(counter,2);
        for j = 1:trialDepths(counter)
            drawGame(tstates(j), params);
            cgdrawsprite(3, params.coords.x(target), params.coords.y(target));
            cgfont(params.fontFamily, params.fontSizeLarge);
            cgtext(sprintf('Sie haben %d %s.', trialDepths(counter), ...
                params.movecode{(trialDepths(counter)~=1)+1}),0,0);
            cgfont(params.fontFamily, params.fontSizeMedium);
            cgtext(sprintf('Erreichen Sie das rote Ziel mit dem letzten Zug.'),0,185*params.scaling);
            cgflip(0,0,0);

            % Make choice
            [keyout, tchoiceTimes(j)] = waitForKey(params, inf, [params.keyone, params.keytwo]);
            if keyout(1)==params.keyone
                tchoices(j) = 1;
            else
                tchoices(j) = 2;
            end
            tstates(j+1) = params.tMatrix(tstates(j), tchoices(j));
        end
        stats.choiceTimes = [stats.choiceTimes; tchoiceTimes];
        stats.choices = [stats.choices; tchoices];
        stats.states = [stats.states; tstates];

        % Give feedback
        drawGame(tstates(j+1), params);
        cgfont(params.fontFamily, params.fontSizeLarge)
        if tstates(j+1) == target
            cgtext('Sehr gut!',0,0)
            stats.success(trial) = 1;
            counter = counter + 1;
        else
            cgdrawsprite(3, params.coords.x(target), params.coords.y(target));
            cgtext('Bitte versuchen Sie',0,13*params.scaling);
            cgtext('es noch einmal.',0,-13*params.scaling);
        end
        cgflip(0,0,0);
        wait(2000);

        timeOut = timeIsUp(params, params.maxTrainingDuration1);
        if timeOut, return, end;
        trial = trial + 1;
    end % while 
end % doGoalTraining

% ------------------------------------------------------------------------
function [doContinue, stats] = doTesting(params)
    timeOut = 0;
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgtext('Bei den folgenden Aufgaben haben Sie nur', 0, 25*params.scaling);
    cgtext('noch jeweils eine Chance, um zum roten Ziel zu kommen', 0, 0);
    cgtext('Bitte drücken Sie eine Taste, um fortzufahren.', 0, -180*params.scaling);
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);
    trialsCheckTrans = [1, 2; 1, 4; 2, 3; 2, 5; 3, 6; 3, 4; ...
                        4, 5; 4, 2; 5, 6; 5, 1; 6, 3; 6, 1];
    trialsCheckIdx = randperm(size(trialsCheckTrans,1));
    trials = trialsCheckTrans(trialsCheckIdx,:);
    
    stats = struct('trialTimes', [], 'choiceTimes', [], 'choices', [], ...
                    'success', [], 'states', []);
    
    stats.states = trials(:,1);
    clearkeys();
    for i=1:size(trials,1)
        stats.trialTimes(i) = time();
        target = trials(i,2);
        drawGame(trials(i,1), params);
        cgdrawsprite(3, params.coords.x(target), params.coords.y(target));
        cgfont(params.fontFamily, params.fontSizeMedium);
        cgtext(sprintf('Erreichen Sie das rote Ziel mit einem Zug.'),0,185*params.scaling);
        cgflip(0,0,0);

        % Make choice
        [keyout, stats.choiceTimes(end+1)] = waitForKey(params, inf, [params.keyone, params.keytwo]);
        if keyout(1) == params.keyone
            stats.choices(end+1) = 1;
        else
            stats.choices(end+1) = 2;
        end

        % Give feedback
        nextState = params.tMatrix(stats.states(i), stats.choices(i));
        drawGame(nextState, params);
        cgfont(params.fontFamily, params.fontSizeLarge)
        if nextState == target
            cgtext('Sehr gut!',0,0)
            stats.success(i) = 1;
        else
            cgdrawsprite(3, params.coords.x(target), params.coords.y(target));
            stats.success(i) = 0;
            cgtext('Leider falsch.',0,0);
        end
        cgflip(0,0,0);
        wait(2000);
        
        timeOut = timeIsUp(params, params.maxTrainingDuration1);
        if timeOut
            doContinue = 0;
            return;
        end
    end
    nCorrect = sum(stats.success);
    cgtext(sprintf('Sie haben %d von %d Problemen richtig gelöst.', nCorrect, size(trials,1)),0,25*params.scaling);
    cgflip(0,0,0);
    wait(2000);

    testPassed = nCorrect >= size(trials,1) - 1;
    if ~testPassed
        cgtext('Wir trainieren jetzt weiter.', 0, 0);
        cgflip(0,0,0);
        wait(2000);
    end
    
    doContinue = timeOut || testPassed;

end % doTesting



