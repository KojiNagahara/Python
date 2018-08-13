import pylab
#先頭でのフォント宣言
font = {'family':'Noto Sans CJK JP'}
pylab.rc('font', **font)

pylab.figure(1)
min = -3
max = 4
y1 = [x1**2 for x1 in range(min,max)]
y2 = [x2**3 for x2 in range(min,max)]
pylab.plot(range(min,max), y1, color='red')
pylab.plot(range(min,max), y2, color='blue', linestyle='dashed')

#個別にフォントを指定する場合の記述
#igfont = {'family':'Noto Serif CJK JP'}
#pylab.title('xの2乗と3乗のグラフ（赤が２乗、青が３乗）', **igfont)

#表題と軸の意味を表示
pylab.title('xの2乗と3乗のグラフ（赤が２乗、青が３乗）')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.show()