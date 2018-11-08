from flask import Flask, render_template
#import requests
#from collections import defaultdict


app = Flask(__name__)

#r = requests.get("http://api.wunderground.com/api/mykey/forecast/q/SouthAFrica/Stellenbosch.json")
#data = r.json()
#weather_data = defaultdict(list)
#
temp = ['Weg grade aa large eggs', 'Basil hayden', 'Weg rainbow sherbet', 'Weg ic garlic minced/oil', 'Wltn rainbow nonpareils', 'Wegf oregano', 'Greens, dandelion', 'Apl,red delicious', 'Weg crkd pepper blnd shak', 'Wegf thyme', 'Fyfga spk wtr orange 1l', 'Weg orange juice 16fo', 'Wb shal tym finishing btr', 'Wb micro mixed beans', 'Oc spray cranberry cktl', 'Cntry style bnls kfp', 'Demi glaze 8oz', 'Weg 1% large cott cheese', 'Weg bacon aplwd nitrit fr', 'Fyfga spk wtr berry  1l', 'Weg puff pastry sheet', 'Jones green apple   4/12z', 'Whlsm og blue agave', 'Weg ic tomato pesto sauce', 'Wb fyfga rstd verde', 'Peychaud bitters', 'Elijah craig bourbon 12yr', 'Wbo vanilla ic', "Barritt's brmda gngr beer", 'Weg white dist vinegar', 'Weg maraschino cherries', 'Wp - copper plate vodka', 'Weg mild gruyere-preshred', 'Squash, green', 'Fyfga all purp flr unblch', 'Tt dc wafers -bulk', 'Weg sea salt fine', 'Wb savory finishing sauce', 'Fresh limes', 'Weg ic mild links', 'Wb fyfga granulated sugar', 'Wb garlic peeled', 'Wb pure mdtrn bln olv oil', 'Weg organic basting oil', 'Lemons bulk', 'Onion, red']
#temp = ["Hi" , "Hello"]
weather_data = {}
#counter = 0
#for day in data['forecast']['simpleforecast']['forecastday']:
#    date= day['date']['weekday'] + ":"
#    cond=  "Conditions: ", day['conditions']
#    temp= "High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C"
#
#
#    counter = counter + 1

#weather_data[0].append("Hi")
#weather_data[1].append("Hello")
#weather_data[0] = " hi"
#weather_data[1] = " hello"
#    weather_data[counter].append(date)
#    weather_data[counter].append(cond)
#    weather_data[counter].append(temp)
i = 0
for val in temp:
    weather_data[i] = val
    i = i + 1

#return weather_data

@app.route('/')
def home():
    return render_template('home.html', weather_data=weather_data)

#def publish():
#
#def subscribe():
#
#def advertise():
#
#def event_generator():
#
#def subscription_generator():
#    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
