import numpy
na = numpy.array([[1,3,5],[2,4,6]])   # Numpy の配列に変換する
nb = numpy.array([[1,4,7],[10,13,16]])
print(na+nb)                          # 配列naとnbの和
print(na*nb)                          # 配列naとnbの積
nc = numpy.array([[2,4],[3,6],[4,8]])
print(na.dot(nc))                     # 行列の積
print(numpy.dot(na,nc))               # 同上
print(na[1,2])
print(na.shape)        # 配列naの形状をタプルの形で返す。結果は(2,3)
print(na.reshape(3,2)) # 形を(3,2)に変更する。結果は
                       # array([[1,3],
                       #        [5,2],
                       #        [4,6]])
print(na.T)            # 転置行列
                       #  array([[1,2],
                       #         [3,4],
                       #         [5,6])
a = numpy.array([[1., 3.], [2., 4.]])
numpy.linalg.inv(a)    # 逆行列
                       # array([[-2. , 1.5],
                       #        [ 1. ,-0.5])
y = numpy.array([[5.],[7.]])
numpy.linalg.solve(a,y) # 方程式y=axを解く
                        # array([ 0.5],
                        #       [ 1.5])
