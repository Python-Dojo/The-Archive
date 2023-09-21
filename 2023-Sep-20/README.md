The task was to create a script that could go from a msvc, C++ link error to a more readable and understandable error

A small description of the example error is provided below: 


Severity    Code    Description    Project    File    Line    Suppression State
Error    
Error code: 
    LNK2019    
Error type (Can't find function) 
    unresolved external symbol 
only here for symbols that are exported
   "declspec(dllimport)
Start return type (vector is a resizable array on the heap) 
   class std::vector<

string:
	class std::basic_string<char,struct std::char_traits<char>,
	class std::allocator<char> >,

allocator for vector:
	class std::allocator<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >
	> > 
the calling convention (ignore)
	cdecl 

the function name
	link_error_helper::GetSuggestions
	
Arguments to the function
	(class std::vector<struct link_error_helper::DllInfo,class std::allocator<struct link_error_helper::DllInfo> > const &,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const &,struct link_errorhelper::Hints const &)" 

Raw symbol (ignore)
(__imp?GetSuggestions@link_error_helper@@YA?AV?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@@std@@AEBV?$vector@UDllInfo@link_error_helper@@V?$allocator@UDllInfo@link_error_helper@@@std@@@3@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@AEBUHints@1@@Z) 

The actual error:
	referenced in function main    
What binary the error was in.
	ConsoleApplication   
The object file that contains the symbol	
	C:\...\Documents\LinkErrorHelper\LinkErrorHelper-draft\LinkErrorHelper-draft\LinkErrorHelper\ConsoleApplication1\App.obj
The line the error occured on: (ignore)
	1
 
