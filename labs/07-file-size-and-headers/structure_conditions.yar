rule File_Header_And_Size_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning filesize and header checks"
        lab = "07"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and filesize < 1KB
}
