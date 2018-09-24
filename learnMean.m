function lm = learnMean(trainData,classnumber)
    idx = find(trainData(:,1)==classnumber);
    lm = mean(trainData(idx,2));
end
    
    
    