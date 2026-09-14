import "pe"

rule PE_Imports_And_Sections_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning PE imports and sections"
        lab = "09"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        pe.imports("KERNEL32.dll", "GetLastError")
}
