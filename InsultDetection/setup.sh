# Installation of DeepPavlov
pip install deeppavlov

# Dependences installation
python3 -m deeppavlov install intent_catcher

# Download and unpack data
mkdir downloads
python3 -m deeppavlov install insults_kaggle_bert
python3 -m deeppavlov interact insults_kaggle_bert -d
