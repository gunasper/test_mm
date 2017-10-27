pyenv = python3

run: 
	$(pyenv) max_milhas/app.py
	
deps:
	$(pyenv) -m pip install -r requirements
	
docker:
	timestamp=$(date +%s)
	sudo docker build --rm -t max-image /home/ubuntu/ --build-arg build=$timestamp
	
clear:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

