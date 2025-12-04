# Sample Delivery Services

A small script containing various class for making a sample of delivery services.

## Features

- Customer and Driver class to use and manipulate.
- DeliveryOrder class to record and manage the item to deliver.
- PostOffice class to record all driver and assign order by the lowest amount.

## How to run
Clone this repository, ensure you have python3 installed.

Run with this command:
```bash
python3 main.py
```

## Project Structure
```
final-exam
|
|> main.py (Main script)
|> README.md (The one you are reading now)
```


### `Person` class:

#### Attribute:
- public `name`: string
    - Name of person

#### Method:
- public `introduce()` -> None
    - Print the introduction of person.


### `Customer` class:
Inherited from `Person` class.

#### Attribute:
- public `address`: string
    - Address of customer

#### Method:
- public `place_order(item)` -> DeliveryOrder
    - Return the new order created.


### `Driver` class:
Inherited from `Person` class.

#### Attribute:
- public `vehicle`: string
    - Vehicle of the driver.

#### Method:
- public `deliver(order)` -> None
    - Set order status to delivered, printing the delivery string.


### `DeliveryOrder` class:

#### Attribute:
- public `customer`: `Customer`
    - Customer who placed the order.
- public `item`: string
    - Name of the item ordered.
- public `status`: string
    - Status of the delivery
- public `vehicle`: `Driver`
    - Driver of that order.

#### Method:
- public `assign_driver(driver)` -> None
    - Assign driver to the order.
- public `summary()` -> None
    - Prints the overall information of the order.


### `PostOffice` class:

#### Attribute:
- public `name`: string
    - Name of the post office.
- public `address`: string
    - Address of poist office
- public `drivers`: list(`Driver`)
    - List of driver in post office.
- public `orders`: list(`Order`)
    - List of order in post office.


#### Method:
- public `add_driver(driver)` -> None
    - Add driver to `drivers` list.
- public `add_order(order)` -> None
    - Add driver to `orders` list.
- public `assign_order(order)`-> None
    - Assign driver with lowest amount of active order to order.
- private `get_driver_lowest` -> `Driver`
    - Get driver with lowest amount of active order.

