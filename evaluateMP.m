%Result:
%6: 0.55
%18: 0.57
%54: 0.58
%162: 0.57

function accuracy=evaluateMP(testData,meansVector,priorVector)

    trueCnt=0;
    letters=['M','Y','A','S'];
    for k=1:size(testData,1)
        l=labelMP(testData(k,2),meansVector,priorVector);
        trueLabel=find(letters==l);
        if (trueLabel==testData(k,1))
            trueCnt=trueCnt+1;
        end
    end
    accuracy = trueCnt/size(testData,1);
end
    

