
ifi = 1/60;
try
    Screen('Preference', 'SkipSyncTests', 1);         
    
    % Choosing the display with the highest display number.
    screens=Screen('Screens');
    screenNumber=max(screens);
    
    % Open window with default settings:
    screenColor = [128,128,128];
    screenSize = [400,400];
    screenUpperLeft = [200,200];
    screenRect = [screenUpperLeft, screenUpperLeft + screenSize];
    w=Screen('OpenWindow', screenNumber, screenColor, screenRect);

    dotPositions = rand(200, 2)' * 400;
    dotSizes = ones(200,1)' * 5;
    Screen('DrawDots', w, dotPositions, dotSizes, [255 255 255], [], 2);
    tflip = Screen('Flip', w);
    % Wait 
    tdown = Screen('Flip', w, tflip + 2 - ifi*.25);
    disp(tdown-tflip)
    tdown2 = GetSecs;

catch
    sca
end
sca