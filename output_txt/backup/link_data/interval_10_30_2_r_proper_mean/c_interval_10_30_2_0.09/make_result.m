link_number=5;
path=pwd;
result=[]
flow_number=0
average_number=5

for i=1:link_number

fprintf(strcat('link',num2str(i),'\n')) 
path=strcat(path,'/',num2str(i),'/');
path_find=strcat(path,'bw*.txt');
file_list=dir(path_find);
file_number=length(file_list);


for j=1:file_number
    file_list(j).name;
    file_name_vector=(file_list(j).name);
    a=load(strcat(path,file_name_vector));
    v=genvarname('result',who);
    eval([v ' =a']);
    flow_number=flow_number+1
    
end

path=pwd;

end



length_vector=[];
for i=1:flow_number
    
p=strcat('result',num2str(i));
length_vector=[length_vector,length(eval(p))];

end
result_length=min(length_vector)


final_result=zeros(result_length,1);
for i=1:flow_number
   
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
title('All link usage')

grid on



  