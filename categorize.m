images = [];

%set = [1,3,4,7,10];
set = [2,5,6,8,9];

for i=1:40
    str = strcat('.\att_faces\s', int2str(i));
    
    for j=1:10
        if ismember(j, set) % mod(j, 2) == 0
            read = strcat(str, '\' ,int2str(j), '.pgm');
            image = imread(read);
            image = reshape(double(image), 1, []);
            images = [images; image];
        end
    end
end

Ws = dlmread('Ws.txt');
W0s = dlmread('W0s.txt');

indexes = [];
correct = 0;

for i=1:200
   
   temps = [];
   
   for j=1:40
        temp = dot(images(i,:), Ws(j,:)) + W0s(j);
        temps = [temps; temp];
   end
   
   m = max(temps);
   
   index = find(temps == m);
   
   indexes = [indexes; index];
   
   x = index;
   
   y = index;
   
   y = (y-1)*5;
   x = x*5;
   
   if i > y && i <= x
        correct = correct + 1;
   end   
end

disp(strcat(int2str((correct/200)*100), '% accuracy'));