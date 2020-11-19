import numpy as np

def mod(w, x1, x2):
  return np.sqrt(w*w + x1*x1)/np.sqrt(w*w + x2*x2)

def fase(w, x1, x2):
  return np.arctan(w/x1) - np.arctan(w/x2)

# w = 2
# x1 = 0.1
# x2=5
 
# print('{}*cos({}t + {})'.format(round(mod(w,x1,x2),3), w, round(np.degrees(fase(2,x1,x2)), 3 )))
