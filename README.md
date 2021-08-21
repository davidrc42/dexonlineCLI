Welcome to dexonlineCLI

INSTALL INTRUCTIONS

Linux:

arch based(arco, manjaro, artix, parabola...):
```
sudo pacman -S git python3 python-pip
pip install bs4
git clone https://github.com/davidrc42/dexonlineCLI
```
debian based(ubuntu, mint, elementary, zorin...):
```
sudo apt install git python3 python3-pip
pip3 install bs4
git clone https://github.com/davidrc42/dexonlineCLI
```
USAGE

go in the configuration of your shell(bashrc,zshrc) and make a convinient alias like:
```
alias dexonline='<path to dexonlineCLI>/main.py'
```

after reopening or sourcing your shell you should be able to:
```
dexonline your-word
```
