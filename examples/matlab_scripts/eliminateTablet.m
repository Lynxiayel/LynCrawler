function newdata=eliminateTablet(data,sizeBound)
%extract all phones which are not Tablet
%judged by size<sizeBound, in inches
index=data(:,3)<sizeBound;
newdata=[data(index,1) data(index,2) data(index,3)];
end