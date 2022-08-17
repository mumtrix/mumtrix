# Mumtrix
[If in plain md: Skip this section]: #
TOC: <a href="#About">About</a> – <a href="#GettingStarted">Getting Started</a> – <a href="#Usage">Usage</a> – <a href="#License">License</a> – <a href="#Contribute">Contribute</a> – <a href="#Contact">Contact</a> – <a href="#Acknowledgments">Acknowledgments</a>

## About {#About}
**Posts the current count of online users – on Mumble – to a Matrix room.**

## Getting started {#GettingStarted}
### Requirements {#Requirements}
  * Python 3
  * [Matrix Webhook](https://github.com/nim65s/matrix-webhook)

### Installation {#Installation}
  1. Configure [Matrix Webhook](https://github.com/nim65s/matrix-webhook/blob/master/README.md) ❗️

  2. Clone the repo\
    `git clone --depth=1 https://github.com/mumtrix/mumtrix.git`
  
  3. Create venv\
    `python -m venv /path/to/new/virtual/environment`

  4. Activate venv

  | Shell       | Command                            |
  | ----------- | ---------------------------------- |
  | bash/zsh    | `source <venv>/bin/activate`       |
  | Windows CMD | `C:\> <venv>\Scripts\activate.bat` |

 > ℹ️ For other shells consult the [venv documentation](https://docs.python.org/3/library/venv.html)

  5. Install dependencies\
    `pip install -r DEPENDENCIES`

  6. Generate config\
    `python mumtrix.py`

  7. Tailor the config `mumtrix.ini` to your needs

## Usage {#Usage}
  1. Activate venv
  
  | Shell       | Command                            |
  | ----------- | ---------------------------------- |
  | bash/zsh    | `source <venv>/bin/activate`       |
  | Windows CMD | `C:\> <venv>\Scripts\activate.bat` |

 > ℹ️ For other shells consult the [venv documentation](https://docs.python.org/3/library/venv.html)

 2. _(optional)_ Edit the config `mumtrix.ini`

 3. Run Mumtrix\
    `python mumtrix.py`

## Contribute {#Contribute}
See [github.com/firstcontributions](https://github.com/firstcontributions/first-contributions/blob/main/README.md).

## License {#License}
Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

## Contact {#Contact}
Matrix: [#mumtrix:cozy.town](https://matrix.to/#/#mumtrix:cozy.town)

Github: [github.com/mumtrix](https://github.com/mumtrix/mumtrix)\
Gitea (Mirror): [code.cozy.town/mumtrix](https://code.cozy.town/mumtrix/mumtrix)

## Acknowledgments {#Acknowledgments}
  - [Ranomier](https://github.com/ranomier)
  - [azlux/pymumble](https://github.com/azlux/pymumble)
  - [nim65s/matrix-webhook](https://github.com/nim65s/matrix-webhook)
  - [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)
