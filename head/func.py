import platform

import io
import zipfile
import os
from head.thread import *
from head.aes import aes_decode


# 创建Nocover.png
def create_img():
    if not os.path.exists("storage/assets/img/noCover.jpeg"):
        zip_file = b'PK\x03\x04\x14\x00\x00\x00\x08\x00FU2V\xbe\xba~\xcc\xeb\x16\x00\x00G\x17\x00\x00\x0c\x00\x00\x00noCover.jpegeV\x05P\xd4]\xd7\xff/K\xe7.\xdd\xb1\xbb\x88R\xb2t\x87\xe4\x12\xd2\xb5,HKHH\x97J<t\x8a\x94\x84t7,%!\xe0\n\xd2\r\x82\x80R+%R*\xa8\xc8\xe7\xf3\xcc\x1b\xf3\xcew\xee\xdcs\xef\x9c\xdf\x99s\xcf\x9ds\xe7\xdc\xdf\xf5\xbb\xeb\x8f\x00D[\x03\xa5\x01\x80@\x00\x00\xfa3\x80\xeb\xf7\xc0_\x00\x191\t\x1d-\x84\x01BG\xc7\xc8\xc0\xc0\xc0\xcc\xc0\xc0\xc4\xcc\xc4\xc0H\xcb\xc4\xc8\xc4\xc4\xcc\xf8\xc7\xc4\xc8\xc0\xccq\x93\x9b\x99\x95\x97\x8d\x81\x81\x07\t\xbbqK@XX\x98\x89KLZLH\xea\xa6\x90\xb0\x00\x88\x9c\x9c\x9c\x9a\x8a\x9a\x15\x02a\x15\xe2\xe0\xe0\x10\x10\x10\xfa\xb7\x08\xfc\xcf\xf2\xcfFJH\xe8\x7f\xe0\xbf\xe7u?\x00%\x05\x81\x81A0\x08\x06\x10@A`(\xe8\x1a\x07\xb0\xfdI\x90\x00\xfcw\xaa\xff\x11B"\x10\x98\x98\x80\xe4\x0f\xa8\x04\x01@`\x02B01!!!\x98\xeco\x9f?\xceP0\x0f!-R\x85\xc8\xd0\x8e\x98\x0e\xf60\xe2\xa9hq\xf3\xc0\x1d\xa3\x99cz\xb8\xfd\x86O\xfa \x03BL\xd5!\xb2e\xf6\xe4\xef\x00\xac\xa0\x7f\xc9\x7f\xa3\x83\x08\xc0\x84\xc4D\x7f0>\xe8\xdf\xf6\xbf\xe3\x93\xfc\x07\x83\x12\x80iy\x90\x86\x84t0Q"\xb8\x98\x8a]\xf3\xf1\xf5\n@\t\xfe\xe7T(\xa0\x04\xfcL\x80q\xc3`\x04\xff_\xdd\xfc\x8a\x84\x9ab7\'\xdd\xc7\xbfzZ\x85\xcamG\xde\xf9/|\xfa=\x1c\x91F"f\xdb+L\xd7\xa6P\xe1\x81\xf6|\xdd\x9c\xe2:A#\x0cXV\xd8\xf3\xe5\x90[%\xc2\xbb\xd5G\x024\xb9L\xb1(\x1cd\x85\xa7\xb4\xdb\xf7\xad+\xb2\x8a\xce\x07\xee\xffb\xeaD^\xef\x81qQ\xf6\xc6\xce:\x9f\x88$\xd1\xe9\x0e7f\x1c\xfdM\x0f\xb9\x08\x83U\xfdO\n\x11C\xcc\x87\x05[\x84}O\'g.\x8b \xf8\x10\xec\xd3\xfd\xca\x12*\x0b\x8c\xaa\x1b\xb2\x8d\xd5\xa9\x01H\xbd\xf7r\xa5\xeb.O\x9c4\xeb\xda\x19\x86#\xb6j\xb7Z\x0b3\x17\xfc<T\xd3\xb8\xaae!\xe5\xb3q\xe2\xdb2+\xae\x18\xe2\xfb\xd0\x06\x97\x9f\xdc\x07/\x8e\t\x9fQL\xb0\x16\x0fj\xbc\x18+\x1c\x98\xf5\xf7\xe10k\n\x87\x0b\xd8\x80\x9e\xfdfN\xad\xe9c\xb0x\xef\xec\x92RL\xbc\x8dVJ\xaa\xbc\x8c\xe4^\x8f\x8b\x93_xl\x96\xcd\x01\xdcX\x9a=\xd8\xc9i@\xb8\xdb\x17`\xe6\xa6D\xd1\x13\xe1\xe0A\x0c\xc9\x1b\xd6\xcc\xf3\x14!\x1c\xdb\x9d\xa75\xc7:*\x04\x83z\x87}\x8f\xee\xc5\x83\xd7\xf3\x15$\xa7\x1d\xa2Z\xa5\x9f\xfb\x0e\x1d\xba\xca\xea\xfe\x12\xb2\xd8\x9e\xd7\xa8Mx\xa4+2N\xd1]\xb9R\xfc\x8bg\xeb#\xfbv\xfc\x1e\xf9b\x07\xe7\x10\xe7~\x1e\xfa\xe6\xa7\x18\xecv\xd2\nA\x98*J\x8e\xd0\xfb\xe1\xa0A\xb1v\xe2\x87\x80\x85*\x1f\x08\x87\x14X\xf2\x9bH\x9d\xf4\xa3@\x87\x13\xfa\x9a\xac\xb6\xe4\xd7\xcf\x9e\xb7\xa0\x10\xf1P\x0f\xde\x92\xf7w\x12v\x838\x04U]\x9f\xc6\x85\xda\xec5se\x11%\xc7\x9c\xd6\x192i\x10\xaa)\xab\xa9\xfdK\xa9l|\x05\xe6\xab\x98\x0f\xad\x12\xb5\xca\xc8d\xb5\xa6\xef\x9ez\x80s\x9b|U\xe6o\x06\xbd\xef\xe8v\xd9swm\xa1yq\x82\xe1\xd5\xecI\xea\xcf\xc3\xf7\x84\xf3\x19\xef\xe7\xc3\xa34\xb8\r\x1b\xd7E\xba\xba\xaa\xb3 |:\x18\x94T\xdc\n\xf9\x17\xefU\x9e\xfa\n\xf4c>\x15\xe1\xf9\xa8&\x0e\xa2\xe1j\xab\xa6\x1c[j{\x907\x8b\xaf\x13\xdd<~\xc9\xee0\x92\x93\xad\xf5\xf0\xfeV\xf0Yj\x93\xf1-\xefQ\x0f1:\xbcc\xe8\xad\xf4\x96\xa8\xb7.\xdb\x89\xb3\x7f\xcaI\xc3P-\xf1Y\xc8\x9b\xdau\x1e\xca}\x19Y\xf40\x8c\xed.c\xbd$V\xdc\xd1\xef\xcf#\r\xd7\n\x97\xad\xe5\x8d\x84x\x87Q\x17\x8fi\x97c\x02\x03\x16\xe3<\xb8w[=hX=:\xf9\xbd\xae\x81\x17\x14\xe6\xf2\xab\x1f\xbe>\xae\xd9Lun\x9a\xa0\xe1x\'\x83\xc7\xef\xb4\xb6\x06\x83Z\x02\xeeG\xe5\x0bI\x89\xa4m~z\x06?}\'\xb5H2\xe1\xac\xfd\xb2SM\xbd\x0c\n\x05A!\xffR\xc4\xa4\xe8\xbd\x19 \x1b\xf5lq=\xc2\xc3BY]\xdd\x9c\xce\xac\\\x93\\_H\xa8\xd9\x0e`&\x16\x13\xcf\xb3\xb6\x9c\xad\xb0EU+\xda^\x11\xd0H\xec\xcaLN\xd5\xb9\xac)\xf8>0\xca4\xe2\xbe(\xbd\xb3\xe4\xc6\xa7*\x17\xdd\xf7\xac1\xe32j*\xff\xabeM\xbf\xd6\xb7\x9fW\x19l\x86vN\x06jjD\x15}\xc2y\x8aRm\xdd\x17\xf9D\xbdf;\xe3\x01\xa7\xd1pe\x99\xa3\x84d\xbenl\xf6c\xe7a!\xca\xc3r\xf8\x9a\xcd\xf2\xc6\x1b\xdd\x17\xb0\xe5\xa4\x8f\x94}!#\x1c\xe6Z\xe4\x1b\xa1H\x1d\x92\xbbi\x8d\x96\x9fo#R!i\xb3k\xe1\x9f\x08Y\xf6\xbbuo\xdc\xcaDs\xe9\rL\xc8E\xf1k\xb7uA\x19\xd3\xfeSQe5\x1b7Y\x107\n\xc8a}\x11\xa7\x00\xab\x19x\xc8\x9a\xe9\xd8\x9e\x87f\xb5\x8d\x95\xc6\xbfP\x039I\xe4D\x95\x0e\x19\x1f\xcdm\x7fY T<\xb8! \xb9\xc0\xaav\r\x18Dq\x16\tn\x06}&\x86\xcc\x19\xd0\xa2\x18{q\xfb\xc1h\xbe\xdc\xfa\xad\xce\xba\xafT\xdc\xef\xde\xf2L!\x92\x8a.R\x0c\x8f\'\r<wM\xe5\xa5\xa0\x99\xa5\xc2>\xba\x8c\xd9A+\xc7#\t\xde\x80\xef\x03\x7f\x97x)\x03\xab-\xe9\xc5\x80\x8en\x19\xc7ndky}\xc4\xc6\xd9D=\xd6\xa6I\xbc{\xee\xd7p\xa4h\x1e\xf9\xe4mBe\xc4S*x\x95\xc9\x055\x9d\xe9\xe9\x99n\xcb\xb3\x82\x1cI\x15?\x16\x960\xdb\xf1\xc7\xc6\xee\xb5\xbf\xb9\x06n\xcd]\x94\xaf\xbc\xd6e/z\x0eS\xa6\x0b=5\xd1\xf0\x97\x17A~X\xb8\x06\x90JN\xd1a$W\xc8Su\xe2s5\x13\xb3\x93\xc7b:\xd4\xd4\x81\xaa%\xaa\xb6\xe9a\xb1\xdf1\xd4J\x89\xf38\xf9\xb6\xe4^}\xc2B\xbaU\xea$6d/\x1b\x07\xca\xfa\x93\x8bu,=\nG\x9c\xb5\x0e\xba\x88Ofa*\xe4U]\xe6\x84fK"\xc7\xc7x\x86\x9ey\xfa\xb4\x7f\xef=o\xda\xc37\x07\xa2\x13&\'\x8f\xb5\xbdp\xf3\xc5\x96\xe5;\x91;)<E+h\xad(Q\xfba\x03\xf3\xc0\xd7\x17\x8fd)GP]Vb\xb4\xba/\x1c\xd3Q\xd3\xa1\xc2\xa1M*\x15\x05\xe8\xb2\xa4/\xc1\x13\xa1\xe1\xc2|\xf3\x993\x9b\'\xf3{\xe2\xbd_\xdc\x95\xf1\x9aMl\x99ASdFP\xe3\x00\xf3\xf8\xc0s\xcc\xe77\xda\x91?\t|\xb1\xa1\xd24\xea>m\x90\xffV\n]\xbb\xe4N\xd85\xd0\xe7\xcc7\x96\xbb\x80k\xa6\xae\xd4\x9br\xa7x\xdbg`\xff\xfe\xb0\xba\x93S8/\x7f\x7f\xc1f\xfdd\x08\xf0\x8fb\x15\xa7\xba\xb1\xbe\x9afaRYp\xb5#\x82W:cL[\xa2\xd6\'\xde\xf6\xb7\xaa1\r\x0cP=\x9d\x95dI\x92\xe9{v.\x10x\xe2w\r\xc8="UR\xa7H\xd9Hv#\x14\xd7\x89\xa0\x06\xe2&XS\r\xf9\xc9\xf3\xef\x913\xd48\x85\x9e\xc5\xe4=\xcb \xc6Z\xb7\x12\xe0\x7f\x84\xec\x810\x1b\x85\x1a\xcf|\x8c\xa22@\x1b\'~\xb4;`\n\x8d\xf8\x0b\xef\xc6\x89N_\x1d4M^RXf2\xab\x1a\x89\xf4p\xac\x06V\x15\xed\xe0\xe9\xfc\xa3\xa8\xfa3\x916\x0e\x1b\xef\xae\xc6\x92\x06\nF\x10\x1f\xf0.\xce\xd5\x14,\xf7x\x05kS$\xbeX\x1eG\xa5;\xbeU\xf2R\x97c\x89\xf2\xd0p\x0c\x14`\xa6\x9d\x83\xe6\xdc\x8d9\xc8r\x82G\xe1T}\xbb\x8a\xc8|\xff"\x01\xd3\x82\xd6H\xec[z\xdaf\x11.\x9e\t\xa9Zq\x917\x94b\x8d\xeb\xb3{<m_\xe7P\xe0\xf6\x1e;\x94d\xb2\tV}=\x99\xcf\xf98<\xef\x8e\xf9\xf2\x17\x13\xa0\x9fQT2\xfcM6q\xddfX\xf6\xa9\x14O\x93\x15_\xf1\x8c\xa6\x97]\xf5\xf8\xcb6\xd5\xdd\x99\xaf\x99\x8bu\xcetl\xd5\xef\x99\xdc\x98H7L\x8e\xc7\x05+(\xe9\x10\xcf\x109\xe0\xc3J\x18\x7f\xe4\x7f?\x8c\xd8\xa4\xd73`\xb1wS\x06\x88\x82\xbf\xaa\x13\xa4 \xae\x822V\xcf\x07\xb7P/\xecUh#\xe5\xdc\x8c\xca\x1c\x06\xe7F\xea\xe7~\xa9\x11}\xa2H\xf10B\x05\xb9\xe4I*#|\xe5\xea\x83\xf8S\x03O\xdf\x88\xf6swMu!\xd6\xfb\x13;\xcf\x96=p\xb6c\xbc\xe7\xf9\xac\x81\xae\xb4\xb3!>\x8a\xdad\xa6\x021\xf1\x9c\x05\xfa<\x13\xec\xab\xd8\xad\xd1\xb0\x91\x97\xa9QE\x9b\x9b\xfb)\xd4BX*\xd0\xd2\x11}\x92{\x0f\xb7\xa7\x16x]\xff-wZm\xd0oz\x93\xa2\xe0\x0e\x9c\x82\xc4\xa5\x00/\xbe\xd4\x11:\x0e\xa9\xda\xb9\xe5\xc0\xc9\xcaJ\x15\x0e\x84\xc0\x96\xca\xbb,\xe99\x12`\xfc\x12Ku\x8b\xe2\xbdC\xac3\x88\x02\x805\xbd\xf3\xf1\xfb\x137\x86\x9c!c\xef\xd0\xdc=\x04\x05\x88P\xc3\xe3\x0b\xab\x8fu6dh\xb6l\xd6\xad\xb7\xde\x95xr\xd5\x13n\xd4\xe7\x84\x8b&Y\x02Srd\xe2hXbFD\xe0\xde\x1fD[G\xdb8\x86\x1d\xa5\x9b\x1b\xd5\xc4\x9b\xfb\xe7\xdc\xadrV\x15\tu\xcf\xda~\xcd?^\x14\xe3} \xe1\x9c\xdf(A$\xaa\x12\xef\xda\xc3\x19\xfa\xb3\xeau\xfc\x96\x8b\xc9Q\x81z&oQ[F\x04(\xd2\xd6F\xbc=\x81\x8bq`\xb3\xb6/\xea!o\x1d\x03Wf\xbdK~V\xba\xbe\xc5\xbe\xc9\x07p7\x05\x7fa\xf81O\xf4\x04\x03\xfb\xaf\x19\x07\x80t\x9dx\x7f\xc3\xe3\xe9\xbf;+#\xc4\xc9\x8e\x11b:\xb7\x894*\x17\x99\xfd\xee\xfc..\x8e\xe0\x93\x13O\xd7\xeaI.!F\x9c\xe5\x95\x14g\x1e\xd1~\n\x13wL\'\xe0\x98\xe32\xee\xfc\xa3\x9a\xd2\x96\x80\xe4\xcb\x84JQ\'rr>[%\xee\x03\xaa@Fp\xb6B\xa7\xf5\xd5\xb4\xcf\x01\xbe\x0cFY\xd7(\xc0\x9f\xa2\x04\xb5\\^\x05\x93u\xedL\xd0\xc7b\xd2\x13\xe1\xd5\xe8f\xf1\xb1\x1c|\x14\xd1\x847!3\xf7SZ\xd2\x19\x0f\xf5\xe21N\x90>\x8d\xde\xc2\xbe\xc4EM\x91\xde\xcel\x88\xe4\xb7\xb3\xcc\xf1\x80\xc8^\xb7\xd427F\x94\x8b\xa0\x93\xd2\xa5\xed\x9f\x86\xe4P\xf2C\x13\xc2 W\xf9\xddp\xddI\x86\xefL\xbd\rcNsX\x10\xb2@\x85Q\xed\xee\x12\xb5\xa7X\r^\x19\xb0\x9fr.\xb7\xb0w\xb3\x7f\x9f\x95\xc7/\xd5C\x9f\xcb\xaeE\xed\xbb/\xce\xf4\xdd6\x0fL\xf35\xba\x9b\r]\xecI^\xee\xbcS\xfd\x81\xf2\xf58t\xcfI\x80f9D\xd0\xe1\xdd\x92\xd2p\x06^\x98\xb0m\x02\xd1\xf6\x99\x9bT\xd4\\a\xa8\x99\xb9]1\x93\xf5\x18\xdf^\xca>\x1an}lO6\xebU\xa6}\x0f\xdc\xa7\xa6\xde\xae\xf6O_\xb0\xb0\xc8`\xb1@Y\x18\x90\xc3\x06\xff\xdc\x94\x88\x9e3\xcb<zO\xdc)\xa8n\xd7U>\xe2\xc7m7)Z\x84\x91\x9f;\x84\x0fu\xab$\xce\xd8\xeb\x9e\x7ffK\x16\xc3NQ\x1a"\\o\xf4Vi\xa9\x9az\x93\x1a\xe6\x1ap\x95\xbb\xf3K *4\x7f`\x10\xbd\xb9\xfb\xe0\x884\xd9\xef\x83_\x07\x89r\x8fI\x19\xc7}\xc06\x12\xa17\x14\x1dvUP;dZ\xc5\x86\xaa/\x1c]t.T\xd8Z\x0e\xc4(\x96\xae\xa1R\xaaVS\xe1\xb85\xdbj\xe1\x06D\xc9?|k@=\xd2\x80\x91\\\x90\x81\xc00x\xb4\xf5&mK"\xb57\x01*bq\x14$W\x7f\xf7\x8d\x08\xe0+\xf9\r\xa2\xf2\xac\x8e\xda\xad5\x9e\xce@\xfa\xbe\xaf\xeb\x9e=\x10\x84]\xbf!\xc1\xda \xd7\x96/Z\xae)\xd9K\xca\xe0\xaa\xf2\x80\xf9\x86\xe4\xef\xc6\xfa\xef\x16;S\xac\xf9\xf7\xd4\x02\xb8\xc1l\x9f\x7f\x08\x15l^\x96\xfe4\xdaO.5\x0co[N\xe4o\xfae\xb2J\xb4\x19\xb0p/\xe0I\xa2b\xd1\x94\xf1 \x196\xaf\xbb\xf2\xcb\x88\xbd\x7f\xd8\x96uC\xf3\xd4N\xa3\xf0\x935\xf5M\x89\x88\xca}\x92\xf9\xab\xa7\xe5\xc3^\xa6L\xc9\x04`k\xae\xcdk`\xd9\x7fQ\x10mX\x01V\xdeU\x8c\xc3"q\xe1\xbey\xf1\xd3\x82E\xb9q\x89.\xffPQ`5\x87"\xfbs k\x91\x8blZB\x8a\x7ft\xdd\xdc\xe5\x99+\xbc\xa4\xf931b.\x80\x1d\x87]\xa4R@\xb9G\xf1U\xd8\xd3\x94\x14\x7f\x8e%\xaf\xa6\xaa\xfb\xb1\xb6!\xec\xce:;=$%\xd9\xfcHP\xc94\xcfL\xfc\xdb\x13\xac\x89\xf7\xb8\x07\x9fq\xef\x99\x89\xb3\xb1(\n\x18~3f:m\xfcY\x8f@\xc3\xce(GV\xe6P\xc8\xeb\xe5\xc7\xfe\xd0\x9f5N\xc9T\xbe\x1b\xe5\xf5\xc03\x9e\x86\xbe\x06\x82@\xebaOvb\xb2\xfe\xa3}\xdb`<\xc9.y\xfa*z\x97\xf9\xa3Z\x14\xf7*4\xd8\xd2\xa47\xb5\x02\xffq\x0f/&\xaa\xa9\x8c\x8a8l0\xdb\x12\xac\x83\x9djSfng\xf0\x06\xf1Sf#\x1a!-\x9bQ\xa2\xbdD\xf8\xe0\xb0\xa5,\x899D\xdcN\xd9MI\xfeI\x85\x82q\xfa\xea_\xfa\xdc\x13I\xc4i_\xfe\xda\xf7(Y\x1dm\xa6\xdd\x04\xe5\xc8\x0e\xb0\xb1\xd8\xb8\x1b\xf9\xc6y{\x07X%g\xd4\xc4\x9a\xc5\xd3\xb7\xa4;RdG".\xf7\x0ek\x9b\xe4\xd9\xd5\x9e\xb2\x94\xc5\x85^\x1d\x996H\xc72\xca|\xc4\xb6?\xd8\x13D\xecb\x88\x9b\xcc~)r\x0c}e\x9f\xeb\xc1\x16\xc8P\xab\xf8\xf68\xd5\xeb\xa4\xe6/\x1eZ\xdf\xb7g\xff\xb6$\x83\xd1\x1b\xa3i\x8e:4\xd7\x19\xf8)\xb9r\x97Z\x82+\x874\x16\xb2{\xca\xb8\xe07\xbf\x17%\x83J\x96\xb9\n0x\x18\xd5U\xc3\x7f\x91\x88\xe1\xf99\x80\xa5\xe3\x10\x96\x84\x1c\xb9\x85u\xbel*\xb3\xf5\xd4\xcf\xe0w[\xc8\xff\xe5\xea\xea=:\r\xb8x\xaf\x93!\xa8$\xe6J:\x1f\xd9\x95\x94\xc3\xaf\x8e\xaf\x01\x01\xa1\x88\xa9\xcb\xf3\xde\x8e\xf7\x05\xd9z\xf7\x19_\xf5K\xdd\x97\xa7\n\xf7\x03d@#L\x85\xdf\x92\x95\xc6\x15]r\xed\x97\xa1L\x1a&\x8f\x9aK\xac\xa3o{b\xf3W\nw\xa4.ikCu\xdex/\xb8\xce\x12\xd7\xea*\xe6\xad\xce v~\xddYa\x16\xa8\x0bU!\x84r\xbfK\xb1S\xee?v\xa3\x7fL\xaeGb\tG\x9e\xf3)\xb7\xda\xf7\x05G\xe2\x0c+\x13=T\xf2g\x1c\x12c7\x91a\x15\xdc\xca\x17\x8f2?=8\xd9\x82\xb8\x18\x94|<<>xb\x9aC\xd3%\xd0,\xce\x92\xd3}3\x1b\x98\xb5\xc5\x905\xef\xf9T\x07\xdds\xbe5\x8d\x93\xed\x14\xbd\xbd\xd6\xaeH\xb6\xf8\xf3\x00\\\xf2\xdc\xdc<\xc8\x8d\'\xc9\x9d8\xd9\xc5\xe5\x94\x80q\xe1\x93\xe8\x80\x80n\x8b\xf6\x99\x00\xb5\x00\xe8\xad\x88\xf6\x80\x00a\x1d\x91x\x88\xdb\x08\x05\xed\xf3\xa7\x0fw\x06\xa5\xa2\xab39\xd5\xdeQ\x97|\xaa\x13j\x08B\xf3\xcf\x8b\x81\xaf\x81\x04\x97i\xd5\x96\xbc\xb7\x8b\xa4\xd8z\xbb\x16\xb9!U\xb8\x05\xdf5\xc0p\xeb<b\xf5\x87\xa5[c\xb4\x8b\x1d\xf2\xb1;\x7f\xca\xfed\x15;\xfb\x01UW\xbd\xb4vy\xbb\x14{\xe3\x11\xfd\xb8\x8e\xaa\xd5\x8b\xdb\x00\x8d\xc23\x92\x18\xa1\xee\x86\xbb\xaf\x9c\xc4F\xf7>\x90\x1e\xf7\xc4\xbd\xbb\x06\xfc7\xbe\xea\xbc\xa7\x86\xd1(\xfb\xedV\x98\xd8\x06\x94\x8ci\xdc\xc8CS\x84\'\x95\xe8\xba\xe9oxU\xeb\xf0\x8fA\xa5\xf5\x8c\\c\xa5U\x18a\xa8\xb19q\xcc\x00\x93a\xd0o\xe9\xb6\x89?<\xfb\xd2Z{\xe3\xf9k\xb05\x89\xcc$)6\xce\xe5\xc3\x0b\xa3Gw\x8a?[\xdfY)Qiu\x0cIO\xe7\xad\xba\xba\xd8O\xc8\xb7\xe7x\xfb\xb3dQ\xac\xb1\xa9\x0e6`\r\xe1\xb5c\xe4UV\x8f\xb7\xf8\x8b\xc5\x82\x88\xc7\x19\x12,0\x96 g\xba\x9d\xc9\x10\xdef\xcf\xafP\x06\x11\x93\x14&\x19\xc6/7\x9fZ-\xf28\xff\xa04\xac[\xc2\xcaT\xa8\x9c\x9f\xc3\x1df\x82p\xe6\xee\xfeJ\xfe{\x9fEt`\xba\xba\xbba?\x06\x89\x01\xc4\xc1\xac\xf57\xe3I*\xaa\xb0\xf8H\xbe\x9c\xa8\xfd\xdemK\x87\xbf\x86\xe7\xa1\xa7\x02\xb6\xb4\xb6\xb0\x1ed\x8c\xad\xa0\x89O\xee\xd0\x9dT\xcb>XC\x90\x9a9\x96\x96\xec\xbd\xbe\xa2\xbb\x8d\x00\xfd\x8a\xc7\xb8^L_XFOBc\x92w\xc3et\x8b\xca6Uj\xe17u\x8b\xa6\xf1`\xb2O\xfe\\I\xa6\x94E\xdf9"dQM\x08\xe5\xd5e\x1f\xbf\x0b<\x9c\xf2\xf7Q)\x08\xd8UqE\xba\xbawt\xe4\xbej\xc4\x85\xfe\x92\xe3\x9f\xa5\x1dV\xe4\xe2\xbb\xe5\xa0j\x9d7\x1e\xc9\n\xaf1\x12\xea~\xba\x01?\x0e\'\xc9\xb8\xd99.\xa6\xe7\xe6\xe5\xab\x02\xe3>}Y\xa8T\x93\x88n\xd53\xeb\x10\x11\x86\xc2<\xc5\xe39\xab\x10\xec\x0cb>C#\xbf\xb3~\xc7u\xc0J}\x06G\x07\xe7\x04\x19\xb6\xeb2\xef\xa5n\x9e\xbb\xe4T\x1d\x8f\xe9\rt\xe6`\xdd"\xbd-\x89\xd46z\xee\x14\x040\xcd\xc9\xe4\x92=\xc0a\xdc9\xf7u\xea\x9f\xa4\x13\xde\xd6\xb1r\xd3\x1e\xcb\x8f\xa2\xa6\x18\xb1\xcc\x8c4!\xee\xe2f\xcbl\x14!\x08\xb0\xe1_LVL\x940Z\xe9m\xe2\xff\xb6E\x84\xc7a\x0e\xa0\x93ZF\xc7_\x11\xc1\\G\x8a5:\x15R\x90\x9e9\x88\xc2"\xe7\x05\x85\x1e\xffVa\xfa\x94p#\xb5\xa4\x0e:\xdfC\x1b\x8d\x14\x06\xe2\xe54\x0b\xb3E\xdbI\xe24\xc4\xefz\xfc\x1e+kiM\xf6p\x95%\xe5\xf0W\xcc\xcf\x8e\x95\xca\xb1B2\xc4\xc5`\t\xb6d\xdf\x01\x12\x0f\xf7\xfcw2\xe2\xbb\x0b\xda\xfb\xa9[\x1f1\x0cT\xcd\x12\x8e\x00+\xc27\xd6k\x98\xa05\xe8~\xb6\xccX\x11*\xbe\xc1A-?0\x13\x93\x99xAm{G\xfe\xe3\r\xcdM\x1f\xab\x8dHp\x84\xb7T\xd6\xc08\xa1[\xf0\xad\xfb\xd1\xf1\xe8\x9a|+\n$\xe8D\x17\xd9O\xb9"\xdf\t\xb5\x0f\xdc\xdbn_\xea\xef\xed\xe3\xa7\x1e{\x15\xf0\x18\xbc\xd3\x1d\x86\xc5|\x87nm\x1c\x11\x94\xaa\xea\xc1\xf9\xdex\x1f=l\xeb\xab\xb1\x8aj\x1d\x97\x85U\x94\xe3V\xf0\xb1:\r\xa0\xe9\xa3D\x85\xb1\x95W\x16\x02\x02Vk\x14\xb5\x94\xb2K\x18}\xe8\xa0\xd9&\x03\xca+&\x11\xe5\x80Q\xc3s\xbf.`\xaf\\g\xf2\xaai\xd88/\xd4\xfa\xceS\xda\xfd \xeb\xa5\xa7c\xbafY\xd1\xfbA\x11\x8fb\x95\x8c\\\x18\xd1e\xf6cXHz\xb9i\r\xf0\xc2\xd0\xcbt\xcf\xadf\x04\x8a\\P\xa9o\x8b\xda\x0f\xd2\x12\xa2\xea"\tn\xba:\xb5zmj\xf9\xa6-\x93\xa7\xe1X\x1c\xd8\x80\xdd\xcfY\x1d\xfa\xedd\xa9X\x14~\xdf\x9a\xd6\xb4\xb9\xa1^\x9f\x17\xfd\x9b\'\xe3u\x12]\xf1\xb2\xeeP\x1f\x9b\xd7\x8c\xd1R\x89\x1bv\x1c:\x16\xb4\xbbU\x92_\xcd\xd0c\x9e"\xadC\xdcUZ\xf9\xc5\xc9cy]q8r\xf0r\x04\xe8S\xbb\xfbmV\xb6\xe16\xd5\xf2\xcb\x85\xfd\xa7\x86\xebP\xef\xf7I\xab\xe1AWLV\x03A\x12\xfc\x8c\x95Z>\x0f\xbb\xe09\xf12Y\xce)\xe5SpCx\xce\xab\xee\'(\x1b\xa7Wt\xb6\x9f\xe1\xde\xd8Yw\x1cq\x1a\xdb\x95\xde\rY\x8a8R\x91I\xe1\x87"\xb3\xea\x89\x7f\x18~W\xcf\x8eMh\xa1~\xb5\x82!\xb2\xb3\xf3\x02\x9b\\\xb6nO\x19"\x1c\n}\x83x\xadZ\xe6\x0b\x11\xf2\xf8R\xcd&<\xbe\xc1\x8c\xdf\x11\x84B+?\x1cU]\xc4\x92\x82\xafn\xc8\x8eP\x7f\xbb\xbc\x9d\xffK\xff\xe3\x8f\xb33\xa9\x97O\xf4\x9f\x0c~\r\t\xcd/\xbdO\x84\xebib\xf2\xc4\x84\x85#\x1b\xbe\x9b\'\xc3\x18$I(\xb5"\x1c^\xf1l3t\xa3\x99?\xf4m7\x06n\x98W\x9f\xfen\xecX\xef\x0c\xd3\xf4\n\x0c\x9f+\xb4(\xe4i9\xdf7\xae\xfeq[\xb0\xf6\xe7\xce\x8c\xe3\x12\x1d[\xe3R\x96\xc3\xf8\x9c9\x89\xdc\x01\x1dc\xce\xac\x89\'\xec0cS\xd9/|u\x08\xf1|T!D\x80D\xfe\xd7b\x92\x0e\x08\xa6vy\x18\xa0d*,\xe8F\xe3\x8b\xf2t\xed\x89\x07\xabvX\x882\xf1\xaep\xb2Ra\x06\xfezI\x11\x9f\x06nl\xd5\xd8|\xec\xde\x1e\n\xaeSV\xb47%a\xdd\xf0p\x7fc\x97\xc3,\xc4M\xb7{\xdfr\xd9\xf9M\xe6\x98\xb3w\xbb\x91\xc2\x8c?\xf6X<\x8e\xd8\xda\x9b\xba\x0c6\xf8\x92h;z\xcf.\xd0\xae\xf8\x0b\x10q\xd0\xb7fV\x93\xfcdh\x18|\x85\xd0\xfa\xcez\xb3\xc7\x9d}\xc5\x16\x15\x95#)35\xa8)7\xf8A\x87\xfc5oV\xcf\xca\xac\xc3vQ\xcc$\xdc\xa0\x0fL\xb6\x87\xac\xe8\x7fJ\xdb\x9c\xd0h\xf8\xe6p\xd45\xbbU\x80/\x9f\xa5\xf3\x93\x12w\x87d\x96\xa5D\x1c\xd1\x10\x8e\x16\xb6\xa2_\xd1n\xda9\xc9\xfba\xa1R;\'\x8d\x93,P\xfa\x9d\x9f\xc5\xce\x93l\xcfl\xea\xcf\'[k\x14\xada!y\xca\xa5\xd6u\x15\xf8\xc8U\x9c\x86\x97M\x87\xf9\xc2-\xc7\xb7\xf8k\xe0\xb5\x9fV\xa4O\xba\xe0\x81\x0b\xb7fG\xfd=\xe8\xe1\xc1C\xbd\xd0\xd7\xfd2\xc9\xb9<e\xbf\xcdi\x15\x13\xce\xa2\xec\xd6\xf4i\xeef\xde\xa1\xc8\x9d\x9e\xebD~\xaa/v\xd3d\xd1\xb5\t\xf7]\x17$\x11-\x15\xe5\xe2\x89Yz0\xf4\xbePBhb$\x98\xb7B0`e\xfd\xc0N\xb2\xd0\xd1\x84k\x83s\xda\x9ec\x9fm\xa7c\xcdr\xbanVh\x03n\xf0@\xf3\x0ec\xb3\xd1hw<>\x98~\xb9\xaaK.\xd5&|\xaa\xc5\x93"\xd6\xccK\xe9\xd5\x8cj=.\xef\xeeQ\xda\x1a\xa2mP~\xdb\xf5\xdcD\xa2i\xb2\xdc\xe8Y^~\xbb\x8e\x1b\xfb6\xb0\xda\xd0\xa3/J\xd5\xb8a&\x1dFt\xff\x97)\xe7">O~\xe4A\x98\xfc\x9b\xef\x16\xf9?{ax\xe1w\x1f\xd5"I\xe5\x12\xeb\xccJ\xd8g\xe7\x8a\xafF\xe3u\x80\xa1\xbb\xcah\xbd\x11\xc2\xd53\xb1jC~S_\xfe\x94\xd3\xdah\xa9 \xf5\x95\xe9\xa5\x07d\x00\xdb\xe5\xbel\xfdj+?\xafm\xbe\x95 7\x9ex\x1b\xc7i\xd8W\xe8\x0f\xef\xcc\xeb\x1cyo+\x1f\xbb\xf6\xc0I\x84\xa9\x9e~c\xf0a\xc1+\xac\xd0\xfb*\xf5\xe8\xf4\x1b\xc1V\xdf\xfd\x13@\xad\xbeOr\x17R\x83|W,~\xaeBHSM\xab\xcfG"\x10,\'Z\xacT/?\xec6\x87aLcx\x16\xd9\xcb\xfc\xd7\xf8\xdd\xe8\x9ds\xe2\x99\xbe\xdb\xec\x99Op\xbbI\xecvT\xc8\xe7\x92(\xbaN\xa3\x97\x00_\xb9\xaa0\x9f\xe6c\xa9[\'\x04\xbe\x0fd\x19\xa4h\xb4d&\x85\xbb\xe6\x9e\xc4(\xddk\xc9F\xe7$\xc6\xb3\'_\x19\'\x9dx\xf0\xd7\xbc@F\x141\xc6\x03\x04\t\x1d\xbd^\xc8#\xa8Co\xa8\xb5\xa1\xa9B9N\xf6\x05\xc7\x94\xdd\xe8\x01\x06&<\xde\xf9\x9bT\xcf\xad\xdfT8H\xf4\xee}\xba\xc7!\x8dE\x12\x11\xf5\xa0"@\x92Q\xcd\xa0F\xf8\x9d\xdc\xa5\x10\x1b\xd3\xbd:0\xb9\x92c5\r]\xc9G\xd2=\xd9\x12a\xf3/\xa9\xf7\xb9\xa6\xaf\x81\xd0\x97fF\\\xf4d\x8c\xdf\x17B|`\xfb\'\xf2R\xfeu4P6\x18\xafa\xc9\xbe$\xb3\xda\xd3j\xdf\xf8\x83M\xf8n\\\xd7\x82\xc7s)\xbcbM\x7f\x89\x90\xdf\x15m\xedE\xb29I[Q?\x0f\xee\r\x16\xfe\xc4\x94\xa0\x97179\xef]^\xfa\xc1[\xb6\xcb\xdd\xb8J\xded\xea7\n\xe11\x9d\xe1\x14\xcat"\x94Z\xb4\x1d\xb6\xb52\x1b\xcf\xe3\xfdV\xa7\xb2\x11\xeaC\xe8Z\x92\xe5\xfa\xe4\x81\xcc\xa6&\xd7\x19h\x80FS\x9b\xb1-\xcd8!\x9d}\xf0e\t_KEW\x1fw\xe0\xcc\x9d\xcd\xb6\xfc\x9b\xf2Q\x0f+_\xc2|\xce\xcb\xd4\xdc\x95!\xc4\x89\xa4\t\xc8\xc6\xeb\xe5\xff\x03PK\x01\x02\x14\x00\x14\x00\x00\x00\x08\x00FU2V\xbe\xba~\xcc\xeb\x16\x00\x00G\x17\x00\x00\x0c\x00$\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00noCover.jpeg\n\x00 \x00\x00\x00\x00\x00\x01\x00\x18\x00!\xbb\x88v\xe6*\xd9\x01\x06\xc5F\xdc\xe6*\xd9\x01!\xbb\x88v\xe6*\xd9\x01PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00^\x00\x00\x00\x15\x17\x00\x00\x00\x00'
        zip_file = io.BytesIO(zip_file)
        with zipfile.ZipFile(zip_file, 'r') as f:
            for file in f.namelist():
                f.extract(file, "./storage/assets/img/")
            f.close()


