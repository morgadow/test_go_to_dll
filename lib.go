package main

// #include <string.h>
import (
	"C"
	"fmt"
)

//export SayHelloPointer
func SayHelloPointer(name *string) string {
	return fmt.Sprintf("Hello from dll to  %v", *name)
}

//export SayHello
func SayHello(name string) string {
	return fmt.Sprintf("Hello from dll to  %v", name)
}

//export LengthName
func LengthName(name string) int {
	return len(name)
}

//export Calc
func Calc(a, b int) int {
	return a + b
}

//export ConcatStrings
func ConcatStrings(left, right *C.char) *C.char {
	return C.CString(C.GoString(left) + C.GoString(right)) // prints warning, which can be ignored
}

func main() {
	fmt.Println("Hello World!")
}
