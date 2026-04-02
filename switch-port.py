import subprocess as sp
import re

state = sp.run(["pactl list sinks"], shell=True, capture_output=True)
# print(state.stdout)

r = re.search(r"Active Port: analog-output-lineout", str(state.stdout))
print(r)

# state = sp.run(["grep 'Active Port: analog-output-lineout'"], shell=True)

if r is not None:
    port = "headphones"
else:
    port = "lineout"

sp.run(
    [
        f"pactl set-sink-port alsa_output.pci-0000_0b_00.4.analog-stereo analog-output-{port}"
    ],
    shell=True,
)
