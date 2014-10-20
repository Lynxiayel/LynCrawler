function dataSingleBrand=extractBrand(data,brandArray,brandtoExtract)
newdate=[];
newbattery=[];
newsize=[];

for i = 1:length(brandArray)
    if strcmp(brandArray(i),brandtoExtract)
        newdate=[newdate;data(i,1)];
        newbattery=[newbattery;data(i,2)];
        newsize=[newsize;data(i,3)];
    end
    dataSingleBrand=[newdate newbattery newsize];
end
end