import flask
import search
import pandas as pd
import numpy as np
import wikipedia
import re

def create_app():
    app = flask.Flask(__name__)

    @app.route('/')
    def root():
        return(flask.render_template('base.html'))

    @app.route('/results', methods=['POST'])
    def results():

        gene = [x.split(',') for x in flask.request.form.values()]
        data = search.get_count(gene)

        return(flask.render_template('base.html', results=data))

    return app


if __name__ == '__main__':
    APP = create_app()
    APP.run()

    # TODO
        # finish route from user input to results to get count
        # figure out how many buttons.
        # figure out how to take user inputs and add to list to itterate over
            # and return to user. (look at car model/app)
        #host to heroku. docker?



        # created connection from user to api.. clean up user input, pass in to
            # function so we can get count of web page,
        # conda env unit4sprint2