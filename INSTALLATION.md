# Installation Details

his works best with Python 3.2 and upwards. It also supports Python
and later if you have a recent pyOpenSSL and native OpenSSL library.

### Installation (Python 3)

You can install directly from Github via pip:

```sh
pip install git+git://github.com/TinkerTravel/partner-api-client-python.git
```

To use the bindings, import the package:

```python
import tinker_partner_api as tinker
```

You can also install the API client via [Setuptools](http://pypi.python.org/pypi/setuptools),
by cloning and running:

```sh
python setup.py install
```

### Installation (Python 2.7)

For Python 2.7+ you need to put some more effort, sorry.

You need to install recent versions of

- `ndg-httpsclient`, `pyopenssl` and `pyasn` ; using a recent version of `openssl`.

On Mac you can install this using homebrew:

```sh
brew update
brew install openssl
```

Then you use this library in your Python builds like so (see `brew info openssl`):

```sh
# install cryptography with newer openssl library
LDFLAGS="-L/usr/local/opt/openssl/lib" pip install cryptography --no-use-wheel

# install rest of dependencies
pip install ndg-httpsclient pyopenssl
```

Phew! Now the example should be working.
