from flask import render_template
from flask import Flask

app = Flask(__name__)
from flask import request

'649, 432'
chet = -1
data = [['Если ты будешь хлебом, в каком случае тебя можно будет подать к столу?',
         'Романтический ужин', 'На новый год', 'Пригожусь где угодно', 'Только если все совсем плохо',
         '/static/img/picture1.jpg'],
        ['А с чем тебя лучше всего есть?', 'С сыром и вином', 'с маслом', 'сладкий чай', 'я и сам справлюсь',
         '/static/img/picture2.jpg'],
        ['Друзья собирают компанию на шашлыки. Какая роль тебе уготована в тусовке?',
         'Я не поеду, там неудобно клеить патчи и вообще — я лечу на курорт',
         'Я буду в центре внимания!', 'Возьму с собой скакалку и гантели и встану утром раньше всех, сварю кофе',
         'Буду скромно сидеть в уголке и общаться с близкими друзьями',
         '/static/img/picture3.jpg'],
        ['Сколько тебя можно хранить?', 'Пару часов', 'День-два', 'Неделя', 'Уже поздно',
         '/static/img/picture4.jpg'],
        ['Что вкуснее всего на тосте?', 'Арахисовое масло. И джем. И нутелла', 'Просто масло', 'Что угодно',
         'Ничего, и так неплохо',
         '/static/img/picture5.jpg'],
        ['Какая мысль пугает тебя больше всего?', 'Деньги кончились', 'Ничего не вечно', 'Слишком много зла',
         'Я бесстрашный',
         '/static/img/picture6.jpg'],
        ['Ты следишь за своим питанием?', 'Считаю калории', 'Ем сладкое или жирное только до 12 дня',
         'Я от природы стройный человек, могу есть что угодно', 'Ем, что придется или что хочется',
         '/static/img/picture7.jpg'],
        ['Выбери любимый бутерброд', 'С авокадо', 'С куриным филе', 'С колбасой', 'С маслом',
         '/static/img/picture8.jpg'],
        ['Твое главное качество - это:', 'Безупречный вкус', 'Доброта', 'Позитив', 'стойкость',
         '/static/img/picture9.jpg'],
        ['Как ты видишь себя через 30 лет?', 'Глава крупной корпорации', 'Примерный семьянин', 'Добренький старичок',
         'Ой, не хочу так далеко думать',
         '/static/img/picture10.jpg'],
        ]

otv = 0


@app.route('/')
@app.route('/test', methods=['POST', 'GET'])
def test():
    global chet
    global data
    global otv
    if request.method == 'GET':
        chet += 1
        if chet < 10:

            return render_template('xleb.html', filename=data[chet][5], vopros=data[chet][0], otvet1=data[chet][1],
                                   otvet2=data[chet][2]
                                   , otvet3=data[chet][3]
                                   , otvet4=data[chet][4])
        else:
            return render_template('index.html', username='sdks')
    elif request.method == 'POST':
        chet += 1
        if chet < 10:
            otv += int(request.form.get('contact'))

            return render_template('xleb.html', filename=data[chet][5], vopros=data[chet][0], otvet1=data[chet][1],
                                   otvet2=data[chet][2]
                                   , otvet3=data[chet][3]
                                   , otvet4=data[chet][4])
        else:
            if otv <= 15:
                return render_template('index.html', text='Увы, вы всего-лишь плесневая горбушка',
                                       filename='/static/img/gorbuchka.jpg')
            elif otv <= 25:
                return render_template('index.html', text='Ого, похоже вы сладкий кексик',
                                       filename='/static/img/keks.jpg')
            elif otv <= 33:
                return render_template('index.html', text='Вау, вы самое настоящее хачапури',
                                       filename='/static/img/hacapuri.jpg')
            else:
                return render_template('index.html', text='Судя по всему, вы самый настоящий элитный тигровый хлеб',
                                       filename='/static/img/tigrovui.jpg')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
