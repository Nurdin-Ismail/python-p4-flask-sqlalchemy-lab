#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal= Animal.query.filter(Animal.id == id).first()
    
    if not animal:
        response_body = '<h1>404 animal not found</h1>'
        response = make_response(response_body, 404)
        return response
    else:
        response_body = f'''
        <h1>Info about {animal.name}</h1>
        <h3>Id: {animal.id}</h3>
        <h3>Species: {animal.species}</h1>
        <h3>Zookeeper: {animal.zookeeper.name}</h1>
        <h3>Enclosure: {animal.enclosure.environment}</h3>
        '''
        response= make_response(response_body, 200)
        return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    
    
            
                
    if not zookeeper:
        response_body = '<h1>404 zookeeper not found</h1>'
        response = make_response(response_body, 404)
        return response
    else:
        
        nemo = [i.name for i in zookeeper.animals]
        response_body = f'''
        <h1>Info about {zookeeper.name}</h1>
        <h3>Birth Date: {zookeeper.birthday}</h3>
        <h3> Animals:</h3>
        <h3></h3>
        ''' + 'Animal:' + ' <br> Animal: '.join([str(i) for i in nemo])
        
        
        response= make_response(response_body, 200)
        return response
        
        
    

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    
    
    if not enclosure:
        response_body = '<h1>404 enclosure not found</h1>'
        response = make_response(response_body, 404)
        return response
    else:
        
        nemo = [i.name for i in enclosure.animals]
        response_body = f'''
        <h1>Id: {enclosure.id}</h1>
        <h3>Enclosure: {enclosure.environment}</h3>
        <h3> Animals:</h3>
        <h3></h3>
        ''' + 'Animal:' + ' <br> Animal: '.join([str(i) for i in nemo])
        
        
        response= make_response(response_body, 200)
        return response
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
