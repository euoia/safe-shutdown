# Safe Shutdown (for Raspberry Pi)

Python program to handle GPIO button press to safely shutdown the Raspberry Pi.

This program also blinks an LED every second, to clearly show when the Pi is
running.

To install the systemd service:
```
sudo cp safe-shutdown.service /lib/systemd/system
sudo systemctl enable safe-shutdown
```