# 禁用Windows下的关闭按钮使得关闭程序只能使用Ctrl+C
def ban_windows_window_close_button():
    import win32console, win32gui, win32con
    hwnd = win32console.GetConsoleWindow()
    if hwnd:
        hMenu = win32gui.GetSystemMenu(hwnd, 0)
        if hMenu:
            win32gui.EnableMenuItem(
                hMenu, win32con.SC_CLOSE, win32con.MF_DISABLED)


def storage_clone():
    if CLONE_MODE and not os.path.exists("storage"):
        os.mkdir("storage")
        origin = f"https://{aes_decode(github_token)}@github.com/{github_name}/{github_repo}.git"
        print("[INFO]\tCLONE_MODE Enable.Start Clone...")
        os.system(f"cd storage & git clone {origin} .")
    elif not CLONE_MODE:
        print("[INFO]\tCLONE_MODE Disable.")


# 启动函数
def start():
    storage_clone()
    create_img()
    thread_starter()
    while True:
        try:
            t_reader.join(timeout=0.1)
        except KeyboardInterrupt:
            sys.exit()


# 结束时运行的函数
def exit_do():
    try:
        if platform.system() == "Windows":
            os.system("taskkill /f /im nginx.exe")
        else:
            os.system("killall -9 nginx")
            os.system("killall -9 nginx")
    except:
        ...
