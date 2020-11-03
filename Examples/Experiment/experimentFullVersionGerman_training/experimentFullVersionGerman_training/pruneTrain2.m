%{
Markov decision-making task, originally used in Tanaka et al. (2006),
then adopted by Neir Eshel and Niall Lally.
This was rewritten, extended and translated to German in March 2015 
by Daniel Renz, renz@biomed.ee.ethz.ch.
The task consists of three parts. This is the second part (reward
training). The structure of the reward training is as follows
1) A free training phase lets the participant explore the maze and the
   rewards attached to each transition/move. The duration can be specified 
   by params.freeTrainingDuration2.
2) A task training phase explains and introduces how the real task will
   work. The participant has to do a few trials without time constraints,
   followed by a few trials with the (usually 9 seconds) time constraint.
3) A test phase checks if the participant has correctly learned all 12
   transition rewards. With one error or less, we finish the training. If 
   more than one error, the training repeats from the first phase until 
   params.maxTrainingDuration2 is reached.
%}


function pruneTrain2()
    % init and setup ----------------------------------------------------
    clear all
    addpath('Cogent2000v1.32/Toolbox', 'lib');
    params.scannermode = 0;
    params = getParticipantCode(params);
    params = getParams(params);
    
    params.savestr = [params.savestr, '_train2'];
    
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
    cgtext('Willkommen zum zweiten Teil des Trainings,', 0, 30*params.scaling)
    cgtext('bitte drücken Sie eine Taste, um das Training zu starten.', 0, 0)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    cgfont(params.fontFamily, params.fontSizeMedium);
    cgtext('Ab jetzt erhalten Sie für jeden Zug eine gewisse Anzahl Punkte.',0,150*params.scaling)
    cgtext('Gewisse Züge ergeben einen Gewinn von 140 oder 20 Punkten,',0,125*params.scaling)
    cgtext('andere einen Verlust von -20  oder -70 Punkten.',0,100*params.scaling)
    cgtext('Ihr Ziel ist jetzt, sich einzuprägen, wie viele Punkte',0,25*params.scaling)
    cgtext('jeder Zug liefert.',0,0*params.scaling)
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);
    
    % main game loop ----------------------------------------------------
    % they are allowed to quit this training only if they have made no more
    % than one error in doTesting(), or if time is up.
    results.freeTrain = {};
    results.test = {};
    while 1
        [timeOut, choices, keyTimes] = doFreeTraining(params);
        results.freeTrain{end+1} = struct('choices', choices, 'keyTimes', keyTimes);
        if timeOut, break, end;
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
        
        timeOut = doTaskTraining(params);
        if timeOut, break, end;
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
%         
        [timeOut, stats] = doTesting(params);
        if timeOut, break, end;
        results.test{end+1} = stats;
        if sum(stats.errors) <= 1, break, end;
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
    end

    % save and clean up -------------------------------------------------
    if ~exist('results', 'dir')
      mkdir('results');
    end
    results.type = 'train2';
    eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
    cgtext('Gut gemacht! Das Training ist nun vorbei.', 0, 50*params.scaling)
    cgtext('Bitte SPACE betätigen, um das Training zu beenden!', 0, -100*params.scaling)
    cgflip(0,0,0)
    waitkeydown(inf,71);
    cgshut; 
    stop_cogent; 
    clear all;
end

% -----------------------------------------------------------------------

function [timeOut, choices, keyTimes] = doFreeTraining(params)
    cgfont(params.fontFamily, params.fontSizeMedium)
    cgtext('Sie können sich nun zunächst wieder frei bewegen, um sich',0,100*params.scaling)
    cgtext('die Punktzahlen in Ruhe anzuschauen.',0,75*params.scaling)
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling)
    cgflip(0,0,0)
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    state = 1;
    tFreeTrain = toc;
    timeOut = 0;
    choices = [];
    keyTimes = [];
    prevState = 0;
    clearkeys();
    while toc - tFreeTrain < params.freeTrainingDuration2
        drawGame(state, params, params.freeTrainingDuration2 - (toc - tFreeTrain));
        % arrow
        if prevState>0
            drawArrow(prevState, state, choices(end), params);
        end
        cgflip(0,0,0);
        [ks, kt] = waitAndCheckKey(time()+100, params);
        if ~isempty(ks)
            ch = getChoicesFromKeys(params, ks);
            prevState = state;
            state = updateState(params, state, ch(1));
            keyTimes = [keyTimes; kt(1)];
            choices = [choices; ch(1)];
        end
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
end % doFreeTraining()

