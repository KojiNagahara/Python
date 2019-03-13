from flask import Flask, render_template, request
import numpy as np
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np

app = Flask(__name__)

def draw_graph(expression="a*(x**2)+b*x+c", 
    param={'a_value':1,'b_value':1,'c_value':1}, 
    start=0, end=10):
    """グラフの画像データを生成する。
       expressionには入力された式の文字列が、
       paramには入力されたパラメータを収めたDictionaryが、
       start,endにはX軸の範囲がそれぞれ格納されている前提"""
    # グラフのコンテナであるFigureを生成
    fig = Figure()
    # 今回は1つしかグラフを書かないので行=列=1、indexも1
    ax = fig.add_subplot(111)
    # X軸の範囲は指定されているので等差数列（要素100の配列で始点、終点を含む）を生成
    x = np.linspace(start, end, 100)
    # 与えられたパラメータと式の評価結果によりグラフのY軸の数列を生成
    a = param['a_value']
    b = param['b_value']
    c = param['c_value']
    y = eval(expression)
    # グラフを描画
    ax.plot(x, y)
    # グラフのPNG形式データを生成し、バイナリデータとして返す
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    img_data = urllib.parse.quote(png_output.getvalue())
    return img_data

@app.route('/graph/', methods=['GET', 'POST'])
def index():
    """GETは初回アクセス時の処理。
       POSTはパラメータ入力後の処理。
       初回表示時にデフォルトの式と各デフォルトパラメータによって描画されるグラフをセットして表示"""
    if request.method == 'POST':
        graph_data = draw_graph()
        return render_template('index.html', graphData=graph_data) 
    else:
        # デフォルトデータを使用してグラフを描画する
        return render_template('index.html', expression='a*(x**2)+b*x+c', graphData=draw_graph())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)