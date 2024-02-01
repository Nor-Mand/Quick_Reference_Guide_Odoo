### `Install odoo from source`

1. Install main dependencies
    ```
   $ sudo apt-get update
   ```
   ```commandline
   $ sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev
   libzip-dev libldap2-dev libsas12-dev python3-setuptoolslibpng12-0 libjpeg-dev gdebi -y
   ```
2. install wkhtmltopdf
    ```
   $ sudo apt install wkhtmltopdf
   ```
3. Install PostgreSQL and configure
   ```commandline
   $ sudo apt install postgresql -y
   ```
   ```commandline
   $ sudo -u postgres createuser --superuser $(whoami)
   ```
4. Configure GIT
   ```commandline
   $ git config --global user.name "your name"
   ```
   ```commandline
   $ git config --global user.email "youremail@mail.com"
   ```
5. Clone odoo base
   ```commandline
   $ git clone -b 16.0 --single-branch --depth 1 https://github.com/odoo/odoo.git
   ```