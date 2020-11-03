%{
Markov decision-making task, originally used in Tanaka et al. (2006),
then adopted by Neir Eshel and Niall Lally.
This was rewritten, extended and translated to German in March 2015 
by Daniel Renz, renz@biomed.ee.ethz.ch.
The task consists of three parts. This is the third part, the task. This 
is programmed to run with an fMRI scanner.

The task runs for params.maxTaskDuration seconds. At half time, there is a
short break.
%}

function pruneTaskMRI()
    % options -----------------------------------------------------------
    clear all
    addpath('Cogent2000v1.32/Toolbox', 'lib');
    params.scannermode = 1;

    % enter subject details
    params= getParticipantCode(params);
    params.savestr = [params.savestr, '_task'];
    params = getParams(params);

    % init and start cogent
    initStartCogent(params);
    makeCogentSprites(params);

    maxdepth = 6;
    nTrials = length(params.planningDepths); 
    results.startDateTime = datestr(now,0);
    results.keyTimes = zeros(nTrials, maxdepth);
    results.choices = zeros(nTrials, maxdepth);
    results.states = zeros(nTrials, maxdepth + 1);
    results.rewards = zeros(nTrials, maxdepth);
    results.tStart = zeros(nTrials,1);
    results.tInput = zeros(nTrials,1);
    results.tFeedback = zeros(nTrials,1);
    results.tArrow = zeros(nTrials,maxdepth);
    results.tInputEnd = zeros(nTrials,1);
    results.tEnd = zeros(nTrials,1);

    % wait for both researcher and participant to confirm that they are ready
    if params.scannermode==1
        cgpencol(1,1,1)
        cgtext('Obere Zeile',0,210*params.scaling); 
        cgtext('Können Sie beide Zeilen ganz oben und',0,25*params.scaling); 
        cgtext('unten komplett lesen?',0,0);
        cgtext('Forscher bitte mit SPACE bestätigen.',0,-25*params.scaling);
        cgtext('Untere Zeile',0,-190*params.scaling);
        cgflip(0,0,0);
        waitkeydown(inf,71);
    end
    
    doTaskTraining(params);
    
    if params.scannermode==1
        cgpencol(1,1,1)
        cgtext('Alles ist nun bereit, um das Experiment zu beginnen.',0,50*params.scaling);
        cgtext('Bitte gedulden Sie sich einen kleinen Moment, es geht gleich los.',0,-150*params.scaling);
        cgflip(0,0,0);
        if strcmp(params.loc,'Z')
            [~,t] = waitserialbyte(params.boxport, inf, params.sliceSignalNum);
            params.firstSliceTime = t(1);
            clearserialbytes(params.boxport);
        else
            clearkeys();
            [~, t] = waitkeydown(inf, params.sliceSignalNum);
            params.firstSliceTime = t(1);
        end
    else
        cgpencol(1,1,1)
        cgtext('Im fMRI Scannermode würde das Programm nun auf das Slice',0,50*params.scaling);
        cgtext('Signal des Scanners warten, und bei Empfang sofort mit dem',0,25*params.scaling);
        cgtext('Experiment beginnen.',0,0*params.scaling);
        cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling);
        cgflip(0,0,0);
        waitForKey(params, inf, [params.keyone, params.keytwo]);
    end
    
    cgpencol(1,1,1)
    cgtext('Jetzt geht es los!',0,25*params.scaling); 
    cgflip(0,0,0);
    wait(3000);
    
    % start timer
    tic;
    
    % main game loop ----------------------------------------------------
    haveToDoBreak = 1;
    timeOut = 0;
    
    for i=1:length(params.startingStates)
        stats = doTaskTrial(params.startingStates(i), ...
                    params.planningDepths(i), params, true);
        results.keyTimes(i,1:length(stats.keyTimes)) = stats.keyTimes;
        results.choices(i,1:length(stats.choices)) = stats.choices;
        results.states(i,1:length(stats.states)) = stats.states;
        results.rewards(i,1:length(stats.rewards)) = stats.rewards;
        results.tStart(i) = stats.tStart;
        results.tInput(i) = stats.tInput;
        results.tFeedback(i) = stats.tFeedback;
        results.tArrow(i,1:length(stats.tArrow)) = stats.tArrow;
        results.tInputEnd(i) = stats.tInputEnd;
        results.tEnd(i) = time();

        cgflip(0,0,0);
        wait(params.getPostTrialBreakDuration());
        timeOut = timeIsUp(params, params.maxTaskDuration);
        if timeOut, break, end;

        if haveToDoBreak && time()-params.firstSliceTime >= params.maxTaskDuration*1000/2
            cgtext('Kurze Pause.',0,20*params.scaling);
            clearkeys();
            cgflip(0,0,0);
            wait(25000);
            cgtext('Kurze Pause. Gleich geht es weiter!',0,20*params.scaling);
            cgflip(0,0,0);
            wait(5000);
	    haveToDoBreak = 0;
	    clearkeys();
        end
        eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
    end % main game loop
    
    results.keyTimes(i+1:end,:) = [];
    results.choices(i+1:end,:) = [];
    results.states(i+1:end,:) = [];
    results.rewards(i+1:end,:) = [];
    results.tStart(i+1:end) = [];
    results.tInput(i+1:end) = [];
    results.tFeedback(i+1:end) = [];
    results.tArrow(i+1:end,:) = [];
    results.tInputEnd(i+1:end) = [];
    results.tEnd(i+1:end,:) = [];
    results.depths =  params.planningDepths(1:i)';
    results.nTrials = size(results.keyTimes,1);
    
    results.type = 'task';

    eval(['save ' fullfile(params.savedir, params.savestr), ' params results']);
    
    cgfont(params.fontFamily, params.fontSizeLarge);
    cgtext('Danke für Ihre Teilnahme!', 0, 25*params.scaling)
    total =sum(results.rewards(:));
