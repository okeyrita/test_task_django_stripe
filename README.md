# Toothless Python Developer Test Task

## Description

Implement __Django + Stripe API backend__ with the following conditions:

* Django Model __Item__ with fields(name, description, price)

* __API__ with to methods:

* * __(GET) /buy/{id}__, using this request get the Stripe Session Id for the following Item. When we execute this method on the backend with a library _strip_, a _stripe.checkout.Session.create(...)_ request is made which returns session.id .

* * __(GET) /item/{id}__, returns a simple HTML page with information about the selected Item and the Buy button. When you click on the _Buy_ button, a request for __/buy/{id}__ occurs, the returned session_id using the JS library __strip__ redirects to the Checkout form __stripe.redirectToCheckout(sessionId=session_id)__ .

## Content of the project 

* Here you can find Django Project _test_task_ with app _pay_system_ . 
* In the docker directory there are _docker-compose_ file and _Dockerfile_ .

## Web paths

* `admin/` - admin panel
* `items/` - show list of all items with details
* `item/{id}` - show data about curent item
* `buy/{id}` - make session_id to buy current item

## Admin panel 

_login_: admin
_password_: admin

## How to run 

### How run locally on your laptop

* Save project 
```
git clone https://github.com/okeyrita/test_task_django_stripe.git
```
* Go to main directory
```
cd test_task_django_stripe/test_task
```
* __Add stripe API keys__ to your project

```
nano data/stripe_key.txt
```
Add your secret key here to first line and add public key to the second line.
You can find your secret and publec keys [here](https://dashboard.stripe.com/test/apikeys)

* Start a local web server
```
python3 manage.py runserver
```
* Go to web browser and go to web page
```
http://localhost:8000/items
```
* To stop the local web server press `Ctrl+C`

### How run Docker container 

 * Main description about how to run Django projects in docker container you can find [here](https://docs.docker.com/compose/django/)
 