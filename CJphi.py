
# coding: utf-8

# In[2]:

from cantera import *
from SDToolbox import *
import matplotlib.pyplot as plt

P=100000
T=300
PHImin=0.2
Xmin=0.2
Xmax=5
Xstep=0.2
Xstep_no=int((Xmax-Xmin)/Xstep)+1

Xmin_coarse=0.5
Xmax_coarse=5
Xstep_coarse=0.5
Xstep_coarse_no=int((Xmax_coarse-Xmin_coarse)/Xstep_coarse)+1


mech='h2air_highT.cti'

CJ = []
CJ_phi = []
X=Xmin

xmlmech = 'h2air_highT.xml'
output_frequency = 1
output_file_name = 'znd_phi_series'

for i in range(0, Xstep_no+1):
    q={'H2':X, 'O2':1, 'N2':3.76}
    [cjspeed,_]=CJspeed(P, T, q, mech,-1)
    CJ.append(cjspeed)
    CJ_phi.append(X/2)
    X+=Xstep

X=Xmin_coarse
        
for i in range(0, Xstep_coarse_no+1):
    
    q={'H2':X, 'O2':1, 'N2':3.76}
    [cjspeed,_]=CJspeed(P, T, q, mech,-1)
    znd = 'znd' + str(i)
    file = open( "pyinp_phi_" + str(i) + ".inp", 'w')
    file.write('#Initial_Temperature_(K)\n%.16e\n' % T);
    file.write('#Initial_Pressure_(Pa)\n%.16e\n' % P);
    file.write('#Shock_Velocity\n%.16e\n' % cjspeed);
    file.write('#Mole_Fractions_(string)\n%s\n' % X);
    file.write('#Mechanism_File_-_xml_format_(string)\n%s\n' % xmlmech);
    file.write('#Writing_output_frequency_flag(1_to_very_large)\n%s\n' % output_frequency);
    file.write('#print_progress(1or0)\n%s\n' % 0); # use 1 to print znd progress to screen
    file.write('#Output_file_title(string)\n%s\n' % znd);
    file.write('#Species_Number\n%s\n' % 0);
    file.write('#Species\n%s\n' % -1);
    file.close()
    X+=Xstep_coarse

    
x=CJ_phi
y=CJ

plt.figure(figsize=(8,6))
plt.plot(x, y, '-', color='orange')
plt.grid()
plt.xlabel(r'Equivalence ratio')
plt.ylabel("CJ speed [m/s]")
plt.savefig('2.png', bbox_inches='tight')
plt.show()






# In[35]:

print cj_speed


# In[ ]:




# In[ ]:



