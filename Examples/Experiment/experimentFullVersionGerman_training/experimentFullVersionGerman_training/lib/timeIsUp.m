function timeOut = timeIsUp(params, maxDuration)
    if toc >= maxDuration
        timeOut = 1;
    else
        timeOut = 0;
    end 
end