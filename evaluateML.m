%Result:
%6: 0.54
%18: 0.53
%54: 0.53
%162: 0.52

function accuracy=evaluateML(testData, meansVector)
    trueCnt=0;
    letters=['M','Y','A','S'];
    for k=1:size(testData,1)
        l=labelML(testData(k,2),meansVector);
        trueLabel=find(letters==l);
        if (trueLabel==testData(k,1))
            trueCnt=trueCnt+1;
        end
    end
    accuracy = trueCnt/size(testData,1);
end