% 
%     if total < 0
%         cgtext(sprintf('Sie haben %d Punkte verloren.', abs(total)),0,-25);
%     else
%         cgtext(sprintf('Sie haben %d Punkte gewonnen.', total),0,-25);
%     end

    cgtext(sprintf('Forscher bitte SPACE drücken.'), 0, -100);

    % flips the end screen on and waits for a key press
    results.block_end_screen = cgflip(0,0,0);
    waitkeydown(inf, 71);
    stop_cogent;
end

% -----------------------------------------------------------------------
function doTaskTraining(params)
    % train 3 times with immediate feedback
    tic
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgpencol(1,1,1)
    cgtext('Wir wiederholen nun noch einmal kurz den letzten Teil',0,75*params.scaling);
    cgtext('des Trainings. Bitte versuchen Sie eine Zugfolge zu',0,50*params.scaling);
    cgtext('wählen, die Ihnen viele Punkte bringt.',0,25*params.scaling);
    cgtext('Bei den ersten paar Versuchen gibt es noch keine Zeitlimite.',0,0*params.scaling);
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling);
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);
    
    for i=1:3
        state = randi(6);
        depth = randi([2,3]);
        doTaskTrial(state, depth, params, false);
        cgflip(0,0,0);
        wait(800);
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
    
    % train 3 times with time constraint
    cgfont(params.fontFamily, params.fontSizeMedium);
    cgpencol(1,1,1)
    cgtext('Gut, nun wiederholen wir noch ein paar Übungen mit 9s Zeitlimite.',0,50*params.scaling);
	 cgtext('Sie können sich also 9s Zeit lassen um zu überlegen',0,25*params.scaling);
    cgtext('Bitte drücken Sie eine Taste.',0,-150*params.scaling);
    cgflip(0,0,0);
    waitForKey(params, inf, [params.keyone, params.keytwo], 5000);

    for i=1:3
        state = randi(6);
        depth = randi([2,3]);
        doTaskTrial(state, depth, params, true);
        cgflip(0,0,0);
        wait(params.getPostTrialBreakDuration());
        timeOut = timeIsUp(params, params.maxTrainingDuration2);
        if timeOut, return, end;
    end
               
end % doTaskTraining
