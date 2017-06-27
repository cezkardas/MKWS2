clear;clc;

P1 = 100000;
T1 = 300;
Xmin=1;
Xmax=5;
Xstep=0.2
Xstepno=int64((Xmax-Xmin)/Xstep);
X=Xmin


for n = 1:(Xstepno)
    if X==2.4
        X=2.6
    end
    '--------NEXT-PHI----------'
    Phi=X/2
    xstr=num2str(X)
    q = strcat('H2:',xstr, ' O2:1', ' N2:3.76');
    mech = 'h2air_highT.cti';  
    species_number_flag = -1
    [cj_speed,gas2] = znd_CJ(1, P1, T1, q, mech, 'h2air', 2);
    cj_speed
    X=Xstep+X
end




