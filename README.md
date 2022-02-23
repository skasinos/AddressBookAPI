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

In an IDE e.g. [PyCharm](https://www.jetbrains.com/pycharm/), make migrations and migrate:
  ```latex
python manage.py makemigrations && python manage.py migrate
  ```

Run tests and check coverage:
  ```latex
coverage run manage.py test && coverage report && coverage html
  ```
  
Runserver locally:
  ```latex
python manage.py runserver
  ```

## Documentation
To view documented endpoints navigate to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) or [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) and to download JSON containing specification of API to [http://127.0.0.1:8000/swagger.json](http://127.0.0.1:8000/swagger.json).

## Registration and login
- A user needs to be registered via a `POST` request at [http://127.0.0.1:8000/api/auth/register](http://127.0.0.1:8000/api/auth/register). 
- Registered users can then login with `username` and `password`.
- The current user can be checked at [http://127.0.0.1:8000/api/auth/user](http://127.0.0.1:8000/api/auth/user). 
- A user can log out.

## Creating, retrieving and updating addresses
- A user can add a new address via a `POST` request at [http://127.0.0.1:8000/api/addressbook/](http://127.0.0.1:8000/api/addressbook/)
- A user can retrieve all his/her addresses via `GET` request at [http://127.0.0.1:8000/api/addressbook/](http://127.0.0.1:8000/api/addressbook/)
- A user can update an existing address via a `PUT` request at [http://127.0.0.1:8000/api/addressbook/id](http://127.0.0.1:8000/api/addressbook/id) where `id` is an integer associated with the identity field of a given address.

## Filterning and Pagination
- A user may request a specific id using [http://127.0.0.1:8000/api/addressbook/?id=5](http://127.0.0.1:8000/api/addressbook/?id=5).
- Specific fields may be searched. For instance, all addresses located at cities containing `borough` may be queried using [http://127.0.0.1:8000/api/addressbook/?search=borough](http://127.0.0.1:8000/api/addressbook/?search=borough).
- All addresses corresponding to a given city may be retrieved using [http://127.0.0.1:8000/api/addressbook/?city=London](http://127.0.0.1:8000/api/addressbook/?city=London). Similarly, addresses associated with a given country may be requested using [http://127.0.0.1:8000/api/addressbook/?country=GB](http://127.0.0.1:8000/api/addressbook/?country=GB).
- `LimitOffsetPagination` has been enabled to allow a user to limit and offset data returned e.g. http://127.0.0.1:8000/api/addressbook/?limit=x&offset=y where `x` and `y` need to be substituted with integers associated with the `limit` and `offset` numbers, respectively

## Deleting addresses
- A user can delete a specific address or all of the addresses through a `DELETE` request.
- A user can filter by specific keywords to retrieve limited number of addresses and then delete only these through a subsequent `DELETE` request.

## Assumptions and Future Work
- A user cannot add a duplicated address associated with his/her account but it is possible to add an address that already exists in the system by another user.
- Basic authentication assumed with a `username` and `password` (can be extended to JWT in future).
- Basic unit testing added and coverage. Further tests required and coverage should be increased.

