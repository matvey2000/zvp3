import pickle
f=open('bl.pkl','wb')
pickle.dump(0,f)
f.close()
f=open('dst.pkl','wb')
pickle.dump(['дремалой.jpg'],f)
f.close()