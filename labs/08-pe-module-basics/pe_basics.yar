import "pe"

rule PE_Module_Basics
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning basic PE-aware YARA conditions"
        lab = "08"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        (pe.machine == pe.MACHINE_I386 or pe.machine == pe.MACHINE_AMD64)
}
