# Projeto NLP

## Como utilizar?

Primeiramente baixar 'requirements.txt'

```python
pip install -r requirements.txt
```

Depois precisamos baixas os três modelos da biblioteca spacy
#### Portugues
```python
python -m spacy download pt
```
#### Ingles
```python
python -m spacy download en
```
#### Epanhol
```python
python -m spacy download es
```

## Como rodar

Para rodar abra seu terminal e execute os seguintes comandos
```python
export FLASK_APP=app.py
```
```python
flask run
```

### Postman
Temos apenas 3 rotas simples para configuração
```python
http://127.0.0.1:5000/language
```
Precisamos substitutir language por qual linguagem nós queremos
#### Portugues
```python
http://127.0.0.1:5000/portuguese
```
#### Ingles
```python
http://127.0.0.1:5000/english
```
#### Epanhol
```python
http://127.0.0.1:5000/spanish
```