from pathlib import Path
import re

error = Path("error.txt").read_text()
error = re.findall('"[^"]*"', error)[0]
error = re.sub(r"declspec\((dllimport|dllexport)\)", "EXPORTED", error)

# target
# :std::vector<std::string> GetSuggestions(const std::vector<DllInfo>& a_allExports, const std::string& a_errorMessage, const Hints& a_extraInfo = Hints())

string_regex = r"class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >"

default_allocator = r"std::(\w+)<(\w+),class\s*std::allocator<\1\s*>"

def allocator_replace(match):
  """Replace whole match with first capture group"""
  return f"Default allocator: {match.groups()[1]}: {match.groups()[0]}"

error = re.sub(string_regex, "STRING", error)
print(error)
print()
error = re.sub(default_allocator, allocator_replace, error)
error = re.sub("class|struct", "", error)
print(error)
print()

print("\n".join(re.split(r"\s", error)))
