function state = updateState(params, state, ch)
    for i = 1:length(ch)
        state = params.tMatrix(state, ch(i));
    end
end