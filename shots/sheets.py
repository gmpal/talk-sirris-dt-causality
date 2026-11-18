import glob, os, sys
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1]
fs = sorted(glob.glob(os.path.join(here, 'tmp', 's*.png')))
for k in range(0, len(fs), 9):
    sheet = Image.new('RGB', (640 * 3, 360 * 3), 'white')
    for i, f in enumerate(fs[k:k + 9]):
        sheet.paste(Image.open(f).convert('RGB').resize((640, 360)), ((i % 3) * 640, (i // 3) * 360))
    sheet.save(os.path.join(out, 'sheet%d.png' % (k // 9)))
