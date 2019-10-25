from app import app
import pymysql
from db_config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/region/', methods=['POST'])
def add():
    try: 
        _json = request.json        
        _region = _json['region']
       

        if request.method == 'POST':
            sql = 'INSERT INTO region(region) VALUES (%s)'
            data = (_region)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Region Saved')
            resp.status_code = 200
            return resp
        else :
            return 'not_found'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/region/', methods=['GET'])
def all():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM region')
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally: 
        cursor.close()
        conn.close()

@app.route('/region/<int:id>')
def findById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM REGION WHERE IDREGION = $s', id)
        row = cursor.fetchone(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally: 
        cursor.close()
        conn.close()

@app.route('/region/<int:id>', methods=['PUT'])
def update(id):
    try:
        _json = request.json
        _id = id
        _region = _json['region']
        
        if request.method == 'PUT':
            sql = 'UPDATE region SET region=%s WHERE idregion=%s'
            data = (_region,_id)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Region updated')
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally: 
        cursor.close()
        conn.close()

@app.route('/region/<int:id>', methods=['DELETE'])
def delete(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM region WHERE idregion=%s", (id,))
		conn.commit()
		resp = jsonify('Region deleted')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()       

if __name__ == "__main__":
    app.run(debug=True,host="10.40.91.10")