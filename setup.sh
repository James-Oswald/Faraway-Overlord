
#add to crontab
crontab -l > /tmp/mycron
#Remove previous instances of the command
sed -i '/bot.py/d' /tmp/mycron 
#Add a cron job that posts the tweet at 9 am each morning
echo "0 9 * * * cd "$PWD" && /usr/bin/python3 "$PWD"/bot.py >> /tmp/OverlordBotLog 2>&1" >> /tmp/mycron
crontab /tmp/mycron
rm /tmp/mycron