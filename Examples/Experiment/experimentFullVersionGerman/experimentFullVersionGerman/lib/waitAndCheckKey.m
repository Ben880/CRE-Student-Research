function [keyStrokes, keyTimes] = waitAndCheckKey(timeToWait, params)
    waituntil(timeToWait);
    if params.debugmode == 0 && strcmp(params.loc,'Z')
        readserialbytes(4);
        [keyStrokes, keyTimes, n] = getserialbytes(params.boxport, [params.keyone params.keytwo]); 
    else
        readkeys();
        [keyStrokes, keyTimes, n] = getkeydown([params.keyone params.keytwo]);
    end
end
