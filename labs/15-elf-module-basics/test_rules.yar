import "elf"

rule Lab15_ELF_Executable_With_Training_Marker
{
    meta:
        description = "Harmless training rule combining ELF structure with a lab marker"
        purpose = "Practice the YARA ELF module"
        lab = "15"

    strings:
        $marker = "YARA_ELF_LAB_15" ascii

    condition:
        elf.type == elf.ET_EXEC and
        elf.machine == elf.EM_X86_64 and
        elf.number_of_sections > 0 and
        $marker
}

rule Lab15_ELF_Entry_Point_Present
{
    meta:
        description = "Harmless structural rule for an ELF training executable"
        purpose = "Practice entry point and ELF metadata"

    condition:
        elf.type == elf.ET_EXEC and
        elf.entry_point > 0 and
        elf.number_of_sections > 0
}
