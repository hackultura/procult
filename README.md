# procult
API do projeto Procult

# Instalação de desenvolvimento

Banco de dados padrão: Postgresql
  * nome: procult
  * user: procult
  * password: 123456

`
sudo apt-get install python-dev
`

`
pip install -r requirements.txt
`

`
python manage.py migrate
`

`
python manage.py collectstatic
`

`
DEBUG=True python manage.py runserver
`
