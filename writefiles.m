images = [];

set = [1,3,4,7,10];
%set = [2,5,6,8,9];

for i=1:40
    str = strcat('.\att_faces\s', int2str(i));
    
    for j=1:10
        if ismember(j, set) %mod(j ,2) ~= 0
            read = strcat(str, '\' ,int2str(j), '.pgm');
            image = imread(read);
            image = reshape(double(image), 1, []);
            images = [images; image];
        end
    end
end

Z = -ones(200, 1);

j = 1;

X = images;

f = -ones(200, 1);

A = -eye(200);
a = zeros(200, 1);

B = [Z'; zeros(199, 200)];
b = zeros(200, 1);

Ws = [];
W0s = [];

%Zs = [];

ind1s = [];

for i=1:40
    
    bla = j;
    t = j;
    t = t+4;
    
    for index=bla:t   
        Z(index) = 1;
    end
    
    %Zs = [Zs; Z'];
    
    B = [Z'; zeros(199, 200)];
    
    H = (X*X').*(Z*Z');
    
    alpha = quadprog(H + eye(200)*0.1, f, A, a, B, b);
    
    m = max(alpha);
    
    ind1 = find(alpha == m);
    ind1s = [ind1s; ind1];
    
    z = Z(ind1);
        
    W = (alpha.*Z)'*X;
    Ws = [Ws; W];
    
    minusterm = dot(W, X(ind1,:));
    
    W0 = 1/z - minusterm;
    
    W0s = [W0s; W0];
    
    j = j+5;
    Z = -ones(200, 1);
end

dlmwrite('Ws.txt', Ws);
dlmwrite('W0s.txt', W0s);