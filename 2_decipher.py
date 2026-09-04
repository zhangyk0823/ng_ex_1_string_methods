encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

results = []
for chunk in encoded.split("[")[1:]:
    inner = chunk.split("]")[0].split("::")
    if len(inner) == 3 and inner[2] == "ok":
        num = int(inner[0])
        decoded = ""
        for ch in inner[1]:
            if ch in alphabet:
                decoded += alphabet[(alphabet.find(ch) - num) % 26]
            else:
                decoded += ch
        results.append((num, decoded))

results.sort()
print(" ".join(r[1] for r in results))
