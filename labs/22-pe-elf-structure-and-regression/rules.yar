import "pe"
import "elf"
rule Lab22_PE_Example : training {
 strings: $s="LAB22_PE_SAMPLE"
 condition: uint16(0)==0x5A4D and pe.number_of_sections > 0 and $s
}
rule Lab22_ELF_Example : training {
 strings: $s="LAB22_ELF_SAMPLE"
 condition: uint32be(0)==0x7F454C46 and elf.type != 0 and $s
}
rule Lab22_Control : training {
 strings: $s="LAB22_CONTROL"
 condition: filesize < 1KB and $s
}