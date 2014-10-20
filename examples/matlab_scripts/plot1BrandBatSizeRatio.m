function plot1BrandBatSizeRatio(data,brand,brandToExtract, sizeBound)
if ~strcmp(brandToExtract,'')
    tmpData=extractBrand(data,brand,brandToExtract);
else
    tmpData=data;
end
tmpDataNoTab=eliminateTablet(tmpData,sizeBound);
ratio=tmpDataNoTab(:,2)./tmpDataNoTab(:,3);
scatter(tmpDataNoTab(:,1),ratio);
end