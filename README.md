# AddressBookAPI

## Set-up Instructions
Clone repository:
  ```latex
cd Desktop && git clone git@github.com:skasinos/AddressBookAPI.git && cd AddressBookAPI
  ```
  
Setup `pyenv` and install `poetry` dependencies:
  ```latex
pyenv local 3.9.0 && poetry env use 3.9.0 && poetry install
  ```

Run tests and check coverage:
  ```latex
coverage run manage.py test && coverage report && coverage html
  ```
  
Makemigrations, migrate and runserver locally:
  ```latex
python manage.py makemigrations && python manage.py migrate && python manage.py runserver
  ```

## Documentation
To view documented endpoints navigate to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) or [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) and to download JSON containing specification of API to [http://127.0.0.1:8000/swagger.json](http://127.0.0.1:8000/swagger.json).



## Filterning and Pagination
- A user may request a specific id using [http://127.0.0.1:8000/api/addressbook/?id=5](http://127.0.0.1:8000/api/addressbook/?id=5).
- Specific fields may be searched. For instance, all addresses located at cities containing `borough` may be queried using [http://127.0.0.1:8000/api/addressbook/?search=borough](http://127.0.0.1:8000/api/addressbook/?id=5).
- All addresses corresponding to a given city may be retrieved using [http://127.0.0.1:8000/api/addressbook/?city=London](http://127.0.0.1:8000/api/addressbook/?city=London). Similarly, addresses associated with a given country may be requested using [http://127.0.0.1:8000/api/addressbook/?country=GB](http://127.0.0.1:8000/api/addressbook/?country=GB).
- `LimitOffsetPagination` has been enabled to allow a user to limit and offset data returned e.g. http://127.0.0.1:8000/api/addressbook/?limit=x&offset=y where `x` and `y` need to be substituted with integers associated with the `limit` and `offset` numbers, respectively

## Assumptions
- A user cannot add a duplicated address associated with his/her account but it is possible to add an address that already exists in the system by another user.

