from flask import Flask    
from flask import Flask, request, jsonify
import os 
import gunicorn
app = Flask(__name__)                                                                         

                                                                                                      
@app.route('/send', methods=['GET'])                                                                                     

def My_code():
	
	ci = request.args.get("chat_id")
	os.system(f'python db.py {ci}')

	return('done')                                                                                  

if __name__ == '__main__':                                                                     

   app.run()                                                                                            