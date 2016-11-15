path=pwd;
result=[]
average_number=1
flow_number_in_link=0
length_vector=[];


path_find=strcat(path,'/','bw*.txt');
file_list=dir(path_find);
file_number=length(file_list);
flow_number_in_link=file_number

for i=1:file_number

file_list(i).name;
file_name_vector=(file_list(i).name);

a=load(strcat(path,'/',file_name_vector));
v=genvarname('result',who);
eval([v ' =a']);
    
end




for i=1:flow_number_in_link
    
p=strcat('result',num2str(i));
length_vector=[length_vector,length(eval(p))];

end
result_length=min(length_vector)




final_result=zeros(result_length,1);
for i=1:flow_number_in_link
   
    p=strcat('result',num2str(i));
    z=eval(p);
    final_result=final_result + z(1:result_length);
    
end




average_bw=[]
for k=1:fix(result_length/average_number)

mean_bw=mean(final_result(average_number*(k-1)+1:average_number*k));
average_bw=[average_bw,mean_bw]

end


if mod(result_length,average_number) ~= 0
mean_bw=mean(final_result(fix(result_length/average_number)*average_number+1:result_length));
average_bw=[average_bw,mean_bw] 
end


hold on
plot(average_bw,'LineWidth',2)

xlabel('Time');
ylabel('Bandwidth(Mbps)');
title('link usage')

grid on

  