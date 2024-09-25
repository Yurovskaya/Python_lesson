import re

def strip_rtf(rtf):
   with open(rtf) as f:
      symbols_regexp = r"\\u(\d+)\?"
      content = f.read()
      matches = re.findall(r"(?:\\u(\d+)\?)|(?:\s+)", content)
      print(matches)
      result = ""
      for content in matches:
         if re.match(r"\d+", content):
            result += chr(int(content, 10))
            print(result)
         else:
            result += " "
      return re.sub(r"\s+$", "", re.sub(r"\s+", " ", result))


print(strip_rtf("file.rtf").endswith("Схема взаимодействия основных участников отсутствует"))

