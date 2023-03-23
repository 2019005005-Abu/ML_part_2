##NumPy
##------------------------
import numpy as np;
##Normal distribution
ND=np.random.standard_normal((3,4));
print(ND)
##Uniform distribution
print("\n");
UD=np.random.uniform(1,12,(3,4));
print(UD);
print(np.random.rand());
print("\n");
print(np.random.randint(1,50,(2,5)));
print('\n');
Ze=np.zeros((3,4));
print(Ze);
print('\n');
Ones=np.ones((3,4));
print(Ones);
print('\n');
random_arr=np.random.randint(1,50,(2,5))
filter_Ar=np.logical_and(random_arr>30,random_arr<50);
print(filter_Ar);
Filter_Random=random_arr[filter_Ar];
print(Filter_Random);

##Statics using numpy
Data_N=np.array([1,3,4,5,7,9]);
print(Data_N);

Mean_N=np.mean(Data_N);
print(Mean_N);

Median_N=np.median(Data_N);
print(Median_N);

Var_n=np.var(Data_N);
print(Var_n);

SD_N=np.std(Data_N);
print(SD_N);

print("\n");
NUMPY_Arr=np.array([[1,2,3],[4,6,7]]);
print(NUMPY_Arr);
print("\n");
var_Nump=np.var(NUMPY_Arr,axis=1);
print(var_Nump);
print('\n');
var_Nump2=np.var(NUMPY_Arr,axis=0);
print(var_Nump2);

##





