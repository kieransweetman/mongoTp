# setup

1. setup the virtual enviornement first

    `python -m venv .venv` 

---

2. Activate the environement

    ## windows

    `.venv\Scripts\activate`

    ## macos/linux

    `source .venv/bin/activate`

---

3. Once `venv` has started, download dependencies from the `requirements.txt` file

    `pip install -r requirements.txt`

---

4. setup mongoDB server instance 

    start a server instance with default params

    `mongod -dbpath [PATH/TO/DB/DATA]`

---

5. run 

    `python main.py`

