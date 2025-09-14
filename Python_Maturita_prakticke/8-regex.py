import re

text = (input("Zadejte text: "))

souhlasky = re.findall(r"[aeiouyáéěíóúůýAEIOUYÁÉĚÍÓÚŮÝ]", text)
samohlasky = re.findall(r"[bcčdďfghjklmnňprřsštťvwxzžBCČDĎFGHJKLMNŇPRŘSŠTŤVWXZŽ]", text)
cisla = re.findall(r"\d", text)
slova = re.findall(r"\w+", text)

print(f"Souhlasky: \t{len(souhlasky)}")
print(f"Samohlasky: \t{len(samohlasky)}")
print(f"Cisla: \t\t{len(cisla)}")
print(f"Slova: \t\t{len(slova)}")
print(f"Celkove znaky: \t{len(text)}")