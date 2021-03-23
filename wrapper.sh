export FLASK_APP=/home/ubuntu/flaskVirtualEnv1/venv/git/ProsecuteJournalists/helloworld.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port 443 --cert=/etc/letsencrypt/live/ad-astra.hu/fullchain.pem --key=/etc/letsencrypt/live/ad-astra.hu/privkey.pem
