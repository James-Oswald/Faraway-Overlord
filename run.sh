
[ -f ./.env ] || { echo "please create a .env file, read the readme.md for instructions"; exit 1; }
python3 bot.py