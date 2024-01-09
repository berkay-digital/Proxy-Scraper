# Proxy Scraper

Proxy Scraper is a Python-based project that scrapes and validates HTTP proxies from various sources. It uses the `requests` library to fetch proxy lists and then validates each proxy to ensure it's working.

![Demo](https://cdn.discordapp.com/attachments/853203826600181790/1194213449174110238/scraperr.gif)

## Project Structure

The main script of the project is located in `main.py`. This script performs the scraping and validation of proxies. The validated proxies are then written to a file named `proxies.txt`.

## How It Works

The script fetches proxy lists from two sources. After fetching the proxies, the script validates each proxy to ensure it's working. This is done by attempting to open a URL using the proxy. If the URL opens successfully, the proxy is considered working; otherwise, it's considered bad.

The script uses multithreading to speed up the validation process. The number of threads used is equal to the number of proxies to be validated.

Once all proxies have been validated, the script writes the working proxies to a file named `proxies.txt`.

## How to Run

To run the script, simply run `python3 main.py`. Make sure you have the required Python libraries installed. You can install them using pip:

```sh
pip install requests termcolor
```

## Output
The output of the script is a file named **proxies.txt** that contains the list of working proxies. Each proxy is written on a new line.

## Future Improvements
Future improvements to the project could include adding more sources for proxy lists, improving the validation process, and adding a user interface for easier use.

## Contributing
Contributions to the project are welcome. If you have a feature request, bug report, or want to improve the code, feel free to open an issue or submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE).
