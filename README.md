# Unchock

Unchock is an Django and Angular application that takes your Southwest Airlines reservation and checks you in automatically. It is containerized in docker so anyone can run it.

## Running

You will need to make sure docker is installed. If it is, you can run the project by running the following command.

`docker-compose build & docker-compose up`

## Usage

Once the containers are running, open a browser up to [http://localhost:80](http://localhost:80) to show the UI. From there, you can enter in your information for the reservation, leave your containers running, and we will check you in.

## Other notes

Since this uses a container locally, you must keep them running. The best way for this to work is to fire it up the night before if you have an early morning flight and leave it on all night or make sure it is running in the background if using it during the day.

The public use of the southwest api is frowned upon, so if they change it and it no longer works, please open an issue so I can fix it and update the version number.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)