## Clone and run tests  
```  
(Windows machine)  
git clone https://github.com/nava071/sample-parasoft.git  
cd sample-parasoft  
pip install pipenv  
pipenv install -r requirements.txt  
playwright install --with-deps  
pipenv run pytest -s -v --browser firefox --headed --slowmo 500 --output=.\\results --video=on --screenshot=only-on-failure  
# In the above command, Change browser name to "chromium" or "webkit" to run in that target
```

## Build a docker and run tests

```  
# Screenshots and vifdeos are not copied to the host
git clone https://github.com/nava071/sample-parasoft.git  
cd sample-parasoft  
docker build --tag parasoft-tests .  
docker run -it --rm parasoft-tests firefox  
# In the above command, change the browwser name to "chromium" or "webkit" to run in that target
```
