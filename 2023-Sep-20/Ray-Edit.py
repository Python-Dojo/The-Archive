import re

def remove_class_and_struct_keywords(symbol:str) -> str:
    symbol = re.sub("struct|class", "", symbol);
    return symbol;

def substiute_strings(symbol:str) -> str:
    default_string:str = r"class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >"
    symbol = re.sub(default_string, "std::string", symbol);
    return symbol;

def substitute_hashmap(symbol:str) -> str:
    default_unordered_map = r"std::unordered_map<([^,]*?),([^,]*?), ?std::hash<\1 ?>, ?std::equal_to<\2 ?>, ?std::allocator< ?std::pair<\1 ?const ?,\2 ?> ?> ?>" 
    replacement_string = r"std::unorded_map<\1,\2>"
    symbol = re.sub(default_unordered_map, replacement_string, symbol)
    return symbol;

def substiute_filesystem(symbol:str) -> str:
    # I don't know what this is yet but will probably be templated on a string (which we can remove)
    return symbol;

def remove_default_allocators(symbol:str) -> str:
    return symbol;

def abstract_common_templates(symbol:str) -> str:
    symbol = substiute_strings(symbol);
    symbol = substiute_filesystem(symbol);
    symbol = substitute_hashmap(symbol);
    symbol = remove_default_allocators(symbol);
    return symbol;

def remove_assumed_conventions(symbol:str) -> str:
    # exported but the link error was internal
    symbol = re.sub("declspec\\(dllimport\\)", "Exported", symbol);
    # exported but the link error was external
    symbol = re.sub("declspec\\(dllexport\\)", "Exported", symbol);
    # some errors seem to not have __? maybe they are pasted wrong and turned to bold by markdown?
    symbol = re.sub(" (__)?cdecl ", " ", symbol);
    return symbol;

if __name__ == "__main__":
    import os
    symbol_from_error = "void __cdecl foo::Serialize<class boost::archive::text_iarchive,class std::unordered_map<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,struct std::hash<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,struct std::equal_to<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,class std::allocator<struct std::pair<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const ,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > > > >(class boost::archive::text_iarchive &,class std::unordered_map<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,struct std::hash<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,struct std::equal_to<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,class std::allocator<struct std::pair<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const ,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > > > &)"
    symbol_from_error = substiute_strings(symbol_from_error);
    symbol_from_error = remove_class_and_struct_keywords(symbol_from_error);
    print("Removing the assumed conventions (like __cdecl)");
    symbol_from_error = remove_assumed_conventions(symbol_from_error);
    print("Removing common templates (like string)");
    symbol_from_error = abstract_common_templates(symbol_from_error);
    print("Removing unrequired info");
    symbol_from_error = remove_class_and_struct_keywords(symbol_from_error);
    print();
    print(symbol_from_error);
    print();
