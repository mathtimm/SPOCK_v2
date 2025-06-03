---
layout: default
title: How SPOCK works
permalink: /examples/ressources/installation
---

# Installation code 👩‍💻


Installation
-------------

Please follow the instructions below to install the package.

1. Fork the repository (highly recommended if you wish to contribute to the developpement of the code)

2. Install *SPOCK* from your forked version:
```python
    git clone git@github.com:your_github_id/SPOCK_v2.git 

    cd spock

    pip install -r requirements.txt
```
If you don't want to fork the repository proceed to the installation by running this lines of codes in a terminal:
```python
    git clone git@github.com:educrot22/SPOCK_v2.git

    cd spock

    pip install -r requirements.txt
```


Using *SPOCK*
---------------

To use *SPOCK* you will need to be part of the SPECULOOS consortium and have access to:
 * the SPECULOOS server,
 * the Portal,
 * the Cambridge Archive,
 * the SPECULOOS WG6 spread sheet,
 * the SSO HUB,
 * the SNO reduction PC.

Then follow the procedure:

1. the first step is to add a *password.csv* file in the folder: "your_SPOCK_path/SPOCK/credentials/".

2. the second step is to connect to the Liège VPN to have access to all functions of *SPOCK*

3. open `SPOCK_app.ipyn` in a jupyter notebook and click on ``run all cells`` to check everything is working fine.

Contact Elsa Ducrot for more details (else.ducrot@cea.fr)

Upgrading
-------------

- In a terminal in *SPOCK* source code folder:

    - Make sure your forked version is in sync
    - run the following command on your terminal when in the repository
        ```python

            git pull
        ```
- If you wish to propose enhancements or find an error in the code please make a pull request on GitHub.


More details on *SPOCK*
--------------------------

*SPOCK* is presented in more details in [How SPOCK works](how)
 and in [Sebastian et al. 2020](http://arxiv.org/abs/2011.02069).