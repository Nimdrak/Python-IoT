%mu_prime = 5.0352756;
%sigma_prime = 1.9550901;

%myfun =@(x) [(  (-mu_prime) + x(1) + x(2) * ((1/(sqrt(2*pi))) * exp(-0.5*(-x(1)/x(2)).^2)) / ( 1 - integral (@(t) (1/(sqrt(2*pi)))*exp(-0.5*t.^2),-inf,-x(1)/x(2))) ) ; ( -sigma_prime.^2 + x(2).^2 *(1 + (-x(1)/x(2))*((1/(sqrt(2*pi))) * exp(-0.5*(-x(1)/x(2)).^2)) / ( 1 - integral (@(t)  (1/(sqrt(2*pi))) * exp(-0.5*t.^2),-inf,-x(1)/x(2)))) - x(2).^2 * ( ((1/(sqrt(2*pi))) * exp(-0.5*(-x(1)/x(2)).^2)) / ( 1 - integral(@(t) (1/(sqrt(2*pi)))*exp(-0.5*t.^2),-inf,-x(1)/x(2)) ) ).^2 )]
%[x,fval]=fsolve(myfun,[mu_prime;sigma_prime])

A=importdata('/home/controller/IoT/input_mean.txt');
length=length(A);
result=zeros(length,2);
verifi=zeros(length,2);


for n=1:length
    mu_prime = A(n,1);    
    sigma_prime = A(n,2);

    myfun =@(x) [(  (-mu_prime) + x(1) + x(2) * ((1/(sqrt(2*pi))) * exp(-0.5*(-x(1)/x(2)).^2)) / ( 1 - integral (@(t) (1/(sqrt(2*pi)))*exp(-0.5*t.^2),-inf,-x(1)/x(2))) ) ; ( -sigma_prime.^2 + x(2).^2 *(1 + (-x(1)/x(2))*((1/(sqrt(2*pi))) * exp(-0.5*(-x(1)/x(2)).^2)) / ( 1 - integral (@(t)  (1/(sqrt(2*pi))) * exp(-0.5*t.^2),-inf,-x(1)/x(2)))) - x(2).^2 * ( ((1/(sqrt(2*pi))) * exp(-0.5*(-x(1)/x(2)).^2)) / ( 1 - integral(@(t) (1/(sqrt(2*pi)))*exp(-0.5*t.^2),-inf,-x(1)/x(2)) ) ).^2 )];
    [x,fval]=fsolve(myfun,[mu_prime;sigma_prime]);
           
    result(n,1) = x(1);
    result(n,2) = x(2);
    
end

f_output=fopen('/home/controller/IoT/input_mean_trun.txt','w');

for n=1:length
fprintf(f_output,'%f\t%f\n',result(n,1),result(n,2));
end




