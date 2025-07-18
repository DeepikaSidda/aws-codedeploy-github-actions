cat << EOF >app.py 

from flask import Flask 

app = Flask(__name__) 

 

@app.route('/') 

def demoapp(): 

  return 'Hello from EKS! This application is built using Github Actions on AWS CodeBuild' 

 

if __name__ == '__main__': 

  app.run(port=8080,host='0.0.0.0') 

EOF 
