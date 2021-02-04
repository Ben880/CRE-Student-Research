function drawGame(activeState, params, timeLeft)
    cgdrawsprite(1,0,0);
    cgdrawsprite(2,params.coords.x(activeState),params.coords.y(activeState));
    cgdrawsprite(4,240*params.scaling,-180*params.scaling);
    cgfont(params.fontFamily, params.fontSizeMedium);
    if nargin==3
        cgtext(sprintf('%d',ceil(timeLeft)),0,200*params.scaling);
    end
end