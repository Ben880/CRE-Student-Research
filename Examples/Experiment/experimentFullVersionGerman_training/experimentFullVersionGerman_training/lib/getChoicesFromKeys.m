function ch = getChoicesFromKeys(params, ks)
    ch = zeros(length(ks),1);
    for i = 1:length(ks)
        if ks(i) == params.keyone
            ch(i)=1;
        else
            ch(i)=2;
        end
    end
end