from flask import Flask, render_template, send_file
import pickle
import pandas as pd

app = Flask(__name__)

#титульная страница
@app.route('/')
def index():
    return render_template('index.html')

#загружаем модель
with open('KMeans.pkl', 'rb') as f:
    KMeans = pickle.load(f)

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, StringField, SelectField, RadioField
import os
from wtforms.validators import DataRequired, InputRequired
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

#форма получения вводимых данных
class MyForm(FlaskForm):
    genre = RadioField('genre', choices=["Female","Male"], validators=[InputRequired()])
    age = StringField('age', validators=[DataRequired()])
    income = StringField('income', validators=[DataRequired()])
    score = StringField('score', validators=[DataRequired()])

#форма получения данных из файла
class MyForm_file(FlaskForm):
    file = FileField('file', validators=[DataRequired()])

#Страница с предсказаниями модели
@app.route('/predict')
def pred():
    data_form = MyForm()
    file_form = MyForm_file()
    return render_template('pred.html', data_form=data_form, file_form=file_form)

@app.route('/data', methods=['POST'])
def data():
    data_form = MyForm()
    file_form = MyForm_file()

    if data_form.validate_on_submit():
        data = pd.DataFrame(
            {'Genre': [data_form.genre.data], 'Age': [data_form.age.data], 'Annual Income (k$)': [data_form.income.data],
             'Spending Score (1-100)': [data_form.score.data]})

        # преобразование данных
        data['Genre'] = data['Genre'].replace({'Female': 0, 'Male': 1})

        # делаем предсказание
        predictions = KMeans.predict(data)

        customers_clusters = {0: "customers with average annual income and average spending score",
                              1: "customers with hight annual income and hight spending score",
                              2: "customers with low annual income and low spending score",
                              3: "customers with hight annual income and low spending score",
                              4: "customers with low annual income and hight spending score"}
        return render_template('data.html', number=predictions[0], describe=customers_clusters.get(predictions[0]))

    return render_template('pred.html', data_form=data_form, file_form=file_form)

@app.route('/file', methods=['POST'])
def file():
    data_form = MyForm()
    file_form = MyForm_file()

    if file_form.validate_on_submit():
        f = file_form.file.data

        #получаем данные из файла
        df = pd.read_csv(f, names=['CustomerID', 'Genre', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])

        # преобразование данных
        df['Genre'] = df['Genre'].replace({'Female': 0, 'Male': 1})
        customer_id = df['CustomerID'].tolist()
        df = df.drop('CustomerID', axis=1)

        # делаем предсказание
        predictions = KMeans.predict(df)

        #сохраняем данные
        result = pd.DataFrame({"CustomerID": customer_id, "Cluster": predictions.tolist()})
        result.to_csv('predictions.csv', index=None)

        #возвращаем файл с пердсказаниями пользователю
        return send_file('predictions.csv', mimetype='text/csv', attachment_filename='predictions.csv', as_attachment=True)

    return render_template('pred.html', data_form=data_form, file_form=file_form)