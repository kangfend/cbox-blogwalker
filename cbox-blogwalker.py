#!/usr/bin/env python
# Developed by Sutrisno Efendi
# Sabtu, 28 September 2013
# Cbox auto blogwalking

import urllib, urllib2, cookielib, re
from datetime import datetime, timedelta

url_blog = "http://kangfendi.blogspot.com"
nama_blog = "Kang Fendi"

tanggal = datetime.utcnow() + timedelta(hours=7)
sekarang = int(tanggal.strftime('%H'))

if sekarang <= 3:
    pesan = "Selamat malam sobat, selamat istirahat.. ^_^"
elif sekarang <= 6:
    pesan = "Blogwalking di pagi hari.. :)"
elif sekarang <= 10:
    pesan = "Selamat beraktifitas sobat.. :)"
elif sekarang <= 15:
    pesan = "Selamat siang, jangan lupa makan siang.. :D"
elif sekarang <= 18:
    pesan = "Selamat sore sobat, jangan lupa mampir yah.. :)"
elif sekarang <= 21:
    pesan = "Singgah di blog kawanku yang satu ini.. :)"
else:
    pesan = "Blogwalking.. :)"

cookies    = cookielib.CookieJar()
browser    = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
pesan      = urllib.urlencode({'key': '',
                               'nme': nama_blog,
                               'eml': url_blog,
                               'pst': pesan,
                               'sub': 'Go'
                                })
browser.addheaders.append(('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)'))

def proses(situs):
    try:
        print '[*] Mengakses situs %s' % situs
        akses = browser.open(situs)
        baca = akses.read()
        cbox = re.search(r'http://www(\d+).*boxid=(\d+).*boxtag=([a-zA-Z0-9]+)', baca).groups()
        situs = 'http://www' + cbox[0] + '.cbox.ws/box/index.php?boxid=' + cbox[1] + '&boxtag=' + cbox[2] + '&sec=submit'
        cek = browser.open(situs)
        if nama_blog in cek.read():
            print '[+] Sudah pernah blogwalking ke blog ini'
        else:
            buka = browser.open(situs, pesan)
            if nama_blog in buka.read():
                print '[+] Blogwalking OK'
            else:
                print '[-] Blogwalking Gagal'
    except AttributeError:
        print '[-] Blogwalking Gagal'
        pass
    except Exception:
        pass
        
def main():
    berkas = open('situs.txt')
    for situs in berkas.readlines():
        proses(situs.strip())
        print ''
        
if __name__ == '__main__':
    main()
