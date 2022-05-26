import matplotlib.pyplot as plt
import base64
from io import BytesIO
import mne
import matplotlib
matplotlib.use("Agg")
def get_graph():

	buffer=BytesIO()
	plt.savefig(buffer,format='png')
	buffer.seek(0)
	image_png=buffer.getvalue()
	graph=base64.b64encode(image_png)
	graph=graph.decode('utf-8')
	buffer.close()
	return graph

def read(file):
	#data=mne.io.read_raw_edf('C:/Users/DIVYA/DESKTOP/MAJOR PROJECT/finalproject/'+file.name,preload=True)
	import mne
	data=mne.io.read_raw_edf(file.name,preload=True)
	return data


def get_plot(data):
	
	#data=mne.io.read_raw_edf('C:\\Users\\DIVYA\\Desktop\\MAJOR PROJECT\\FINALDATASET\\chb03_01.edf',preload=True)
	#data.plot(duration=50)
	#or
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=5)
	#plt.switch_backend('AGG')
	#plt.title('sales of items')
	#plt.plot(x,y)
	# plt.xticks(rotation=45)
	# plt.xlabel('item')
	# plt.ylabel('price')
	# plt.tight_layout()
	graph=get_graph()
	return graph

def get_beta_plot(data):
	low_freq, high_freq = 12.0, 30.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph

def get_alpha_plot(data):
	low_freq, high_freq = 8.0, 12.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph

def get_theta_plot(data):
	low_freq, high_freq = 4.0, 8.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23,scalings={"eeg":75e-6}, title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph


def get_delta_plot(data):
	low_freq, high_freq = 0.5, 4.0
	data = data.filter(low_freq, high_freq, n_jobs=4)
	data.plot(n_channels=23, scalings={"eeg":75e-6},title='Auto-scaled Data from arrays',
         show=True,color=dict(eeg='darkblue'), duration=15.0,start=10)
	graph=get_graph()
	return graph


def get_acc():

	plt.figure(figsize = (8,8))  

	import pandas as pd
	df_results = pd.DataFrame({'classifier':['Random Forest','Random Forest','XGBoost','XGBoost','Xtrees','Xtrees','CNN','CNN'],
                           'data_set':['train data ','test data']*4,
                          'accuracy':[99.98,95.8,99.91,96.63,99.99,97.16,97.21,94.27]})
                          
	import seaborn as sns
	sns.set_style("whitegrid")
	plt.rcParams.update({'font.size': 13})
	ax = sns.barplot(x = 'classifier', y = 'accuracy',hue = 'data_set', color= '#88cfff',data = df_results,palette="Paired")

	ax.set_xlabel('model', fontsize = 15)
	ax.set_ylabel('Accuracy', fontsize = 15)
	ax.tick_params(labelsize = 15)

	#Separate legend from graph
	plt.legend(bbox_to_anchor = (1.05, 1), loc = 4, borderaxespad = 0., fontsize = 12)
	for p in ax.patches:
	    width = p.get_width()
	    height = p.get_height()
	    x, y = p.get_xy() 
	    ax.annotate(f'{height:.2f}', (x + width/2, y + height*1.02), ha='center')

	

	
	graph=get_graph()
	return graph




