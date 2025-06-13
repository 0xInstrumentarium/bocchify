# Bocchify
An extension that makes every thumbnail on youtube have Bocchi!

Thanks to the peeps below for the base Implementation.

DenzHa24: https://github.com/DenzHa24/kumify
chikenuwu: https://github.com/IsaacSohn/Sechify
Mrbeastify: https://github.com/MagicJinn/MrBeastify-Youtube

## Specific to this fork
rembg for batch image background removal
https://github.com/danielgatis/rembg

I made a script to Automatically make 1280x720 Images that puts PNGs in the bottom left or right corner and numerizes them so its easy to add more images in the future.

### usage
```bash
cd ./assets/images
rembg p ./ output // removes background of pngs.
python postprocess.py // creates the thumbnail overlays with the pngs and puts them in the final folder.
```

for some reason lowercase .png makes the entire extention not work so I used this command to convert them to Uppercase.
```bash
for f in *.png; do mv "$f" "${f%.png}.PNG"; done
```



