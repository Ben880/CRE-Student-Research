function [keyout, keytime] = waitForKey(params, duration, validKeyList, minWaitTime)
    if nargin == 4
        wait(minWaitTime);
    end
    if params.debugmode == 0 && strcmp(params.loc,'Z')
        clearserialbytes(params.boxport);
        [keyout, keytime] = waitserialbyte(params.boxport, duration, validKeyList);
    else
        clearkeys();
        [keyout, keytime] = waitkeydown(duration, validKeyList);
    end 
end
