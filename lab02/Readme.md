Cele 2 scripturi pentru laboratorul 2

screenshot.png este rezultatul fb2img cu setarile default
$ sudo ./fb2img.py screenshot.png

output.jpg este rezultatul lui blueSquare.jpg trecut prin cele 2 scripturi
$ ./img2fb.py --dst frame_buffer.bin blueSquare.jpg --width 600 --height 600
$ ./fb2img.py --src frame_buffer.bin  output.jpg

Am avut probleme cu VirtualBox-ul si a trebuit sa rescriu programul de 2 ori si
din pacate nu am avut timp pentru debugging :(