
%% Conduct timing test
nRepeats = 100;
timeToWait = 0.1;
times = zeros(nRepeats,1);
for j = 1:nRepeats
    % Get time prior to function of interest
    a = GetSecs; 
    % Function to test
    %WaitSecs(timeToWait); 
    % Get time after function of interest
    b = GetSecs; 
    times(j) = b-a;
end

%% Make a histogram
timeResolution = 0.001;
lookAhead = 0.01;
bins = (timeToWait-lookAhead):timeResolution:(timeToWait+lookAhead);
histogram(times, bins);
set(gca, 'fontsize', 24)