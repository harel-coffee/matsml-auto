#  By Huan Tran (huantd@gmail.com), 2021                 
#
import pandas as pd

##### (1) OBTAIN A RAW DATASET

# (2) FINGERPRINT THE RAW DATA
from matsml.fingerprint import Fingerprint

sum_list='/home/huan/work/matsml/examples/ex2_crystals/crystals/sum_list.csv'
data_loc='/home/huan/work/matsml/examples/ex2_crystals/crystals/'
fp_type='pesm_crystals'
n_atoms_max=28
struct_format='xyz'
fp_file='fp.csv'
fp_dim=50
verbosity=0

data_params={'sum_list':sum_list,'data_loc':data_loc,'fp_file':fp_file,
    'struct_format':struct_format,'fp_type':fp_type,'fp_dim':fp_dim,
    'verbosity':verbosity,'n_atoms_max':n_atoms_max}

fp=Fingerprint(data_params)
fp.get_fingerprint()

# (3) TRAIN A MODEL
from matsml.models import FCNeuralNet

# data parameters
data_file='fp_PRM18_MgSi_structs.csv.gz'
id_col=['id']         
y_cols=['target']
comment_cols=[]
n_trains=0.85
sampling='random'
x_scaling='minmax'      
y_scaling='minmax' 

data_params={'data_file':data_file, 'id_col':id_col,'y_cols':y_cols,
    'comment_cols':comment_cols,'y_scaling':y_scaling,'x_scaling':x_scaling,
    'sampling':sampling, 'n_trains':n_trains}

# Model parameters
layers=[8,8]                     # list of nodes in hidden layers
epochs=300                      # Epochs
nfold_cv=5                       # Number of folds for cross validation
use_bias=True                    # Use bias term or not
model_file='model.pkl'           # Name of the model file to be created
loss='mse'                       #
metric='mse'                     #
verbosity=0
batch_size=32                    #
activ_funct='tanh'               # Options: "tanh","relu","sigmoid","softmax","softplus","softsign","selu","elu","exponential"
optimizer='nadam'                # options: "SGD","RMSprop","Adam","Adadelta","Adagrad","Adamax","Nadam","Ftrl"

model_params={'layers':layers,'activ_funct':activ_funct,'epochs':epochs,
    'nfold_cv':nfold_cv,'optimizer':optimizer,'use_bias':use_bias,
    'model_file':model_file,'loss':loss,'metric':metric,
    'batch_size':batch_size,'verbosity':verbosity,'rmse_cv':False}

# Compile a model
model=FCNeuralNet(data_params=data_params,model_params=model_params)

# Train the model
model.train()

# Load the saved model (in file_model)
#model.predict()