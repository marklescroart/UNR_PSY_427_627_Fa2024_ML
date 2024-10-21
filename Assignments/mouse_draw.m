
fps = 60;
ifi = 1/fps;
exp_time = 15;
n_second_tail = 3;
tdelta = 0.002;
n_dots = fps * n_second_tail;
dot_array = ones(n_second_tail, 2) * -1;

fullscreen = true;

% Below is only relevant for non-full-screen 
screenColor = [128,128,128];
if fullscreen
    screenRect = []; % for fullscreen
else
    screenSize = [800,600];
    screenUpperLeft = [30,30];
    screenRect = [screenUpperLeft, screenUpperLeft + screenSize];
end
% Choose screen, in case you want to display on another screen (e.g. the 
% projector in an fMRI experiment setup)
screens=Screen('Screens');
% Choosing the display with the highest display number is
% a best guess about where you want the stimulus displayed.
screenNumber=max(screens);

manual_quit = false;
ftime_array = zeros(fps * exp_time);
k = 1;
%% Set up screen
try
    % Skip sync tests for now (sync tests cause issues on Mac OS)
    Screen('Preference', 'SkipSyncTests', 1);         
    % Open window with default settings:
    win = Screen('OpenWindow', screenNumber, screenColor, screenRect);

    t0 = GetSecs;
    ftime = Screen('Flip', win);
    
    k = k+1;
    j = 1;
    while GetSecs < t0 + exp_time
        [x, y, buttons] = GetMouse(win);
        i = mod(j, length(dot_array));
        if i == 0
            i = length(dot_array)
        end
        if any(buttons)
            dot_array(i, :) = [x, y];
        end
        Screen('DrawDots', win, dot_array', 10, [1, 0, 0]);
        FlushEvents;
        while GetSecs < ftime + (ifi - tdelta)
            [keydown, rt, keycode] = KbCheck;
            if keydown
                disp("Manual quit!")
                manual_quit = true;
            end
        end
        if manual_quit
            break
        end
        ftime = Screen('Flip', win);
        ftime_array(k) = ftime;
        j = j+1;
    end
catch
    sca;
    error(lasterror)
end
sca


