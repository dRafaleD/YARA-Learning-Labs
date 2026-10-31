rule Lab41_LittleEndian {
 condition:
  filesize >= 4 and uint32(0) == 0x3442414C
}

rule Lab41_BigEndian {
 condition:
  filesize >= 4 and uint32be(0) == 0x4C414234
}

rule Lab41_WrongOrder {
 condition:
  filesize >= 4 and uint32(0) == 0x4C414234
}
