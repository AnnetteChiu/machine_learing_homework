
function c=labelMP(amountAlchohol, meansVector,priorVector)
    
    letters=['M','Y','A','S'];
    probs=[0,0,0,0];
    for k=1:4
        probs(k)= 1/(2*sqrt(2*pi)) ...
            *exp(-(amountAlchohol-meansVector(k))^2/8) ...
            *priorVector(k);
    end
    p=0;n=0;
    for k=1:4
        if(p<probs(k))
            p=probs(k);
            n=k;
        end
    end
    c=letters(n);
end