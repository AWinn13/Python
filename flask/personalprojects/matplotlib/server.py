# from flask import Flask, render_template
# import matplotlib.pyplot as plt
# import io
# import base64

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Generate a line plot
#     x = [1, 2, 3, 4, 5]
#     y = [2, 4, 1, 5, 3]
#     plt.plot(x, y, label='Line 1')

#     # Generate a bar plot
#     x2 = [1, 2, 3, 4, 5]
#     y2 = [4, 2, 5, 1, 3]
#     plt.bar(x2, y2, label='Bar 1')

#     # Generate a scatter plot
#     x3 = [1, 2, 3, 4, 5]
#     y3 = [3, 5, 2, 4, 1]
#     plt.scatter(x3, y3, label='Scatter 1', color='red')

#     # Add a legend to the plot
#     plt.legend()

#     # Add a grid to the plot
#     plt.grid(True)

#     # Add x and y axis labels
#     plt.xlabel("X axis")
#     plt.ylabel("Y axis")

#     # Add a title to the plot
#     plt.title("Multiple Plots")

#     # convert the plot to a PNG image
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)
#     plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')

#     # return the plot to the template
#     return render_template('index.html', plot_url=plot_url)

# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Generate a line plot
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 5, 3]
    plt.plot(x, y, label='Line 1')

    # Generate a bar plot
    x2 = [1, 2, 3, 4, 5]
    y2 = [4, 2, 5, 1, 3]
    plt.bar(x2, y2, label='Bar 1')

    # Generate a scatter plot
    x3 = [1, 2, 3, 4, 5]
    y3 = [3, 5, 2, 4, 1]
    plt.scatter(x3, y3, label='Scatter 1', color='red')

    # Add a legend to the plot
    plt.legend()

    # Add a grid to the plot
    plt.grid(True)

    # Add x and y axis labels
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    # Add a title to the plot
    plt.title("Multiple Plots")

    # convert the plot to a PNG image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')

    # return the plot to the template
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run()
