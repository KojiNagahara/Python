from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import numpy as np
from io import BytesIO
import logging
import logging.handlers
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from graph_form import GraphForm

app = Flask(__name__)
app.secret_key = "graphApp"
# CSRFトークン処理を有効にする
csrf = CSRFProtect(app)

def draw_graph(expression="a*(x**2)+b*x+c", 
    param={'a_value':1,'b_value':1,'c_value':1, 'start':0, 'end':10}):
    """グラフの画像データを生成する。
       expressionには入力された式の文字列が、
       paramには入力されたパラメータを収めたDictionaryが、
       start,endにはX軸の範囲がそれぞれ格納されている前提"""
    # グラフのコンテナであるFigureを生成
    fig = Figure()
    # 今回は1つしかグラフを書かないので行=列=1、indexも1
    ax = fig.add_subplot(111)

    # X軸の範囲は指定されているので等差数列（要素100の配列で始点、終点を含む）を生成
    start = param.get('start', 0)
    end = param.get('end', 10)
    
    x = np.linspace(start, end, 100)
    # 与えられたパラメータと式の評価結果によりグラフのY軸の数列を生成
    a = param.get('a_value', 1)
    b = param.get('b_value', 1)
    c = param.get('c_value', 1)
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
    form = GraphForm(request.form, meta={'locales': ['ja']})
    if request.method == 'POST':
        # 入力のバリデーション
        if form.validate_on_submit():
            app.logger.info("バリデーション成功")
            try:
                graph_data = draw_graph(form.expression.data, form.get_param())
            except ValueError as error:
                app.logger.error("グラフ生成失敗")
                app.logger.error(error)
                graph_data = None
        else:
            app.logger.info("バリデーション失敗")
            graph_data = None

        return render_template('index.html', form=form, graphData=graph_data) 
    else:
        app.logger.info("初期表示")
        # デフォルトデータを使用してグラフを描画する
        form.expression.data = 'a*(x**2)+b*x+c'
        form.a_value.data = 1
        form.b_value.data = 1
        form.c_value.data = 1
        form.x_start.data = 0
        form.x_end.data = 10

        return render_template('index.html', form=form, graphData=draw_graph())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)