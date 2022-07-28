

crontab -l > /tmp/mycron
echo "0 9 * * * lux python3"$PWD"/bot.py" >> /tmp/mycron
crontab /tmp/mycron
rm /tmp/mycron

#add to crontab