function [rewards, tArrow] = showFeedback(states, choices, depth, params)
    rewards = zeros(1,depth);
    tArrow = zeros(1,depth);
    if length(choices) ~= depth
        cgfont(params.fontFamily, params.fontSizeLarge);
        cgtext('Sie haben nicht genug Züge eingegeben.', 0, 20);
        cgtext('Sie haben 200 Punkte verloren.',0,-20);
        cgflip(0,0,0);
        rewards(1) = -200;
        wait(2000);
        return;
    end
    for j=1:length(choices)
        drawGame(states(j+1), params);
        drawArrow(states(j), states(j+1), choices(j), params);
        rewards(j) = params.rMatrix(states(j) , choices(j));
        tArrow(j) = time();
        cgflip(0,0,0);
        wait(params.timePerFeedbackArrow);
    end
end