% -----------------------------------------------------------------------
function timeOut= doTaskTraining(params)
    timeOut = 0;
    stats = struct();
    
    % train 3 times with immediate feedback
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgpencol(1,1,1)
    cgtext('Wir kommen dem Ziel näher.',0,75*params.scaling);
    cgtext('In diesem Teil können Sie ganz frei eine Zugfolge einer',0,50*params.scaling);
    cgtext('gewissen Länge wählen. Versuchen Sie sie so zu wählen,',0,25*params.scaling);
    cgtext('dass Sie so viele Punkte wie möglich ergattern.',0,0);
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling);
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);
    
    for i=1:3
        state = randi(6);
        depth = randi([2,3]);
        stats = doTaskTrial(state, depth, params, false, true);
        cgflip(0,0,0);
        wait(800);
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
    
    % train 3 times without time constraint
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgpencol(1,1,1)
    cgtext('Jetzt zeigen wir Ihnen erst nach Eingabe der gesamten',0,75*params.scaling);
    cgtext('Zugreihenfolge, wie Sie sich bewegt und wie viel Sie',0,50*params.scaling);
    cgtext('gewonnen oder verloren haben.',0,25*params.scaling);
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling);
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo]);

    for i=1:3
        state = randi(6);
        depth = randi([2,3]);
        stats = doTaskTrial(state, depth, params, false);
        cgflip(0,0,0);
        wait(800);
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
    
    % train 3 times with time constraint
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgpencol(1,1,1)
    cgtext('Gut, nun versuchen wir ein paar Übungen unter Zeitdruck!',0,100*params.scaling);
    cgtext('Sie haben ab jetzt nur noch 9s Denkzeit.',0,75*params.scaling);
    cgtext('Danach haben Sie ca. 2.5s Zeit, die Züge einzugeben.',0,25*params.scaling);
    cgtext('Die Denkzeit kann mit der Eingabe des ersten Zugs abgebrochen',0,0*params.scaling);
    cgtext('werden. Geben Sie die Zugreihenfolge also erst dann ein, wenn Sie',0,-25*params.scaling);
    cgtext('die gesamte Zugfolge klar vor Ihren Augen haben. Sie müssen',0,-50*params.scaling);
    cgtext('sich aber etwas beeilen, dies innerhalb von 9s zu erreichen.',0,-75*params.scaling);
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling);
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    for i=1:3
        state = randi(6);
        depth = randi([2,3]);
        stats = doTaskTrial(state, depth, params, true);
        cgflip(0,0,0);
        wait(params.getPostTrialBreakDuration());
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
               
end % doTaskTraining

% ------------------------------------------------------------------------
function [timeOut, stats] = doTesting(params)
    timeOut = 0;
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgtext('Wir testen nun, wie gut Sie bisher die Punkte gelernt haben.',0,75*params.scaling)
    cgtext('Bitte benutzen Sie hier die Tastatur zur Eingabe!',0,-50*params.scaling)
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling)
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    moves = [2,3; 4,2; 6,3;...
             3,4; 2,5; 5,6;...
             1,4; 3,4; 1,2;...
             4,5; 5,1; 3,6];
    money = [140, 20, -20, -70];
    solutions = [3,2,2,3,4,3,2,3,1,3,4,4];
    choices = [1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1];
    
    idx = randperm(12);
    stats.errors = zeros(12,1);
    stats.states = moves(idx,1);
    stats.targets = moves(idx,2);
    stats.tOnset = zeros(12,1);
    stats.tChoice = zeros(12,1);
    for i=1:length(idx)
        clearkeys();
        move = moves(idx(i),:);
        cgpencol(1,1,1);
        cgdrawsprite(1,0,0);
        cgfont(params.fontFamily, params.fontSizeLarge);
        cgtext('Wie viel ist der folgende Zug wert?',0,220*params.scaling);
        cgtext('1: 140, 2: 20, 3: -20, 4: -70',0,190*params.scaling);
        drawArrow(move(1),move(2), choices(idx(i)), params, true);
        stats.tOnset(i) = cgflip(0,0,0) * 1000;
        k = waitkeydown(inf, [28, 29, 30, 31]);
        stats.tChoice(i) = time();
        if k - 27 == solutions(idx(i))
            cgdrawsprite(1,0,0);
            drawArrow(move(1),move(2), choices(idx(i)), params);
            cgtext(sprintf('Korrekt!'),0,220*params.scaling);
            cgtext(sprintf('Dieser Zug ist %i Punkte wert.', money(solutions(idx(i)))),0,190*params.scaling);
            cgflip(0,0,0);
        else
            cgdrawsprite(1,0,0);
            drawArrow(move(1),move(2), choices(idx(i)), params);
            cgtext(sprintf('Leider falsch.'),0,220*params.scaling);
            cgtext(sprintf('Dieser Zug ist %i Punkte wert.', money(solutions(idx(i)))),0,190*params.scaling);
            cgflip(0,0,0);
            stats.errors(i) = 1;
        end
        wait(2000);
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
    
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgtext(sprintf('Gut gemacht. Sie hatten %i von %i richtig.', 12-sum(stats.errors),12),0,0);
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling)
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo]);
end % doTesting

