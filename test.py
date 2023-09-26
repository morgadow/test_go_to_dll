
import os
import ctypes
import platform

DLL_PATH = os.path.join(os.path.dirname(__file__), "lib.dll")

if __name__ == "__main__":

    # call function from golang dll
    if platform.system() == 'Windows':
        # Loads the API on Windows
        dll_obj = ctypes.windll.LoadLibrary(os.path.splitext(DLL_PATH)[0])
    elif platform.system() == 'Linux':
        # Loads the API on Linux
        dll_obj = ctypes.cdll.LoadLibrary(DLL_PATH)            
    elif platform.system() == 'Darwin':
        dll_obj = ctypes.cdll.LoadLibrary("lib.dylib")
    else:
         raise RuntimeError(f"Unknown system: {platform.system()}")
                
    # calling calc function with integers
    print("Calculation result: ", dll_obj.Calc(1, 2))

    # getting name length 
    print("Length name: ", dll_obj.LengthName("Alfred"))

    # concat of two strings which were passed to golang code
    dll_obj.ConcatStrings.restype = ctypes.c_char_p
    retval = dll_obj.ConcatStrings("apple".encode("utf-8"), "orange".encode("utf-8"))
    print("Concat strings: ", retval.decode('utf-8'))    

    # calling SayHello with name directly -> this is not working, use the approach from ConcatStrings
    print(dll_obj.SayHello("Alfred".encode('utf-8')))

    # calling SayHello with pointer to value -> this is not working, use the approach from ConcatStrings
    buffer = ctypes.create_string_buffer(256)
    buffer.value = "Alfred".encode('ascii')
    print(dll_obj.SayHelloPointer(ctypes.byref(buffer)))

