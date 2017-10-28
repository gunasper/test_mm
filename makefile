pyenv = python3.5

run: 
	$(pyenv) max_milhas/app.py
	
deps:
	$(pyenv) -m pip install -r requirements
	
docker:
	timestamp=$(date +%s)
	sudo docker build --rm -t max-image . --build-arg build=$timestamp
	sudo docker rm -f mmcontainer; sudo docker run -e LANG=C.UTF-8 -p 5000:5000 --name="mmcontainer" -d mmimage;

tests:
	echo "TODO"

clear:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

