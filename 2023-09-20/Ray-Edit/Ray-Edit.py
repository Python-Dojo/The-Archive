import re;
from typing import Callable;

def get_symbol_from_message(message:str) -> str:
    try:
        message = re.findall('"[^"]*"', message)[0][1:-1]
    except IndexError:
        ...
    return message;

def remove_class_and_struct_keywords(symbol:str) -> str:
    symbol = re.sub(" ?(struct|class)", "", symbol);
    return symbol;

def substiute_strings(symbol:str) -> str:
    default_string:str = r"(class)? *std::basic_string< *char,(struct)? *std::char_traits< *char *>, *(class)? *std::allocator< *char *> *>"
    symbol = re.sub(default_string, "std::string", symbol);
    return symbol;

def substitute_hashmap(symbol:str) -> str:
    default_unordered_map = r"std::unordered_map<([^,]*?),([^,]*?), *std::hash<\1 *>, *std::equal_to<\2 *>, *std::allocator< *std::pair<\1 *const *,\2 *> *> *>" 
    replacement_string = r"std::unorded_map<\1,\2>"
    # replacement_string = r"std::unoreded_map<\1,\2>"
    symbol = re.sub(default_unordered_map, replacement_string, symbol)
    return symbol;

def substiute_filesystem(symbol:str) -> str:
    # I don't know what this is yet but will probably be templated
    return symbol;

def substitute_vector(symbol:str) -> str:
    default_vector:str = r"std::vector<([^,]*?), *std::allocator< *\1 *> *>";
    replacement_string = r"std::vector<\1>";
    symbol = re.sub(default_vector, replacement_string, symbol);
    return symbol;

def remove_default_allocators(symbol:str) -> str:
    regexString:str = r"<([^,]*?), *std::allocator< *\1 *>";
    symbol = re.sub(regexString, r"<\1>", symbol);
    return symbol;

def move_const_to_start(symbol:str) -> str:
    regex:str = r", *([^,]*) *const *(&?) *,";
    symbol = re.sub(regex, r", const \1\2 ,", symbol);
    return symbol;

def abstract_common_templates(symbol:str) -> str:
    symbol = substiute_strings(symbol);
    symbol = substiute_filesystem(symbol);
    symbol = substitute_hashmap(symbol);
    symbol = substitute_vector(symbol);
    symbol = remove_default_allocators(symbol);
    return symbol;

def remove_assumed_conventions(symbol:str) -> str:
    # exported but the link error was internal
    symbol = re.sub(r"( )?declspec\(dllimport\) ", r"\1Exported ", symbol);
    # exported but the link error was external
    symbol = re.sub(r"( )?declspec\(dllexport\) ", r"\1Exported ", symbol);
    symbol = re.sub(" (__)?cdecl ", " ", symbol);
    return symbol;

def main(error_message:str, print_progress:bool = True) -> str:
    if print_progress:
        _print = print;
    else:
        _print = lambda _, *__, **___ : None
    _print("Getting symbol From message");
    symbol = get_symbol_from_message(error_message);
    _print("Removing unrequired info..", end="");
    symbol = remove_class_and_struct_keywords(symbol);
    _print(".", end="")
    symbol = remove_assumed_conventions(symbol);
    _print("\nRemoving common templates... ");
    symbol = abstract_common_templates(symbol);
    _print("\n")
    print(symbol);
    return symbol; 

if __name__ == "__main__":
    symbol = "void __cdecl foo::Serialize<class boost::archive::text_iarchive,class std::unordered_map<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,struct std::hash<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,struct std::equal_to<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,class std::allocator<struct std::pair<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const ,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > > > >(class boost::archive::text_iarchive &,class std::unordered_map<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,struct std::hash<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,struct std::equal_to<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >,class std::allocator<struct std::pair<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const ,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > > > &)"
    main(symbol, False);
    print("")
    symbol = r"""Severity    Code    Description    Project    File    Line    Suppression State
Error    LNK2019    unresolved external symbol "declspec(dllimport) class std::vector<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::allocator<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > > cdecl link_error_helper::GetSuggestions(class std::vector<struct link_error_helper::DllInfo,class std::allocator<struct link_error_helper::DllInfo> > const &,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const &,struct link_errorhelper::Hints const &)" (__imp?GetSuggestions@link_error_helper@@YA?AV?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@@std@@AEBV?$vector@UDllInfo@link_error_helper@@V?$allocator@UDllInfo@link_error_helper@@@std@@@3@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@AEBUHints@1@@Z) referenced in function main    ConsoleApplication    C:\Users\olekr\Documents\LinkErrorHelper\LinkErrorHelper-draft\LinkErrorHelper-draft\LinkErrorHelper\ConsoleApplication1\App.obj"""
    main(symbol, False);
