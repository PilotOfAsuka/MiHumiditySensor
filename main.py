from bluepy import btle

print("Connecting...")
dev = btle.Peripheral("MAC-address")

print("Services...")

for svc in dev.services:
    print(str(svc))
    print(svc.uuid)