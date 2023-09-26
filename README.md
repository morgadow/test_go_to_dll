# Compile golang to DLL / SO

## Compiler
I had an error calling the gcc installation using msys2:
`\\_\_\runtime\cgo/gcc_util.c:18: undefined reference to `__imp___iob_func'`

Used approach: https://stackoverflow.com/questions/44605108/any-ideas-how-to-solve-this-cygwin-go-build-error
Download other GCC compiler here: https://jmeubank.github.io/tdm-gcc/download/

> Note: Bevor installation delete all other GCC installations and remove those from PATH, , then add new to path.

## Pass string from python to golang function
Link: https://gist.github.com/helinwang/4f287a52efa4ab75424c01c65d77d939

Go code:
```golang
The Go Source

// a.go
package main

// #include <string.h>
import "C"

//export add
func add(left, right int) int {
	return left + right
}

//export concat
func concat(left, right *C.char) *C.char {
	return C.CString(C.GoString(left) + C.GoString(right))
}

func main() {
}
```

python code:
```python
import ctypes
lib = ctypes.cdll.LoadLibrary('./liba.so')
lib.concat.restype = ctypes.c_char_p
print(lib.concat("apple".encode("utf-8"), "orange".encode("utf-8")))
```