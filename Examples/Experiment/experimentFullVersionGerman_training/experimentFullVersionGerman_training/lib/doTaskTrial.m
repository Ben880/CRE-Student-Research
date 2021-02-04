function stats = doTaskTrial(state, depth, params, isTimed, immFeedb)
    stats = struct();
    stats.keyTimes = [];
    stats.choices = [];
    stats.rewards = [];
    stats.states = state;

    clearkeys();
    if params.debugmode == 0 && strcmp(params.loc,'Z')
        clearserialbytes(params.boxport);
    end
    stats.tStart = time();
    while 1
        if ~(nargin==5 && immFeedb)
            drawGame(stats.states(1), params);
            cgfont(params.fontFamily, params.fontSizeLarge);
            cgtext(sprintf('Sie haben %d Züge', depth),0,210*params.scaling);
            if isTimed
                countdown = (params.planningTime-time()+stats.tStart) / 1000;
                cgtext(sprintf('%d', ceil(countdown)),0,185*params.scaling);
            else
                cgtext('Bitte erst alle Züge eingeben, um das Ergebnis zu sehen.',0,185*params.scaling);
            end
        else
            drawGame(stats.states(end), params);
            cgfont(params.fontFamily, params.fontSizeLarge);
            cgtext(sprintf('Sie haben %d Züge', depth),0,210*params.scaling);
            if length(stats.states) > 1
                drawArrow(stats.states(end-1), stats.states(end), stats.choices(end), params);
            end
        end
        cgflip(0,0,0);
        [ks, kt] = waitAndCheckKey(time()+100, params);
        if ~isempty(ks)
            ch = getChoicesFromKeys(params, ks);
            for c=1:length(ch)
                stats.rewards = [stats.rewards; params.rMatrix(state, ch(c))];
                state = updateState(params, state, ch(c));
                stats.states = [stats.states; state];
            end
            stats.choices = [stats.choices; ch];
            stats.keyTimes = [stats.keyTimes; kt];
            stats.tInput = kt(1);
        end
        if ~isTimed && length(stats.choices) == depth || ...
            isTimed && ~isempty(stats.choices)
            break, 
        end;
        if isTimed && time() - stats.tStart >= params.planningTime
            stats.tInput = time();
            break;
        end
    end
    if isTimed
        drawGame(stats.states(1), params);
        cgfont(params.fontFamily, params.fontSizeLarge);
        cgtext(sprintf('Sie haben %d Züge', depth),0,210*params.scaling);
        cgtext('Züge jetzt eingeben', 0, 185*params.scaling);
        cgflip(0,0,0);
        tWait = params.timeInputBase + params.timeInputPerChoice * depth;
        % wait until time is up or all stats.choices have been made
        while 1
            [ks, kt] = waitAndCheckKey(time()+100, params);
            if ~isempty(ks)
                maxadd = min(depth-length(stats.choices), length(ks));
                ch = getChoicesFromKeys(params, ks);
                for c=1:maxadd
                    state = updateState(params, state, ch(c));
                    stats.states = [stats.states; state];
                end
                stats.choices = [stats.choices; ch(1:maxadd)];
                stats.keyTimes = [stats.keyTimes; kt(1:maxadd)];
            end
            if length(stats.choices) == depth || time() - stats.tInput >= tWait
                break;
            end
        end
    end
    stats.tInputEnd = time();
    if nargin==5 && immFeedb
        drawGame(stats.states(end), params);
        drawArrow(stats.states(end-1), stats.states(end), stats.choices(end), params);
        cgflip(0,0,0);
        wait(800);
        drawGame(stats.states(end), params);
        cgfont(params.fontFamily, params.fontSizeLarge);
        cgtext(sprintf('Sie haben insgesamt %d', sum(stats.rewards)), 0, 20*params.scaling);
        if sum(stats.rewards) >= 0
            cgtext('Punkte gewonnen.', 0, -5*params.scaling);
        else
            cgtext('Punkte verloren.', 0, -5*params.scaling);
        end
        cgflip(0,0,0);
        wait(2000);
    else
        wait(params.getPreFeedbackBreakDuration());
        stats.tFeedback = time();
        [stats.rewards, stats.tArrow] = showFeedback(stats.states, stats.choices, depth, params);
    end
end