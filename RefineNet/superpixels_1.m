  A = imread('San_2008_PauliRGB.bmp');  
  [L,N] = superpixels(A,6000);
  figure
  BW = boundarymask(L);
  imshow(imoverlay(A,BW,'cyan'))

  % Set color of each pixel in output image to the mean RGB color of the
  % superpixel region.
  outputImage = zeros(size(A),'like',A);
  idx = label2idx(L);
  numRows = size(A,1);
  numCols = size(A,2);
  for labelVal = 1:N
      redIdx = idx{labelVal};
      greenIdx = idx{labelVal}+numRows*numCols;
      blueIdx = idx{labelVal}+2*numRows*numCols;
      outputImage(redIdx) = mean(A(redIdx));
      outputImage(greenIdx) = mean(A(greenIdx));
      outputImage(blueIdx) = mean(A(blueIdx));
  end
  save sp_result_tu L
%   figure
%   imshow(outputImage)
  imwrite(L,'sp_result_tu.bmp');
% %     lenna = rgb2gray(lenna);

%     %-------------------------------------------------------------  
%     %�Դ���  
%     lenna=double(lenna);  
%     lenna_1 = edge(lenna,'log');   
%     subplot(122)  
%     imshow(lenna_1,[]);title('LoG 0.5')  
%     
%     se=strel('disk',3');%Բ���ͽṹԪ��
%     fo=imclose(lenna_1,se);%ֱ�ӱ�����
%     figure,imshow(fo);
