from flask import Flask
from marketplaces import


app = Flask(__name__)


@app.route('/')
def index():
    h1 = "<h1>Marketplaces</h1>"
    ol = '''
            <div>
                <label for="marketplace">Marketplace choices</label>
                <select name="marketplace" required>
                    <option value="">Choose a marketplace</option>
                </select>
            </div>
        '''

    return f'{h1} {ol}'


app.run()