# TODO


How to start rasa server automatically on boot up if server crashes?

How to run on EC2
https://stackocean.com/blog/how-to-run-a-rasa-nlu-only-server/




# On EC2

# ~/README.md
Instructions:
- https://forum.rasa.com/t/how-to-run-rasa-as-service-in-linux/22588/4
- https://superuser.com/a/1276822
- https://unix.stackexchange.com/a/47715

/etc/systemd/system/rasa-core.service

On a new EC-2 instance, start the rasa.service now and also on boot:
sudo systemctl enable --now rasa-core.service
sudo systemctl is-enabled rasa-core

After you make changes to rasa-core.service
service rasa-action status
sudo service rasa-core stop
sudo systemctl daemon-reload
service rasa-action status
journalctl -e -u rasa.service

After logout, login
screen -ls
screen -r Rasa
crtl + a, d to detach

# /etc/systemd/system/rasa-core.service
[Unit]
Description=Rasa-Core
[Service]
Type=forking
WorkingDirectory=/home/ec2-user/rasa
ExecStart=/bin/sh -c "source ./venv/bin/activate && screen -d -m -S 'Rasa' rasa run --enable-api --cors='*'"
User=ec2-user
Group=daemon
[Install]
WantedBy=multi-user.target

# Explaination
[Install] is needed for sudo systemctl is-enabled rasa-core to return "enabled", which is needed to run on reboot. Without it, it returns "static" (as done here https://forum.rasa.com/t/how-to-run-rasa-as-service-in-linux/22588/4)
