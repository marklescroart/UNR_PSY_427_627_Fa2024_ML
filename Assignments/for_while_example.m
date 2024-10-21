% for / while example

% i = 1;
% while i <= 10 % (SOME STATE)
%     disp(i)
%     i = i + 1;
% end





% for / while example

i = 1;
start = GetSecs;
now = GetSecs;
while now <= start+5 % (SOME STATE)
    now = GetSecs;
    %disp(i)
    i = i + 1;
end
    