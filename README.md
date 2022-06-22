# Open edX Transifex Downloader

This project is dedicated to downloading translations for Open edX release on [Transifex](https://www.transifex.com/open-edx/open-edx-releases).


## How to install

First, you need to add your own Transifex API key to the project.
go to : [**User Settings** > **API Token**](https://www.transifex.com/user/settings/api/)
click on **Generate a token** and save your key.

<img src="https://raw.githubusercontent.com/Edspirit/TransifexDownloader/master/screenshot/generate-token.png" width="500" title="Generate token">

then, clone the project and install required packages in a virtual environment:
```
git clone git@github.com:Edspirit/TransifexDownloader.git
cd TransifexDownloader
virtualenv -p python3 .venv
source .venv/bin/activate 
pip install -r requirements.txt
```

in the project's root, rename `api_key.env.sample` file to `api_key.env` and add your key there:
```
mv api_key.env.sample api_key.env
echo "TRANSIFEX_API_KEY=<YOUR_KEY_GOES_HERE>" > api_key.env
```
and you're good to go ;)

## How to run
I assume that you have Pyhton 3 installed on your machine. 
simply just run `main.py` with your desired language on your virtual environment:
```
source .venv/bin/activate
python main.py fa_IR en ar
```

## How to contribute
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

Pull requests are the best way to propose changes to the codebase (we use Github Flow). We actively welcome your pull requests:

### We Use [Github](https://guides.github.com/introduction/flow/index.html) Flow, So All Code Changes Happen Through Pull Requests

1. Fork the repo and create your branch from master.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!



## Licence
By contributing, you agree that your contributions will be licensed under its MIT License.