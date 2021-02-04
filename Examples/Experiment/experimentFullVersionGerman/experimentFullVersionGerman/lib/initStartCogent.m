function initStartCogent(params)
    config_keyboard();
    cgloadlib();
    cgopen(1,0,0,1);
    cgscale();
    config_log([params.savedir '/log_' params.savestr '_' datestr(now,'YYYYmmdd_HHMM') '.log']);
    
    %set random number generator
    rand('state', sum(100*clock));
    start_cogent;
end