from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    temp = ['Priya Murthy Bakchod', 'Weg rainbow sherbet', 'Weg ic garlic minced/oil', 'Wltn rainbow nonpareils', 'Wegf oregano', 'Greens, dandelion', 'Apl,red delicious', 'Weg crkd pepper blnd shak', 'Wegf thyme', 'Fyfga spk wtr orange 1l', 'Weg orange juice 16fo', 'Wb shal tym finishing btr', 'Wb micro mixed beans', 'Oc spray cranberry cktl', 'Cntry style bnls kfp', 'Demi glaze 8oz', 'Weg 1% large cott cheese', 'Weg bacon aplwd nitrit fr', 'Fyfga spk wtr berry  1l', 'Weg puff pastry sheet', 'Jones green apple   4/12z', 'Whlsm og blue agave', 'Weg ic tomato pesto sauce', 'Wb fyfga rstd verde', 'Peychaud bitters', 'Elijah craig bourbon 12yr', 'Wbo vanilla ic', "Barritt's brmda gngr beer", 'Weg white dist vinegar', 'Weg maraschino cherries', 'Wp - copper plate vodka', 'Weg mild gruyere-preshred', 'Squash, green', 'Fyfga all purp flr unblch', 'Tt dc wafers -bulk', 'Weg sea salt fine', 'Wb savory finishing sauce', 'Fresh limes', 'Weg ic mild links', 'Wb fyfga granulated sugar', 'Wb garlic peeled', 'Wb pure mdtrn bln olv oil', 'Weg organic basting oil', 'Lemons bulk', 'Onion, red']
    weather_data = {}
    i = 0
    for val in temp:
        weather_data[i] = val
        i = i + 1
    return render_template('home.html', weather_data=weather_data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4006)