# qwik lookup

Should allow for quick population of symbol data from all available exchanges based on asset type. By default this supports:
* Crypto
* Forex

Uses [Finnhub API](https://finnhub.io/docs/api) to get data but any REST API could be used with a few tweaks, as long as returned payload is JSON.

Generates in CSV files at the moment but could populate a DB to query this data in the future.