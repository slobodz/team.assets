#upgrade
python -m pip install --user --upgrade setuptools wheel

# build
python setup.py sdist bdist_wheel

#install whl
pip install *.whl

pip install C:\Project\team.datasync\dist\team.datasync-0.0.5-py3-none-any.whl
python setup.py install

#on PRD server
cd D:\Release\team.assets\venv36-64
activate venv
pip install --extra-index-url https://teampypi.herokuapp.com/ team.datasync==0.0.91